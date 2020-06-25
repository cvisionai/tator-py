#!/usr/bin/env python3

# Standard imports
import logging
import os
import sys

# External imports
import pandas as pd
import progressbar

# Local imports

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

def sanitizeString(string):
    """ Sanitize a string to be safe for filenames """
    return string.replace("|", "-").\
        replace("/","-").\
        replace("\\","-").\
        replace(":","-").\
        replace("*","").\
        replace('"',"").\
        replace("<","").\
        replace(">","").\
        replace("|","-")

def processSection(
        tator_api,
        project_id: int,
        section_name: str,
        medias: list,
        column_names: list,
        summary_filename: str=None) -> None:
    """ Creates the report for the given project section

    :param tator_api: tator_openapi.api.tator_api.TatorApi
        Interface to tator. Used to retrieve data

    :param project_id: int
        Unique integer identifying the project

    :param section_name: str
        Unique string identifier of the section to get the summary of

    :param medias: list of tator_openapi.models.media.Media
        Media objects associated with section_name

    :param column_names: list of str
        List of strings that will be the columns of the section report

    :param summary_filename: str
        User specified file name for the section summary

    Summary report file will contain the following columns:
    section, media, thumbnail, id, user, frame, type, x, y, width, height, url? 
    #TODO ... what about this URL?

    """

    # Display a progress bar in the console based on the medias processed
    bar = progressbar.ProgressBar()

    # Let's get to work, grab information about each localization in the media and store
    # it in a pandas DataFrame. That DataFrame will be used to create the sumamry report
    for media in bar(medias):

        # Grab information about the media
        width = media.width
        height = media.height

        

        localizations = tator_api.get_localization_list(project=project_id, media_id=[media.id])

        for localization in localizations:
            
            if localization.

    # Create the final .csv report
    output_name = f'{section_name}_summary.csv'
    if summary_filename:
        output_name = summary_filename

    log_msg = f'Creating summary report file: {output_name}'
    logging.info(log_msg)


def main():
    """ Main routine of this script
    """

    import tator

    # Create the argument list and extract them
    # TODO Maybe we don't want to inherit the "--host", the previous
    #      iteration of this script used "--url".
    parser = tator.get_parser()
    parser.add_argument('--project', type=int, required=True)
    parser.add_argument('--section', type=str, required=False)
    parser.add_argument('--output', type=str, required=False)
    args = parser.parse_args()

    # Get the interface to Tator
    tator_api = tator.get_api(host=args.host, token=args.token)

    # Get the list of projects and ensure the project exists.
    # Otherwise, complain and spit out what projects are available.
    projects = tator_api.get_project_list()
    project_id = args.project

    found_project = False
    for project_info in projects:
        if project_info.id == args.project:
            found_project = True
            break

    if not found_project:
        error_msg = f"Invalid project ID provided: {project_id}"
        logging.error(error_msg)
        logging.error("Project list: ")
        logging.error(projects)
        raise ValueError(error_msg)

    # Report column names will always have the following.
    # Additional column names will be added based on the project
    column_names=[
        'section','media','thumbnail','id','user','frame','type','x','y','width','height']

    # Get the attributes associated with the localizations in this project
    # and save them as a report column
    localization_types = tator_api.get_localization_type_list(project=project_id)

    for loc_type in localization_types:
        for attr in loc_type.attribute_types:
            if attr not in column_names:
                column_names.append(attr.name)

    # If a section name was provided, then verify the corresponding section exists
    #     If not, then complain back to the user.
    # If no section name was provided, process all of the sections.
    sections = tator_api.get_media_sections(project=project_id)

    if args.section is not None:
        # Section name specified
        section_name = args.section_name
        if section_name not in sections:
            error_msg = f"Invalid section name provided: {section_name}"
            logging.error(error_msg)
            logging.error("Section names: ")
            logging.error(sections.keys())
            raise ValueError(error_msg)

        sections = [section_name]
        summary_filename = args.output

    else:
        # No section name specified, process all sections
        # For now use the default summary output filename for each section
        # #TODO Maybe a basename can be used instead
        if args.output:
            log_msg = f'Ignoring provided summary file name: ({args.output}) Processing all sections.'
            logging.warn(log_msg)

        summary_filename = None

    # Loop over the selected sections 
    for section_name in sections:

        # First grab all the medias associated with this section
        attribute_filter = f'tator_user_sections::{section_name}'
        medias = tator_api.get_media_list(project=project_id, attribute_contains=attribute_filter)

        # Ready to rock and roll
        processSection(
            tator_api=tator_api,
            project_id=project_id,
            section_name=section_name,
            medias=medias,
            column_names=column_names,
            summary_filename=summary_filename)

    # fin.

if __name__=="__main__":

    main()