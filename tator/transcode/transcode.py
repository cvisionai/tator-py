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
import tator

from .make_fragment_info import make_fragment_info
from .filtergraph import build_streaming_filtergraph
from .encoder_args import (
    STREAMING_PRESET_DEFAULTS,
    STREAMING_TUNE_DEFAULTS,
    SW_TO_HW_PIXEL_FORMAT_CONVERSION, # Re-exported for existing importers
    encoder_args,
    encoder_family,
    hwupload_filters,
    parse_streaming_config,
    require_encoder,
    resolve_pixel_format,
    source_bit_depth,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# If HW is available, use this as lookup swap, keyed by whether hwaccel was requested
encoder_lookup={}

BLACK_VIDEO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "black.mp4")

# Only deinterlace frames flagged as interlaced, one output frame per input frame.
DEINTERLACE_FILTER = "bwdif=mode=send_frame:deint=interlaced"

STREAMING_GOP_SIZE = 25
STREAMING_MOVFLAGS = "frag_keyframe+empty_moov+default_base_moof"

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
def _launch_and_monitor_resources(cmd, interval=300):
    # SVT_LOG=2 keeps SVT-AV1 warnings and errors but drops its per-encoder info banner.
    env = {"SVT_LOG": "2", **os.environ}
    proc = subprocess.Popen(cmd, env=env)
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
    if hwaccel not in encoder_lookup:
        # Default codecs
        lookup={"hevc": os.getenv("TATOR_HEVC_ENCODER", "libx265"),
                "h264": os.getenv("TATOR_H264_ENCODER", "libx264"),
                "av1": os.getenv("TATOR_AV1_ENCODER", "libsvtav1")}
        if hwaccel:
            cmd = [
                "ffmpeg",
                "-encoders" ]
            output=subprocess.run(cmd,stdout=subprocess.PIPE,check=True).stdout.decode()
            # Look for QSV, but use VAAPI frontend
            # TODO: Use `vainfo` directly to query available hardware entry points
            if output.find("hevc_qsv") >= 0:
                lookup["hevc"] = "hevc_vaapi"
            if output.find("h264_qsv") >= 0:
                lookup["h264"] = "h264_vaapi"
            if output.find("av1_qsv") >= 0:
                lookup["av1"] = "av1_vaapi"
        logger.info("encoder_lookup = %s", lookup)
        encoder_lookup[hwaccel] = lookup
    return encoder_lookup[hwaccel].get(codec, codec)

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
    parser.add_argument('--configs', type=str, help='Output configs, either a JSON list of '
                                                    'streaming configs or a comma separated list '
                                                    'of resolution:crf:codec[:preset[:pixel_format]].')
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

def _get_rotation(stream):
    """ Returns the display rotation of a probed stream in degrees. """
    for side_data in stream.get("side_data_list", []):
        if "rotation" in side_data:
            return int(round(float(side_data["rotation"])))
    # ffprobe before 5.0 reported rotation as a stream tag
    return int(stream.get("tags", {}).get("rotate", 0))

def get_display_dimensions(stream):
    """ Returns (width, height) of a probed video stream's frames as ffmpeg decodes them.

    ffmpeg autorotates on decode, so a stream with a 90 or 270 degree display matrix comes out
    with its width and height swapped.
    """
    width = int(stream["width"])
    height = int(stream["height"])
    if _get_rotation(stream) % 180 == 90:
        width, height = height, width
    return width, height

