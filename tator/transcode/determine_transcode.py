#!/usr/bin/env python

import subprocess
import json
import logging
import os

from ..openapi.tator_openapi.models import MediaType
from ..util.get_api import get_api
from ..util.get_parser import get_parser
from .transcode import find_best_encoder, get_length_info
from collections import defaultdict

STREAMING_RESOLUTIONS=[144, 360, 480, 720, 1080]

logger = logging.getLogger(__name__)

def parse_args():
    parser = get_parser()
    parser.add_argument('path', help='Path to original file.')
    parser.add_argument('--project', type=int, help='Unique integer identifying a project. This is '
                                                    'only needed if media_type is -1.')
    parser.add_argument('--media_type', type=int, help='Unique integer identifying a media type.')
    parser.add_argument('--group_to', type=int, default=480,
                         help='Vertical resolutions below this will be transcoded with '
                              'multi-headed ffmpeg.')
    parser.add_argument('--output', help='Path to output json file.')
    parser.add_argument('--media-id', type=int, help="Existing media ID, if applicable", default=-1)
    return parser.parse_args()

def determine_transcode(host, token, media_type, media_id, path, group_to):
    """ Determine transcode workloads to be performed.

    :param host: URL of host.
    :param token: API token.
    :param media_type: Unique integer identifying a media type.
    :param media_id: Unique integer identifying the media object for which the transcode workloads
                     need to be determined.
    :param path: Path to original file.
    :param group_to: Resolutions less or equal to this will be grouped into one workload.
    """
    slow_cmd = [
        "ffprobe",
        "-v","error",
        "-show_entries", "stream:format=duration",
        "-print_format", "json",
        "-count_frames",
        "-skip_frame", "nokey",
        path,
    ]
    # The magic to reliably getting duration appears to be
    # the 'format=duration'. Out of an abundance of caution
    # we will leave the slow command in there in the event duration
    # slips by this faster method.
    fast_cmd = [
        "ffprobe",
        "-v","error",
        "-show_entries", "stream:format=duration",
        "-print_format", "json",
        path,
    ]
    output = subprocess.run(fast_cmd, stdout=subprocess.PIPE, check=True).stdout
    video_info = json.loads(output)
    if video_info['streams'][0].get('duration', None) is None:
        logger.info("NOTICE: Duration was null have to resort to slow method.")
        output = subprocess.run(slow_cmd, stdout=subprocess.PIPE, check=True).stdout
        video_info = json.loads(output)
    stream_idx=0
    audio=False
    for idx, stream in enumerate(video_info["streams"]):
        if stream["codec_type"] == "video":
            stream_idx=idx
        if stream["codec_type"] == "audio":
            logger.info("Found Audio Track")
            audio=True
    stream = video_info["streams"][stream_idx]
    stream = {**video_info.get("format", {}), **stream}
    fps, num_frames = get_length_info(stream)

    # Handle up to but not exceeding FHD
    height = int(stream["height"])
    width = int(stream["width"])

    # Handle rotated videos
    if "tags" in stream:
        if "rotate" in stream["tags"]:
            if stream["tags"]["rotate"] == "90":
                height = int(stream["width"])
                width = int(stream["height"])
    logger.info(f"Height of video is : {height}")

    # Generate output path
    base, ext = os.path.splitext(path)

    # Get media type object.
    api = get_api(host, token)
    if media_type == -1:
        media_types = api.get_media_type_list(args.project)
        for media_type_obj in media_types:
            if media_type_obj.dtype == 'video':
                break
    else:
        media_type_obj = api.get_media_type(media_type)

    assert isinstance(media_type_obj, MediaType)

    # Get media object
    try:
        media_obj = api.get_media(media_id)
    except:
        media_obj = None

    if media_obj:
        # Get existing streaming/archival/audio file info
        if media_obj.media_files and media_obj.media_files.streaming:
            existing_streaming_resolutions = set(
                [
                    (stream_info.resolution[0], find_best_encoder(stream_info.codec))
                    for stream_info in media_obj.media_files.streaming
                ]
            )
        else:
            existing_streaming_resolutions = []

        if media_obj.media_files and media_obj.media_files.archival:
            existing_archival_resolutions = set(
                [
                    (archival_info.resolution[0], find_best_encoder(archival_info.codec))
                    for archival_info in media_obj.media_files.archival
                ]
            )
        else:
            existing_archival_resolutions = []

        # If at least one audio track exists, don't retranscode it
        if audio and media_obj.media_files and media_obj.media_files.audio:
            audio = False
    else:
        existing_streaming_resolutions = set()
        existing_archival_resolutions = set()

    available_resolutions = STREAMING_RESOLUTIONS
    crf_map = defaultdict(lambda: 23)
    codec_map = defaultdict(lambda: 'libx264')
    preset_map = defaultdict(lambda: '')
    pixel_format_map = defaultdict(lambda: 'yuv420p')
    try:
        if media_type_obj.streaming_config:
            available_resolutions = []
            for config in media_type_obj.streaming_config:
                available_resolutions.append(config.resolution)
                crf_map[config.resolution] = config.crf
                codec_map[config.resolution] = config.vcodec
                preset_map[config.resolution] = config.preset
                pixel_format_map[config.resolution] = config.pixel_format
    except Exception as e:
        # Likely an old version of the server
        # TODO: Remove me someday
        logger.info(e)
        logger.info("Defaulting to STREAMING_RESOLUTIONS")
    logger.info(f"Selected Resolutions {available_resolutions}")

    # Returns `True` if the resolution is smaller than the source video and it does not exist
    # already in the media object
    def _is_resolution_needed(resolution):
        if resolution > height:
            return False
        if (resolution, find_best_encoder(codec_map[resolution])) in existing_streaming_resolutions:
            return False
        return True

    # Make a list of resolutions needed
    resolutions = [res for res in available_resolutions if _is_resolution_needed(res)]
    if height < max(available_resolutions) and not height in resolutions:
        smallest_higher_res = min(r for r in available_resolutions if r > height)

        if not (height, codec_map[smallest_higher_res]) in existing_streaming_resolutions:
            # copy personality form the nearest higher resolution
            crf_map[height] = crf_map[smallest_higher_res]
            codec_map[height] = codec_map[smallest_higher_res]
            preset_map[height] = preset_map[smallest_higher_res]
            pixel_format_map[height] = pixel_format_map[smallest_higher_res]
            resolutions.append(height)

    # Streaming workloads (lower res)
    if any(res <= group_to for res in resolutions):
        workloads = [
            {
                "category": "streaming",
                "path": path,
                "raw_height": height,
                "raw_width": width,
                "configs": [
                    f"{res}:{crf_map[res]}:{codec_map[res]}:{preset_map[res]}:{pixel_format_map[res]}"
                    for res in resolutions
                    if res <= group_to
                ],
            }
        ]
    else:
        workloads = []

    # Streaming workloads (higher res)
    workloads.extend(
        {
            "category": "streaming",
            "path": path,
            "raw_height": height,
            "raw_width": width,
            "configs": [
                f"{res}:{crf_map[res]}:{codec_map[res]}:{preset_map[res]}"
            ],
        }
        for res in resolutions
        if res > group_to
    )

    # Archival workloads
    # This will force all transcodes to run `convert_archival` on the raw video,
    # which will fetch the media type and take action based on the returned 
    # archive config.
    if not existing_archival_resolutions:
        workloads.append(
            {
                'category': 'archival',
                'path': path,
                'raw_height': height,
                'raw_width': width,
                'configs': [],
            }
        )

    # Audio workloads
    if audio:
        workloads += [{
            'category': 'audio',
            'path': path,
            'raw_height': height,
            'raw_width': width,
            'configs': [],
        }]

    # Assign a sequential numerical ID to each workload.
    for idx in range(len(workloads)):
        workloads[idx]['id'] = idx

    return workloads

if __name__ == '__main__':
    args = parse_args()
    workloads = determine_transcode(
        args.host, args.token, args.media_type, args.media_id, args.path, args.group_to
    )
    for workload in workloads:
        workload['configs'] = ','.join(workload['configs'])
    with open(args.output, 'w') as f:
        json.dump(workloads, f)
