#!/usr/bin/env python

import argparse
import subprocess
import os
import json
import logging
import tempfile

from ..util import get_api

from .upload import upload_file
from .transcode import get_length_info

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def parse_args():
    parser = argparse.ArgumentParser(description='Makes thumbnails for a video.')
    parser.add_argument('--host', type=str, default='https://www.tatorapp.com', help='Host URL.')
    parser.add_argument('--token', type=str, help='REST API token.')
    parser.add_argument('--media', type=int, help='Unique integer identifying a media.')
    parser.add_argument('input', type=str, help='Path to input file.')
    parser.add_argument("-o", "--output", type=str, help='Path to output thumbnail.')
    parser.add_argument("-g", "--gif", type=str, help='Path to output thumbnail gif.')
    return parser.parse_args()

def get_metadata(path):
    cmd = [
        "ffprobe",
        "-v","error",
        "-show_entries", "stream",
        "-print_format", "json",
        "-select_streams", "v",
        "{}".format(path)
    ]
    output = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout

    logger.info("Got info = {}".format(output))
    video_info = json.loads(output)
    stream = video_info["streams"][0]

    fps, num_frames = get_length_info(stream)
    # Fill in object information based on probe
    codec = stream["codec_name"]
    width = stream["width"]
    height = stream["height"]

    return (codec, fps, num_frames, width, height)

def make_thumbnails(host, token, media_id, video_path, thumb_path, thumb_gif_path):
    """ Makes thumbnails and gets metadata for original file.
    """
    # Get metadata for original file.
    codec, fps, num_frames, width, height = get_metadata(video_path)

    # Create thumbnail.
    cmd = ["ffmpeg", "-y", "-i", video_path, "-vf", "scale=256:-1", "-vframes", "1", thumb_path]
    subprocess.run(cmd, check=True)

    with tempfile.TemporaryDirectory() as dirname:
        pts_scale = (fps / 3) * (10 / num_frames)

        # Create gif thumbnail.
        cmd1 = ["ffmpeg", "-y"]
        if num_frames > 10000:
            cmd2 = ["-skip_frame", "nokey"]
        else:
            cmd2 = []
        cmd3 = ["-i", video_path, "-vf", f"scale=256:-1:flags=lanczos,setpts={pts_scale}*PTS",
                "-r", "3", os.path.join(dirname, "%09d.jpg")]
        cmd = cmd1 + cmd2 + cmd3
        subprocess.run(cmd, check=True)
        cmd = [
            "ffmpeg", "-y", "-r", "3", "-i", os.path.join(dirname, '%09d.jpg'), "-vf",
            "split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse",
            "-r", "3",
            thumb_gif_path
        ]
        subprocess.run(cmd, check=True)

    # Upload thumbnail and thumbnail gif.
    api = get_api(host, token)
    thumbnail_url = upload_file(thumb_path, api)
    thumbnail_gif_url = upload_file(thumb_gif_path, api)

    # Update the media object.
    response = api.update_media(media_id, media_update={
        'thumbnail_url': thumbnail_url,
        'thumbnail_gif_url': thumbnail_gif_url,
        'num_frames': num_frames,
        'fps': fps,
        'codec': codec,
        'width': width,
        'height': height,
    })
    logger.info(f'Thumbnail upload done! {response.message}')

if __name__ == '__main__':
    args = parse_args()
    make_thumbnails(args.host, args.token, args.media, args.input, args.output, args.gif)
