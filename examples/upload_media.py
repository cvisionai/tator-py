#!/usr/bin/env python

""" This example shows how to upload a media file.
"""

import logging
import sys
import time

import tator

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # Create a parser that includes path to media file.
    parser = tator.get_parser()
    parser.add_argument('--type_id',
                        help='Media type ID for upload.',
                        required=True, type=int)
    parser.add_argument('--media_path', help='Path to media file.', required=True)
    args = parser.parse_args()

    # Create the api.
    tator_api = tator.get_api(args.host, args.token)

    # Upload the media.
    for progress, response in tator.util.upload_media(tator_api, args.type_id, args.media_path):
        logger.info(f"Upload progress: {progress}%")
    logger.info(response.message)

    # Take a look at transcode progress, wait until complete.
    while True:
        job = tator_api.get_job(response.uid)
        if job.status == 'Succeeded':
            break
        elif job.status == 'Failed':
            raise ValueError("Upload failed!")
        time.sleep(10)
    
