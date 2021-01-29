#!/usr/bin/env python3
"""
Script that gets tracks that begin/end in the region of interest
"""

import os
import argparse
import logging
import json
import shutil
from typing import List
from pprint import pformat
from math import floor
from itertools import cycle
from collections import Counter

import tator

log_filename = "sorted_graphics.log"

logging.basicConfig(
    handlers=[logging.FileHandler(log_filename, mode="w"), logging.StreamHandler()],
    format="%(asctime)s %(levelname)s:%(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

P_CYCLE = cycle(["\\", "|", "/", "-"])


def _print_progress(progress: int) -> None:
    not_done = progress < 100
    print(
        f"{progress}% [{'*' * progress}{next(P_CYCLE) if not_done else ''}{' ' * (99 - progress)}]",
        end="\r" if not_done else "\n",
    )


def parse_args() -> argparse.Namespace:
    """Parse the provided arguments

    Returns parsed arguments in a namespace object.

    """
    parser = argparse.ArgumentParser(description="Add attribute to existing type")
    parser = tator.get_parser(parser=parser)
    parser.add_argument("--project", type=int, required=True, help="Unique project id")
    parser.add_argument(
        "--localization-type", type=int, required=True, help="The type of localization to consider"
    )
    parser.add_argument(
        "--version", nargs="*", type=int, help="The list of layers to retrieve states from"
    )
    parser.add_argument(
        "--localization-file",
        type=str,
        help="The text file where the intermediate list of localizations will be stored or read from",
        default="localization_list.txt",
    )

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "--get-localizations",
        help="Stop processing after all localizations are retrieved",
        action="store_true",
    )

    args = parser.parse_args()
    return args


def _obj_to_dict(obj):
    obj_dict = obj.to_dict()
    obj_dict.pop("created_datetime", None)
    obj_dict.pop("modified_datetime", None)
    return obj_dict


def main(
    host: str,
    token: str,
    project: int,
    localization_type: int,
    version: List[int],
    localization_file: str,
    get_localizations: bool,
) -> None:
    """Main routine of this script"""

    # Get the interface to Tator
    tator_api = tator.get_api(host=host, token=token)

    get_localization_list_params = {
        "type": localization_type,
    }

    if version:
        get_localization_list_params["version"] = version

    values_loaded = False
    if os.path.exists(localization_file):
        logger.info(f"Found file {localization_file}, loading values")
        with open(localization_file, "r") as fp:
            serializable_localization_list = json.load(fp)
        stored_localization_list_params = serializable_localization_list.pop(0)
        if stored_localization_list_params == get_localization_list_params:
            values_loaded = True
            logger.info(f"Values loaded!")
        else:
            logger.info("Stored values not retrieved with the same parameters")
    else:
        logger.info(f"File {localization_file} not found")

    if not values_loaded:
        logger.info("Retrieving values from server")
        localization_list = tator_api.get_localization_list(project, **get_localization_list_params)
        serializable_localization_list = [_obj_to_dict(loc) for loc in localization_list]
        del localization_list
        logger.info(f"Values retireved!")

        if localization_file:
            logger.info(f"Storing retrieved values in {localization_file}")
            serializable_localization_list.insert(0, get_localization_list_params)
            with open(localization_file, "w") as fp:
                json.dump(serializable_localization_list, fp)
            logger.info(f"Values stored!")
            serializable_localization_list.pop(0)

    n_localizations_total = len(serializable_localization_list)
    logger.info(f"Total number of localizations: {n_localizations_total}")

    if get_localizations:
        return

    logger.info(f"Retrieving localization graphics from server...")
    current_localization = 0
    out_folder = f"localization_graphics_prj_{project}_type_{localization_type}"
    species_folders = {}
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    if version:
        out_folder += f"_ver_{'_'.join(str(v) for v in version)}"
    for idx, localization in enumerate(serializable_localization_list):
        species = localization.get("attributes", {}).get("Species", "Unknown").replace(" ", "-")
        localization_id = localization["id"]
        species_folder = species_folders.get(species)
        if not species_folder:
            species_folder = os.path.join(out_folder, species)
            species_folders[species] = species_folder
            if not os.path.exists(species_folder):
                os.makedirs(species_folder)
        img_dest = os.path.join(species_folder, f"{localization_id}-{species}.png")
        if os.path.isfile(img_dest):
            logger.warn(f"Localization graphic {img_dest} exists, skipping fetch.")
            continue

        tmp_img_path = tator_api.get_localization_graphic(localization_id)
        shutil.move(tmp_img_path, img_dest)
        _print_progress(floor((idx + 1) / n_localizations_total * 100))

    logger.info(f"Localization graphics retrieved!")
    return


if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))
