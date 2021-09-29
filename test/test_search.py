import os
import random
import datetime
import uuid
import glob
import time
import json

import tator

def random_localization(project, box_type, media_ids):
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
        'test_float_array': [random.uniform(-1.0, 1.0) for _ in range(3)],
    }
    out = {
        'x': x,
        'y': y,
        'width': w,
        'height': h,
        'project': project,
        'type': box_type,
        'media_id': random.choice(media_ids),
        'frame': 0,
    }
    out = {**out, **attributes}
    return out

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
    section = random.choice(['Search Section A', 'Search Section B'])
    path = random.choice(paths)
    for progress, response in tator.util.upload_media(api, image_type, path,
                                                      attributes=attributes,
                                                      section=section):
        pass
    return response.id, attributes, section

def random_search(sections=None):
    """ Runs a random query and compares results with ES enabled and disabled.
    """
    bool_value = random.choice([True, False])
    int_lower = random.randint(-1000, 0)
    int_upper = random.randint(0, 1000)
    float_lower = random.uniform(-1000.0, 0.0)
    float_upper = random.uniform(0.0, 1000.0)
    enum_value = random.choice(['a', 'b', 'c'])
    search = (f"test_bool:{str(bool_value).lower()} AND "
              f"test_int:>{int_lower} AND "
              f"test_int:<{int_upper} AND "
              f"test_float:>{float_lower} AND "
              f"test_float:<{float_upper} AND "
              f"test_enum:{enum_value}")
    values = {'bool_value': bool_value,
              'int_lower': int_lower,
              'int_upper': int_upper,
              'float_lower': float_lower,
              'float_upper': float_upper,
              'enum_value': enum_value}
    if sections:
        section = random.choice(sections)
        search += f" AND tator_user_sections:{section.tator_user_sections}"
        values['section'] = section
    return search, values

def check_box_result(results, values, media_values, box_specs, medias):
    """ Checks search results against values cached locally.
    """
    expected_media = [media_id for media_id, attributes, section in medias
                      if (attributes['test_bool'] == media_values['bool_value'])
                      and (attributes['test_int'] > media_values['int_lower'])
                      and (attributes['test_int'] < media_values['int_upper'])
                      and (attributes['test_float'] > media_values['float_lower'])
                      and (attributes['test_float'] < media_values['float_upper'])
                      and (attributes['test_enum'] == media_values['enum_value'])
                      and (section == media_values['section'].name)]
    expected_boxes = [box for box in box_specs
                      if (box['media_id'] in expected_media)
                      and (box['test_bool'] == values['bool_value'])
                      and (box['test_int'] > values['int_lower'])
                      and (box['test_int'] < values['int_upper'])
                      and (box['test_float'] > values['float_lower'])
                      and (box['test_float'] < values['float_upper'])
                      and (box['test_enum'] == values['enum_value'])]
    box_ids = [box['id'] for box in expected_boxes]
    assert(len(expected_boxes) == len(results))
    for result in results:
        assert(result.id in box_ids)

def check_media_result(results, values, annotation_values, box_specs, medias):
    """ Checks search results against values cached locally.
    """
    expected_boxes = [box for box in box_specs
                      if (box['test_bool'] == annotation_values['bool_value'])
                      and (box['test_int'] > annotation_values['int_lower'])
                      and (box['test_int'] < annotation_values['int_upper'])
                      and (box['test_float'] > annotation_values['float_lower'])
                      and (box['test_float'] < annotation_values['float_upper'])
                      and (box['test_enum'] == annotation_values['enum_value'])]
    parent_media = [box['media_id'] for box in expected_boxes]
    expected_media = [media_id for media_id, attributes, section in medias
                      if (media_id in parent_media)
                      and (attributes['test_bool'] == values['bool_value'])
                      and (attributes['test_int'] > values['int_lower'])
                      and (attributes['test_int'] < values['int_upper'])
                      and (attributes['test_float'] > values['float_lower'])
                      and (attributes['test_float'] < values['float_upper'])
                      and (attributes['test_enum'] == values['enum_value'])
                      and (section == values['section'].name)]
    assert(len(expected_media) == len(results))
    for result in results:
        assert(result.id in expected_media)

def test_search(host, token, project, image_type, image_set, box_type):
    api = tator.get_api(host, token)
    paths = os.listdir(image_set)
    paths = glob.glob(os.path.join(image_set, '**/*.jpg'), recursive=True)
    # Create some random media.
    print("Uploading 20 images...")
    medias = [random_media(api, project, paths, image_type) for _ in range(20)]
    media_ids = [media[0] for media in medias]
    # Create some random boxes.
    print("Creating 500 boxes...")
    box_specs = [random_localization(project, box_type, media_ids) for _ in range(500)]
    response = api.create_localization_list(project, box_specs)
    for idx, box_id in enumerate(response.id):
        box_specs[idx]['id'] = box_id
    # Retrieve sections.
    sections = [api.get_section_list(project, name='Search Section A')[0],
                api.get_section_list(project, name='Search Section B')[0]]
    # Sleep for a bit to make sure localizations are indexed.
    time.sleep(10)
    # Test search on localizations.
    print("Performing 100 random searches on localizations...")
    for _ in range(100):
        search, values = random_search()
        media_search, media_values = random_search(sections)
        response = api.get_localization_list(project, search=search, media_search=media_search)
        check_box_result(response, values, media_values, box_specs, medias)
        # Test search with section parameter
        media_search, media_values = random_search()
        section = random.choice(sections)
        response = api.get_localization_list(project, search=search, media_search=media_search,
                                             section=section.id)
        media_values['section'] = section
        check_box_result(response, values, media_values, box_specs, medias)
    # Test search on media.
    print("Performing 100 random searches on media...")
    for _ in range(100):
        search, values = random_search(sections)
        annotation_search, annotation_values = random_search()
        response = api.get_media_list(project, search=search, annotation_search=annotation_search)
        check_media_result(response, values, annotation_values, box_specs, medias)
        # Test search with section parameter
        search, values = random_search()
        section = random.choice(sections)
        response = api.get_media_list(project, search=search, annotation_search=annotation_search,
                                      section=section.id)
        values['section'] = section
        check_media_result(response, values, annotation_values, box_specs, medias)

