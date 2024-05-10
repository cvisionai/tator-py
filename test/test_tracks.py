import random
import uuid
import datetime

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
        "attributes": attributes,
    }

    return {**out}


def random_state(project, state_type, video_obj, post=False):
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
        "project": project,
        "type": state_type,
        "media_ids": [video_obj.id],
        "frame": random.randint(0, video_obj.num_frames - 1),
        "attributes": attributes,
    }

    return {**out}


def test_append(host, token, project, video_type, video, track_type, box_type):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    # Create some boxes.
    num_localizations = random.randint(5, 10)
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

    # Create a track.
    track = random_state(project, track_type, video_obj, post=True)
    response = tator_api.create_state_list(project, track)
    assert isinstance(response, tator.models.CreateListResponse)
    print(response.message)
    state_id = response.id[0]
    state_obj = tator_api.get_state(state_id)
    elemental_id = state_obj.elemental_id
    version = state_obj.version

    # Add boxes to track one at a time.
    for box_id in box_ids:
        for _ in range(2):
            update = {"localization_ids_add": [box_id]}
            response = tator_api.update_state_by_elemental_id(
                version, elemental_id, state_update=update
            )
            assert "message" in response.to_dict()

    # Add boxes to track.
    update = {"localization_ids_add": box_ids}
    response = tator_api.update_state_by_elemental_id(version, elemental_id, state_update=update)
    assert "message" in response.to_dict()

    # Try adding boxes to track again.
    response = tator_api.update_state_by_elemental_id(version, elemental_id, state_update=update)
    assert "message" in response.to_dict()
    print(response.message)

    # Try adding boxes to track with repeated entries.
    update = {"localization_ids_add": box_ids + box_ids}
    response = tator_api.update_state_by_elemental_id(version, elemental_id, state_update=update)
    assert "message" in response.to_dict()
    print(response.message)

    # Make sure we have the expected number of added localizations.
    track = tator_api.get_state_by_elemental_id(version, elemental_id)
    assert len(track.localizations) == num_localizations
