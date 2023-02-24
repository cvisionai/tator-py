import datetime
import random
import string
import uuid

import tator
from ._common import assert_close_enough


def random_leaf(project, leaf_type, parent_obj=None, post=False):
    attributes = {}
    name = "".join(random.choice(string.ascii_letters) for _ in range(10))
    out = {
        "project": project,
        "type": leaf_type,
        "name": name,
        "attributes": attributes
    }
    if parent_obj:
        out["parent"] = parent_obj.id

    return {**out}


def test_leaf_type_delete(host, token, project):
    tator_api = tator.get_api(host, token)

    response = tator_api.create_leaf_type(
        project,
        leaf_type_spec={
            "name": "leaf_type",
            "description": "Test leaf type",
            "attribute_types": [],
        },
    )
    leaf_type = response.id

    # Verify no leaves exist to start
    response = tator_api.get_leaf_list(project, type=leaf_type)
    assert len(response) == 0

    # Create root leaf.
    root_spec = random_leaf(project, leaf_type, None, True)
    response = tator_api.create_leaf_list(project=project, body=root_spec)
    assert isinstance(response, tator.models.CreateListResponse)
    prev_ids = response.id

    response = tator_api.delete_leaf_type(leaf_type)

    assert str(leaf_type) in response.message, "Leaf type id not found in delete response"
    assert "1" in response.message, "Leaf count not found in delete response"

    try:
        caught_it = False
        tator_api.get_leaf_count(project, type=leaf_type)
    except:
        caught_it=True
    finally:
        assert caught_it
