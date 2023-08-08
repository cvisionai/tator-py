import os
import random
import datetime
import uuid
import glob
import time
import collections

import tator

def random_media(api, project, paths, image_type):
    attributes = {
        'test_bool': random.choice([False, True]),
        'test_int': random.randint(-1000, 1000),
        'test_float': random.uniform(-1000.0, 1000.0),
        'test_enum': random.choice(['a', 'b', 'c']),
        'test_string': str(uuid.uuid1()),
        'test_datetime': datetime.datetime.now().isoformat(),
        'test_geopos': [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
        'test_float_array': [random.uniform(-1.0, 1.0) for _ in range(3)],
    }
    section = 'Media State Test'
    path = random.choice(paths)
    for progress, response in tator.util.upload_media(api, image_type, path,
                                                      attributes=attributes,
                                                      section=section):
        pass
    return response.id, attributes, section

def random_state(project, collection_type, media_ids, post=False):
    attributes = {
        'test_bool': random.choice([False, True]),
        'test_int': random.randint(-1000, 1000),
        'test_float': random.uniform(-1000.0, 1000.0),
        'test_enum': random.choice(['a', 'b', 'c']),
        'test_string': str(uuid.uuid1()),
        'test_datetime': datetime.datetime.now().isoformat(),
        'test_geopos': [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
        'test_float_array': [random.uniform(-1.0, 1.0) for _ in range(3)],
    }
    out = {
        'project': project,
        'type': collection_type,
        'media_ids': list(set(random.choices(media_ids, k=5))),
        'attributes': attributes
    }

    return {**out}

def test_media_states(host, token, project, image_type, image_set, collection_type):
    api = tator.get_api(host, token)
    paths = os.listdir(image_set)
    paths = glob.glob(os.path.join(image_set, '**/*.jpg'), recursive=True)
    # Create some random media.
    print("Uploading 20 images...")
    medias = [random_media(api, project, paths, image_type) for _ in range(20)]
    media_ids = [media[0] for media in medias]
    # Create states that include random sets of media.
    print("Creating 500 collections (media states)...")
    state_specs = [random_state(project, collection_type, media_ids, post=True) for _ in range(500)]
    response = api.create_state_list(project, state_specs)
    time.sleep(5)
    for idx, state_id in enumerate(response.id):
        state_specs[idx]['id'] = state_id
    # Do a search on all states.
    expected_states = [spec for spec in state_specs if spec['attributes']['test_bool'] == False]
    all_states = api.get_state_list(project, type=collection_type, attribute=["test_bool::false"])
    assert(len(all_states) == len(expected_states))

    # Do a search on all states.
    expected_states = [spec for spec in state_specs if spec['attributes']['test_bool'] == False]
    all_states = api.get_state_list_by_id(project,{'object_search':{"attribute": 'test_bool', 'operation': 'eq', 'value': False}}, type=collection_type)
    assert(len(all_states) == len(expected_states))

    # Do a search on paginated states.
    states = []
    for start in [0, 100, 200, 300, 400]:
        states += api.get_state_list(project, type=collection_type, attribute=["test_bool::false"],start=start, stop=start+100)
    assert(len(states) == len(expected_states))
    assert(collections.Counter([state.id for state in states]) == \
           collections.Counter([state.id for state in all_states]))
