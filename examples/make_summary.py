#!/usr/bin/env python3
import logging
import os
import shutil
import sys
import traceback

import pandas as pd
import progressbar

import tator
import tator_openapi

logging.basicConfig(
    filename='make_summary.logs',
    filemode='a',
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG)
logger = logging.getLogger(__name__)

# TODO This probably should be based on the OS, but this number is a conservative one
#      that should work in all cases.
MAX_FILENAME_LEN = 200

def sanitizeString(string: str) -> str:
    """ Sanitize a string to be safe for filenames

    Args:
        string: String to sanitize for filenames

    Returns:
        Version of input string safe for filenames
    """
    return string.replace("|", "-").\
        replace("/","-").\
        replace("\\","-").\
        replace(":","-").\
        replace("*","").\
        replace('"',"").\
        replace("<","").\
        replace(">","").\
        replace("|","-")

def getAttributeTypeData(localization_types_df: pd.DataFrame) -> dict:
    """ Gets a dictionary of ordered attribute type information per localization type id

    Args:
        localization_types_df: DataFrame of output to

    Returns:
        Dictionary of pandas.DataFrame objects describing the attribute types.
        Keys are localization type ids
    """

    attribute_data = {}

    for _, row in localization_types_df.iterrows():
        df = pd.DataFrame(row.attribute_types)
        if 'order' in df.keys():
            df = df.sort_values('order')

            if len(df[df['order'] == 0]) > 1:
                log_msg = 'More than one attribute type has an order value of 0. Only expected one.'
                logging.warning(log_msg)

        attribute_data[row['id']] = df

    return attribute_data

def processLocalization(
        host: str,
        tator_api: tator_openapi.api.tator_api.TatorApi,
        project_id: int,
        section_name: str,
        media: tator_openapi.models.media.Media,
        localization: tator_openapi.models.localization.Localization,
        localization_types_df: pd.DataFrame,
        attribute_types_info: dict,
        image_folder: str,
        disable_thumbnails: bool) -> dict:
    """ Returns a dictionary of localization properties and generates a thumbnail image

    Args:
        host: Host URL
        tator_api: Interface object to tator connected to the host
        project_id: Unique identifier of project associated with the given localization
        section_name: Name of the section associated with the localization
        media: Media associated with the localization
        localization: Localization to process
        localization_types_df: DataFrame of localization types associated with the localization
        attribute_types_info: Output of getAttributeTypeData
        image_folder: Folder that will contain the thumbnail image
        disable_thumbnails: Don't create thumbnails if true

    Returns:
        Dictionary of localization data. Keys are localization properties.

    Postconditions:
        Thumbnail image of the localization is created in the given folder

    Raises:
        ValueError if a localization dtype is invalid.
    """

    # Get the media's pixel width to convert the relative width/height and position info
    width = media.width
    height = media.height

    # Grab the dtype information associated with this localization
    df = localization_types_df
    dtype_matches = df[df['id'] == localization.meta]

    if len(dtype_matches) != 1:
        log_msg = f'Localization {localization.id} ignored. Unexpected dtype match ({len(dtype_matches)} matches)'
        logging.warning(log_msg)
        raise ValueError("Invalid dtype match")

    dtype = dtype_matches.iloc[0]['dtype']

    # Grab the URL associated with this localization
    url = f"{host.rstrip('/')}/{project_id}/annotation/{media.id}?frame={localization.frame}"

    # Create the datum that will capture the localization info to be stored in the summary
    datum={
        'section': section_name,
        'media_id': media.id,
        'media': media.name,
        'dtype': dtype,
        'x': localization.x * width,
        'y': localization.y * height,
        'frame': localization.frame,
        'id': localization.id,
        'user_id': localization.user,
        'url': url}

    # Apply the width/height attributes based on the localization dtype
    if dtype == 'box':
        datum.update({
            'width': localization.width * width,
            'height': localization.height * height
        })

    elif dtype == 'line':
        datum.update({
            'width': localization.u * width,
            'height': localization.v * height
        })

    elif dtype == 'dot':
        datum.update({
            'width': 0.0,
            'height': 0.0
        })

    else:
        log_msg = f'Localization dtype invalid {dtype}'
        logging.warning(log_msg)
        raise ValueError("Invalid dtype detected")

    # Save the attributes of the localization specific to the localization type
    datum.update(localization.attributes)

    if not disable_thumbnails:
        # Lastly, create the thumbnail of this localization and move it to the user defined location
        # If the localization is a dot, take a large enough image segment, 
        # otherwise use the default marigins
        if dtype =='dot':
            image_path = tator_api.get_localization_graphic(
                localization.id,
                use_default_margins=False,
                margin_x=50,
                margin_y=50)

        else:
            try:
                image_path = tator_api.get_localization_graphic(localization.id)
            except:
                # This is a band-aid that should not happen anymore if the endpoint is updated
                # on the server. There was an issue with the localization graphic endpoint with
                # localizations that might result in a 1 pixel width and/or height. This would
                # result in an exception and this try/except block attempts to redo the graphic
                # with a small margin around the presumable box. If another exception occurs,
                # then that is a problem that should be raised.
                #
                # #TODO It's worth revisiting removing this down the road based on the comments above.
                image_path = tator_api.get_localization_graphic(
                    localization.id,
                    use_default_margins=False,
                    margin_x=1,
                    margin_y=1)

        # The thumbnail created is a temporary file. Move it using a specific filename/path.
        # The filename of the thumbnail will have the following format:
        # - primary attribute (if available, order == 0)
        # - media name
        # - frame number
        # - localization id
        # - all other attributes
        # - .png
        target_filename = ''
        main_basename = f'{sanitizeString(media.name)}_Frame_{localization.frame}_Id_{localization.id}'
        extension = '.png'
        set_main_basename = False
        if len(attribute_types_info[localization.meta]) > 0:
            # Since we have a sorted attribute type dataframe, if the first entry doesn't
            # have a 'primary attribute flag' (i.e. order == 0), we can just iterate over
            # the entries.
            for idx, row in attribute_types_info[localization.meta].iterrows():

                # Not all of the attributes available for a localization will always be used
                # If it doesn't exist, skip over it
                attr_name = row['name']
                if attr_name in localization.attributes:
                    attr_val = str(localization.attributes[attr_name])
                else:
                    continue

                if row['order'] == 0:
                    target_filename += f"{sanitizeString(attr_val)}_"

                else:
                    target_filename += f"{sanitizeString(row['name'])}_{sanitizeString(attr_val)}_"

                if not set_main_basename:
                    target_filename += main_basename
                    set_main_basename = True

        else:
            # In the case where there are no attributes associated with the localizaiton, just use
            # the base string defined earlier.
            target_filename = main_basename

        # Move the thumbnail using the new filename and save it to the outgoing datum
        if len(target_filename) > MAX_FILENAME_LEN:
            new_target_filename = target_filename[:MAX_FILENAME_LEN]
            log_msg = f"Trimming image filename: {target_filename} to {new_target_filename}"
            logging.warning(log_msg)
            target_filename = new_target_filename

        target_filename += '.png'
        target_path = os.path.join(image_folder, target_filename)
        os.makedirs(image_folder, exist_ok=True)
        shutil.move(image_path, target_path)
    else:
        # No thumbnail created. Empty string for the outgoing datum
        target_path = ''

    datum.update({'thumbnail': target_path})

    return datum

