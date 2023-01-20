from pprint import pformat
import datetime
import random
from time import sleep
import uuid
from collections import Counter

import tator
from ._common import assert_close_enough


def wait_for_parity(tator_api, project, patch, expected_ids):
    attribute_filter = [f"test_string::{patch['attributes']['test_string']}"]
    state_id_query = {"ids": expected_ids}
    total_timeout = 60.0 # seconds
    wait_time = 2.0 # seconds

    print(f"Using attribute filter:\n{pformat(attribute_filter)}")
    from_psql = tator_api.get_state_list_by_id(
        project,
        state_id_query=state_id_query,
        attribute=attribute_filter,
    )
    count = tator_api.get_state_count_by_id(
        project,
        state_id_query=state_id_query,
        attribute=attribute_filter,
    )
    assert(len(from_psql) == count)
    for idx in range(int(total_timeout / wait_time) + 1):
        from_es = tator_api.get_state_list_by_id(
            project,
            state_id_query=state_id_query,
            attribute=attribute_filter
        )
        count = tator_api.get_state_count_by_id(
            project,
            state_id_query=state_id_query,
            attribute=attribute_filter
        )
        assert(len(from_es) == count)

        if len(from_es) == len(from_psql):
            print(f"Found expected number of results after {idx * wait_time} seconds")
            return True

        sleep(wait_time)

    print(f"Did not find expected number of results after {idx * wait_time} seconds")
    return False

def random_state(project, state_type, video_obj, post=False):
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
        'type': state_type,
        'media_ids': [video_obj.id],
        'frame': random.randint(0, video_obj.num_frames - 1),
        'attributes':  attributes
    }
    return {**out}

def comparison_query(tator_api, project, state_ids, exclude):
    """ Runs a random query and compares results with ES enabled and disabled.
    """
    bool_value = random.choice([True, False])
    int_lower = random.randint(-1000, 0)
    int_upper = random.randint(0, 1000)
    float_lower = random.uniform(-1000.0, 0.0)
    float_upper = random.uniform(0.0, 1000.0)
    enum_value = random.choice(['a', 'b', 'c'])
    state_id_query = {"ids": state_ids}
    attribute_filter = [f"test_bool::{'true' if bool_value else 'false'}", f"test_enum::{enum_value}"]
    attribute_lte_filter = [f"test_int::{int_upper}"]
    attribute_gte_filter = [f"test_int::{int_lower}"]
    attribute_lt_filter = [f"test_float::{float_upper}"]
    attribute_gt_filter = [f"test_float::{float_lower}"]
    print("Starting PSQL query...")
    t0 = datetime.datetime.now()
    from_psql = tator_api.get_state_list_by_id(
        project,
        state_id_query=state_id_query,
        attribute=attribute_filter,
        attribute_lte=attribute_lte_filter,
        attribute_gte=attribute_gte_filter,
        attribute_lt=attribute_lt_filter,
        attribute_gt=attribute_gt_filter,
    )
    psql_time = datetime.datetime.now() - t0
    print("Starting ES query...")
    t0 = datetime.datetime.now()
    from_es = tator_api.get_state_list_by_id(
        project,
        state_id_query=state_id_query,
        attribute=attribute_filter,
        attribute_lte=attribute_lte_filter,
        attribute_gte=attribute_gte_filter,
        attribute_lt=attribute_lt_filter,
        attribute_gt=attribute_gt_filter,
        force_es=1,
    )
    es_time = datetime.datetime.now() - t0

    print("Checking PSQL and ES ids...")
    psql_ids = [ele.id for ele in from_psql]
    es_ids = [ele.id for ele in from_es]
    assert(Counter(psql_ids) == Counter(es_ids))

    print("Checking PSQL and ES values...")
    assert len(from_psql) == len(from_es)
    for psql, es in zip(from_psql, from_es):
        assert_close_enough(psql, es, exclude)
        assert(psql.attributes['test_bool'] == bool_value)
        assert(psql.attributes['test_int'] <= int_upper)
        assert(psql.attributes['test_int'] >= int_lower)
        assert(psql.attributes['test_float'] < float_upper)
        assert(psql.attributes['test_float'] > float_lower)
        assert(psql.attributes['test_enum'] == enum_value)
    return psql_time, es_time

