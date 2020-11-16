#!/usr/bin/env python

import subprocess
import json
import argparse
import logging
import os

from ..openapi.tator_openapi.models import MediaType
from ..util.get_api import get_api
from ..util.get_parser import get_parser
from .transcode import get_length_info
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
    return parser.parse_args()

def determine_transcode(host, token, media_type, path, group_to):
    """ Determine transcode workloads to be performed.

    :param host: URL of host.
    :param token: API token.
    :param media_type: Unique integer identifying a media type.
    :param path: Path to original file.
    :param group_to: Resolutions less or equal to this will be grouped into one workload.
    """
    cmd = [
        "ffprobe",
        "-v","error",
        "-show_entries", "stream",
        "-print_format", "json",
        "-count_frames",
        "-skip_frame", "nokey",
        path,
    ]
    output = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout
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
    print(f"Height of video is : {height}")

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

    available_resolutions = STREAMING_RESOLUTIONS
    crf_map = defaultdict(lambda: 23)
    codec_map = defaultdict(lambda: 'libx264')
    try:
        if media_type_obj.streaming_config:
            available_resolutions = []
            for config in media_type_obj.streaming_config:
                available_resolutions.append(config.resolution)
                crf_map[config.resolution] = config.crf
                codec_map[config.resolution] = config.vcodec
    except Exception as e:
        # Likely an old version of the server
        # TODO: Remove me someday
        print(e)
        print("Defaulting to STREAMING_RESOLUTIONS")
    print(f"Selected Resolutions {available_resolutions}")
    # Make a list of resolutions needed
    resolutions = [resolution for resolution in available_resolutions if resolution < height]
    if height <= max(available_resolutions) and not height in resolutions:
        resolutions.append(height)

    # Streaming workloads (low res)
    workloads = [{
        'category': 'streaming',
        'path': path,
        'raw_height': height,
        'raw_width': width,
        'configs': [f"{resolution}:{crf_map[resolution]}:{codec_map[resolution]}"
                    for resolution in resolutions if resolution <= group_to],
    }]

    # Streaming workloads (higher res)
    workloads += [{
        'category': 'streaming',
        'path': path,
        'raw_height': height,
        'raw_width': width,
        'configs': [f"{resolution}:{crf_map[resolution]}:{codec_map[resolution]}"],
    } for resolution in resolutions if resolution > group_to]

    # Archival workloads
    # This will force all transcodes to run `convert_archival` on the raw video,
    # which will fetch the media type and take action based on the returned 
    # archive config.
    workloads += [{
        'category': 'archival',
        'path': path,
        'raw_height': height,
        'raw_width': width,
        'configs': [],
    }]

    # Audio workloads
    if audio:
        workloads += [{
            'category': 'audio',
            'path': path,
            'raw_height': height,
            'raw_width': width,
            'configs': [],
        }]

    return workloads

if __name__ == '__main__':
    args = parse_args()
    workloads = determine_transcode(args.host, args.token, args.media_type, args.path,
                                    args.group_to)
    for workload in workloads:
        workload['configs'] = ','.join(workload['configs'])
    with open(args.output, 'w') as f:
        json.dump(workloads, f)