def processSection(
        host: str,
        tator_api: tator_openapi.api.tator_api.TatorApi,
        project_id: int,
        section_name: str,
        medias: list,
        localization_types_df: pd.DataFrame,
        attribute_types_info: dict,
        column_names: list,
        summary_filename: str=None,
        image_folder: str='images',
        disable_thumbnails: bool=False) -> None:
    """ Creates the report for the given project section

    Args:
        host: Host URL
        tator_api: Interface object to tator connected to the host
        project_id: Unique identifier of project associated with the given section
        section_name: Name of the section to be processed
        medias: List of media associated with the given section
        localization_types_df: DataFrame of localization types associated with the localization
        attribute_types_info: Output of getAttributeTypeData
        column_names: Columns to output in the section report
        summary_filename: File name to use for the summary report
            If None, then section_name_summary.csv is used
        image_folder: Folder that will contain the thumbnail image
        disable_thumbnails: Don't create thumbnails if true

    Postconditions:
        Images of the localizations created in the image folder
        .csv report of the section created
    """
    # Display a progress bar in the console based on the medias processed
    bar = progressbar.ProgressBar()

    # Let's get to work, grab information about each localization in the media and store
    # it in a dictionary. This dictionary will then be stored in a list to be written out to file.
    report_data = []

    for media in bar(medias):

        # Loop through each of the localizations associated with this media
        # Process the localization and get the report data
        try:
            localizations = tator_api.get_localization_list(project=project_id, media_id=[media.id])
            for localization in localizations:
                try:
                    datum = processLocalization(
                        host=host,
                        project_id=project_id,
                        tator_api=tator_api,
                        section_name=section_name,
                        media=media,
                        localization=localization,
                        localization_types_df=localization_types_df,
                        attribute_types_info=attribute_types_info,
                        image_folder=image_folder,
                        disable_thumbnails=disable_thumbnails)
                    report_data.append(datum)

                except Exception:
                    error_msg = f'Error encountered processing localization {localization.id}'
                    logging.error(error_msg)

                    error_msg = traceback.format_exc()
                    logging.error(error_msg)

        except Exception:
                error_msg = f'Error encountered processing media {media.id}'
                logging.error(error_msg)

                error_msg = traceback.format_exc()
                logging.error(error_msg)


    # Create the final .csv report
    output_name = f'{section_name}_summary.csv'
    if summary_filename:
        output_name = summary_filename

    log_msg = f'Creating summary report file: {output_name}'
    logging.info(log_msg)

    df = pd.DataFrame(data=report_data, columns=column_names)
    df.to_csv(output_name, index=False)

