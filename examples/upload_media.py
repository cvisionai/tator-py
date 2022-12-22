#!/usr/bin/env python

""" This example shows how to upload a media file.
"""

import logging
import sys
import time

import tator

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Create a parser that includes path to media file.
    parser = tator.get_parser()
    parser.add_argument("--type-id", help="Media type ID for upload.", required=True, type=int)
    parser.add_argument(
        "--chunk-size",
        help="The maximum chunk size for uploads.",
        required=False,
        type=int,
        default=10 * 1024 * 1024,
    )
    parser.add_argument("--media-path", help="Path to media file.", required=True)
    args = parser.parse_args()

    # Create the api.
    tator_api = tator.get_api(args.host, args.token)

    # Upload the media.
    for progress, response in tator.util.upload_media(
        api=tator_api, type_id=args.type_id, path=args.media_path, chunk_size=args.chunk_size
    ):
        logger.info(f"Upload progress: {progress}%")
    logger.info(response.message)

    # Take a look at transcode progress, wait until complete.
    project = tator_api.get_media_type(args.type_id).project
    while True:
        transcode = tator_api.get_transcode_list(project, uid=response.id)[0]
        if transcode.job.status == "Succeeded":
            break
        elif transcode.job.status == "Failed":
            raise ValueError("Upload failed!")
        time.sleep(10)
