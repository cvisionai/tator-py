""" Assumes
"""

import argparse
import logging
import random
import sys

import tator
import progressbar

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

def create_state_types(
        tator_api,
        project) -> None:
    """
    """

    state_types = tator_api.get_state_type_list(project=project)
    assert len(state_types) == 0

    media_types = tator_api.get_media_type_list(project=project)
    media_type_ids = [media_type.id for media_type in media_types]

    # Create the media-associated state type used by the main() function of this project
    spec = {
        "name": "Submission",
        "description": "Media associated state type",
        "dtype": "state",
        "association": "Media",
        "visible": True,
        "grouping_default": False,
        "media_types": media_type_ids,
        "attribute_types": [
            {
                "name": "Submission IDNUM",
                "dtype": "string",
            },
            {
                "name": "Submission Truth Species",
                "dtype": "string",
            },
            {
                "name": "Submission Classifier Dataset",
                "dtype": "string",
            },
            {
                "name": "Run classifier",
                "dtype": "bool",
            },
        ]
    }

    response = tator_api.create_state_type(project=project, state_type_spec=spec)
    logger.info(response)

    # Create the localization-associated state type used by the main() function of this project
    spec = {
        "name": "Submission Result",
        "description": "Localization associated state type",
        "dtype": "state",
        "association": "Localization",
        "visible": True,
        "grouping_default": False,
        "media_types": media_type_ids,
        "attribute_types": [
            {
                "name": "Predicted Species",
                "dtype": "string",
            },
            {
                "name": "Entropy",
                "dtype": "float",
            },
        ]
    }

    response = tator_api.create_state_type(project=project, state_type_spec=spec)
    logger.info(response)

def main(
      tator_api: tator.api,
      project: int) -> None:
    """
    """

    # Remove existing states
    states = tator_api.get_state_list(project=project)
    logger.info(f"Deleting {len(states)} existing states")
    tator_api.delete_state_list(project=project)

    # Remove existing localizations
    locs = tator_api.get_localization_list(project=project)
    logger.info(f"Deleting {len(locs)} existing localizations")
    tator_api.delete_localization_list(project=project)

    # Get the state type list
    state_types = tator_api.get_state_type_list(project=project)
    assert len(state_types) == 2
    for this_type in state_types:
        if this_type.name == "Submission":
            media_state_type = this_type
        elif this_type.name == "Submission Result":
            loc_state_type = this_type

    # Get the localization type list
    loc_types = tator_api.get_localization_type_list(project=project)
    for this_type in loc_types:
        if this_type.name == "Box":
            loc_type = this_type


    # Get all the media (assumed to be images for now)
    medias = tator_api.get_media_list(project=project)
    logger.info(f"Project has {len(medias)} medias")

    # Create the random states using the media
    # - Randomize the media
    # - Create a new state with a random set of 1 - 5 media
    # - State will have the following random attributes
    #   - Run classifier (True/False)
    #   - Submission Truth Species ("ALEWIFE", "COD, ATLANTIC", "FLOUNDER, YELLOWTAIL", "HADDOCK", "HERRING, ATLANTIC")
    #   - Submission IDNUM ("%05d"%random.randint(0,99999))
    #   - Submission Classifier Dataset (Training/Test)
    # - Repeat creating new states until all media has been exhausted
    random.shuffle(medias)

    media_index = 0
    num_media = len(medias)
    new_state_specs = []
    created_media_ids = []
    while media_index < num_media:
        if num_media - media_index <= 5:
            # Use the rest of the media to create the final state
            media_count = num_media - media_index
        else:
            media_count = random.choice([1,2,3,4,5])

        media_ids = []
        while media_count > 0:
            media_ids.append(medias[media_index + media_count - 1].id)
            media_count -= 1

        state_spec = {
          "type": media_state_type.id,
          "media_ids": media_ids,
          "Run Classifier": random.choice([True, False]),
          "Submission Truth Species": random.choice(["ALEWIFE", "COD, ATLANTIC", "FLOUNDER, YELLOWTAIL", "HADDOCK", "HERRING, ATLANTIC"]),
          "Submission IDNUM": "%05d"%random.randint(0,99999),
          "Submission Classifier Dataset": random.choice(["Training", "Test"])
        }
        new_state_specs.append(state_spec)
        media_index += len(media_ids)

    logger.info(f"Making {len(new_state_specs)} media-associated {media_state_type.name} states")

    # Finally create the states
    for idx in range(0, len(new_state_specs), 500):
        response = tator_api.create_state_list(
            project=project,
            state_spec=new_state_specs[idx:idx+500])
        created_media_ids += response.id

    media_id_map = {}
    for media_id, media_spec in zip(created_media_ids, new_state_specs):
        media_id_map[media_id] = media_spec

    logger.info(f"{len(created_media_ids)} media-associated {media_state_type.name} states created")

    # Now, create the localization state specs based on the media state specs
    # Loop through each of the
    media_state_specs = new_state_specs
    new_state_specs = []
    for media_state in media_state_specs:

        # Create a localization for each
        new_loc_specs = []
        localization_ids = []
        best_species = "UNKNOWN"
        best_entropy = 1.0
        for media_id in media_state["media_ids"]:
            loc_spec = {
                "frame": 0,
                "type": loc_type.id,
                "media_id": media_id,
                "x": 0.1,
                "y": 0.1,
                "width": 0.8,
                "height": 0.8
            }
            new_loc_specs.append(loc_spec)

        for idx in range(0, len(new_loc_specs), 500):
            response = tator_api.create_localization_list(
                project=project,
                localization_spec=new_loc_specs[idx:idx+500])
            localization_ids += response.id

        state_spec = {
            "type": loc_state_type.id,
            "media_ids": media_state["media_ids"],
            "localization_ids": localization_ids,
            "Predicted Species": random.choice(["ALEWIFE", "COD, ATLANTIC", "FLOUNDER, YELLOWTAIL", "HADDOCK", "HERRING, ATLANTIC"]),
            "Submission Entropy": random.random(),
        }
        new_state_specs.append(state_spec)

    # Finally create the states
    for idx in range(0, len(new_state_specs), 500):
        response = tator_api.create_state_list(
            project=project,
            state_spec=new_state_specs[idx:idx+500])

    logger.info(f"{len(new_state_specs)} localization-associated {media_state_type.name} states created")

def parse_args() -> argparse.Namespace:
    """ Process script arguments
    """

    parser = argparse.ArgumentParser(description="Uploads the classifier results to Tator")
    parser.add_argument("--host", type=str, required=True)
    parser.add_argument("--token", type=str, required=True)
    parser.add_argument("--project", type=int, required=True)
    parser.add_argument("--create-state-types", action="store_true")
    return parser.parse_args()

def script_main() -> None:
    """ Script entrypoint
    """

    args = parse_args()
    tator_api = tator.get_api(host=args.host, token=args.token)

    if args.create_state_types:
        create_state_types(tator_api=tator_api, project=args.project)
    main(tator_api=tator_api, project=args.project)

if __name__ == "__main__":
    script_main()