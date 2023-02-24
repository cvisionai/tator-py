#!/usr/bin/env python3
"""
Script that adds a new attribute type to a localization type.
"""

import argparse
import logging
import json
from pprint import pformat

import tator

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    """Parse the provided arguments

    Returns parsed arguments in a namespace object.

    """
    parser = argparse.ArgumentParser(description="Add attribute to existing type")
    parser = tator.get_parser(parser=parser)
    parser.add_argument("project", type=int, help="Unique project id")
    parser.add_argument(
        "localization_type_id", type=int, help="ID of localization type to add attribute to"
    )
    parser.add_argument("new_attribute", type=str, help="Attribute to add (JSON string)")

    args = parser.parse_args()
    logger.info(args)

    return args


def main(
    host: str, token: str, project: int, localization_type_id: int, new_attribute: dict
) -> None:
    """Main routine of this script"""

    # Get the interface to Tator
    tator_api = tator.get_api(host=host, token=token)

    # Get attribute type list before addition
    localization_type = tator_api.get_localization_type(localization_type_id)
    logger.info(f"Existing list of attributes:\n{pformat(localization_type.attribute_types)}")

    # Create the attribute addition message
    addition = {"entity_type": "LocalizationType", "addition": new_attribute}
    logger.info(f"Calling create_attribute_type with id '{localization_type_id}' and "
                f"attribute_type_spec\n{pformat(addition)}")

    # Add the attribute to the given localization type
    response = tator_api.create_attribute_type(
        id=localization_type_id, attribute_type_spec=addition
    )

    # Get attribute type list after addition
    localization_type = tator_api.get_localization_type(localization_type_id)
    logger.info(f"New list of attributes:\n{pformat(localization_type.attribute_types)}")

    logger.info("[FINISHED] localization_attribute_addition.py")


if __name__ == "__main__":

    args = parse_args()
    new_attribute = json.loads(args.new_attribute)
    main(args.host, args.token, args.project, args.localization_type_id, new_attribute)
