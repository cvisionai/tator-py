import random
import datetime
import uuid

import tator

def _create_localization(project, box_type, video_obj, float_array_val):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    w = random.uniform(0.0, 1.0 - x)
    h = random.uniform(0.0, 1.0 - y)
    attributes = {
        'test_bool': random.choice([False, True]),
        'test_int': random.randint(-1000, 1000),
        'test_float': random.uniform(-1000.0, 1000.0),
        'test_enum': random.choice(['a', 'b', 'c']),
        'test_string': str(uuid.uuid1()),
        'test_datetime': datetime.datetime.now().isoformat(),
        'test_geopos': [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
        'test_float_array': float_array_val,
    }
    out = {
        'x': x,
        'y': y,
        'width': w,
        'height': h,
        'project': project,
        'type': box_type,
        'media_id': video_obj.id,
        'frame': random.randint(0, video_obj.num_frames - 1),
        'attributes': attributes
    }

    return {**out}

def test_float_array(host, token, project, box_type, video_temp):
    api = tator.get_api(host, token)
    video_obj = api.get_media(video_temp)

    # Create eight boxes in a line.
    spec = [
        _create_localization(project, box_type, video_obj, [-4.0, 0.0, 0.0]),
        _create_localization(project, box_type, video_obj, [-3.0, 0.0, 0.0]),
        _create_localization(project, box_type, video_obj, [-2.0, 0.0, 0.0]),
        _create_localization(project, box_type, video_obj, [-1.0, 0.0, 0.0]),
        _create_localization(project, box_type, video_obj, [0.0, 0.0, 0.0]),
        _create_localization(project, box_type, video_obj, [1.0, 0.0, 0.0]),
        _create_localization(project, box_type, video_obj, [2.0, 0.0, 0.0]),
        _create_localization(project, box_type, video_obj, [3.0, 0.0, 0.0]),
    ]
    response = api.create_localization_list(project, spec)
    assert(isinstance(response, tator.models.CreateListResponse))
    assert(len(spec) == len(response.id))
    ids = response.id

    # Test default vector search.
    search = {
        'name': 'test_float_array',
        'center': [2.1, 0.0, 0.0],
    }
    search = {'float_array': [search]}
    boxes = api.get_localization_list_by_id(project, type=box_type, media_id=[video_temp], localization_id_query=search)
    assert(len(boxes) == 8)

    # Test bounded search.
    search = {
        'name': 'test_float_array',
        'center': [2.1, 0.0, 0.0],
        'lower_bound': 1.0,
        'upper_bound': 3.0,
    }
    search = {'float_array': [search]}
    boxes = api.get_localization_list_by_id(project, type=box_type, media_id=[video_temp], localization_id_query=search, stop=1)
    assert(len(boxes) == 1)
    assert(boxes[0].attributes['test_float_array'][0] == 1.0)
    boxes = api.get_localization_list_by_id(project, type=box_type, media_id=[video_temp], localization_id_query=search, stop=1)

    # Test descending search.
    search = {
        'name': 'test_float_array',
        'center': [2.1, 0.0, 0.0],
        'lower_bound': 1.0,
        'upper_bound': 3.0,
        'order': 'desc',
    }
    search = {'float_array': [search]}
    boxes = api.get_localization_list_by_id(project, type=box_type,media_id=[video_temp],localization_id_query=search, stop=1)
    assert(len(boxes) == 1)
    assert(boxes[0].attributes['test_float_array'][0] == 0.0)

    # Update localizations.
    search = {
        'name': 'test_float_array',
        'center': [3.0, 0.0, 0.0],
        'upper_bound': 3.1,
    }
    search = {'float_array': [search]}
    update = {'attributes': {'test_float_array': [1000.0, 0.0, 0.0]}}
    response = api.update_localization_list(project, type=box_type,media_id=[video_temp],
                                            localization_bulk_update={**search, **update})
    assert(isinstance(response, tator.models.MessageResponse))

    # Delete localizations.
    search = {
        'name': 'test_float_array',
        'center': [1000.0, 0.0, 0.0],
        'upper_bound': 1.0,
    }
    search = {'float_array': [search]}
    response = api.delete_localization_list(project, type=box_type,media_id=[video_temp],localization_bulk_delete=search)
    assert(isinstance(response, tator.models.MessageResponse))

    # Check we deleted the right boxes.
    count = api.get_localization_count(project, type=box_type)
    assert(count == 4)

    # Delete remaining localizations.
    search = {
        'name': 'test_float_array',
        'center': [-2.0, 0.0, 0.0],
        'upper_bound': 2.1,
    }
    search = {'float_array': [search]}
    response = api.delete_localization_list(project, type=box_type,localization_bulk_delete=search,media_id=[video_temp])
    assert(isinstance(response, tator.models.MessageResponse))

    # Check localizations are gone.
    count = api.get_localization_count(project, type=box_type)
    assert(count == 0)
