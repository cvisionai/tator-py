#!/usr/bin/env python

""" This example shows how to create activities.
"""

import logging
import sys
import random
import time

import tator

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    parser = tator.get_parser()
    parser.add_argument('--video_type_id', help="Video type ID.", type=int, required=True)
    parser.add_argument('--video_id', help="Video ID.", type=int, required=True)
    args = parser.parse_args()
    tator_api = tator.get_api(args.host, args.token)

    # Get the video object and video type object.
    video = tator_api.get_media(args.video_id)
    video_type = tator_api.get_media_type(args.video_type_id)

    # Create a new state type for the project to represent activities. Activities will
    # have a user-defined attribute called "Something in view" to indicate whether
    # an object of interest is visible in the video during that frame. The interpolation
    # parameter indicates that the latest update to this value should be used for
    # visual indication in the UI.
    response = tator_api.create_state_type(video_type.project, state_type_spec={
        'name': 'Activity Change',
        'association': 'Frame',
        'media_types': [video_type.id],
        'attribute_types': [{
            'name': 'Something in view',
            'dtype': 'bool',
        }],
    })
    state_type_id = response.id
    logger.info(response.message)

    # Create activity change every 10 frames with "Something in view" indicator
    # switching between true and false.
    states = [{
        'type': state_type_id,
        'frame': frame,
        'media_ids': [args.video_id],
        'Something in view': (frame % 20) == 0,
    } for frame in range(0, video.num_frames, 10)]
    state_ids = []
    for response in tator.util.chunked_create(
            tator_api.create_state_list, video_type.project, body=states
    ):
        state_ids += response.id
    logger.info(f"Created {len(state_ids)} activity changes!")

