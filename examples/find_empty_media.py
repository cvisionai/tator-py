#!/usr/bin/env python3

import argparse
import logging
import sys
from textwrap import dedent

import tator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description=dedent('''\
    Finds media that contains no streaming, no archival, or neither media.

    Example:
    python3 find_empty_media.py --host https://tatorapp.com --token asdf --project 1 --section 1
    '''), formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--host', help='Host containing source project.', required=True)
    parser.add_argument('--token', help='Token for host containing source project.', required=True)
    parser.add_argument('--project', help='Unique integer identifying project containing data to '
                                          'be migrated.', required=True, type=int)
    parser.add_argument('--sections', help='Section IDs to search for empty media.', nargs='+',
                        type=int)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    api = tator.get_api(host=args.host, token=args.token)
    if args.sections:
        medias = []
        for section in args.sections:
            medias += api.get_media_list(args.project, section=section)
    else:
        medias = api.get_media_list(project=args.project)
    no_archival = []
    no_streaming = []
    neither = []
    for media in medias:
        if media.media_files is None:
            no_archival.append(media)
            no_streaming.append(media)
            neither.append(media)
        else:
            has_archival = True
            has_streaming = True
            if media.media_files.archival is None:
                has_archival = False
            else:
                if len(media.media_files.archival) == 0:
                    has_archival = False
            if media.media_files.streaming is None:
                has_streaming = False
            else:
                if len(media.media_files.streaming) == 0:
                    has_streaming = False
            if not has_streaming:
                no_streaming.append(media)
            if not has_archival:
                no_archival.append(media)
            if not has_streaming and not has_archival:
                neither.append(media)
    logger.info(f"{len(no_streaming)} media have no streaming files.")
    logger.info(f"{len(no_archival)} media have no archival files.")
    logger.info(f"{len(neither)} media have neither streaming or archival files.")

