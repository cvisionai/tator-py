#!/usr/bin/env python

import argparse
import logging
import subprocess
import json
import os
import sys

from ..util.get_api import get_api
from ..openapi.tator_openapi.models import CreateResponse

from .upload import upload_file
from .make_fragment_info import make_fragment_info

logger = logging.getLogger(__name__)

# If HW is available, use this as lookup swap
encoder_lookup=None

def find_best_encoder(codec):
    """ Find the best encoder based on what is available on the system """
    global encoder_lookup
    if encoder_lookup is None:
        # Default codecs
        encoder_lookup={"hevc": "libsvt_hevc",
                        "h264": "libx264"}
        cmd = [
            "ffmpeg",
            "-encoders" ]
        output=subprocess.run(cmd,stdout=subprocess.PIPE,check=True).stdout.decode()
        if output.find("hevc_qsv") >= 0:
            encoder_lookup["hevc"] = "hevc_qsv"
        if output.find("h264_qsv") >= 0:
            encoder_lookup["h264"] = "h264_qsv"
        print(f"encoder_lookup = {encoder_lookup}")
    return encoder_lookup.get(codec,codec)

def parse_args():
    parser = argparse.ArgumentParser(description='Transcodes a raw video.')
    parser.add_argument('--host', type=str, default='https://www.tatorapp.com', help='Host URL.')
    parser.add_argument('--token', type=str, help='REST API token.')
    parser.add_argument('--media', type=int, help='Unique integer identifying a media.')
    parser.add_argument('--category', required=True, help='One of streaming, archival, or audio.')
    parser.add_argument('--raw_width', type=int, help='Pixel width of original video.')
    parser.add_argument('--raw_height', type=int, help='Pixel height of original video.')
    parser.add_argument('--configs', type=str, help='Comma separated list of output configs, '
                                                    'format is resolution:crf:codec.')
    parser.add_argument('--input', type=str, help='Path to raw video.')
    parser.add_argument("-o", "--output")
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
                 "bit_rate": int(stream.get("bit_rate",-1))}
    return video_def

def convert_streaming(host, token, media, path, outpath, raw_width, raw_height, configs):
    print(f"Transcoding {path} to {outpath}...")
    # Get workload parameters.
    os.makedirs(outpath, exist_ok=True)

    # Convert settings into resolution/crf/codec.
    resolutions = [int(config.split(':')[0]) for config in configs]
    crfs = [config.split(':')[1] for config in configs]
    codecs = [config.split(':')[2] for config in configs]

    # Need to get avg_framerate
    cmd = [
        "ffprobe",
        "-v","error",
        "-show_entries", "stream",
        "-print_format", "json",
        "-select_streams", "v",
        path,
    ]
    output = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout
    video_info = json.loads(output)
    avg_frame_rate=video_info['streams'][0]['avg_frame_rate']

    vid_dims = [raw_height, raw_width]
    cmd = [
        "ffmpeg", "-y",
        "-i", path,
        "-i", os.path.join(os.path.dirname(os.path.abspath(__file__)), "black.mp4"),
    ]

    per_res = ["-an",
        "-metadata:s", "handler_name=tator",
        "-g", "25",
        "-preset", "fast",
        "-movflags",
        "faststart+frag_keyframe+empty_moov+default_base_moof",
        "-tune", "fastdecode",]

    print(f"Transcoding to {resolutions}")
    for ridx, resolution in enumerate(resolutions):
        logger.info(f"Generating resolution @ {resolution}")
        output_file = os.path.join(outpath, f"{resolution}.mp4")
        codec = find_best_encoder(codecs[ridx])
        quality_flag = "-crf"
        pixel_format = "yuv420p"
        if codec.find("qsv") >= 0:
            quality_flag = "-global_quality"
            pixel_format = "nv12"
        cmd.extend([*per_res,
                    "-vcodec", codec,
                    "-pix_fmt", pixel_format,
                    quality_flag, crfs[ridx],
                    "-filter_complex",
                    # Scale the black mp4 to the input resolution prior to concating and scaling back down.
                    f"[0:v:0]yadif[a{ridx}];[a{ridx}]setsar=1[vid{ridx}];[1:v:0]scale={vid_dims[1]}:{vid_dims[0]},setsar=1[bv{ridx}];[vid{ridx}][bv{ridx}]concat=n=2:v=1:a=0[rv{ridx}];[rv{ridx}]scale=-2:{resolution}[catv{ridx}];[catv{ridx}]pad=ceil(iw/2)*2:ceil(ih/2)*2[norate{ridx}];[norate{ridx}]fps={avg_frame_rate}[outv{ridx}]",
                    "-map", f"[outv{ridx}]",
                    output_file])

    logger.info('ffmpeg cmd = {}'.format(cmd))
    subprocess.run(cmd, check=True)
    api = get_api(host, token)

    for resolution in resolutions:
        output_file = os.path.join(outpath, f"{resolution}.mp4")

        segments_file = os.path.join(outpath, f"{resolution}.json")
        make_fragment_info(output_file, segments_file)

        logger.info("Uploading transcoded file...")
        url = upload_file(output_file, api)

        logger.info("Uploading segments file...")
        segments_url = upload_file(segments_file, api)

        # Construct move video spec.
        spec = {
            'media_files': {'streaming': [{
                **make_video_definition(output_file),
                'url': url,
                'segments_url': segments_url,
            }]}
        }

        # Move video file with the api.
        response = api.move_video(media, move_video_spec=spec)
        assert isinstance(response, CreateResponse)

