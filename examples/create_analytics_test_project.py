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
              "order": 0,
          },
          {
              "name": "Algorithm Confidence",
              "dtype": "float",
              "order": 1,
          },
          {
              "name": "Count",
              "dtype": "int",
              "order": 2,
          },
          {
              "name": "Valid",
              "dtype": "bool",
              "order": -1,
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
        project_name: str,
        project_id: int,
        create_organization_check: bool,
        create_project_check: bool,
        create_media_types_check: bool,
        create_localization_types_check: bool,
        create_versions_check: bool) -> None:
    """ Main function that creates all the types
    """

    if create_organization_check:
        organization = create_organization(
            tator_api=tator_api,
            project_name=project_name)
        print(f"Created organization")
    else:
        print(f"Skipping creating organization")

    if create_project_check:
        project = create_project(
            tator_api=tator_api,
            project_name=project_name,
            organization=organization)
        print(f"Created project")
    else:
        print(f"Skipping creating project. Using project ID {project_id}")
        project = project_id

    if create_media_types_check:
        media_types = create_media_types(
            tator_api=tator_api,
            project=project)
        print(f"Created media types")
    else:
        print(f"Skipping creating media types. Querying media types")
        media_types_list = tator_api.get_media_type_list(project=project)
        media_types = [media_type.id for media_type in media_types_list]

    if create_localization_types_check:
        localization_types = create_localization_types(
            tator_api=tator_api,
            project=project,
            media_types=media_types)
        print(f"Created localization types")
    else:
        print(f"Skipping creating localization types")

    if create_versions_check:
        versions = create_versions(
            tator_api=tator_api,
            project=project)
        print(f"Created versions")
    else:
        print(f"Skipping creating versions")

def parse_args() -> argparse.Namespace:
    """ Process script arguments
    """

    parser = argparse.ArgumentParser(description="Uploads the classifier results to Tator")
    parser.add_argument("--host", type=str, required=True)
    parser.add_argument("--token", type=str, required=True)
    parser.add_argument("--project-name", type=str, help="Required if creating the project")
    parser.add_argument("--project", type=int, help="Required if not creating the project")
    parser.add_argument("--create-all", action="store_true", help="Create organization, project, media types, localization types, and versions")
    parser.add_argument("--create-organization", action="store_true")
    parser.add_argument("--create-project", action="store_true")
    parser.add_argument("--create-media-types", action="store_true")
    parser.add_argument("--create-localization-types", action="store_true")
    parser.add_argument("--create-versions", action="store_true")
    return parser.parse_args()

def script_main() -> None:
    """ Script entrypoint
    """

    args = parse_args()
    tator_api = tator.get_api(host=args.host, token=args.token)

    create_organization_check = False
    create_project_check = False
    create_media_types_check = False
    create_localization_types_check = False
    create_versions_check = False

    if args.create_all:
        create_organization_check = True
        create_project_check = True
        create_media_types_check = True
        create_localization_types_check = True
        create_versions_check = True
    else:
        if args.create_organization:
            create_organization_check = True
        if args.create_project:
            create_project_check = True
        if args.create_media_types:
            create_media_types_check = True
        if args.create_localization_types:
            create_localization_types_check = True
        if args.create_versions:
            create_versions_check = True

    main(
        tator_api=tator_api,
        project_name=args.project_name,
        project_id=args.project,
        create_organization_check=create_organization_check,
        create_project_check=create_project_check,
        create_media_types_check=create_media_types_check,
        create_localization_types_check=create_localization_types_check,
        create_versions_check=create_versions_check)

if __name__ == "__main__":
    script_main()