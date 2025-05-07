#!/usr/bin/env python

import argparse
import logging
import subprocess
import json
import os
import sys
import psutil
import time

from ..util.get_api import get_api
from ..util._upload_file import _upload_file
from ..openapi.tator_openapi.models import MessageResponse

from .make_fragment_info import make_fragment_info

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# If HW is available, use this as lookup swap
encoder_lookup=None

SW_TO_HW_PIXEL_FORMAT_CONVERSION = {
    'yuv420p': 'nv12', # QSV h264 supports this
    'yuv420p10le': 'p010le', # QSV h264 supports this
    'yuv422p': 'nv16', # Not sure if any hw encoders actually support this
    'yuv444p' : 'nv21' # Not sure if any hw encoders actually support this
}

def _get_resource_usage():
    """ Returns an object representing memory + CPU usage """
    cpu_percentages=psutil.cpu_percent(percpu=True)
    load_avg = psutil.getloadavg()
    memory_raw = psutil.virtual_memory()
    memory_utilization = (memory_raw.used / memory_raw.total) * 100
    memory_in_gb = memory_raw.used / 1024 / 1024
    return {'cpu_percentages': cpu_percentages,
           'load_avg': load_avg,
           'memory_utilization': memory_utilization,
           'memory_in_gb': memory_in_gb}
def _launch_and_monitor_resources(cmd, interval=5):
    proc = subprocess.Popen(cmd)
    start = time.time()
    while proc.returncode == None:
        try:
            proc.wait(timeout=interval)
        except subprocess.TimeoutExpired:
            pass # we don't care
        logger.info(f"RESOURCE_INFO = {json.dumps(_get_resource_usage())}")
    if proc.returncode != 0:
        raise RuntimeError("Transcode process failed")
    end = time.time()
    logger.info(f"cmd={cmd}")
    logger.info(f"time={end-start}")

def find_best_encoder(codec, hwaccel=False):
    """ Find the best encoder based on what is available on the system """
    global encoder_lookup
    if encoder_lookup is None:
        # Default codecs
        encoder_lookup={"hevc": os.getenv("TATOR_HEVC_ENCODER", "libx265"),
                        "h264": os.getenv("TATOR_H264_ENCODER", "libx264"),
                        "av1": os.getenv("TATOR_AV1_ENCODER", "libsvtav1")}
        if hwaccel:
            cmd = [
                "ffmpeg",
                "-encoders" ]
            output=subprocess.run(cmd,stdout=subprocess.PIPE,check=True).stdout.decode()
            # Look for QSV, but use VAAPI frontend
            # TODO: Use `vainfo` directly to query available hardware entry points
            if output.find("libsvt_hevc") >= 0:
                encoder_lookup["hevc"] = "libsvt_hevc"
            if output.find("hevc_qsv") >= 0:
                encoder_lookup["hevc"] = "hevc_vaapi"
            if output.find("h264_qsv") >= 0:
                encoder_lookup["h264"] = "h264_vaapi"
            if output.find("av1_qsv") >= 0:
                encoder_lookup["av1"] = "av1_vaapi"
        logger.info("encoder_lookup = %s", encoder_lookup)
    return encoder_lookup.get(codec, codec)

def parse_args():
    parser = argparse.ArgumentParser(description='Transcodes a raw video.')
    parser.add_argument('--url', type=str, help='URL where original file is hosted.')
    parser.add_argument('--work_dir', type=str, help='Directory where info should be saved.')
    parser.add_argument('--host', type=str, default='https://cloud.tator.io', help='Host URL.')
    parser.add_argument('--token', type=str, help='REST API token.')
    parser.add_argument('--media', type=int, help='Unique integer identifying a media.')
    parser.add_argument('--category', required=True, help='One of streaming, archival, or audio.')
    parser.add_argument('--raw_width', type=int, help='Pixel width of original video.')
    parser.add_argument('--raw_height', type=int, help='Pixel height of original video.')
    parser.add_argument('--configs', type=str, help='Comma separated list of output configs, '
                                                    'format is resolution:crf:codec.')
    parser.add_argument('--size', type=int, help='Size of the file, if not inferrable')
    parser.add_argument('--hwaccel', action='store_true', help="Use hardware acceleration.")
    parser.add_argument('--force_fps', type=float, default=-1, help='Force a specific fps for the video.')
    parser.add_argument('--bucket_id', type=int, help='Bucket ID if not default.')
    return parser.parse_args()

