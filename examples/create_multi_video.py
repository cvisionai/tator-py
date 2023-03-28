""" Script to create a multi-video media from existing videos
"""

import argparse
import logging
import sys

import tator

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """ Main function of script
    """

    args = parse_args()

    tator_api = tator.get_api(host=args.host, token=args.token)

    media_types = tator_api.get_media_type_list(project=args.project)
    multi_type_id = None
    for media_type in media_types:
        if media_type.dtype == "multi":
            multi_type_id = media_type.id
            break

    if multi_type_id is None:
        raise ValueError("ERROR: Could not find a registered media type of dtype=multi")

    layout = [args.layout_rows, args.layout_cols]

    response = tator.util.make_multi_stream(
        api=tator_api,
        type_id=multi_type_id,
        media_ids=args.media,
        layout=layout,
        name=args.multi_media_name,
        section=args.section_name,
        quality=args.quality)

    logger.info(response)

def parse_args() -> argparse.Namespace:
    """ Parse script arguments
    """
    parser = tator.get_parser()
    parser.add_argument("--project", type=int, required=True, help="Associated unique project ID.")
    parser.add_argument("--media", type=int, nargs="+", required=True, help="List of media IDs to display.")
    parser.add_argument("--multi-media-name", type=str, required=True, help="Name of multi-media file. Note *.multi extension is applied automatically.")
    parser.add_argument("--layout-rows", type=int, required=True, help="Number of rows to use in the multi-gridview.")
    parser.add_argument("--layout-cols", type=int, required=True, help="Number of columns to use in the multi-gridview.")
    parser.add_argument("--quality", type=int, required=True, help="Video quality. 360 for 360p, 720 for 720p, etc.")
    parser.add_argument("--section-name", type=str, help="If provided, the new multi media will be applied to the given section. If section with the name does not exist, one will be created.")
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    main()