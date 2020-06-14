#!/usr/bin/env python

""" This example shows how to get a video clip from a video.
"""

import logging
import sys

import tator

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # Create a parser that includes path to text file.
    parser = tator.get_parser()
    parser.add_argument('--video_id',
                        help='Media ID for a video.',
                        required=True, type=int)
    parser.add_argument('--file_path',
                        help='Save path for the clip.',
                        required=True)
    args = parser.parse_args()

    # Create the api.
    tator_api = tator.get_api(args.host, args.token)

    # Get the video clip.
    temporary_file = tator.get_clip(args.video_id, frame_ranges=['0:30', '50:90'])

    # Download the file.
    for progress in tator.download_temporary_file(tator_api, temporary_file,
                                                  args.file_path):
        logger.info(f"Download progress: {progress}%")
    