def get_length_of_file(path):
    cmd = [
        "ffprobe",
        "-v","error",
        "-show_entries", "stream:format=duration",
        "-print_format", "json",
        "-select_streams", "v",
        path,
    ]
    output = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout
    video_info = json.loads(output)
    stream_idx=0
    for idx, stream in enumerate(video_info["streams"]):
        if stream["codec_type"] == "video":
            stream_idx=idx
            break
    stream = video_info["streams"][stream_idx]
    stream = {**video_info.get("format", {}), **stream}
    fps, length = get_length_info(stream)
    return fps, length

def make_video_definition(path, size=None):
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
    stream_idx=0
    if size is None or size <= 0:
        size = os.stat(path).st_size
    for idx, stream in enumerate(video_info["streams"]):
        if stream["codec_type"] == "video":
            stream_idx=idx
            break
    stream = video_info["streams"][stream_idx]
    video_def = {"resolution": (stream["height"], stream["width"]),
                 "codec": stream["codec_name"],
                 "codec_description": stream["codec_long_name"],
                 "size": size,
                 "bit_rate": int(stream.get("bit_rate",-1))}
    return video_def

def convert_streaming(host, token, media, path, outpath, raw_width, raw_height, configs, hwaccel=False, inhibit_upload=False, force_fps=-1, filter_complex=None, bucket_id=None):
    logger.info("Transcoding %s to %s...", path, outpath)
    # Get workload parameters.
    os.makedirs(outpath, exist_ok=True)

    # Convert settings into resolution/crf/codec/presets/pixel_formats.
    resolutions = [int(config.split(':')[0]) for config in configs]
    crfs = [config.split(':')[1] for config in configs]
    codecs = [config.split(':')[2] for config in configs]
    presets = [config.split(':')[3] for config in configs] # Presets must be the same for all outputs in a multiheaded transcode

    # Handle pixel format addition as an optional argument
    # This will maintain backwards API compatibility to folks using
    # this function
    # TODO: It'd be nice if we didn't pass in the config so awkwardly.
    pixel_formats = []
    for c in configs:
        split_comps = c.split(':')
        if len(split_comps) == 5:
            pixel_formats.append(split_comps[4])
        else:
            pixel_formats.append("yuv420p")

    # Need to get avg_framerate
    if isinstance(path, list):
        # Assume that files are the same frame rate and resolution
        ffprobe_path = path[0]
    else:
        ffprobe_path = path

    cmd = [
        "ffprobe",
        "-v","error",
        "-show_entries", "stream",
        "-print_format", "json",
        "-select_streams", "v",
        ffprobe_path,
    ]
    output = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout
    video_info = json.loads(output)
    if force_fps < 0:
        avg_frame_rate=video_info['streams'][0]['avg_frame_rate']
        fps_fractional = avg_frame_rate.split("/")
        avg_frame_rate = float(fps_fractional[0]) / float(fps_fractional[1])
        avg_frame_rate = round(avg_frame_rate, 4)
    else:
        avg_frame_rate=force_fps
    tags=video_info['streams'][0].get('tags')
    rotation = 0
    if tags is not None:
        rotation = int(tags.get('rotate', "0")) % 360
    transpose = "null"
    if rotation == 90:
        transpose = "transpose=2"
    elif rotation == 180:
        transpose = "hflip,vflip"
    elif rotation == 270:
        transpose = "transpose=1"

    if video_info['streams'][0].get('field_order') == "progressive":
        yadif = "null"
    else:
        yadif = "yadif"

    vid_dims = [raw_height, raw_width]
    cmd = [
        "ffmpeg", "-y",
        "-loglevel", "error",
        "-progress", "-",
        "-stats_period", "10"
    ]
    # We are going to concatenate multiple segments together
    if isinstance(path, list):
        num_segments = len(path)
        for segment in path:
            cmd.extend(["-noautorotate", "-i", segment])
    else:
        num_segments = 1
        cmd.extend(["-noautorotate", "-i", path])
        cmd.extend(["-noautorotate", "-i", os.path.join(os.path.dirname(os.path.abspath(__file__)), "black.mp4")])
    
    hw_upload = ''
    vaapi_present = [c for c in codecs if find_best_encoder(c, hwaccel).find('vaapi') >= 0]
    if vaapi_present:
        cmd.extend(['-init_hw_device', 'vaapi=hw',
                    '-filter_hw_device', 'hw'])

    logger.info("Transcoding to %s", resolutions)

    cmd.extend(["-filter_complex"])
    # Construct the complex filter
    filter_parts = []
    if filter_complex is None:
        if num_segments == 1:
            if vaapi_present:
                seg_idx = 0
                hw_upload=f'[uf{seg_idx}];[uf{seg_idx}]format={pixel_format}[format{seg_idx}];[format{seg_idx}]hwupload'
            # Scale the black mp4 to the input resolution prior to concating and scaling back down.
            filter_string=f"[0:v:0]{transpose}[rot0];[rot0]{yadif}[a];[a]setsar=1[vid];[vid]fps={avg_frame_rate}{hw_upload}[vid_fps];[1:v:0]scale={vid_dims[1]}:{vid_dims[0]},setsar=1[bv];[bv]fps={avg_frame_rate}[bv_fps];[vid_fps][bv_fps]concat=n=2:v=1:a=0[concatenated];"
        else:
            filter_string = ""
            if vaapi_present:
                hw_upload=f'[uf{seg_idx}];[uf{seg_idx}]format={pixel_format}[format{seg_idx}];[format{seg_idx}]hwupload'
            for seg_idx in range(num_segments):
                filter_string += f"[{seg_idx}:v:0]{transpose}[rot{seg_idx}];[rot{seg_idx}]yadif[a{seg_idx}];[a{seg_idx}]setsar=1[vid{seg_idx}];[vid{seg_idx}]fps={avg_frame_rate}{hw_upload}[vid_fps{seg_idx}];"
                
            filter_string += f"[{num_segments}:v:0]scale={vid_dims[1]}:{vid_dims[0]},setsar=1[bv];"
            filter_string += "".join([f"[vid_fps{seg_idx}]" for seg_idx in range(num_segments)]) 
                
            filter_string += f"[bv]concat=n={num_segments+1}:v=1:a=0[concatenated];"
            filter_parts.append(filter_string)

    else:
        #width = round(raw_width * resolution / raw_height)
        filter_string = filter_complex.format(fps=avg_frame_rate, hw_upload=hw_upload)
        #filter_parts.append(filter_complex.format(fps=avg_frame_rate, hw_upload=hw_upload))

    # Add split parameters for each resolution
    split_output_labels = "".join([f"[split{ridx}]" for ridx in range(len(resolutions))])
    scale_parts = "".join([f"[split{ridx}]scale=-2:{resolution},pad=ceil(iw/2)*2:ceil(ih/2)*2[outv{ridx}];" for ridx,resolution in enumerate(resolutions)])
    # Last part of scale parts should now be ";" and needs to be removed
    if scale_parts.endswith(";"):
        scale_parts = scale_parts[:-1]
    filter_string += f"[concatenated] split={len(resolutions)} " + split_output_labels + ";" + scale_parts
    filter_parts.append(filter_string)
    cmd.extend(filter_parts)
    for ridx, resolution in enumerate(resolutions):
        per_res = ["-an",
            "-metadata:s", "handler_name=tator",
            "-metadata:s", "rotate=0",
            "-g", "25",
            "-movflags",
            "faststart+frag_keyframe+empty_moov+default_base_moof"]
        logger.info(f"Generating resolution @ {resolution}")
        output_file = os.path.join(outpath, f"{resolution}.mp4")
        codec = find_best_encoder(codecs[ridx], hwaccel)
        quality_flag = "-crf"
        pixel_format = pixel_formats[ridx]
        
        preset = presets[ridx]
        if codec.find("qsv") >= 0:
            quality_flag = "-global_quality"
        if codec.find("vaapi") >= 0:
            quality_flag = "-global_quality"
            pixel_format = SW_TO_HW_PIXEL_FORMAT_CONVERSION[pixel_format]
        if codec.find('264') > 0:
            preset = preset if preset else 'fast'
            per_res.extend(["-preset", preset,
                            "-tune", "fastdecode"])
        if codec.find('libsvtav1') >= 0:
            preset = preset if preset else '5'
            per_res.extend(['-preset', preset, "-tune", "fastdecode"])

        cmd.extend([f"-map", f"[outv{ridx}]",
                    *per_res,
                    "-vcodec", codec,
                    "-pix_fmt", pixel_format,
                    quality_flag, crfs[ridx],
                    output_file
                    ])
        
        

    logger.info('ffmpeg cmd = {}'.format(cmd))
    _launch_and_monitor_resources(cmd)

    api = get_api(host, token)
    media_obj = api.get_media(media)

    # Skip this check for now, need to calculate concat duration for concat files
    '''
    for ridx, resolution in enumerate(resolutions):
        output_file = os.path.join(outpath, f"{resolution}.mp4")
        _, res_length = get_length_of_file(output_file)
        length_delta = abs((media_obj.num_frames - res_length)/media_obj.num_frames)
        assert length_delta < 0.1 # Assert length delta is less than 10 percent.
    '''
    
    # if we are inhibiting upload, we are done!
    if inhibit_upload:
        return

    for resolution in resolutions:
        output_file = os.path.join(outpath, f"{resolution}.mp4")

        segments_file = os.path.join(outpath, f"{resolution}.json")
        make_fragment_info(output_file, segments_file)

        logger.info("Uploading transcoded file...")
        for progress, upload_info in _upload_file(api, media_obj.project, output_file,
                                                  media_id=media, filename=os.path.basename(output_file), bucket_id=bucket_id):
            logger.info(f"Progress: {progress}%")

        logger.info("Uploading segments file...")
        for progress, segment_info in _upload_file(api, media_obj.project, segments_file,
                                                  media_id=media, filename=os.path.basename(segments_file), bucket_id=bucket_id):
            logger.info(f"Progress: {progress}%")

        # Construct video definition.
        video_def = {
            **make_video_definition(output_file),
            'path': upload_info.key,
            'segment_info': segment_info.key,
        }

        # Patch in video file with the api.
        response = api.create_video_file(media, role='streaming', video_definition=video_def, bucket_id=bucket_id)
        assert isinstance(response, MessageResponse)

