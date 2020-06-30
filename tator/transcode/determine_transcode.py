#!/usr/bin/env python

import subprocess
import json
import argparse
import logging
import os

from ..openapi.tator_openapi.models import MediaType
from ..util.get_api import get_api
from ..util.get_parser import get_parser

STREAMING_RESOLUTIONS=[144, 360, 480, 720, 1080]
MAX_RESOLUTION=max(STREAMING_RESOLUTIONS)

logger = logging.getLogger(__name__)

def parse_args():
    parser = get_parser()
    parser.add_argument('path', help='Path to original file.')
    parser.add_argument('--media_type', type=int, help='Unique integer identifying a media type.')
    parser.add_argument('--output', help='Path to output json file.')
    return parser.parse_args()

def determine_transcode(host, token, media_type, path, group_to=480):
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
    if "nb_frames" in stream:
        num_frames = float(stream["nb_frames"])
    else:
        fps_fractional = stream["avg_frame_rate"].split("/")
        fps = float(fps_fractional[0]) / float(fps_fractional[1])
        seconds = float(stream["duration"]);
        num_frames = float(fps * seconds)

    # Handle up to but not exceeding FHD
    height = int(stream["height"])
    width = int(stream["width"])
    print(f"Height of video is : {height}")

    # Make a list of resolutions needed
    resolutions=[resolution for resolution in STREAMING_RESOLUTIONS if resolution < height]
    if height <= MAX_RESOLUTION:
        resolutions.append(height)

    # Generate output path
    base, ext = os.path.splitext(path)

    # Get media type object.
    api = get_api(host, token)
    media_type_obj = api.get_media_type(media_type)
    assert isinstance(media_type_obj, MediaType)

    # Streaming workloads (low res)
    workloads = [{
        'category': 'streaming',
        'path': path,
        'raw_height': height,
        'raw_width': width,
        'resolutions': [str(resolution) for resolution in resolutions if resolution <= group_to],
    }]

    # Streaming workloads (higher res)
    workloads += [{
        'category': 'streaming',
        'path': path,
        'raw_height': height,
        'raw_width': width,
        'resolutions': [str(resolution)],
    } for resolution in resolutions if resolution > group_to]

    # Archival workloads
    # TODO: Make this configurable with codec, resolution, storage location in media type object.
    workloads += [{
        'category': 'archival',
        'path': path,
        'raw_height': height,
        'raw_width': width,
        'resolutions': [],
    }]

    # Audio workloads
    if audio:
        workloads += [{
            'category': 'audio',
            'path': path,
            'raw_height': height,
            'raw_width': width,
            'resolutions': [],
        }]
    
    return workloads

if __name__ == '__main__':
    args = parse_args()
    workloads = determine_transcode(args.host, args.token, args.media_type, args.path)
    for workload in workloads:
        workload['resolutions'] = ','.join(workload['resolutions'])
    with open(args.output, 'w') as f:
        json.dump(workloads, f)

