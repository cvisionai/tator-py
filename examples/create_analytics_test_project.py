""" Tool to create a test project used for testing the analytics view
"""
import argparse

import tator

def create_organization(
        tator_api: tator.api,
        project_name: str) -> int:
    """ Create the organization
    """
    spec = {
        "name": project_name
    }
    response = tator_api.create_organization(organization_spec=spec)
    return response.id

def create_project(
        tator_api: tator.api,
        project_name: str,
        organization: int) -> int:
    """ Create the project
    """
    spec = {
        'name': project_name,
        'summary': 'A test project.',
        'organization': organization
    }
    response = tator_api.create_project(project_spec=spec)
    return response.id

def create_media_types(
        tator_api: tator.api,
        project: int) -> list:
    """ Create the media types
    """

    spec = {
      "name": "Image",
      "description": "Image type",
      "dtype": "image",
      "attribute_types": [
          {
              "name": "Trip ID",
              "dtype": "string"
          },
          {
              "name": "Media Reviewed",
              "dtype": "bool",
              "default": False
          }
      ]
    }
    response = tator_api.create_media_type(project=project, media_type_spec=spec)
    image_type_id = response.id

    spec["name"] = "Video"
    spec["description"] = "Video type"
    spec["dtype"] = "video"
    response = tator_api.create_media_type(project=project, media_type_spec=spec)
    video_type_id = response.id

    return [image_type_id, video_type_id]

def create_localization_types(
        tator_api: tator.api,
        project: int,
        media_types: list) -> list:
    """ Create the localization types
    """

    spec = {
      "name": "Box",
      "description": "Box type",
      "dtype": "box",
      "media_types": media_types,
      "attribute_types": [
          {
              "name": "Species",
              "dtype": "enum",
              "choices": ["Herring, Atlantic", "Herring, Blueback", "Lobster", "Scallop"],
          },
          {
              "name": "Confidence",
              "dtype": "float",
          },
          {
              "name": "Count",
              "dtype": "int",
          },
          {
              "name": "Valid",
              "dtype": "bool"
          }
      ]
    }
    response = tator_api.create_localization_type(project=project, localization_type_spec=spec)
    box_type_id = response.id

    spec["name"] = "Line"
    spec["description"] = "Line type"
    spec["dtype"] = "line"
    response = tator_api.create_localization_type(project=project, localization_type_spec=spec)
    line_type_id = response.id

    spec["name"] = "Dot"
    spec["description"] = "Dot type"
    spec["dtype"] = "dot"
    response = tator_api.create_localization_type(project=project, localization_type_spec=spec)
    dot_type_id = response.id

    return [box_type_id, line_type_id, dot_type_id]

def create_versions(
        tator_api: tator.api,
        project: int) -> None:
    """
    """

    response = tator_api.create_version(
        project,
        version_spec={
            "name": "User Annotations",
        },
    )

    response = tator_api.create_version(
        project,
        version_spec={
            "name": "Algorithm Results",
        },
    )

def main(
        tator_api: tator.api,
        project_name: str) -> None:
    """ Main function that creates all the types
    """

    organization = create_organization(
        tator_api=tator_api,
        project_name=project_name)

    project = create_project(
        tator_api=tator_api,
        project_name=project_name,
        organization=organization)

    media_types = create_media_types(
        tator_api=tator_api,
        project=project)

    localization_types = create_localization_types(
        tator_api=tator_api,
        project=project,
        media_types=media_types)

    versions = create_versions(
        tator_api=tator_api,
        project=project)

def parse_args() -> argparse.Namespace:
    """ Process script arguments
    """

    parser = argparse.ArgumentParser(description="Uploads the classifier results to Tator")
    parser.add_argument("--host", type=str, required=True)
    parser.add_argument("--token", type=str, required=True)
    parser.add_argument("--project-name", type=str, required=True)
    return parser.parse_args()

def script_main() -> None:
    """ Script entrypoint
    """

    args = parse_args()
    tator_api = tator.get_api(host=args.host, token=args.token)
    main(tator_api=tator_api, project_name=args.project_name)

if __name__ == "__main__":
    script_main()