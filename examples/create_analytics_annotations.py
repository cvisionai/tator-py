""" Tool used to modify the media in a given project for testing the annotation analytics view
"""

import argparse
import datetime
import dateutil
import logging
import random
import sys
import uuid

import tator
import progressbar

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

def create_random_localization(
        tator_api: tator.api,
        project: int,
        localization_types: list,
        versions: list,
        media: tator.models.Media) -> dict:
    """ Create a random localization
    """

    selected_loc_type = random.choice(localization_types)
    version = random.choice(versions)

    if media.num_frames is None:
        frame = 0
    else:
        frame = random.randint(0, media.num_frames - 1)


    start_date = datetime.datetime(2021, 2, 2)
    end_date = datetime.datetime(2021, 10, 10)
    sighting_date = random.random() * (end_date - start_date) + start_date

    spec = {
        "project": project,
        "type": selected_loc_type.id,
        "frame": frame,
        "media_id": media.id,
        "version": version.id,
        "Species": random.choice(["Herring, Atlantic", "Herring, Blueback", "Lobster", "Scallop"]),
        "Algorithm Confidence": random.uniform(0, 1),
        "Count": random.randint(0, 5),
        "Valid": random.choice([True, False]),
        "Sighting Date": sighting_date
    }

    if selected_loc_type.dtype == "dot":
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 1.0)
        spec["x"] = x
        spec["y"] = y

    elif selected_loc_type.dtype == "line":
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 1.0)
        u = random.uniform(0.0, 1.0)
        v = random.uniform(0.0, 1.0)
        spec["x"] = x
        spec["y"] = y
        spec["u"] = u
        spec["v"] = v

    elif selected_loc_type.dtype == "box":
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 1.0)
        w = random.uniform(0.0, 1.0 - x)
        h = random.uniform(0.0, 1.0 - y)
        spec["x"] = x
        spec["y"] = y
        spec["width"] = w
        spec["height"] = h

    tator_api.create_localization_list(project=project, localization_spec=[spec])
    return spec

def create_localizations(
        tator_api: tator.api,
        project: int,
        medias : list,
        localization_types: list,
        versions: list) -> list:
    """ Create random localizations for each media
    """

    max_number_of_locs_per_video = 100
    max_number_of_locs_per_image = 10

    # Gather the meda type information
    media_types = tator_api.get_media_type_list(project=project)
    image_type_id = None
    video_type_id = None
    for media_type in media_types:
        if media_type.dtype == "image":
            image_type_id = media_type.id
        elif media_type.dtype == "video":
            video_type_id = media_type.id

    # Create the localizations for each media
    logger.info(f"Creating localizations in {len(medias)} medias")

    analytics_data = {}
    bar = progressbar.ProgressBar()
    for media in bar(medias):

        analytics_data[media.id] = []
        count = None
        if media.meta == image_type_id:
            count = max_number_of_locs_per_image
        elif media.meta == video_type_id:
            count = max_number_of_locs_per_video
        else:
            count = None

        for _ in range(count):
            if random.choice([True, False]):
                loc_spec = create_random_localization(
                    tator_api=tator_api,
                    project=project,
                    localization_types=localization_types,
                    versions=versions,
                    media=media)

                analytics_data[media.id].append(loc_spec)

    return analytics_data

def update_medias_and_sections(
        tator_api: tator.api,
        project: int):
    """ Move medias into sections and update their attributes
    """

    # Available options
    trip_id_choices = ["Atlantic 05/2021", "Atlantic 06/2021", "Atlantic 07/2021", "Atlantic 08/2021"]
    reviewed_choices = [True, False]

    # Create sections
    section_ids = []
    for trip_id in trip_id_choices:
        section_uuid = str(uuid.uuid4())
        section_spec = {"name": trip_id, "tator_user_sections" : section_uuid}
        response = tator_api.create_section(project=project, section_spec=section_spec)
        section_ids.append(response.id)

    sections = tator_api.get_section_list(project=project)
    tator_user_sections = {}
    for section in sections:
        tator_user_sections[section.name] = section.tator_user_sections
    logger.info(f"Created {len(sections)} sections")

    # Loop through all the media, move them into a random section and randomize the attributes
    medias = tator_api.get_media_list(project=project)
    start_date = datetime.datetime(2010, 5, 5)
    end_date = datetime.datetime(2015, 10, 10)
    for media in medias:
        trip_id = random.choice(trip_id_choices)
        trip_date = random.random() * (end_date - start_date) + start_date
        update = {
            "attributes": {
                "Trip ID": trip_id,
                "Media Reviewed": random.choice(reviewed_choices),
                "Trip Date": trip_date.isoformat(),
                "tator_user_sections": tator_user_sections[trip_id]
            }
        }
        tator_api.update_media(id=media.id, media_update=update)
    logger.info(f"Updated {len(medias)} medias")

