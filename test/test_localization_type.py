import datetime
import random
import uuid

import tator


def random_localization(project, box_type, video_obj, post=False):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    w = random.uniform(0.0, 1.0 - x)
    h = random.uniform(0.0, 1.0 - y)
    attributes = {}
    out = {
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "project": project,
        "type": box_type,
        "media_id": video_obj.id,
        "frame": random.randint(0, video_obj.num_frames - 1),
        "attributes": attributes
    }

    return {**out}


def test_localization_type_delete(host, token, project, video_type, video):
    tator_api = tator.get_api(host, token)
    response = tator_api.create_localization_type(
        project,
        localization_type_spec={
            "name": "box_type",
            "description": "Test box type",
            "project": project,
            "media_types": [video_type],
            "dtype": "box",
            "attribute_types": [],
        },
    )
    box_type = response.id
    video_obj = tator_api.get_media(video)

    # Verify no localizations exist to start
    response = tator_api.get_localization_list(project, type=box_type)
    assert len(response) == 0

    # Test bulk create.
    num_localizations = random.randint(20, 100)
    boxes = [
        random_localization(project, box_type, video_obj, post=True)
        for _ in range(num_localizations)
    ]
    box_ids = []
    for response in tator.util.chunked_create(
        tator_api.create_localization_list, project, body=boxes
    ):
        box_ids += response.id
    assert len(box_ids) == len(boxes)
    print(f"Created {len(box_ids)} boxes!")

    # Verify list is the right length
    response = tator_api.get_localization_list(project, type=box_type)
    assert len(response) == num_localizations

    response = tator_api.delete_localization_type(box_type)

    assert str(box_type) in response.message, "Localization type id not found in delete response"
    assert (
        str(num_localizations) in response.message
    ), "Localization count not found in delete response"

    try:
        caught_it = False
        response = tator_api.get_localization_count(project, type=box_type)
    except:
        caught_it=True
    finally:
        assert caught_it
