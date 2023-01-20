import datetime
import random
import uuid

import tator


def random_state(project, state_type, video_obj, post=False):
    attributes = {}
    out = {
        "project": project,
        "type": state_type,
        "media_ids": [video_obj.id],
        "frame": random.randint(0, video_obj.num_frames - 1),
        "attributes": attributes
    }

    return {**out}


def test_state_type_delete(host, token, project, video_type, video):
    tator_api = tator.get_api(host, token)
    response = tator_api.create_state_type(
        project,
        state_type_spec={
            "name": "state_type",
            "description": "Test state type",
            "project": project,
            "media_types": [video_type],
            "association": "Frame",
            "attribute_types": [],
        },
    )
    state_type = response.id
    video_obj = tator_api.get_media(video)

    # Verify no states exist to start
    response = tator_api.get_state_list(project, type=state_type)
    assert len(response) == 0

    # Test bulk create.
    num_states = random.randint(20, 100)
    states = [random_state(project, state_type, video_obj, post=True) for _ in range(num_states)]
    state_ids = []
    for response in tator.util.chunked_create(tator_api.create_state_list, project, body=states):
        state_ids += response.id
    assert len(state_ids) == len(states)
    print(f"Created {len(state_ids)} states!")

    # Verify list is the right length
    response = tator_api.get_state_list(project, type=state_type)
    assert len(response) == num_states

    response = tator_api.delete_state_type(state_type)

    assert str(state_type) in response.message, "State type id not found in delete response"
    assert str(num_states) in response.message, "State count not found in delete response"
    try:
        caught_it = False
        tator_api.get_state_count(project, type=state_type)
    except:
        caught_it=True
    finally:
        assert caught_it
