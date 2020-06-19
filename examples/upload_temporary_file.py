#!/usr/bin/env python

""" This example shows how to upload a file as a temporary file. The
    file may be an output from an algorithm or similar.
"""

import logging
import sys

import tator

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # Create a parser that includes path to file to upload.
    parser = tator.get_parser()
    parser.add_argument('--project_id',
                        help='Project ID.',
                        required=True, type=int)
    parser.add_argument('--file_path',
                        help='Path to the file on disk.',
                        required=True)
    args = parser.parse_args()

    # Create the api.
    tator_api = tator.get_api(args.host, args.token)

    # Upload the file.
    for progress, response in tator.util.upload_temporary_file(tator_api, args.project_id,
                                                          args.file_path):
        logger.info(f"Upload progress: {progress}%")
    logger.info(response.message)
    
