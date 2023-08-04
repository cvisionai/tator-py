#!/usr/bin/env python3

import argparse
import logging
import os
import shutil
import sys
import traceback
import json
from textwrap import dedent
from collections import defaultdict

import tator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))

def parse_args():
    parser = argparse.ArgumentParser(description=dedent('''\
    Imports JSON files that were created with Tator Native. Assumes destination media has same
    base name as JSON file.

    Example:
    python3 import_tator_native.py --host https://cloud.tator.io --token asdf --project 1 
    /path/to/directory/with/json
    '''), formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--host', help='Host containing source project.', required=True)
    parser.add_argument('--token', help='Token for host containing source project.', required=True)
    parser.add_argument('--project', help='Unique integer identifying project containing data to '
                                          'import annotations.', required=True, type=int)
    parser.add_argument('--attribute_mappings', help='Mappings between json attribute name and '
                                                     'attribute name defined in the project. Form '
                                                     'is source_name:dest_name.', nargs='+')
    parser.add_argument('path', help='Directory containing JSON files. Scanned recursively.')
    return parser.parse_args()

def _find_types(api, project):
    """ Returns dict containing mapping from dtype to type.
    """
    loc_types = api.get_localization_type_list(project)
    state_types = api.get_state_type_list(project)
    loc_types = {loc_type.dtype:loc_type for loc_type in loc_types}
    state_types = {state_type.association:state_type for state_type in state_types}
    return loc_types, state_types

def _convert_detection(loc, loc_types, media, attribute_mapping):
    """ Converts a Tator Native detection into a Localization spec.
    """
    spec = {'type': loc_types[loc['type']].id,
            'media_id': media.id,
            'frame': int(loc['frame'])}
    spec['x'] = float(loc['x']) / media.width
    spec['y'] = float(loc['y']) / media.height
    if loc['type'] == 'box':
        spec['width'] = float(loc['w']) / media.width
        spec['height'] = float(loc['h']) / media.height
    elif loc['type'] == 'line':
        spec['u'] = (float(loc['w']) - float(loc['x'])) / media.width
        spec['v'] = (float(loc['h']) - float(loc['y'])) / media.height
    for src_name in attribute_mapping:
        if src_name in loc:
            spec[attribute_mapping[src_name]] = loc[src_name]
    return spec

def _convert_track(track, state_types, media, attribute_mapping, localizations):
    """ Converts a Tator Native track into a State spec.
    """
    spec = {'type': state_types['Localization'].id,
            'media_id': media.id,
            'frame': int(track['frame_added'])}
    spec['localization_ids'] = localizations[int(track['id'])]
    spec['media_ids'] = [media.id]
    for src_name in attribute_mapping:
        if src_name in track:
            spec[attribute_mapping[src_name]] = track[src_name]
    return spec

def _import_data(api, project, media, loc_types, state_types, attribute_mapping, full_path):
    with open(full_path, 'r') as f:
        data = json.load(f)
    detections = data['detections']
    tracks = data['tracks']
    localization_spec = [_convert_detection(det, loc_types, media, attribute_mapping)
                         for det in detections]
    localization_ids = []
    for response in tator.util.chunked_create(
        api.create_localization_list, project, create_localization_list_request=localization_spec
    ):
        localization_ids += response.id
        logger.info(f"Imported {len(localization_ids)} of {len(localization_spec)} localizations...")
    assert(len(detections) == len(localization_ids))
    localizations = defaultdict(list)
    for det, loc_id in zip(detections, localization_ids):
        localizations[int(det['id'])].append(loc_id)
    track_spec = [_convert_track(state, state_types, media, attribute_mapping, localizations)
                  for state in tracks]
    track_ids = []
    for response in tator.util.chunked_create(
            api.create_state_list, project, create_state_list_request=track_spec
    ):
        track_ids += response.id
        logger.info(f"Imported {len(track_ids)} of {len(track_spec)} tracks...")
    state_ids = []

if __name__ == '__main__':
    args = parse_args()
    api = tator.get_api(host=args.host, token=args.token)
    medias = api.get_media_list(args.project)
    medias = {media.name.lower():media for media in medias}
    loc_types, state_types = _find_types(api, args.project)
    attribute_mapping = [item.split(':') for item in args.attribute_mappings]
    attribute_mapping = {item[0]:item[1] for item in attribute_mapping}
    for root, dirs, files in os.walk(args.path):
        for fname in files:
            basename, ext = os.path.splitext(fname)
            media_name = f"{basename}.MP4".lower()
            media = None
            if media_name in medias and ext == '.json':
                media = medias[media_name]
            if ext == '.json':
                full_path = os.path.join(root, fname)
                if media is None:
                    logger.warning(f"Couldn't find media for file {media_name}, skipping!")
                    continue
                logger.info(f"Importing {full_path}...")
                _import_data(api, args.project, media, loc_types, state_types, attribute_mapping, full_path)
                