def main(
        tator_api: tator.api,
        project: int) -> None:
    """ Main function that uploads the media and creates the corresponding localizations
    """

    # Remove existing localizations
    locs = tator_api.get_localization_list(project=project)
    logger.info(f"Deleting {len(locs)} existing localizations")
    for loc in locs:
        tator_api.delete_localization(id=loc.id)

    # Get all the existing sections and delete them
    sections = tator_api.get_section_list(project=project)
    logger.info(f"Deleting {len(sections)} existing sections")
    for section in sections:
        tator_api.delete_section(id=section.id)

    # Update existing media and create new localizations
    update_medias_and_sections(tator_api=tator_api, project=project)
    medias = tator_api.get_media_list(project=project)
    media_id_map = {}
    for media in medias:
        media_id_map[media.id] = media

    # Get the localization types to choose from
    localization_types = tator_api.get_localization_type_list(project=project)
    loc_type_label = {}
    for loc_type in localization_types:
        loc_type_label[loc_type.id] = loc_type.dtype

    # Get the versions to choose from
    versions = tator_api.get_version_list(project=project)
    version_map = {}
    for version in versions:
        version_map[version.id] = version

    # Create the random localizations
    analytics_data = create_localizations(
        tator_api=tator_api,
        project=project,
        medias=medias,
        localization_types=localization_types,
        versions=versions)

    # Print out various stats about the media and localization
    # This info is useful for testing
    #
    # The following localization counts for each filter condition are display
    # All localization counts (no filter)
    # Section is Atlantic 05/2021 and reviewed is true
    # All species equaling "Lobster" in version "Algorithm Results"
    # All species equaling "Scallop" and Valid is false
    # All count > 2 and confidence < 0.5 and dtype == "line"
    # All species including Herring and confidence > 0.25
    # Reviewed is true and confidence > 0.5
    # Trip ID including Atlantic and version "User Annotations"
    # Media reviewed is true and species equaling "Scallop"
    # Media whose Trip Date is between 2011-01-01 to 2013-01-01
    # Media whose Trip Date is before 2012-05-05
    # Media whose Trip Date is after 2013-04-04

    # All localization counts (no filter)
    loc_count = 0
    for media_id in analytics_data:
        loc_count += len(analytics_data[media_id])
    logger.info(f"Count of all localizations -> {loc_count}")

    # Trip ID is Atlantic 05/2021 and reviewed is true
    loc_count = 0
    for media_id in analytics_data:
        media = media_id_map[media_id]
        attrs = media.attributes
        if attrs["Trip ID"] == "Atlantic 05/2021" and attrs["Media Reviewed"]:
            loc_count += len(analytics_data[media_id])
    logger.info(f"Count localizations in media whose section:Atlantic 05/2021 AND Media Reviewed:true -> {loc_count}")

    # All species equaling to "Lobster" in version "Algorithm Results"
    loc_count = 0
    for media_id in analytics_data:
        for loc in analytics_data[media_id]:
            if loc["Species"] == "Lobster" and version_map[loc["version"]].name == "Algorithm Results":
                loc_count += 1
    logger.info(f"Count of localizations whose Species:Lobster AND version:Algorithm Results -> {loc_count}")

    # All species equaling "Scallop" and Valid is false
    loc_count = 0
    for media_id in analytics_data:
        for loc in analytics_data[media_id]:
            if loc["Species"] == "Scallop" and not loc["Valid"]:
                loc_count += 1
    logger.info(f"Count of localizations whose Species:Scallop AND Valid:false -> {loc_count}")

    # All count > 2 and confidence < 0.5 and dtype == "line"
    loc_count = 0
    for media_id in analytics_data:
        for loc in analytics_data[media_id]:
            if loc["Count"] > 2 and loc["Algorithm Confidence"] < 0.5 and loc_type_label[loc["type"]] == "line":
                loc_count += 1
    logger.info(f"Count of localizations whose Count:>2 AND Algorithm Confidence:<0.5 AND dtype:line -> {loc_count}")

    # All species including Herring and confidence > 0.25
    loc_count = 0
    for media_id in analytics_data:
        for loc in analytics_data[media_id]:
            if "Herring" in loc["Species"] and loc["Algorithm Confidence"] > 0.25:
                loc_count += 1
    logger.info(f"Count of localizations whose Species:*Herring* AND Algorithm Confidence:>0.25 -> {loc_count}")

    # Reviewed is true and confidence < 0.5
    loc_count = 0
    for media_id in analytics_data:
        media = media_id_map[media_id]
        attrs = media.attributes
        if attrs["Media Reviewed"]:
            for loc in analytics_data[media_id]:
                if loc["Algorithm Confidence"] > 0.5:
                    loc_count += 1
    logger.info(f"Count of localizations whose Algorithm Confidence:>0.5 AND in media whose Media Reviewed:true -> {loc_count}")

    # Trip ID including Atlantic and version "User Annotations"
    loc_count = 0
    for media_id in analytics_data:
        media = media_id_map[media_id]
        attrs = media.attributes
        if "Atlantic" in attrs["Trip ID"]:
            for loc in analytics_data[media_id]:
                if version_map[loc["version"]].name == "User Annotations":
                    loc_count += 1
    logger.info(f"Count of localizations in media whose Trip ID includes Atlantic AND version:User Annotations -> {loc_count}")

    # Media reviewed is true and species equaling "Scallop"
    loc_count = 0
    for media_id in analytics_data:
        media = media_id_map[media_id]
        attrs = media.attributes
        if attrs["Media Reviewed"]:
            for loc in analytics_data[media_id]:
                if loc["Species"] == "Scallop":
                    loc_count += 1
    logger.info(f"Count of localizations whose Species:Scallop AND in media whose Media Reviewed:true -> {loc_count}")

    # Media whose Trip Date is between 2011-01-01 to 2013-01-01
    loc_count = 0
    start_date = datetime.datetime(2011, 1, 1)
    end_date = datetime.datetime(2013, 1, 1)
    for media_id in analytics_data:
        media = media_id_map[media_id]
        attrs = media.attributes
        trip_date = dateutil.parser.parse(attrs["Trip Date"])
        if trip_date >= start_date and trip_date <= end_date:
            for loc in analytics_data[media_id]:
                loc_count += 1
    logger.info(f"Count of localizations whose in media whose Trip Date:{{{start_date.isoformat()} TO {end_date.isoformat()}}} -> {loc_count}")

    # Media whose Trip Date is before 2012-05-05
    loc_count = 0
    end_date = datetime.datetime(2012, 5, 5)
    for media_id in analytics_data:
        media = media_id_map[media_id]
        attrs = media.attributes
        trip_date = dateutil.parser.parse(attrs["Trip Date"])
        if trip_date <= end_date:
            for loc in analytics_data[media_id]:
                loc_count += 1
    logger.info(f"Count of localizations whose in media whose Trip Date:{{* TO {end_date.isoformat()}}} -> {loc_count}")

    # Media whose Trip Date is after 2013-04-04
    loc_count = 0
    start_date = datetime.datetime(2013, 4, 4)
    for media_id in analytics_data:
        media = media_id_map[media_id]
        attrs = media.attributes
        trip_date = dateutil.parser.parse(attrs["Trip Date"])
        if trip_date >= start_date:
            for loc in analytics_data[media_id]:
                loc_count += 1
    logger.info(f"Count of localizations whose in media whose Trip Date:{{{start_date.isoformat()} TO *}} -> {loc_count}")

    # Localization whose Sighting Date is before 2021-03-03 and after 2021-06-06
    loc_count = 0
    start_date = datetime.datetime(2021, 3, 3)
    end_date = datetime.datetime(2021, 6, 6)
    for media_id in analytics_data:
        media = media_id_map[media_id]
        for loc in analytics_data[media_id]:
            sighting_date = loc["Sighting Date"]
            if sighting_date >= start_date and sighting_date <= end_date:
                loc_count += 1
    logger.info(f"Count of localizations whose Sighting Date is:{{{start_date.isoformat()} TO {end_date.isoformat()}}} -> {loc_count}")

    # Localization whose Sighting Date is before 2021-04-04
    loc_count = 0
    end_date = datetime.datetime(2021, 4, 4)
    for media_id in analytics_data:
        media = media_id_map[media_id]
        for loc in analytics_data[media_id]:
            sighting_date = loc["Sighting Date"]
            if sighting_date <= end_date:
                loc_count += 1
    logger.info(f"Count of localizations whose Sighting Date is:{{* TO {end_date.isoformat()}}} -> {loc_count}")

    # Localization whose Sighting Date is after 2021-06-06
    loc_count = 0
    start_date = datetime.datetime(2021, 6, 6)
    for media_id in analytics_data:
        media = media_id_map[media_id]
        for loc in analytics_data[media_id]:
            sighting_date = loc["Sighting Date"]
            if sighting_date >= start_date:
                loc_count += 1
    logger.info(f"Count of localizations whose Sighting Date is:{{{start_date.isoformat()} TO *}} -> {loc_count}")


def parse_args() -> argparse.Namespace:
    """ Process script arguments
    """

    parser = argparse.ArgumentParser(description="Uploads the classifier results to Tator")
    parser.add_argument("--host", type=str, required=True)
    parser.add_argument("--token", type=str, required=True)
    parser.add_argument("--project", type=int, required=True)
    return parser.parse_args()

def script_main() -> None:
    """ Script entrypoint
    """

    args = parse_args()
    tator_api = tator.get_api(host=args.host, token=args.token)
    main(tator_api=tator_api, project=args.project)

if __name__ == "__main__":
    script_main()