def default_archival_upload(api, host, media, path, encoded, size, bucket_id=None):
    # Default action if no archive config is upload raw video.
    media_obj = api.get_media(media)
    logger.info(f"Uploading original file as archival...")
    for progress, upload_info in _upload_file(api, media_obj.project, path,
                                              media_id=media, filename=os.path.basename(path), file_size=size, bucket_id=bucket_id):
        logger.info(f"Progress: {progress}%")
    video_def = make_video_definition(path, size)

    # If video was encoded, set codec_mime to video/mp4; otherwise do
    # not set codec_mime.
    if encoded:
        video_def['codec_mime'] = 'video/mp4'

    # Patch in video file with the api.
    video_def['path'] = upload_info.key
    response = api.create_video_file(media, role='archival', video_definition=video_def, bucket_id=bucket_id)
    assert isinstance(response, MessageResponse)


def convert_archival(
    host,
    token,
    media,
    path,
    outpath,
    raw_width,
    raw_height,
    size=None,
    explicit_config=None,
    hwaccel=False,
    inhibit_upload=False,
    bucket_id=None
):
    # Retrieve this media's type to inspect archive config.
    api = get_api(host, token)
    media_obj = api.get_media(media)
    media_type = api.get_media_type(media_obj.type)
    config = explicit_config or media_type.archive_config
    if config is not None:
        for idx, archive_config in enumerate(config):
            os.makedirs(outpath, exist_ok=True)
            output_file = os.path.join(outpath, f"archival_{idx}.mp4")
            if archive_config.encode.vcodec == 'copy':
                # If no encode, just use the original file.
                output_file = path
            else:
                # Encode the media to archival format.
                codec = find_best_encoder(archive_config.encode.vcodec, hwaccel)
                quality_flag = "-crf"
                pixel_format = archive_config.encode.pixel_format
                tune_settings = ["-preset", archive_config.encode.preset,
                                 "-tune", archive_config.encode.tune]
                if archive_config.encode.movflags:
                    tune_settings.extend(['-movflags', archive_config.encode.movflags])
                if codec.find("qsv") >= 0:
                    quality_flag = "-global_quality"
                    pixel_format = SW_TO_HW_PIXEL_FORMAT_CONVERSION[pixel_format]
                    tune_settings=[] #QSV doesn't do tuning
                elif codec == "libsvt_hevc":
                    # SVT for HEVC does not do tuning or CRF
                    tune_settings=[]
                    quality_flag = "-global_quality"

                hw_preamble = []
                vaapi_present = codec.find('vaapi') >= 0
                if vaapi_present:
                    hw_preamble = ['-init_hw_device', 'vaapi=hw',
                                   '-filter_hw_device', 'hw']
                cmd = [
                    "ffmpeg",
                    "-loglevel", "error",
                    "-progress", "-",
                    "-stats_period", "10",
                    *hw_preamble,
                    "-y",
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
                _launch_and_monitor_resources(cmd)

            if inhibit_upload:
                continue
            if archive_config.s3_storage is None:
                default_archival_upload(api, host, media, output_file, True, size, bucket_id=bucket_id)
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


def convert_audio(host, token, media, path, outpath, inhibit_upload=False, bucket_id=None):
    if isinstance(path, list):
        logger.info("Concatenation with audio not supported yet")
        return
    os.makedirs(outpath, exist_ok=True)
    logger.info("Extracting audio")
    output_file = os.path.join(outpath, f"audio.m4a")
    audio_extraction=["ffmpeg", "-y",
                      "-loglevel", "error",
                      "-progress", "-",
                      "-stats_period", "10",
                      "-i", path,
                      "-vn", # Strip video
                      "-c:a", "aac",
                      "-ac", "2",
                      output_file]
    subprocess.run(audio_extraction, check=True)
    logger.info("Finished extracting audio!")

    if inhibit_upload:
        return

    # Upload audio.
    api = get_api(host, token)
    media_obj = api.get_media(media)
    for progress, upload_info in _upload_file(api, media_obj.project, output_file,
                                              media_id=media, filename=os.path.basename(output_file), bucket_id=bucket_id):
        logger.info(f"Progress: {progress}%")

    # Patch in audio file with the api.
    audio_def = {**make_audio_definition(output_file),
                 'path': upload_info.key}
    response = api.create_audio_file(media, role='audio', audio_definition=audio_def, bucket_id=bucket_id)
    assert isinstance(response, MessageResponse)


def get_length_info(stream):
    """ Given a json dump of the stream return the length of the video """
    fps_fractional = stream["avg_frame_rate"].split("/")
    fps = float(fps_fractional[0]) / float(fps_fractional[1])

    if 'duration' in stream:
        seconds = float(stream["duration"])
    elif 'tags' in stream and 'DURATION' in stream['tags']:
        length = stream['tags']['DURATION'].split(':')
        seconds = float(length[0])*3600
        seconds += float(length[1])*60
        seconds += float(length[2])
    else:
        raise Exception('No way to determine file length!')

    num_frames = float(fps * seconds)
    return fps,int(num_frames)

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    # Parse arguments.
    args = parse_args()

    if args.category == 'streaming':
        if args.configs == '':
            configs = []
        else:
            configs = [res for res in args.configs.split(',')]
        convert_streaming(args.host, args.token, args.media, args.url, args.work_dir,
                          args.raw_width, args.raw_height, configs, args.hwaccel, False, args.force_fps, bucket_id=args.bucket_id)
    elif args.category == 'archival':
        convert_archival(args.host, args.token, args.media, args.url, args.work_dir,
                         args.raw_width, args.raw_height, args.size, bucket_id=args.bucket_id)
    elif args.category == 'audio':
        convert_audio(args.host, args.token, args.media, args.url, args.work_dir, bucket_id=args.bucket_id)
