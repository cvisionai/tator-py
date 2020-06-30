#!/usr/bin/env python

import subprocess
import json
import argparse
import logging
import os

STREAMING_RESOLUTIONS=[144, 360, 480, 720, 1080]
MAX_RESOLUTION=max(STREAMING_RESOLUTIONS)

logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to original file.')
    parser.add_argument('out', help='Path to output json file.')
    args = parser.parse_args()

def determine_transcode(path, media_type, group_to=480):
    """ Determine transcode workloads to be performed.

    :param path: Path to original file.
    :param media_type: `tator.models.MediaType` object.
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

    # Streaming workloads
    workloads = [{
        'category': 'streaming',
        'path': path,
        'raw_height': height,
        'raw_width': width,
        'resolutions': [str(resolution) for resolution in resolutions if resolution <= group_to],
    }]
    workloads += [{
        'category': 'streaming',
        'path': path,
        'raw_height': height,
        'raw_width': width,
        'resolutions': [str(resolution)],
    } for resolution in resolutions if resolution > group_to]

    # Archival workloads
    # TODO: Make this configurable with codec, resolution, storage location in media type.
    workloads += [{
        'category': 'archival',
        'path': path,
        'raw_height': height,
        'raw_width': width,
    }]

    # Audio workloads
    if audio:
        workloads += [{
            'category': 'audio',
            'path': path,
        }]
    
    return workloads

if __name__ == '__main__':
    args = parse_args()
    workloads = determine_transcode(args.path)
    with open(args.out, 'w') as f:
        json.dump(workloads, f)

