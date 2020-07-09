#!/usr/bin/env python

import argparse
import logging
import subprocess
import json
import os

from ..util.get_api import get_api
from ..openapi.tator_openapi.models import CreateResponse

from .upload import upload_file
from .make_fragment_info import make_fragment_info

logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description='Transcodes a raw video.')
    parser.add_argument('--host', type=str, default='https://www.tatorapp.com', help='Host URL.')
    parser.add_argument('--token', type=str, help='REST API token.')
    parser.add_argument('--media', type=int, help='Unique integer identifying a media.')
    parser.add_argument('--category', required=True, help='One of streaming, archival, or audio.')
    parser.add_argument('--raw_width', type=int, help='Pixel width of original video.')
    parser.add_argument('--raw_height', type=int, help='Pixel height of original video.')
    parser.add_argument('--resolutions', type=str, help='Comma separated list of output resolutions.')
    parser.add_argument('--gid', type=str, help='Group ID for this upload for sending progress.')
    parser.add_argument('--uid', type=str, help='Unique ID for this upload for sending progress.')
    parser.add_argument('--input', type=str, help='Path to raw video.')
    parser.add_argument("-o", "--output");
    return parser.parse_args()

def make_video_definition(disk_file):
    cmd = [
        "ffprobe",
        "-v","error",
        "-show_entries", "stream",
        "-print_format", "json",
        "-select_streams", "v",
        disk_file,
    ]
    output = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout
    video_info = json.loads(output)
    stream_idx=0
    for idx, stream in enumerate(video_info["streams"]):
        if stream["codec_type"] == "video":
            stream_idx=idx
            break
    stream = video_info["streams"][stream_idx]
    video_def = {"resolution": (stream["height"], stream["width"]),
                 "codec": stream["codec_name"],
                 "codec_description": stream["codec_long_name"],
                 "size": os.stat(disk_file).st_size,
                 "bit_rate": int(stream["bit_rate"])}
    return video_def

def convert_streaming(host, token, media, path, outpath, raw_width, raw_height, resolutions, gid, uid):
    print(f"Transcoding {path} to {outpath}...")
    # Get workload parameters.
    os.makedirs(outpath, exist_ok=True)
    vid_dims = [raw_height, raw_width]
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

    for resolution in resolutions:
        output_file = os.path.join(outpath, f"{resolution}.mp4")

        segments_file = os.path.join(outpath, f"{resolution}.json")
        make_fragment_info(output_file, segments_file)

        logger.info("Uploading transcoded file...")
        url = upload_file(output_file, host)
       
        logger.info("Uploading segments file...")
        segments_url = upload_file(segments_file, host)

        # Construct move video spec.
        spec = {
            'media_files': {'streaming': [{
                **make_video_definition(output_file),
                'url': url,
                'segments_url': segments_url,
            }]}
        }
        if gid is not None and uid is not None:
            spec['gid'] = gid
            spec['uid'] = uid

        # Move video file with the api.
        api = get_api(host, token)
        response = api.move_video(media, move_video_spec=spec)
        assert isinstance(response, CreateResponse)

def default_archival_upload(api, host, media, path):
    # Default action if no archive config is upload raw video.
    url = upload_file(path, host)
   
    # Move video file with the api.
    response = api.move_video(media, move_video_spec={
        'media_files': {'archival': [{
            **make_video_definition(path),
            'url': url,
        }]},
    })
    assert isinstance(response, CreateResponse)

def convert_archival(host, token, media, path, outpath, raw_width, raw_height):
    # Retrieve this media's type to inspect archive config.
    api = get_api(host, token)
    media_obj = api.get_media(media)
    media_type = api.get_media_type(media_obj.meta)

    if media_type.archive_config is None:
        default_archival_upload(api, host, media, path)
    else:
        for idx, archive_config in enumerate(media_type.archive_config):
            if archive_config.encode is None: 
                # If no encode, just use the original file.
                output_file = path
            else:
                # Encode the media to archival format.
                os.makedirs(outpath, exist_ok=True)
                output_file = os.path.join(outpath, f"archival_{idx}.mp4")
                cmd = [
                    "ffmpeg", "-y",
                    "-i", path,
                    "-vcodec", archive_config.encode.vcodec,
                    "-crf", str(archive_config.encode.crf),
                    "-preset", archive_config.encode.preset,
                    "-tune", archive_config.encode.tune,
                    "-pix_fmt", "yuv420p",
                    output_file
                ]
                logger.info('ffmpeg cmd = {}'.format(cmd))
                subprocess.run(cmd, check=True)
                
            if archive_config.s3_storage is None:
                default_archival_upload(api, host, media, output_file)
            else:
                import boto3
                # Get credentials from config object.
                aws_access_key = archive_config.s3_storage.aws_access_key
                aws_secret_access_key = archive_config.s3_storage.aws_secret_access_key
                bucket_name = archive_config.s3_storage.bucket_name
                logger.info(f"Uploading {output_file} to S3 bucket {bucket_name}...")

                # Upload the video to S3.
                client = boto3.client('s3', aws_access_key_id=aws_access_key,
                                      aws_secret_access_key=aws_secret_access_key)
                client.upload_file(output_file, bucket_name, os.path.basename(output_file))

def make_audio_definition(disk_file):
    cmd = [
        "ffprobe",
        "-v","error",
        "-show_entries", "stream",
        "-print_format", "json",
        "-select_streams", "a",
        disk_file,
    ]
    output = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout
    audio_info = json.loads(output)
    stream_idx=0
    for idx, stream in enumerate(audio_info["streams"]):
        if stream["codec_type"] == "audio":
            stream_idx=idx
            break
    stream = audio_info["streams"][stream_idx]
    audio_def = {"codec": stream["codec_name"],
                 "codec_description": stream["codec_long_name"],
                 "size": os.stat(disk_file).st_size,
                 "bit_rate": int(stream["bit_rate"])}
    return audio_def

def convert_audio(host, token, media, path, outpath):
    os.makedirs(outpath, exist_ok=True)
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
  
    # Upload audio. 
    url = upload_file(output_file, host)
   
    # Move video file with the api.
    api = get_api(host, token)
    response = api.move_video(media, move_video_spec={
        'media_files': {'audio': [{
            **make_audio_definition(output_file),
            'url': url,
        }]},
    })
    assert isinstance(response, CreateResponse)

if __name__ == '__main__':
    args = parse_args()
    if args.category == 'streaming':
        if args.resolutions == '':
            resolutions = []
        else:
            resolutions = [int(res) for res in args.resolutions.split(',')]
        convert_streaming(args.host, args.token, args.media, args.input, args.output,
                          args.raw_width, args.raw_height, resolutions, args.gid, args.uid)
    elif args.category == 'archival':
        convert_archival(args.host, args.token, args.media, args.input, args.output,
                         args.raw_width, args.raw_height)
    elif args.category == 'audio':
        convert_audio(args.host, args.token, args.media, args.input, args.output)
