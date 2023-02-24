#!/usr/bin/env python

""" This example shows how to create tracks.
"""

import logging
import sys
import random
import time

import tator

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

def random_box(video, type_id, frame):
    """ Returns random localization spec for given video object and frame.

    :param video: :class:`tator.models.Media` object.
    :param type_id: Localization type ID.
    :returns: Random localization spec.
    """
    x = random.uniform(0.0, 0.95)
    y = random.uniform(0.0, 0.95)
    return dict(
        x=x, y=y,
        width=random.uniform(0.05, 1.0 - x),
        height=random.uniform(0.05, 1.0 - y),
        frame=frame,
        media_id=video.id,
        type=type_id,
    )

if __name__ == '__main__':
    parser = tator.get_parser()
    parser.add_argument('--video_type_id', help="Video type ID.", type=int, required=True)
    parser.add_argument('--video_id', help="Video ID.", type=int, required=True)
    args = parser.parse_args()
    tator_api = tator.get_api(args.host, args.token)

    # Get the video object and video type object.
    video = tator_api.get_media(args.video_id)
    video_type = tator_api.get_media_type(args.video_type_id)

    # Create a new localization type for the project. We set it to 
    # not visible because we only want to see tracks in the UI.
    response = tator_api.create_localization_type(video_type.project, localization_type_spec={
        'name': 'Track boxes',
        'dtype': 'box',
        'media_types': [video_type.id],
        'visible': False,
    })
    loc_type_id = response.id
    logger.info(response.message)

    # Create a new state type for the project to represent tracks. Tracks will
    # have a user-defined attribute called "Label".
    response = tator_api.create_state_type(video_type.project, state_type_spec={
        'name': 'Tracks',
        'association': 'Localization',
        'media_types': [video_type.id],
        'attribute_types': [{
            'name': 'Label',
            'dtype': 'string',
        }],
    })
    state_type_id = response.id
    logger.info(response.message)

    # Create one localization per frame.
    localizations = [random_box(video, loc_type_id, frame) for frame in range(video.num_frames)] 
    localization_ids = []
    for response in tator.util.chunked_create(
        tator_api.create_localization_list, video_type.project, body=localizations
    ):
        localization_ids += response.id
    logger.info(f"Created {len(localization_ids)} localizations!")
  
    # Create a new track for every 10 localizations.
    states = [{
        'type': state_type_id,
        'localization_ids': localization_ids[idx:idx+10],
        'media_ids': [args.video_id],
        'Label': f'Track {int(idx / 10)}', # Providing values for attributes is optional
    } for idx in range(0, len(localization_ids), 10)]
    state_ids = []
    for response in tator.util.chunked_create(
            tator_api.create_state_list, video_type.project, body=states
    ):
        state_ids += response.id
    logger.info(f"Created {len(state_ids)} tracks!")

    # Retrieve tracks associated to localizations.
    states = tator_api.get_state_list_by_id(video_type.project,
                                            {'localization_ids': localization_ids})
    assert(len(states) == len(state_ids))

    # Retrieve localizations associated to tracks.
    localizations = tator_api.get_localization_list_by_id(video_type.project,
                                                          {'state_ids': state_ids})
    assert(len(localizations) == len(localization_ids))

    # The "state graphic", a series of localization images associated with the
    # track, can be retrieved. Below this is done for the first track. Using the
    # full_state_graphic utility, a list of PIL images is returned.
    images = tator.util.full_state_graphic(tator_api, state_ids[0])

