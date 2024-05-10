from pprint import pformat
import datetime
import random
from time import sleep
import uuid
from collections import Counter

import tator
from ._common import assert_close_enough


def random_localization(project, poly_type, video_obj, post=False):
    attributes = {
        "test_bool": random.choice([False, True]),
        "test_int": random.randint(-1000, 1000),
        "test_float": random.uniform(-1000.0, 1000.0),
        "test_enum": random.choice(["a", "b", "c"]),
        "test_string": str(uuid.uuid1()),
        "test_datetime": datetime.datetime.now().isoformat(),
        "test_geopos": [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
        "test_float_array": [random.uniform(-1.0, 1.0) for _ in range(3)],
    }
    out = {
        "points": [
            [random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)]
            for _ in range(random.randint(1, 10))
        ],
        "project": project,
        "type": poly_type,
        "media_id": video_obj.id,
        "frame": random.randint(0, video_obj.num_frames - 1),
        "attributes": attributes,
    }

    return {**out}


def test_poly(host, token, project, video_type, video, poly_type):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    # These fields will not be checked for object equivalence after patch.
    exclude = ["project", "type", "media_id", "id", "type", "user", "ids", "in_place"]

    # Test single create.
    poly = random_localization(project, poly_type, video_obj, post=True)
    response = tator_api.create_localization_list(project, poly)
    assert isinstance(response, tator.models.CreateListResponse)
    poly_id = response.id[0]
    response = tator_api.get_localization(poly_id)

    # Patch single poly.
    patch = random_localization(project, poly_type, video_obj)
    patch_obj = {**patch, "in_place": 1}
    response = tator_api.update_localization(poly_id, localization_update=patch_obj)
    assert "message" in response.to_dict()
    print(response.message)

    # Get single poly.
    updated_poly = tator_api.get_localization(poly_id)
    assert_close_enough(patch, updated_poly, exclude)

    # Get poly by ID.
    poly_by_id = tator_api.get_localization_list_by_id(project, {"ids": [poly_id]})
    assert len(poly_by_id) == 1
    poly_by_id = poly_by_id[0]
    assert_close_enough(updated_poly, poly_by_id, exclude)

    # Delete single poly.
    response = tator_api.delete_localization(poly_id)
    assert "message" in response.to_dict()
    print(response.message)
