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

log_filename = "tracks_of_interest.log"

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


class StateFilterer:
    def __init__(self, tator_api, project, states, roi):
        self._tator_api = tator_api
        self._project = project
        self._state_list = states
        self._roi = roi
        self._filtered_states = None

    @property
    def roi(self) -> dict:
        return self._roi

    @roi.setter
    def roi(self, roi: dict):
        required_keys = ["x", "y", "width", "height"]
        if type(roi) == dict and all(key in roi for key in required_keys):
            self._roi = roi

            # Clear the currently filtered states on an ROI change
            self._filtered_states = None
        else:
            raise ValueError(f"roi value should be a dict containing the keys {required_keys}")

    def get_filtered_states(self, force_refilter: bool = False) -> List[dict]:
        if force_refilter or self._filtered_states is None:
            self._filtered_states = self._filter_states()

        return self._filtered_states

    @staticmethod
    def _localization_in_roi(localization, roi, state, overlap=0.9):

        # Localization extents
        l_x = [localization["x"], localization["width"] + localization["x"]]
        l_y = [localization["y"], localization["height"] + localization["y"]]

        # ROI extents
        r_x, r_y = roi

        # Intersection extents
        i_x = [max(l_x[0], r_x[0]), min(l_x[1], r_x[1])]
        i_y = [max(l_y[0], r_y[0]), min(l_y[1], r_y[1])]

        # If the max x/y intersection value is less than min x/y, this means there is zero overlap
        if i_x[1] < i_x[0] or i_y[1] < i_y[0]:
            return False

        # Return True if the overlap is at least the desired ratio of the localization area
        overlap_area = (i_x[1] - i_x[0]) * (i_y[1] - i_y[0])
        localization_area = localization["width"] * localization["height"]
        return overlap_area / localization_area >= overlap

    def _filter_states(self):
        id_set = set()
        filtered_states = []
        # ROI extents
        roi = (
            [self.roi["x"], self.roi["width"] + self.roi["x"]],
            [self.roi["y"], self.roi["height"] + self.roi["y"]],
        )

        n_states = len(self._state_list)
        for idx, state in enumerate(self._state_list):
            state_id = state["id"]

            # Only consider unique states
            if state_id in id_set:
                continue

            id_set.add(state_id)

            # Get list of localizations comprising the state
            localization_list = [
                localization.to_dict()
                for localization in self._tator_api.get_localization_list_by_id(
                    self._project, state["localizations"]
                )
            ]

            # Determine first and last localization
            first = localization_list[0]
            last = localization_list[0]
            for localization in localization_list:
                frame = localization["frame"]
                if frame < first["frame"]:
                    first = localization
                elif frame > last["frame"]:
                    last = localization

            started_in_roi = self._localization_in_roi(first, roi, state)
            ended_in_roi = self._localization_in_roi(last, roi, state)
            if started_in_roi or ended_in_roi:
                if started_in_roi and ended_in_roi:
                    endpoint_in_roi = "both"
                elif started_in_roi:
                    endpoint_in_roi = "start"
                elif ended_in_roi:
                    endpoint_in_roi = "end"
                else:
                    raise RuntimeError(f"Somehow `started_in_roi` or `ended_in_roi` changed values")

                state["endpoint_in_roi"] = endpoint_in_roi
                filtered_states.append(state)

            _print_progress(floor((idx + 1) / n_states * 100))

        return filtered_states


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
