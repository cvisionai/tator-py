#!/usr/bin/env python

""" Setup Tator Test Project

This example demonstrates how to create a project and configure media
and metadata type definitions.

There are a few options available in this script:

- Default behavior is to:
    1. create the image/video/multi media types
    2. create a test version based off the baseline
    3. create the box/line/dot localization types
    4. does not create any state types

- Options are available to add the following state types:
    1. create a state type that utilizes the latest interpolation and frame association attributes
       with bool states
    2. create a few state types that utilize the attr_style_range interpolation and frame
       association attributes
    3. create a state type that utilizes no interpolation and localization association attributes

"""

import argparse
import logging
import sys

import tator

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_latest_state_types(
        tator_api,
        project,
        video_type_id,
        multi_type_id):
    """ Create a state type using latest interpolation and frame association
    """

    spec = {
        "name": "Test State",
        "description": "Test latest/frame state",
        "dtype": "state",
        "interpolation": "latest",
        "association": "Frame",
        "visible": True,
        "grouping_default": True,
        "media_types": [video_type_id, multi_type_id],
        "attribute_types": [
            {
                "name": "Activity 1",
                "dtype": "bool",
                "default": False,
                "order": 0,
            },
            {
                "name": "Activity 2",
                "dtype": "bool",
                "default": False,
                "order": 1,
            },
        ]
    }

    response = tator_api.create_state_type(project=project, state_type_spec=spec)
    logger.info(response.message)

    return response.id

def create_attr_style_range_state_types(
        tator_api,
        project,
        video_type_id):
    """ Create a few state types using attr_style_range interpolation and frame association
    """

    type_ids = []

    for index in range(1):
        spec = {
            "name": f"Single Range {index}",
            "description": f"Test event {index} information",
            "dtype": "state",
            "interpolation": "attr_style_range",
            "association": "Frame",
            "visible": True,
            "grouping_default": False,
            "media_types": [video_type_id],
            "attribute_types": [
                {
                    "name": "Start Frame",
                    "dtype": "int",
                    "default": -1,
                    "minimum": -1,
                    "style": "start_frame",
                },
                {
                    "name": "End Frame",
                    "dtype": "int",
                    "default": -1,
                    "minimum": -1,
                    "style": "end_frame",
                },
                {
                    "name": "Notes Area",
                    "dtype": "string",
                    "default": "",
                    "style": "long_string",
                },
                {
                    "name": "Disabled Notes Area",
                    "dtype": "string",
                    "default": "Not verified",
                    "style": "disabled long_string"
                },
                {
                    "name": "Disabled Field 1",
                    "dtype": "int",
                    "style": "disabled",
                },
                {
                    "name": "Disabled Field 2",
                    "dtype": "string",
                    "style": "disabled",
                },
            ]
        }

        response = tator_api.create_state_type(project=project, state_type_spec=spec)
        logger.info(response.message)
        type_ids.append(response.id)

    for index in range(1):
        spec = {
            "name": f"Single Range (Endchecks) {index}",
            "description": f"Test event {index} information",
            "dtype": "state",
            "interpolation": "attr_style_range",
            "association": "Frame",
            "visible": True,
            "grouping_default": False,
            "media_types": [video_type_id],
            "attribute_types": [
                {
                    "name": "Start Frame",
                    "dtype": "int",
                    "default": -1,
                    "minimum": -1,
                    "style": "start_frame",
                },
                {
                    "name": "End Frame",
                    "dtype": "int",
                    "default": -1,
                    "minimum": -1,
                    "style": "end_frame",
                },
                {
                    "name": "Starts In This Video",
                    "dtype": "bool",
                    "default": True,
                    "style": "start_frame_check"
                },
                {
                    "name": "Ends In This Video",
                    "dtype": "bool",
                    "default": True,
                    "style": "end_frame_check"
                },
                {
                    "name": "Notes Area",
                    "dtype": "string",
                    "default": "",
                    "style": "long_string",
                },
                {
                    "name": "Disabled Notes Area",
                    "dtype": "string",
                    "default": "Not verified",
                    "style": "disabled long_string"
                },
                {
                    "name": "Disabled Field 1",
                    "dtype": "int",
                    "style": "disabled",
                },
                {
                    "name": "Disabled Field 2",
                    "dtype": "string",
                    "style": "disabled",
                },
            ]
        }

        response = tator_api.create_state_type(project=project, state_type_spec=spec)
        logger.info(response.message)
        type_ids.append(response.id)

    for index in range(1):
        spec = {
            "name": f"Test Multirange {index}",
            "description": f"Test event {index} information",
            "dtype": "state",
            "interpolation": "attr_style_range",
            "association": "Frame",
            "visible": True,
            "grouping_default": False,
            "media_types": [video_type_id],
            "attribute_types": [
                {
                    "name": "Range2",
                    "default": "Range2 Start Frame|Range2 End Frame|Range2 In Video",
                    "dtype": "string",
                    "style": "range_set",
                    "order": -2,
                },
                {
                    "name": "Range 3",
                    "default": "Range3 Start Frame|Range3 End Frame|Range3 In Video",
                    "dtype": "string",
                    "style": "range_set",
                    "order": -3,
                },
                {
                    "name": "Range 1",
                    "default": "Range1 Start Frame|Range1 End Frame|Range1 In Video",
                    "dtype": "string",
                    "style": "range_set",
                    "order": -1,
                },
                {
                    "name": "Range1 In Video",
                    "dtype": "bool",
                    "default": False,
                    "style": "in_video_check",
                },
                {
                    "name": "Range1 Start Frame",
                    "dtype": "int",
                    "default": -1,
                    "minimum": -1,
                    "style": "start_frame",
                },
                {
                    "name": "Range1 End Frame",
                    "dtype": "int",
                    "default": -1,
                    "minimum": -1,
                    "style": "end_frame",
                },
                {
                    "name": "Range2 In Video",
                    "dtype": "bool",
                    "default": False,
                    "style": "in_video_check",
                },
                {
                    "name": "Range2 Start Frame",
                    "dtype": "int",
                    "default": -1,
                    "minimum": -1,
                    "style": "start_frame",
                },
                {
                    "name": "Range2 End Frame",
                    "dtype": "int",
                    "default": -1,
                    "minimum": -1,
                    "style": "end_frame",
                },
                {
                    "name": "Range3 In Video",
                    "dtype": "bool",
                    "default": False,
                    "style": "in_video_check",
                },
                {
                    "name": "Range3 Start Frame",
                    "dtype": "int",
                    "default": -1,
                    "minimum": -1,
                    "style": "start_frame",
                },
                {
                    "name": "Range3 End Frame",
                    "dtype": "int",
                    "default": -1,
                    "minimum": -1,
                    "style": "end_frame",
                },
                {
                    "name": "Notes Area",
                    "dtype": "string",
                    "default": "",
                    "style": "long_string",
                },
                {
                    "name": "Disabled Notes Area",
                    "dtype": "string",
                    "default": "Not verified",
                    "style": "disabled long_string"
                },
                {
                    "name": "Disabled Field 1",
                    "dtype": "int",
                    "style": "disabled",
                },
                {
                    "name": "Disabled Field 2",
                    "dtype": "string",
                    "style": "disabled",
                },
            ]
        }

        response = tator_api.create_state_type(project=project, state_type_spec=spec)
        logger.info(response.message)
        type_ids.append(response.id)


    return type_ids

