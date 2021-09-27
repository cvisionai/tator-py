import tator

def _create_localization(project, box_type, float_array_val):
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
    }
    out = {**out, **attributes}
    return out

def test_float_array(project, box_type, video):
    api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    # Create eight boxes in a line.
    spec = [
        _create_localization(project, box_type, [-4.0, 0.0, 0.0]),
        _create_localization(project, box_type, [-3.0, 0.0, 0.0]),
        _create_localization(project, box_type, [-2.0, 0.0, 0.0]),
        _create_localization(project, box_type, [-1.0, 0.0, 0.0]),
        _create_localization(project, box_type, [0.0, 0.0, 0.0]),
        _create_localization(project, box_type, [1.0, 0.0, 0.0]),
        _create_localization(project, box_type, [2.0, 0.0, 0.0]),
        _create_localization(project, box_type, [3.0, 0.0, 0.0]),
    ]
    response = api.create_localization_list(project, localization_spec=spec)
    assert(isinstance(response, tator.models.CreateResponse))
    assert(len(spec) == response.id)
    ids = response.id

    # Test default vector search.
    search = {
        'name': 'test_float_array',
        'center': [2.1, 0.0, 0.0],
    }
    response = api.get_localization_list_by_id(project, media_id_query=search)
    assert(len(response) == 8)
    assert(response[0].id == ids[6])
    assert(response[1].id == ids[7])
    assert(response[2].id == ids[5])

    # Test bounded search.
    search = {
        'name': 'test_float_array',
        'center': [2.1, 0.0, 0.0],
        'lower_bound': 1.0,
        'upper_bound': 3.0,
    }
    response = api.get_localization_list_by_id(project, media_id_query=search)
    assert(len(response) == 2)
    assert(response[0].id == ids[5])
    assert(resposne[1].id == ids[4])

    # Test descending search.
    search = {
        'name': 'test_float_array',
        'center': [2.1, 0.0, 0.0],
        'lower_bound': 1.0,
        'upper_bound': 3.0,
        'order': 'desc',
    }
    response = api.get_localization_list_by_id(project, media_id_query=search)
    assert(len(response) == 2)
    assert(response[0].id == ids[4])
    assert(resposne[1].id == ids[5])

    # Test alternative metrics.
    for metric in ['cosine_similarity', 'dot_product', 'l1norm']:
        search = {
            'name': 'test_float_array',
            'center': [2.1, 0.0, 0.0],
            'metric': metric,
        }
        response = api.get_localization_list_by_id(project, media_id_query=search)
        assert(len(response) == 8)
