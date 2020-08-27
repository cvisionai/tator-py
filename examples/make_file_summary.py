#!/usr/bin/env python3
"""
Script that gathers counts of localizations and states (e.g. detections and tracks)
for each file in a particular section. Also gathers the last edit session duration for
each of the media.
"""

import argparse
import datetime
import logging
import urllib.parse
import sys
import traceback

import progressbar
import pandas as pd

import tator

logging.basicConfig(
    filename='make_file_summary.log',
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
        description="Creates a file (media) summary for the provided project/section. Localization counts, state counts, and last session duration are recorded.")
    parser = tator.get_parser(parser=parser)
    parser.add_argument('--project', type=int, required=True, help='Unique project id')
    parser.add_argument('--section', type=str, required=True, help='Name of section to process')

    args = parser.parse_args()
    logger.info(args)

    return args

def process_section(
        host: str,
        token: str,
        project_id: int,
        section_name: str) -> str:
    """ Processes media in section and creates a summary .csv file

    Collects counts of localization types and state types.
    Also gather last session durations.

    Args:
        host (str): Tator url server
        token (str): User access token to tator server
        project_id (int): Unique identifier of section's project
        section_name (str): Section name to process

    Returns:
        Returns the filename of the report created

    Postconditions:
        section_name.csv created with summary information

    """

    # Get the interface to Tator
    tator_api = tator.get_api(host=host, token=token)

    # Get the localization types associated with the project and gather
    # the names of the visible ones
    localization_types = tator_api.get_localization_type_list(project=project_id)

    localization_type_names = []
    localization_type_id_name_map = {}
    for loc_type in localization_types:
        name = loc_type.name + " (counts)"
        localization_type_names.append(name)
        localization_type_id_name_map[loc_type.id] = name

    # Get the state names (e.g. track type names) associated with the project
    state_types = tator_api.get_state_type_list(project=project_id)

    state_type_names = []
    state_type_id_name_map = {}
    for state_type in state_types:
        name = state_type.name + " (counts)"
        state_type_names.append(name)
        state_type_id_name_map[state_type.id] = name

    # Grab all the media in this section
    attribute_filter = f'tator_user_sections::{section_name}'
    medias = tator_api.get_media_list(project=project_id, attribute_contains=attribute_filter)

    # Set the column names
    column_names = [
        'Section',
        'Media ID',
        'Media',
        'URL',
        'Last Session Duration',
    ]
    column_names.extend(localization_type_names)
    column_names.extend(state_type_names)

    # Loop over each of the media, extract the appropriate data, and save it for later processing
    report_data = []
    progress = progressbar.ProgressBar()
    for media in progress(medias):

        # User may or may not have edited the media. If not, the datetime entries will be None.
        # Otherwise, these values will be DateTime objects
        if media.last_edit_end == None:
            last_session_duration = "N/A"
        else:
            last_session_duration = str(media.last_edit_end - media.last_edit_start)

        # Cycle through the localization types and gather the localizations associated with
        # the current type. Then count it.
        localization_type_counts = {}
        for type_id in localization_type_id_name_map:
            localizations = tator_api.get_localization_list(
                project=project_id,
                media_id=[media.id],
                type=type_id)
            loc_name = localization_type_id_name_map[type_id]
            localization_type_counts[loc_name] = len(localizations)

        # Cycle through the state types and gather the states associated with the
        # current type. Then count it.
        state_type_counts = {}
        for type_id in state_type_id_name_map:
            states = tator_api.get_state_list(
                project=project_id,
                media_id=[media.id],
                type=type_id)
            state_name = state_type_id_name_map[type_id]
            state_type_counts[state_name] = len(states)

        # Gather all the data into a dictionary to be later converted
        media_data = {
            'Section': section_name,
            'Media ID': media.id,
            'Media': media.name,
            'URL': urllib.parse.urljoin(host, f"{project_id}/annotation/{media.id}"),
            "Last Session Duration": last_session_duration,
            **localization_type_counts,
            **state_type_counts,
        }

        report_data.append(media_data)

    # Create the summary report
    output_name = f"{section_name}.csv"
    df = pd.DataFrame(data=report_data, columns=column_names)
    df.to_csv(output_name, index=False)

    return output_name

def main():
    """ Main routine of this script
    """

    args = parse_args()

    try:
        report_filename = process_section(
            host=args.host,
            token=args.token,
            project_id=args.project,
            section_name=args.section)

        print(f"Created {report_filename}")

    except Exception:
        print(f"[ERROR] Problem occurred. Review the .log file.")
        error_msg = traceback.format_exc()
        logging.error(error_msg)

    print(f"[FINISHED] make_file_summary.py ")

if __name__ == "__main__":

    main()