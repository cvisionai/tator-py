#!/usr/bin/env python

""" This example shows how to download a file as a temporary file. The 
    file may be an output from an algorithm or similar.
"""

import logging
import sys

import tator

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # Create a parser that includes save path.
    parser = tator.get_parser()
    parser.add_argument('--temporary_file_id',
                        help='Temporary file ID.',
                        required=True, type=int)
    parser.add_argument('--file_path',
                        help='Save path for the file.',
                        required=True)
    args = parser.parse_args()

    # Create the api.
    tator_api = tator.get_api(args.host, args.token)

    # Get the temporary file object.
    temporary_file = tator_api.get_temporary_file(args.temporary_file_id)

    # Download the file.
    for progress in tator.download_temporary_file(tator_api, temporary_file,
                                                  args.file_path):
        logger.info(f"Download progress: {progress}%")
    
