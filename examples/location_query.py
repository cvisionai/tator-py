#!/usr/bin/env python3
"""
Script that queries localizations based on a lat/lon location and radius.
Output is stored in this script's log file.
"""

import argparse
import logging

import tator

log_filename = 'location_query.log'

logging.basicConfig(
    filename=log_filename,
    filemode='w',
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args() -> argparse.Namespace:
    """ Parse the provided arguments

    Returns parsed arguments in a namespace object.

    """
    parser = argparse.ArgumentParser(
        description="Query localization based on media location")
    parser = tator.get_parser(parser=parser)
    parser.add_argument('--project',
        type=int, required=True, help='Unique project id')
    parser.add_argument('--section',
        type=str, required=True, help='Section name of media to process')
    parser.add_argument('--media_type_id',
        type=int, required=True, help='ID of media type to process (required for numerical attribute filtering)')
    parser.add_argument('--radius',
        type=float, required=True, help='Radius (km) of location query')
    parser.add_argument('--latitude',
        type=float, required=True, help='Latitude of location query center point')
    parser.add_argument('--longitude',
        type=float, required=True, help='Longitude of location query center point')
    parser.add_argument('--location_field',
        type=str, required=True, help='Name of lat/lon field of media')

    args = parser.parse_args()
    logger.info(args)

    return args

def main() -> None:
    """ Main routine of this script
    """

    args = parse_args()

    # Get the interface to Tator
    tator_api = tator.get_api(host=args.host, token=args.token)

    # Create the filter that will get all the media in the provided section
    attribute_contains_filter = f'tator_user_sections::{args.section}'

    # Create the distance filter
    attribute_distance_filter = \
        f'{args.location_field}::{args.radius}::{args.longitude}::{args.latitude}'

    # Get the media using the section and distance filter
    medias = tator_api.get_media_list(
        project=args.project,
        type=args.media_type_id,
        attribute_contains=attribute_contains_filter,
        attribute_distance=attribute_distance_filter)

    # Now, grab the localizations associated with these media and save it
    # to this script's log file
    media_id_list = []
    for media in medias:
        media_id_list.append(media.id)

    localizations = tator_api.get_localization_list(project=args.project, media_id=media_id_list)
    logger.info(localizations)

    print(f"{len(localizations)} localizations logged in: {log_filename}")
    print(f"[FINISHED] location_query.py ")

if __name__ == "__main__":

    main()