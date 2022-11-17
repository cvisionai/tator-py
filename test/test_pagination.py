from types import GeneratorType
import datetime
import random
import uuid

import tator


def random_localization(project, box_type, video_obj, post=False):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    w = random.uniform(0.0, 1.0 - x)
    h = random.uniform(0.0, 1.0 - y)
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
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "project": project,
        "type": box_type,
        "media_id": video_obj.id,
        "frame": random.randint(0, video_obj.num_frames - 1),
    }
    if post:
        out = {**out, **attributes}
    else:
        out["attributes"] = attributes
    return out


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


def test_localization_pagination(host, token, project, video_type, video, box_type):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    existing_localizations = tator_api.get_localization_list(project, type=box_type)
    n_existing_loc = len(existing_localizations)
    batch_size = 100
    num_localizations = 2222  # Should not be a multiple of batch_size
    boxes = [
        random_localization(project, box_type, video_obj, post=True)
        for _ in range(num_localizations)
    ]
    box_ids = []
    for response in tator.util.chunked_create(
        tator_api.create_localization_list, project, localization_spec=boxes
    ):
        box_ids += response.id
    assert len(box_ids) == len(boxes)
    assert len(box_ids) % 100 != 0
    print(f"Created {len(box_ids)} boxes!")

    # Verify list is the right length
    response = tator_api.get_localization_list(project, type=box_type)
    assert len(response) == num_localizations

    # Check `get_localization_list`
    _assert_pagination(
        tator_api,
        "get_localization_list",
        batch_size,
        num_localizations,
        project=project,
        type=box_type,
    )

    # Check `get_localization_list_by_id`
    _assert_pagination(
        tator_api,
        "get_localization_list_by_id",
        batch_size,
        num_localizations,
        project=project,
        localization_id_query={"media_ids": [video]},
    )
