from pprint import pprint
from uuid import uuid1

import tator


def test_clone_project_only(host, token, organization, project):
    tator_api = tator.get_api(host, token)

    spec = {
        "new_project_name": str(uuid1()),
        "dest_organization": organization,
        "sections": [],
        "skip_memberships": True,
        "skip_sections": True,
        "skip_versions": True,
        "skip_media_types": True,
        "skip_localization_types": True,
        "skip_state_types": True,
        "skip_leaf_types": True,
        "skip_media": True,
        "skip_localizations": True,
        "skip_states": True,
        "skip_leaves": True,
        "ignore_media_transfer": True,
    }

    response = tator_api.migrate_project(project, migrate_project=spec)
    pprint(response)
    assert response.message == f"Successfully cloned project {project}!"
    tator_api.delete_project(response.id)
