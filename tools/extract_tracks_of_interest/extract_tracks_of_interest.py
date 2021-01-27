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

            # If either the first or last localization is within the ROI, use this state, but if
            # neither or both are, do not use it
            if self._localization_in_roi(first, roi, state) != self._localization_in_roi(
                last, roi, state
            ):
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
        "--state-type", type=int, required=True, help="The type of state to consider"
    )
    parser.add_argument(
        "--state-file",
        type=str,
        help="The text file where the intermediate list of states will be stored or read from",
        default="state_list.txt",
    )
    parser.add_argument(
        "--versions", nargs="*", type=int, help="The list of layers to retrieve states from"
    )
    parser.add_argument(
        "--tracks-file",
        type=str,
        help="The text file where the intermediate list of filtered states will be stored or read from",
        default="track_list.txt",
    )
    parser.add_argument(
        "--out-folder",
        type=str,
        help="The folder where the localization graphics will be downloaded",
        default="tracks_of_interest",
    )
    parser.add_argument(
        "--roi",
        type=int,
        help="The id of the localization that defines the region of interest",
        default=94684778,
    )

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "--get-states", help="Stop processing after all states are retrieved", action="store_true"
    )
    group.add_argument(
        "--filter-states", help="Stop processing after states are filtered", action="store_true"
    )

    args = parser.parse_args()
    return args


def _state_to_dict(state):
    state_dict = state.to_dict()
    state_dict.pop("created_datetime", None)
    state_dict.pop("modified_datetime", None)
    return state_dict


def main(
    host: str,
    token: str,
    project: int,
    state_type: int,
    versions: List[int],
    state_file: str,
    tracks_file: str,
    roi: int,
    out_folder: str,
    get_states: bool,
    filter_states: bool,
) -> None:
    """Main routine of this script"""

    # Get the interface to Tator
    tator_api = tator.get_api(host=host, token=token)

    get_state_list_params = {"project": project, "type": state_type}
    if versions:
        get_state_list_params["versions"] = versions

    values_loaded = False
    if os.path.exists(state_file):
        logger.info(f"Found file {state_file}, loading values")
        with open(state_file, "r") as fp:
            serializable_state_list = json.load(fp)
        stored_state_list_params = serializable_state_list.pop(0)
        if stored_state_list_params == get_state_list_params:
            values_loaded = True
            logger.info(f"Values loaded!")
        else:
            logger.info("Stored values not retrieved with the same parameters")
    else:
        logger.info(f"File {state_file} not found")

    if not values_loaded:
        logger.info("Retrieving values from server")
        state_list = tator_api.get_state_list(project, type=state_type, version=versions)
        serializable_state_list = [_state_to_dict(state) for state in state_list]
        del state_list
        logger.info(f"Values retireved!")

        if state_file:
            logger.info(f"Storing retrieved values in {state_file}")
            serializable_state_list.insert(0, get_state_list_params)
            with open(state_file, "w") as fp:
                json.dump(serializable_state_list, fp)
            logger.info(f"Values stored!")
            serializable_state_list.pop(0)

    logger.info(f"Total number of states: {len(serializable_state_list)}")

    if get_states:
        return

    if os.path.exists(tracks_file) and values_loaded:
        # Load from disk
        logger.info(f"Found file {tracks_file}, loading values")
        with open(tracks_file, "r") as fp:
            filtered_states = json.load(fp)
        stored_roi = filtered_states.pop(0)
        if stored_roi == roi:
            logger.info(f"Values loaded!")
        else:
            logger.info("Stored values not filtered with the same parameters")
            values_loaded = False
    else:
        values_loaded = False
        logger.info(f"File {tracks_file} not found or contains stale data")

    if not values_loaded:
        logger.info(f"Filtering values")
        localization_roi = tator_api.get_localization(id=roi).to_dict()
        sf = StateFilterer(tator_api, project, serializable_state_list, localization_roi)
        filtered_states = sf.get_filtered_states()
        logger.info(f"Values filtered!")

        if state_file:
            logger.info(f"Storing calculated values in {tracks_file}")
            filtered_states.insert(0, roi)
            with open(tracks_file, "w") as fp:
                json.dump(filtered_states, fp)
            logger.info(f"Values stored!")
            filtered_states.pop(0)

    logger.info(f"Filtered number of states: {len(filtered_states)}")

    if filter_states:
        return

    logger.info(f"Retrieving localization graphics from server...")
    n_localizations_total = sum(len(state["localizations"]) for state in filtered_states)
    current_localization = 0
    for state in filtered_states:
        state_folder = os.path.join(out_folder, str(state["id"]))
        if not os.path.exists(state_folder):
            os.makedirs(state_folder)

        for localization_id in state["localizations"]:
            current_localization += 1
            img_dest = os.path.join(state_folder, str(localization_id) + ".png")

            if os.path.exists(img_dest):
                logger.warn(f"Localization graphic {img_dest} exists, skipping fetch.")
            else:
                tmp_img_path = tator_api.get_localization_graphic(localization_id)
                shutil.move(tmp_img_path, img_dest)

            _print_progress(floor(current_localization / n_localizations_total * 100))

    logger.info(f"Localization graphics retrieved!")
    return


if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))