def create_track_type(
        tator_api,
        project,
        video_type_id):
    """ Create a state type using no interpolation and localization association
    """

    spec = {
      "name": "Test Track",
      "description": f"Test track using localizations as detections",
      "interpolation": "none",
      "association": "Localization",
      "visible": True,
      "grouping_default": True,
      "media_types": [video_type_id],
      "attribute_types": [
        {
          "name": "Label",
          "dtype": "string",
          "order": 0,
          "default": "",
        },
        {
          "name": "Confidence",
          "dtype": "float",
          "order": 1,
          "default": 0.0,
        },
      ]
    }

    response = tator_api.create_state_type(project=project, state_type_spec=spec)
    logger.info(response.message)

def create_media_types(tator_api, project):
    """
    """

    # Create image type.
    result = tator_api.create_media_type(project, media_type_spec={
        "name": "Test Images",
        "description": "A test image type.",
        "dtype": "image",
        "attribute_types": [
            {
              "name": "Test Bool",
              "dtype": "bool",
              "order": 0,
              "default": False
            },
            {
              "name": "Test Int",
              "dtype": "int",
              "order": 1,
              "default": 0,
              "minimum": 0,
              "maximum": 1000
            },
            {
              "name": "Test Float",
              "dtype": "float",
              "order": 2,
              "default": 0.0,
              "minimum": -1000.0,
              "maximum": 1000.0
            },
            {
              "name": "Test String",
              "dtype": "string",
              "order": 3
            },
            {
              "name": "Test Enum",
              "dtype": "enum",
              "order": 4,
              "choices": ["Test Choice 1", "Test Choice 2", "Test Choice 3"],
              "labels": ["Test Choice 1", "Test Choice 2", "Test Choice 3"],
              "default": "Test Choice 1"
            },
            {
              "name": "Test Datetime",
              "dtype": "datetime",
              "order": 5,
              "use_current": True
            },
            {
              "name": "Test Geoposition",
              "dtype": "geopos",
              "order": 6,
              "default": [-71.05674, 42.35866]
            }
        ]
    })
    image_type = result.id
    logger.info(result.message)

    # Create video type.
    result = tator_api.create_media_type(project, media_type_spec={
        "name": "Test Videos",
        "description": "A test video type.",
        "dtype": "video",
        "default_volume": 50,
        "attribute_types": [
            {
              "name": "Test Bool",
              "dtype": "bool",
              "order": 0,
              "default": False
            },
            {
              "name": "Test Int",
              "dtype": "int",
              "order": 1,
              "default": 0,
              "minimum": 0,
              "maximum": 1000
            },
            {
              "name": "Test Float",
              "dtype": "float",
              "order": 2,
              "default": 0.0,
              "minimum": -1000.0,
              "maximum": 1000.0
            },
            {
              "name": "Test String",
              "dtype": "string",
              "order": 3
            },
            {
              "name": "Test Enum",
              "dtype": "enum",
              "order": 4,
              "choices": ["Test Choice 1", "Test Choice 2", "Test Choice 3"],
              "labels": ["Test Choice 1", "Test Choice 2", "Test Choice 3"],
              "default": "Test Choice 1"
            },
            {
              "name": "Test Datetime",
              "dtype": "datetime",
              "order": 5,
              "use_current": True
            },
            {
              "name": "Test Geoposition",
              "dtype": "geopos",
              "order": 6,
              "default": [-71.05674, 42.35866]
            }
        ]
    })
    video_type = result.id
    logger.info(result.message)

    # Create multi type
    result = tator_api.create_media_type(project, media_type_spec={
        "name": "Test Multi Video",
        "description": "A test multi video type.",
        "dtype": "multi",
        "attribute_types": [
            {
              "name": "Test String",
              "dtype": "string",
              "style": "long_string",
              "order": 0
            },
        ]
    })
    multi_type = result.id
    logger.info(result.message)

    return image_type, video_type, multi_type

