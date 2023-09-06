"""Utility used to copy a streaming file from one media to another.

This downloads the streaming file from one media, re-uploads it, and adds the video file definition at the specified streaming resolution in the destination media.
It is added to the end of the streaming list.
Does not check if a streaming file with the same resolution exists.

"""

import argparse
import logging
import os
import sys

import tator
from tator.util._upload_file import _upload_file
from tator.util._download_file import _download_file

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args() -> argparse.Namespace:
    """ Parse script's arguments
    """

    help_parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser = tator.get_parser(parser=help_parser)
    parser.add_argument("--work-folder", type=str, required=True, help="Folder to download the large video files temporarily to")
    parser.add_argument("--src-media", type=int, required=True, help="Source media ID")
    parser.add_argument("--dest-media", type=int, required=True, help="Destination media ID")
    parser.add_argument("--resolution", type=int, required=True, help="Resolution to add from source to destination")
    parser.add_argument("--description", type=str, required=True, help="Description associated with patched video file")
    args = parser.parse_args()
    return args

def script_main() -> None:
    """
    """

    args = parse_args()

    assert os.path.exists(args.work_folder)

    tator_api = tator.get_api(host=args.host, token=args.token)

    src_media = tator_api.get_media(id=args.src_media)
    dest_media = tator_api.get_media(id=args.dest_media)

    # Find the streaming
    src_streaming = None
    for media_file in src_media.media_files.streaming:
        if media_file.resolution[0] == args.resolution:
            src_streaming = media_file
            break

    # Download the streaming file and segments json
    segment_file_path = os.path.join(args.work_folder, f"{args.resolution}_hq.json")
    logger.info(f"Downloading segment file: {src_streaming.segment_info} to {segment_file_path}")
    for progress in _download_file(
          api=tator_api,
          project=src_media.project,
          url=src_streaming.segment_info,
          out_path=segment_file_path):
        logger.info(progress)

    video_file_path = os.path.join(args.work_folder, f"{args.resolution}_hq.mp4")
    logger.info(f"Downloading video file: {src_streaming.path} to {video_file_path}")
    for progress in _download_file(
          api=tator_api,
          project=src_media.project,
          url=src_streaming.path,
          out_path=video_file_path):
        logger.info(progress)

    for progress, upload_info in _upload_file(tator_api, dest_media.project, video_file_path,
                                        media_id=dest_media.id,
                                        filename=f"{args.resolution}_hq.mp4"):
        logger.info(f"Uploading video: {progress}")
    for progress, segment_info in _upload_file(tator_api, dest_media.project, segment_file_path,
                                        media_id=dest_media.id,
                                        filename=f"{args.resolution}_hq.json"):
        logger.info(f"Uploading video: {progress}")

    os.remove(video_file_path)
    os.remove(segment_file_path)

    media_def = {
        "bit_rate": src_streaming.bit_rate,
        "codec": src_streaming.codec,
        "codec_description": src_streaming.codec_description,
        "codec_mime": src_streaming.codec_mime,
        "description": args.description,
        "host": src_streaming.host,
        "http_auth": src_streaming.http_auth,
        "path": upload_info.key,
        "resolution": src_streaming.resolution,
        "segment_info": segment_info.key,
        "size": src_streaming.size,
    }
    final_media_def = {}
    for field in media_def:
        if media_def[field] is not None:
            final_media_def[field] = media_def[field]
    response = tator_api.create_video_file(
        id=dest_media.id,
        role="streaming",
        video_definition=final_media_def)
    logger.info(response)

if __name__ == "__main__":
    script_main()