def _streaming_command(path, outpath, configs, hwaccel=False, force_fps=-1, filter_complex=None):
    """ Builds the multi-output ffmpeg command for a streaming transcode.

    :returns: Tuple of the command and the output resolutions, in config order.
    """
    configs = [parse_streaming_config(config) for config in configs]
    # We are going to concatenate multiple segments together if path is a list.
    # Assume that files are the same frame rate, resolution and pixel format.
    paths = path if isinstance(path, list) else [path]
    num_segments = len(paths)

    cmd = [
        "ffprobe",
        "-v","error",
        "-show_entries", "stream",
        "-print_format", "json",
        "-select_streams", "v",
        paths[0],
    ]
    output = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout
    stream = json.loads(output)['streams'][0]
    if force_fps < 0:
        fps_fractional = stream['avg_frame_rate'].split("/")
        avg_frame_rate = float(fps_fractional[0]) / float(fps_fractional[1])
        avg_frame_rate = round(avg_frame_rate, 4)
    else:
        avg_frame_rate=force_fps
    width, height = get_display_dimensions(stream)
    source_depth = source_bit_depth(stream.get("pix_fmt"))

    outputs = []
    for config in configs:
        encoder = find_best_encoder(config["vcodec"], hwaccel)
        require_encoder(encoder, f"the {config['resolution']} {config['vcodec']} stream")
        family = encoder_family(encoder)
        pixel_format = resolve_pixel_format(encoder, config["pixel_format"],
                                            config["match_source_bit_depth"], source_depth)
        preset = config["preset"] or STREAMING_PRESET_DEFAULTS.get(family, "")
        tune = config["tune"] or STREAMING_TUNE_DEFAULTS.get(family)
        outputs.append({
            "resolution": config["resolution"],
            "filters": hwupload_filters(encoder, pixel_format),
            "args": encoder_args(encoder, config["crf"], preset, tune, pixel_format,
                                 config["encoder_params"]),
        })

    cmd = [
        "ffmpeg", "-y",
        "-loglevel", "warning",
        "-progress", "-",
        "-stats_period", "300"
    ]
    if any(output["filters"] for output in outputs):
        cmd.extend(['-init_hw_device', 'vaapi=hw',
                    '-filter_hw_device', 'hw'])
    # ffmpeg autorotates each input, so frames come out in display orientation.
    for segment in paths:
        cmd.extend(["-i", segment])
    cmd.extend(["-i", BLACK_VIDEO])

    logger.info("Transcoding to %s", [output["resolution"] for output in outputs])

    filter_string = build_streaming_filtergraph(num_segments, width, height, avg_frame_rate,
                                                outputs, DEINTERLACE_FILTER, filter_complex)
    cmd.extend([
        "-filter_complex_threads", "1",
        "-filter_complex", filter_string,
    ])
    for ridx, output in enumerate(outputs):
        logger.info(f"Generating resolution @ {output['resolution']}")
        cmd.extend(["-map", f"[outv{ridx}]",
                    "-an",
                    "-metadata:s", "handler_name=tator",
                    "-g", str(STREAMING_GOP_SIZE),
                    "-max_muxing_queue_size", "9999",
                    "-movflags", STREAMING_MOVFLAGS,
                    *output["args"],
                    "-write_tmcd", "0", # Strip off timecode metadata which can cause issues with some players (TODO: should we preserve this in some way?)
                    os.path.join(outpath, f"{output['resolution']}.mp4"),
                    ])
    return cmd, [output["resolution"] for output in outputs]

def convert_streaming(host, token, media, path, outpath, raw_width, raw_height, configs, hwaccel=False, inhibit_upload=False, force_fps=-1, filter_complex=None, bucket_id=None):
    """ Transcodes a video into streaming resolutions and uploads them to a media.

    :param configs: List of streaming configs, each a ResolutionConfig-like mapping or a
                    ``resolution:crf:codec[:preset[:pixel_format]]`` string.
    :param raw_width: Unused; dimensions are read from the source. Kept for compatibility.
    :param raw_height: Unused; dimensions are read from the source. Kept for compatibility.
    """
    logger.info("Transcoding %s to %s...", path, outpath)
    # Get workload parameters.
    os.makedirs(outpath, exist_ok=True)

    cmd, resolutions = _streaming_command(path, outpath, configs, hwaccel, force_fps,
                                          filter_complex)
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
        assert isinstance(response, tator.models.MessageResponse)

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
    assert isinstance(response, tator.models.MessageResponse)


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
                encode = archive_config.encode
                codec = find_best_encoder(encode.vcodec, hwaccel)
                require_encoder(codec, f"the {encode.vcodec} archival encode")
                hw_preamble = []
                if encoder_family(codec) == "vaapi":
                    hw_preamble = ['-init_hw_device', 'vaapi=hw',
                                   '-filter_hw_device', 'hw']
                cmd = [
                    "ffmpeg",
                    "-loglevel", "warning",
                    "-progress", "-",
                    "-stats_period", "300",
                    *hw_preamble,
                    "-y",
                    "-i", path,
                    "-vf", ",".join([DEINTERLACE_FILTER,
                                     *hwupload_filters(codec, encode.pixel_format)]),
                    *encoder_args(codec, encode.crf, encode.preset, encode.tune,
                                  encode.pixel_format, encode.encoder_params),
                ]
                if encode.movflags:
                    cmd.extend(['-movflags', encode.movflags])

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
                      "-stats_period", "300",
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
    assert isinstance(response, tator.models.MessageResponse)


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
        if not args.configs:
            configs = []
        elif args.configs.startswith('['):
            configs = json.loads(args.configs)
        else:
            configs = [res for res in args.configs.split(',')]
        convert_streaming(args.host, args.token, args.media, args.url, args.work_dir,
                          args.raw_width, args.raw_height, configs, args.hwaccel, False, args.force_fps, bucket_id=args.bucket_id)
    elif args.category == 'archival':
        convert_archival(args.host, args.token, args.media, args.url, args.work_dir,
                         args.raw_width, args.raw_height, args.size, bucket_id=args.bucket_id)
    elif args.category == 'audio':
        convert_audio(args.host, args.token, args.media, args.url, args.work_dir, bucket_id=args.bucket_id)
