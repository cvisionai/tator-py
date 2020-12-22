#!/usr/bin/env python3

import argparse
import os
import sys
import tempfile
import uuid

import tator

from .extractor import process_file


if __name__ == "__main__":
    """ CLI Frontend to extractor """
    parser = argparse.ArgumentParser(description="Thumbnail Extractor")
    tator.get_parser(parser)
    parser.add_argument("--mode",
                        required=True,
                        type=str,
                        choices=['state',
                                 'localization_keyframe',
                                 'localization_thumbnail',
                                 'track_thumbnail'],
                        help="""
                        state : Whole frame capture based on state's frame
                        localization_keyframe : Whole frame on localization frame
                        localization_thumbnail : Thumbnail of localization
                        track_thumbnail : Thumbnail of track (mp4)"""
                        )
    parser.add_argument("--metadata-type-id",
                        type=int,
                        required=True)
    parser.add_argument("--output-local",
                        type=str)
    parser.add_argument("--output-tator-section",
                        type=str)
    parser.add_argument("--output-type-id",
                        type=int)
    parser.add_argument("--project",
                        required=True,
                        type=int)
    parser.add_argument('--work-dir',
                        help='Optional hint to work directory',
                        type=str)
    parser.add_argument("media_ids",
                        nargs="+")

    args = parser.parse_args()

    api = tator.get_api(args.host, args.token)

    if args.mode in ['state', 'track_thumbnail']:
        print("Using States")
        meta_ep = api.get_state_list
    else:
        print("Using Localizations")
        meta_ep = api.get_localization_list

    if not any([args.output_local, args.output_tator_section]):
        print("Must supply at least one output")
        sys.exit(-1)

    if args.output_local:
        os.makedirs(args.output_local, exist_ok=True)
    upload_gid = str(uuid.uuid1())
    for media_id in args.media_ids:
        media_element = api.get_media(media_id)
        metadata = meta_ep(args.project,
                           type=args.metadata_type_id,
                           media_id=[media_id])
        metadata = [m for m in metadata if m.attributes.get('_extracted', None) is None]
        if len(metadata) == 0:
            print(f"No non-extracted metadata for '{media_element.name}'({media_id})")
            continue

        with tempfile.TemporaryDirectory(dir=args.work_dir) as td:
            print(f"Downloading {media_element.name}")
            for p in tator.download_media(api,
                                          media_element,
                                          os.path.join(td, media_element.name)):
                print(f"\r{p}", end='', flush=True)
            print('')
            print(f"Processing {media_element.name}")
            process_file(api,
                         args.project,
                         os.path.join(td, media_element.name),
                         media_element,
                         args.mode,
                         metadata,
                         args.output_local if args.output_local else td,
                         args.output_tator_section,
                         output_type_id=args.output_type_id,
                         upload_gid=upload_gid,
                         work_dir=args.work_dir)
