#!/usr/bin/env python

""" This example shows how to get video frames from a video.
"""

import logging
import sys

import tator

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # Create a parser.
    parser = tator.get_parser()
    parser.add_argument('--video_id',
                        help='Media ID for a video.',
                        required=True, type=int)
    args = parser.parse_args()

    # Create the api.
    tator_api = tator.get_api(args.host, args.token)

    # Get some video frames. The path to a local image that contains the tiled
    # frames.
    image_path = tator_api.get_frame(args.video_id, frames=[0, 50, 100, 150])

    # The get_images utility can be used to retrieve individual frames from
    # the tiled output image. The returned value is a list of PIL.Image.
    video = tator_api.get_media(args.video_id)
    images = tator.util.get_images(image_path, video)

    # Region of interest can also be specified. This will retrieve the 100x100 
    # square in the top left of the frame (format is w:h:x:y).
    image_path = tator_api.get_frame(args.video_id, frames=[0, 50, 100, 150],
                                      roi='100:100:0:0')
    roi_images = tator.util.get_images(image_path, video, width=100, height=100)
