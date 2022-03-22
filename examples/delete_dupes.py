#!/usr/bin/env python

""" Deletes duplicate media within a project.
"""

import argparse
import logging
import sys
import re
from textwrap import dedent
from collections import defaultdict
from datetime import datetime
from datetime import timezone

import tator

logging.basicConfig(
    filename='migrate.log',
    filemode='w',
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))

def parse_args():
    parser = argparse.ArgumentParser(description=dedent("""\
    Deletes duplicate media in a project.

    Duplicates are determined using the md5 sum. To avoid deleting media that has metadata
    (localizations or states), pass --preserve_annotations. If this parameter is not passed,
    the script will keep the media with the latest edit date.

    Examples:
    Delete duplicate media with latest edit date
    python3 delete_dupes.py --host https://cloud.tator.io --token asdf --project 1

    Delete duplicate media if it contains no annotations
    python3 delete_dupes.py --host https://cloud.tator.io --token asdf --project 1
    --preserve_annotations
    """), formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--host', help='Tator host.', required=True)
    parser.add_argument('--token', help='Tator token.', required=True)
    parser.add_argument('--project', help='Project ID.', required=True)
    parser.add_argument('--section', help='Optional section ID.', type=int)
    parser.add_argument('--exclude', help='RegEx pattern for filenames that should not be considered '
                                          'for deletion.', default='.*')
    parser.add_argument('--preserve_annotations', help='If given, will not delete any media that '
                                                       'contains a localization or state.',
                        action='store_true')
    return parser.parse_args()

def find_dupes(args, api):
    logger.info("Finding duplicate media...")
    if args.section:
        medias = api.get_media_list(args.project, section=args.section)
    else:
        medias = api.get_media_list(args.project)
    regex = re.compile(args.exclude)
    # Build dict of md5 -> media objects.
    md5_map = defaultdict(list)
    for media in medias:
        if not regex.match(media.name):
            md5_map[media.md5].append(media)
    # Filter out unique md5s.
    md5_map = {md5:md5_map[md5] for md5 in md5_map if len(md5_map[md5]) > 1}
    # Sort lists by last edit date.
    sorter = lambda media: datetime(2000, 1, 1, tzinfo=timezone.utc)\
                           if media.last_edit_end is None else media.last_edit_end
    for md5 in md5_map:
        md5_map[md5].sort(key=sorter)
    # Return list of media that could be deleted.
    dupes = []
    for md5 in md5_map:
        dupes += md5_map[md5][:-1]
    logger.info(f"{len(dupes)} dupes found...")
    return dupes

def exclude_metadata(args, api, dupes):
    logger.info("Finding annotations in duplicate media...")
    # Find annotations in the duplicate media.
    excluded = set()
    for idx in range(0, len(dupes), 100):
        media_ids = [media.id for media in dupes[idx:idx+100]]
        localizations = api.get_localization_list(args.project, media_id=media_ids)
        for localization in localizations:
            excluded.add(localization.media)
        states = api.get_state_list(args.project, media_id=media_ids)
        for state in states:
            excluded.update(state.media)
    logger.info(f"{len(excluded)} dupes contain annotations...")
    dupes = [media for media in dupes if media.id not in excluded]
    logger.info(f"{len(dupes)} dupes contain no annotations...")
    return dupes

def delete_dupes(args, api, dupes):
    logger.info("Deleting dupes...")
    num_deleted = 0
    for idx in range(0, len(dupes), 100):
        media_ids = [media.id for media in dupes[idx:idx+100]]
        response = api.delete_localization_list(args.project, media_id=media_ids)
        num_deleted += len(media_ids)
        logger.info(f"Deleted {num_deleted} of {len(dupes)} dupes...")
    logger.info(f"Deleted {len(dupes)} dupes.")

if __name__ == '__main__':
    args = parse_args()
    api = tator.get_api(host=args.host, token=args.token)
    dupes = find_dupes(args, api)
    if args.preserve_annotations:
        dupes = exclude_metadata(args, api, dupes)
    logger.info("The following medias will be deleted:")
    for dupe in dupes:
        logger.info(f"ID: {dupe.id}, {dupe.name}")
    confirm = input("Proceed with deletion [y/N]? ")
    if confirm == 'y':
        delete_dupes(args, api, dupes)
    else:
        logger.info("Deletion cancelled by user.")
