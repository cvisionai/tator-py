#!/usr/bin/env python

""" This example shows how to upload multiple media files as an archive.
"""

import logging
import sys
import os

import tator

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # Create a parser that includes path to media file.
    parser = tator.get_parser()
    parser.add_argument('--project_id',
                        help='Project ID for upload.',
                        required=True, type=int)
    parser.add_argument('--media_dir', 
                        help='Directory containing media files.', 
                        required=True)
    args = parser.parse_args()

    # Create the api.
    tator_api = tator.get_api(args.host, args.token)

    # Construct list of files.
    paths = os.listdir(args.media_dir)
    paths = [os.path.join(args.media_dir, path) for path in paths]
    paths = paths[:1000] # Only upload the first 1000 files.

    # Upload the media.
    batch_num = 0
    for batch in tator.util.chunked_file_list(paths):
        print(f"Uploading file {batch_num*100} / {len(paths)}")
        for progress, response in tator.util.upload_media_archive(tator_api, args.project_id, batch):
            logger.info(f"Upload progress: {progress}%")
        logger.info(response.message)
        batch_num += 1
    