def default_archival_upload(api, host, media, path, encoded):
    # Default action if no archive config is upload raw video.
    url = upload_file(path, api)
    video_def = make_video_definition(path)

    # If video was encoded, set codec_mime to video/mp4; otherwise do
    # not set codec_mime.
    if encoded:
        video_def['codec_mime'] = 'video/mp4'

    # Move video file with the api.
    response = api.move_video(media, move_video_spec={
        'media_files': {'archival': [{
            **video_def,
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
        default_archival_upload(api, host, media, path, False)
    else:
        for idx, archive_config in enumerate(media_type.archive_config):
            if archive_config.encode is None:
                # If no encode, just use the original file.
                output_file = path
            else:
                # Encode the media to archival format.
                os.makedirs(outpath, exist_ok=True)
                output_file = os.path.join(outpath, f"archival_{idx}.mp4")
                codec = find_best_encoder(archive_config.encode.vcodec)
                quality_flag = "-crf"
                pixel_format = "yuv420p"
                tune_settings = ["-preset", archive_config.encode.preset,
                                 "-tune", archive_config.encode.tune]
                if codec.find("qsv") >= 0:
                    quality_flag = "-global_quality"
                    pixel_format = "nv12"
                    tune_settings=[] #QSV doesn't do tuning
                elif codec == "libsvt_hevc":
                    # SVT for HEVC does not do tuning or CRF
                    tune_settings=[]
                    quality_flag = "-global_quality"
                cmd = [
                    "ffmpeg", "-y",
                    "-i", path,
                    "-vcodec", codec,
                    "-vf", "yadif",
                    quality_flag, str(archive_config.encode.crf),
                    "-pix_fmt", pixel_format,
                    *tune_settings
                ]
                if archive_config.encode.vcodec == 'hevc':
                    cmd += ["-tag:v", "hvc1"]
                elif archive_config.encode.vcodec == 'h264':
                    cmd += ["-tag:v", "avc1"]
                cmd.append(output_file)
                    
                logger.info('ffmpeg cmd = {}'.format(cmd))
                subprocess.run(cmd, check=True)

            if archive_config.s3_storage is None:
                default_archival_upload(api, host, media, output_file, True)
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
                 "bit_rate": int(stream.get("bit_rate",-1))}
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
    api = get_api(host, token)
    url = upload_file(output_file, api)
   
    # Move video file with the api.
    response = api.move_video(media, move_video_spec={
        'media_files': {'audio': [{
            **make_audio_definition(output_file),
            'url': url,
        }]},
    })
    assert isinstance(response, CreateResponse)

def get_length_info(stream):
    """ Given a json dump of the stream return the length of the video """
    fps_fractional = stream["avg_frame_rate"].split("/")
    fps = float(fps_fractional[0]) / float(fps_fractional[1])

    start_time = float(stream["start_time"])
    if 'duration' in stream:
        seconds = float(stream["duration"])
    elif 'tags' in stream:
        if 'DURATION' in stream['tags']:
            length = stream['tags']['DURATION'].split(':')
            seconds = float(length[0])*3600
            seconds += float(length[1])*60
            seconds += float(length[2])
    else:
        raise Exception('No way to determine file length!')

    num_frames = float(fps * seconds)
    return fps,int(num_frames)

if __name__ == '__main__':
    args = parse_args()
    if args.category == 'streaming':
        if args.configs == '':
            configs = []
        else:
            configs = [res for res in args.configs.split(',')]
        convert_streaming(args.host, args.token, args.media, args.input, args.output,
                          args.raw_width, args.raw_height, configs)
    elif args.category == 'archival':
        convert_archival(args.host, args.token, args.media, args.input, args.output,
                         args.raw_width, args.raw_height)
    elif args.category == 'audio':
        convert_audio(args.host, args.token, args.media, args.input, args.output)