def create_localization_types(
        tator_api,
        project,
        image_type,
        video_type,
        version_color_map):
    """
    """

    # Create box type.
    result = tator_api.create_localization_type(project, localization_type_spec={
        "name": "Test Boxes",
        "description": "A test box type.",
        "dtype": "box",
        "media_types": [image_type, video_type],
        "colorMap": {
          "default": [255, 0, 0],
          "key": "Test Enum",
          "map": {
              "Test Choice 1": [0, 255, 0],
              "Test Choice 2": [0, 0, 255]
          }
        },
        "attribute_types": [
            {
              "name": "Test Bool",
              "dtype": "bool",
              "order": 0,
              "default": False
            },
            {
              "name": "Test Int",
              "dtype": "int",
              "order": 1,
              "default": 0,
              "minimum": 0,
              "maximum": 1000
            },
            {
              "name": "Test Float",
              "dtype": "float",
              "order": 2,
              "default": 0.0,
              "minimum": -1000.0,
              "maximum": 1000.0
            },
            {
              "name": "Test String",
              "dtype": "string",
              "order": 3
            },
            {
              "name": "Test Enum",
              "dtype": "enum",
              "order": 4,
              "choices": ["Test Choice 1", "Test Choice 2", "Test Choice 3"],
              "labels": ["Test Choice 1", "Test Choice 2", "Test Choice 3"],
              "default": "Test Choice 1"
            },
            {
              "name": "Test Datetime",
              "dtype": "datetime",
              "order": 5,
              "use_current": True
            },
            {
              "name": "Test Geoposition",
              "dtype": "geopos",
              "order": 6,
              "default": [-71.05674, 42.35866]
            }
        ]
    })
    box_type = result.id
    logger.info(result.message)

    # Create line type.
    result = tator_api.create_localization_type(project, localization_type_spec={
        "name": "Test Lines",
        "description": "A test line type.",
        "dtype": "line",
        "media_types": [image_type, video_type],
        "attribute_types": [
            {
              "name": "Test Bool",
              "dtype": "bool",
              "order": 0,
              "default": False
            },
            {
              "name": "Test Int",
              "dtype": "int",
              "order": 1,
              "default": 0,
              "minimum": 0,
              "maximum": 1000
            },
            {
              "name": "Test Float",
              "dtype": "float",
              "order": 2,
              "default": 0.0,
              "minimum": -1000.0,
              "maximum": 1000.0
            },
            {
              "name": "Test String",
              "dtype": "string",
              "order": 3
            },
            {
              "name": "Test Enum",
              "dtype": "enum",
              "order": 4,
              "choices": ["Test Choice 1", "Test Choice 2", "Test Choice 3"],
              "labels": ["Test Choice 1", "Test Choice 2", "Test Choice 3"],
              "default": "Test Choice 1"
            },
            {
              "name": "Test Datetime",
              "dtype": "datetime",
              "order": 5,
              "use_current": True
            },
            {
              "name": "Test Geoposition",
              "dtype": "geopos",
              "order": 6,
              "default": [-71.05674, 42.35866]
            }
        ]
    })
    line_type = result.id
    logger.info(result.message)

    # Create dot type.
    result = tator_api.create_localization_type(project, localization_type_spec={
        "name": "Test Dots",
        "description": "A test dot type.",
        "dtype": "dot",
        "media_types": [image_type, video_type],
        "colorMap": {
          "default": [255, 0, 0],
          "version": version_color_map
        },
        "attribute_types": [
            {
              "name": "Test Bool",
              "dtype": "bool",
              "order": 0,
              "default": False
            },
            {
              "name": "Test Int",
              "dtype": "int",
              "order": 1,
              "default": 0,
              "minimum": 0,
              "maximum": 1000
            },
            {
              "name": "Test Float",
              "dtype": "float",
              "order": 2,
              "default": 0.0,
              "minimum": -1000.0,
              "maximum": 1000.0
            },
            {
              "name": "Test String",
              "dtype": "string",
              "order": 3
            },
            {
              "name": "Test Enum",
              "dtype": "enum",
              "order": 4,
              "choices": ["Test Choice 1", "Test Choice 2", "Test Choice 3"],
              "labels": ["Test Choice 1", "Test Choice 2", "Test Choice 3"],
              "default": "Test Choice 1"
            },
            {
              "name": "Test Datetime",
              "dtype": "datetime",
              "order": 5,
              "use_current": True
            },
            {
              "name": "Test Geoposition",
              "dtype": "geopos",
              "order": 6,
              "default": [-71.05674, 42.35866]
            }
        ]
    })
    dot_type = result.id
    logger.info(result.message)

    return box_type, line_type, dot_type

