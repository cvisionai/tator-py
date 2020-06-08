import argparse
import logging
import sys

import tator as pytator

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Creates a test project.")
    parser.add_argument('--host', default='https://www.tatorapp.com')
    parser.add_argument('--token', help="Your API token.")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    config = pytator.Configuration()
    config.host=args.host
    config.api_key['Authorization'] = args.token
    config.api_key_prefix['Authorization'] = 'Token'
    tator = pytator.TatorApi(pytator.ApiClient(config))

    # Create the project.
    result = tator.create_project(body={'name': 'Test Project', 'summary': 'A test project.'})
    project = result.id
    logger.info(result.message)

    # Create image type.
    result = tator.create_media_type(project, body={
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
    result = tator.create_media_type(project, body={
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

    # Get baseline version.
    baseline_version = tator.get_version_list(project)[0].id

    # Create additional version.
    result = tator.create_version(project, body={
        "name": "Test Version",
        "description": "A test version.",
        "show_empty": True,
        "bases": [baseline_version],
    })
    version = result.id
    logger.info(result.message)

    # Create box type.
    result = tator.create_localization_type(project, body={
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
    result = tator.create_localization_type(project, body={
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
    result = tator.create_localization_type(project, body={
        "name": "Test Dots",
        "description": "A test dot type.",
        "dtype": "dot",
        "media_types": [image_type, video_type],
        "colorMap": {
          "default": [255, 0, 0],
          "version": {
              baseline_version: [0, 255, 0],
              version: [0, 0, 255]
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
    dot_type = result.id
    logger.info(result.message)
    logger.info("Test project setup complete!")
