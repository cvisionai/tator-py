#!/usr/bin/env python

""" This example shows how to create localizations.
"""

import logging
import sys
import random
import time

import tator

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

def random_box(video, type_id):
    """ Returns random localization spec for given video object.

    :param video: :class:`tator.Media` object.
    :param type_id: Localization type ID.
    :returns: Random localization spec.
    """
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    return dict(
        x=x, y=y,
        width=random.uniform(0.0, 1.0 - x),
        height=random.uniform(0.0, 1.0 - y),
        frame=random.randint(0, video.num_frames),
        media_id=video.id,
        type=type_id,
    )

if __name__ == '__main__':
    parser = tator.get_parser()
    parser.add_argument('--video_id', help="Video ID.", type=int, required=True)
    parser.add_argument('--type_id', help="Localization type ID.", type=int, required=True)
    args = parser.parse_args()
    tator_api = tator.get_api(args.host, args.token)

    # Get the video object.
    video = tator_api.get_media(args.video_id)

    # Get the type object.
    loc_type = tator_api.get_localization_type(args.type_id)
    project = loc_type.project

    # Create a list of random box localizations.
    localizations = [random_box(video, args.type_id) for _ in range(5000)]

    # Create the localizations. A maximum of 500 localizations can be created 
    # per request, so we use `chunked_create` to break up our large list.
    created_ids = []
    for response in tator.util.chunked_create(
        tator_api.create_localization_list, project, body=localizations
    ):
        created_ids += response.id
    logger.info(f"Created {len(created_ids)} localizations!")

    # Get all localizations for this video. The `media_id` parameter accepts a list
    # of IDs.
    localizations = tator_api.get_localization_list(project, media_id=[args.video_id])
    logger.info(f"Found {len(localizations)} localizations in this video!")

    # Get the localizations with left edge on the left side of the image.
    # Geometry fields are indexed in elasticsearch with a leading underscore
    # appended before their name.
    localizations = tator_api.get_localization_list(project, media_id=[args.video_id],
                                                    attribute_lt=["_x::0.5"])
    logger.info(f"Found {len(localizations)} localizations on left side of video!")

    # Get the localizations with normalized width less than 0.25.
    localizations = tator_api.get_localization_list(project, media_id=[args.video_id],
                                                    attribute_lt=["_width::0.25"])
    logger.info(f"Found {len(localizations)} localizations with width < 0.25!")

    # Get the localizations between frames 100-200.
    # Frame is also indexed in elasticsearch under the name _frame.
    localizations = tator_api.get_localization_list(project, media_id=[args.video_id],
                                                    attribute_gte=["_frame::100"],
                                                    attribute_lte=["_frame::=200"])
    logger.info(f"Found {len(localizations)} localizations between frames 100-200!")

    # Delete localizations between frames 100-200.
    response = tator_api.delete_localization_list(project, media_id=[args.video_id],
                                                    attribute_gte=["_frame::100"],
                                                    attribute_lte=["_frame::=200"])
    logger.info(response.message)

    # Suppose we want to shrink the first 10 boxes by 50% in each dimension. This
    # can be done by iterating over them and patching them.
    localizations = tator_api.get_localization_list(project, media_id=[args.video_id])
    for loc in localizations[:10]:
        update = {'width': loc.width * 0.5, 'height': loc.height * 0.5}
        response = tator_api.update_localization(loc.id, localization_update=update)
        logger.info(response.message)