def parse_args() -> argparse.Namespace:
    """ Process arguments
    """
    parser = tator.get_parser()
    parser.add_argument("--name", type=str, required=True, help="New project's name")
    parser.add_argument("--create-state-latest-type", action="store_true", help="Create a state type with latest interpolation/frame association attributes")
    parser.add_argument("--create-state-range-type", action="store_true", help="Create state types with attr_style_range interpolation/frame association")
    parser.add_argument("--create-track-type", action="store_true", help="Create a state type with localization association")
    args = parser.parse_args()

    return args

def main() -> None:
    """
    """

    args = parse_args()

    tator_api = tator.get_api(args.host, args.token)

    # Create test organization
    result = tator_api.create_organization(organization_spec={
        'name': 'My Organization',
    })

    # Create the test project
    result = tator_api.create_project(project_spec={
        'name': args.name,
        'summary': 'A test project.',
        'organization': result.id
    })
    project = result.id
    logger.info(result.message)

    # Create the media types
    image_type, video_type, multi_type = create_media_types(tator_api=tator_api, project=project)

    # Get the baseline version
    baseline_version = tator_api.get_version_list(project)[0].id

    # Create another version that is based off the baseline
    result = tator_api.create_version(project, version_spec={
        "name": "Test Version",
        "description": "A test version.",
        "show_empty": True,
        "bases": [baseline_version],
    })
    version = result.id
    logger.info(result.message)

    version_color_map = {
        baseline_version: [0, 255, 0],
        version: [0, 0, 255]
    }

    # Create the localization types
    box_type, line_type, dot_type = create_localization_types(
        tator_api=tator_api,
        project=project,
        image_type=image_type,
        video_type=video_type,
        version_color_map=version_color_map)

    # Create the state types if asked
    if args.create_state_latest_type:
        create_latest_state_types(
            tator_api=tator_api,
            project=project,
            video_type_id=video_type,
            multi_type_id=multi_type)

    if args.create_state_range_type:
        create_attr_style_range_state_types(
            tator_api=tator_api,
            project=project,
            video_type_id=video_type)

    if args.create_track_type:
        create_track_type(
            tator_api=tator_api,
            project=project,
            video_type_id=video_type)

    # fin.
    logger.info("Test project setup complete!")

if __name__ == '__main__':

    main()
