#!/usr/bin/env python

import argparse
import logging
import subprocess
import json
import os

logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description='Transcodes a raw video.')
    parser.add_argument('--host', type=str, default='https://www.tatorapp.com', help='Host URL.')
    parser.add_argument('--token', type=str, help='REST API token.')
    parser.add_argument('--category', required=True, help='One of streaming, archival, or audio.')
    parser.add_argument('--raw_width', type=int, help='Pixel width of original video.')
    parser.add_argument('--raw_height', type=int, help='Pixel height of original video.')
    parser.add_argument('--resolutions', type=str, help='Comma separated list of output resolutions.')
    parser.add_argument('--input', type=str, help='Path to raw video.')
    parser.add_argument("-o", "--output");
    return parser.parse_args()

def convert_streaming(path, outpath, raw_width, raw_height, resolutions):
    print(f"Transcoding {path} to {outpath}...")
    # Get workload parameters.
    path = workload['path']
    resolutions = workload['resolutions']
    vid_dims = [workload['raw_height'], workload['raw_width']]
    cmd = [
        "ffmpeg", "-y",
        "-i", path,
        "-i", os.path.join(os.path.dirname(os.path.abspath(__file__)), "black.mp4"),
    ]

    per_res = ["-an",
        "-metadata:s", "handler_name=tator",
        "-vcodec", "libx264",
        "-g", "25",
        "-preset", "fast",
        "-pix_fmt", "yuv420p",
        "-movflags",
        "faststart+frag_keyframe+empty_moov+default_base_moof",
        "-tune", "fastdecode",]

    print(f"Transcoding to {resolutions}")
    for ridx, resolution in enumerate(resolutions):
        logger.info(f"Generating resolution @ {resolution}")
        output_file = os.path.join(outpath, f"{resolution}.mp4")
        cmd.extend([*per_res,
                    "-filter_complex",
                    # Scale the black mp4 to the input resolution prior to concating and scaling back down.
                    f"[0:v:0]setsar=1[vid{ridx}];[1:v:0]scale={vid_dims[1]}:{vid_dims[0]},setsar=1[bv{ridx}];[vid{ridx}][bv{ridx}]concat=n=2:v=1:a=0[rv{ridx}];[rv{ridx}]scale=-2:{resolution}[catv{ridx}];[catv{ridx}]pad=ceil(iw/2)*2:ceil(ih/2)*2[outv{ridx}]",
                    "-map", f"[outv{ridx}]",
                    output_file])
    logger.info('ffmpeg cmd = {}'.format(cmd))
    subprocess.run(cmd, check=True)

def convert_archival(path, outpath):
    pass

def convert_audio(path, outpath):
    logger.info("Extracting audio")
    output_file = os.path.join(outpath, f"audio.m4a")
    audio_extraction=["ffmpeg", "-y",
                      "-i", path,
                      "-vn", # Strip video
                      "-c:a", "aac",
                      "-ac", "2",
                      output_file]
    subprocess.run(audio_extraction, check=True)
    logger.info("Finished extracting audio!")


if __name__ == '__main__':
    args = parse_args()
    if args.category == 'streaming':
        convert_streaming(args.path, args.output, args.raw_width, args.raw_height, args.resolutions)
    elif args.category == 'archival':
        convert_archival(args.path, args.output)
    elif args.category == 'audio':
        convert_audio(args.path, args.output)
