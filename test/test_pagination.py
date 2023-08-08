from datetime import datetime
import random
from types import GeneratorType
from uuid import uuid1

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


def _assert_pagination(api, function_name, batch_size, total, **kwargs):
    # Get paginator for `get_localization_list`
    paginator = tator.util.get_paginator(api, function_name, batch_size=batch_size)
    page_iter = paginator.paginate(**kwargs)
    assert type(page_iter) == GeneratorType

    # Check the batch size
    all_objects = []
    expect_stop_iteration = False
    while True:
        try:
            response = next(page_iter)
        except StopIteration:
            assert expect_stop_iteration
            break
        else:
            assert expect_stop_iteration == False
            all_objects += response
            if len(response) < batch_size:
                expect_stop_iteration = True
            else:
                assert len(response) == batch_size

    assert len(all_objects) == total


def test_localization_pagination(host, token, project, image_type, image_file, box_type):
    test_string = str(uuid1())
    tator_api = tator.get_api(host, token)
    image = make_image(tator_api, image_type, image_file, test_string)
    image_obj = tator_api.get_media(image)

    batch_size = 100
    num_localizations = 2222  # Should not be a multiple of batch_size
    boxes = [
        random_localization(project, box_type, image_obj, test_string)
        for _ in range(num_localizations)
    ]
    box_ids = []
    for response in tator.util.chunked_create(
        tator_api.create_localization_list, project, body=boxes
    ):
        box_ids += response.id
    assert len(box_ids) == len(boxes)
    assert len(box_ids) % 100 != 0
    print(f"Created {len(box_ids)} boxes!")

    # Verify list is the right length
    response = tator_api.get_localization_count(project, type=box_type, media_id=[image])
    assert response == num_localizations

    # Check `get_localization_list`
    _assert_pagination(
        tator_api,
        "get_localization_list",
        batch_size,
        num_localizations,
        project=project,
        type=box_type,
        media_id=[image],
    )

    # Check `get_localization_list_by_id`
    _assert_pagination(
        tator_api,
        "get_localization_list_by_id",
        batch_size,
        num_localizations,
        project=project,
        localization_id_query={"media_ids": [image]},
    )

    tator_api.delete_media(image)


def test_big_list_pagination(host, token, project, image_type, image_file, box_type):
    test_string = str(uuid1())
    tator_api = tator.get_api(host, token)
    image = make_image(tator_api, image_type, image_file, test_string)
    image_obj = tator_api.get_media(image)

    batch_size = 1000
    num_localizations = 11111
    boxes = [
        random_localization(project, box_type, image_obj, test_string)
        for _ in range(num_localizations)
    ]
    box_ids = []
    for response in tator.util.chunked_create(
        tator_api.create_localization_list, project, body=boxes
    ):
        box_ids += response.id
    assert len(box_ids) == len(boxes)
    assert len(box_ids) % 100 != 0
    print(f"Created {len(box_ids)} boxes!")

    # Verify list is the right length
    response = tator_api.get_localization_count(project, type=box_type, media_id=[image])
    assert response == num_localizations

    # Check `get_localization_list_by_id`
    _assert_pagination(
        tator_api,
        "get_localization_list_by_id",
        batch_size,
        num_localizations,
        project=project,
        localization_id_query={"media_ids": [image]},
    )

    tator_api.delete_media(image)
