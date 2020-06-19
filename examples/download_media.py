#!/usr/bin/env python

""" This example shows how to download media.
"""

import logging
import sys
import os

import tator

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # Create a parser that includes media name and project name.
    parser = tator.get_parser()
    parser.add_argument('--media_name', help='Name of media to download.', required=True)
    parser.add_argument('--project_name', help='Name of project.', required=True)
    parser.add_argument('--save_path', help='Directory to save the media.', required=True)
    args = parser.parse_args()

    # Create the api.
    tator_api = tator.get_api(args.host, args.token)

    # Find the project.
    projects = tator_api.get_project_list()
    for project in projects:
        if project.name == args.project_name:
            break
    if project.name != args.project_name:
        logger.error(f"Could not find project with name {args.project_name}!")
        sys.exit()

    # Find the media.
    media_list = tator_api.get_media_list(project.id, name=args.media_name)
    logger.info(f"Found {len(media_list)} media matching name {args.media_name}.")

    # Download the media.
    for media in media_list:
        logger.info(f"Downloading {media.name}...")
        file_path = os.path.join(args.save_path, media.name)
        for progress in tator.util.download_media(tator_api, media, file_path):
            logger.info(f"Download progress: {progress}%")
    