def processProject(
        host: str,
        token: str,
        project_id: int,
        section_name: str=None,
        summary_filename: str=None,
        disable_thumbnails: bool=False) -> None:
    """ Creates the sumamry report and thumbnail image for the given project/section

    Args:
        host: Host URL
        token: User token used for connecting to the host
        project_id: Unique identifier of project associated with the given section
        section_name: Name of the section to be processed
            If None, then all sections are processed
        summary_filename: File name to use for the summary report
            If None, then section_name_summary.csv is used
            Only valid if section_name is not None
        disable_thumbnails: Don't create thumbnails if true

    Postconditions:
        Images of localizations created in images/
        .csv report of the section created. If no section specified, report and
            thumbnails are created for each section.
    """

    # Get the interface to Tator
    tator_api = tator.get_api(host=host, token=token)

    # Get the list of projects and ensure the project exists.
    # Otherwise, complain and spit out what projects are available.
    projects = tator_api.get_project_list()

    found_project = False
    for project_info in projects:
        if project_info.id == project_id:
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
        'section','media_id','media','thumbnail','id',
        'user_id','frame','dtype','x','y','width','height','url']

    # Get the attributes associated with the localizations in this project
    # and save them as a report column
    localization_types = tator_api.get_localization_type_list(project=project_id)

    for loc_type in localization_types:
        for attr in loc_type.attribute_types:
            if attr.name not in column_names:
                column_names.append(attr.name)

    # Grab the localization types again associated with this section.
    # Convert this to a dataframe to make it easier to use.
    localization_types_df = tator.util.to_dataframe(localization_types)

    # Get the ordered attribute information per localization dtype.
    attribute_types_info = getAttributeTypeData(localization_types_df=localization_types_df)

    # If a section name was provided, then verify the corresponding section exists
    #     If not, then complain back to the user.
    # If no section name was provided, process all of the sections.
    sections = tator_api.get_media_sections(project=project_id)
    ignore_sumamry_filename = True

    if section_name is not None:
        # Section name specified
        if section_name not in sections:
            error_msg = f"Invalid section name provided: {section_name}"
            logging.error(error_msg)
            logging.error("Section names: ")
            logging.error(sections.keys())
            raise ValueError(error_msg)

        sections = [section_name]

    else:
        # No section name specified, process all sections
        # For now use the default summary output filename for each section
        # #TODO Maybe a basename can be used in the future.
        if summary_filename:
            log_msg = f'Ignoring provided summary file name: ({summary_filename}) Processing all sections.'
            logging.warning(log_msg)
            ignore_sumamry_filename = True

    # Loop over the selected sections and create the report(s) and thumbnail(s)
    for section_name in sections:

        # First grab all the medias associated with this section
        attribute_filter = f'tator_user_sections::{section_name}'
        medias = tator_api.get_media_list(project=project_id, attribute_contains=attribute_filter)

        # Ready to rock and roll
        log_msg = f"Processing section: {section_name}"
        logging.info(log_msg)
        section_sumamry_filename = None if ignore_sumamry_filename else summary_filename
        processSection(
            host=host,
            tator_api=tator_api,
            project_id=project_id,
            section_name=section_name,
            medias=medias,
            column_names=column_names,
            localization_types_df=localization_types_df,
            attribute_types_info=attribute_types_info,
            summary_filename=section_sumamry_filename,
            disable_thumbnails=disable_thumbnails)

def main():
    """ Main routine of this script
    """

    # Create the argument list and extract them
    parser = tator.get_parser()
    parser.add_argument('--project', type=int, required=True,
        help='Unique project id')
    parser.add_argument('--section', type=str, required=False,
        help='Optional section name to process')
    parser.add_argument('--output', type=str, required=False,
        help='Filename of section csv report. Only use if section was provided.')
    parser.add_argument('--disable-thumbnails', action='store_true',
        help='Ignore thumbnail creation, no thumbnails reported.')
    args = parser.parse_args()

    # Create the report(s) and thumbnail(s)
    processProject(
        host=args.host,
        token=args.token,
        project_id=args.project,
        section_name=args.section,
        summary_filename=args.output,
        disable_thumbnails=args.disable_thumbnails)

if __name__=="__main__":

    main()