from datetime import datetime
import random
from uuid import uuid1

import pytest
import tator


def make_image(tator_api, image_type, image_file, test_string):
    attributes = {"test_string": test_string}
    for progress, response in tator.util.upload_media(
        tator_api, image_type, image_file, attributes=attributes
    ):
        print(f"Upload image progress: {progress}%")
    return response.id


def random_localization(project, box_type, image_obj, test_string):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    w = random.uniform(0.0, 1.0 - x)
    h = random.uniform(0.0, 1.0 - y)
    attributes = {
        "test_bool": random.choice([False, True]),
        "test_int": random.randint(-1000, 1000),
        "test_float": random.uniform(-1000.0, 1000.0),
        "test_enum": random.choice(["a", "b", "c"]),
        "test_string": test_string,
        "test_datetime": datetime.now().isoformat(),
        "test_geopos": [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
        "test_float_array": [random.uniform(-1.0, 1.0) for _ in range(3)],
    }
    out = {
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "project": project,
        "type": box_type,
        "media_id": image_obj.id,
        "frame": 0,
        "attributes": attributes,
    }

    return {**out}


def test_localization_chunked_create(host, token, project, image_type, image_file, box_type):
    test_string = str(uuid1())
    tator_api = tator.get_api(host, token)
    image = make_image(tator_api, image_type, image_file, test_string)
    image_obj = tator_api.get_media(image)

    num_localizations = 1111
    boxes = [
        random_localization(project, box_type, image_obj, test_string)
        for _ in range(num_localizations)
    ]

    # Default chunk_size
    box_ids = [
        new_id
        for response in tator.util.chunked_create(
            tator_api.create_localization_list, project, body=boxes
        )
        for new_id in response.id
    ]
    assert len(box_ids) == len(boxes)

    # Small chunk_size
    box_ids = [
        new_id
        for response in tator.util.chunked_create(
            tator_api.create_localization_list, project, chunk_size=100, body=boxes
        )
        for new_id in response.id
    ]
    assert len(box_ids) == len(boxes)

    # Huge chunk_size
    box_ids = [
        new_id
        for response in tator.util.chunked_create(
            tator_api.create_localization_list, project, chunk_size=1000, body=boxes
        )
        for new_id in response.id
    ]
    assert len(box_ids) == len(boxes)

    tator_api.delete_media(image)


def helper(api, project, boxes, chunk_size=None):
    kwargs = {}
    if chunk_size:
        kwargs["chunk_size"] = chunk_size
    box_ids = []
    for response in tator.util.chunked_create(
        api.create_localization_list, project, body=boxes, **kwargs
    ):
        box_ids += response.id
        print(f"Created {len(response.id)} boxes")
    assert len(box_ids) == len(boxes)


def test_localization_chunked_create(host, token, project, image_type, image_file, box_type):
    test_string = str(uuid1())
    tator_api = tator.get_api(host, token)
    image = make_image(tator_api, image_type, image_file, test_string)
    image_obj = tator_api.get_media(image)

    num_localizations = 1111
    boxes = [
        random_localization(project, box_type, image_obj, test_string)
        for _ in range(num_localizations)
    ]

    # Default chunk_size
    print("using default chunk size")
    helper(tator_api, project, boxes)

    # Small chunk_size
    print("using small chunk size (100)")
    helper(tator_api, project, boxes, chunk_size=100)

    # Huge chunk_size
    print("using huge chunk size (1000)")
    helper(tator_api, project, boxes, chunk_size=1000)

    # Give bad func to force a failure to create
    with pytest.raises(RuntimeError) as exc:
        for _ in tator.util.chunked_create(lambda _: True, project, body=boxes):
            pass

    n_boxes = len(boxes)
    assert str(exc.value) == f"Was not able to create {n_boxes} of {n_boxes} objects"

    tator_api.delete_media(image)