def test_state_crud(host, token, project, video_type, empty_video, state_type):
    video = empty_video
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    # These fields will not be checked for object equivalence after patch.
    exclude = ['project', 'type', 'media_ids', 'id', 'type', 'user', 'frame', 'ids']

    # Test bulk create.
    num_states = random.randint(2000, 10000)
    states = [
        random_state(project, state_type, video_obj, post=True)
        for _ in range(num_states)
    ]
    state_ids = []
    for response in tator.util.chunked_create(tator_api.create_state_list, project, body=states):
        state_ids += response.id
    assert len(state_ids) == len(states)
    print(f"Created {len(state_ids)} states!")

    # Verify list contains the number of entities created
    response = tator_api.get_state_list(project, type=state_type)
    assert len(response) == num_states

    # Test media retrieval by state ID.
    response = tator_api.get_media_list_by_id(project, {'state_ids': state_ids})
    assert len(response) == 1
    assert response[0].id == video

    # Test state retrival by media ID.
    response = tator_api.get_state_list_by_id(project, {'media_ids': [video]})
    assert(len(response) == len(state_ids))

    # Test single create.
    state = random_state(project, state_type, video_obj, post=True)
    response = tator_api.create_state_list(project, body=state)
    assert isinstance(response, tator.models.CreateListResponse)
    print(response.message)
    state_id = response.id[0]

    # Patch single state.
    patch = random_state(project, state_type, video_obj)
    response = tator_api.update_state(state_id, state_update=patch)
    assert isinstance(response, tator.models.MessageResponse)
    print(response.message)

    # Get single state.
    updated_state = tator_api.get_state(state_id)
    assert isinstance(updated_state, tator.models.State)
    assert_close_enough(patch, updated_state, exclude)

    # Get state by ID.
    state_by_id = tator_api.get_state_list_by_id(project, {'ids': [state_id]})
    assert(len(state_by_id) == 1)
    state_by_id = state_by_id[0]
    assert_close_enough(updated_state, state_by_id, exclude)

    # Delete single state.
    response = tator_api.delete_state(state_id)
    assert isinstance(response, tator.models.MessageResponse)
    print(response.message)

    params = {'media_id': [video], 'type': state_type}
    assert(tator_api.get_state_count(project, **params) == len(states))

    # Bulk update state attributes.
    bulk_patch = random_state(project, state_type, video_obj)
    bulk_patch = {'attributes': bulk_patch['attributes']}
    response = tator_api.update_state_list(project, **params,
                                           state_bulk_update=bulk_patch)
    assert isinstance(response, tator.models.MessageResponse)
    print(response.message)

    # Bulk update specified states by ID.
    id_bulk_patch = random_state(project, state_type, video_obj)
    update_ids = random.choices(state_ids, k=100)
    id_bulk_patch = {'attributes': id_bulk_patch['attributes'], 'ids': update_ids}
    response = tator_api.update_state_list(project, **params,
                                           state_bulk_update=id_bulk_patch)
    assert isinstance(response, tator.models.MessageResponse)
    print(response.message)

    # Verify all states have been updated.
    states = tator_api.get_state_list(project, **params)
    dataframe = tator.util.to_dataframe(states)
    assert(len(states)==len(dataframe))
    for state in states:
        if state.id in update_ids:
            assert_close_enough(id_bulk_patch, state, exclude)
        else:
            assert_close_enough(bulk_patch, state, exclude)

    # Clone states to same media.
    version_mapping = {version.id: version.id for version in tator_api.get_version_list(project)}
    generator = tator.util.clone_state_list(tator_api, {**params, 'project': project},
                                            project, version_mapping, {video:video}, {},
                                            {state_type:state_type}, tator_api)
    for num_created, num_total, response, id_map in generator:
        print(f"Created {num_created} of {num_total} states...")
    print(f"Finished creating {num_created} states!")
    assert(tator_api.get_state_count(project, **params) == 2 * len(states))

    # Delete all states.
    response = tator_api.delete_state_list(project, **params)
    assert isinstance(response, tator.models.MessageResponse)

    # Verify all states are gone.
    states = tator_api.get_state_list(project, **params)
    assert states == []
