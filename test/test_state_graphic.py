import os
import tempfile
import random
import uuid
import datetime

import tator

def random_localization(project, box_type, video_obj, post=False):
    x = random.uniform(0.0, 0.95)
    y = random.uniform(0.0, 0.95)
    w = random.uniform(0.05, 1.0 - x)
    h = random.uniform(0.05, 1.0 - y)
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
        'media_id': video_obj.id,
        'frame': random.randint(0, video_obj.num_frames - 1),
        'attributes': attributes
    }

    return {**out}

def test_state_graphic(host, token, project, video, box_type, track_type):
    api = tator.get_api(host, token)
    video_obj = api.get_media(video)
    localizations = [random_localization(project, box_type, video_obj, post=True) for _ in range(100)]
    response = api.create_localization_list(project, localizations)
    localization_ids = response.id
    track_spec = {
        'type': track_type,
        'localization_ids': localization_ids,
        'media_ids': [video],
    }
    tracks = api.create_state_list(project, body=track_spec)
    image = api.get_state_graphic(tracks.id[0])
    images = tator.util.full_state_graphic(api, tracks.id[0])
    api.delete_state_list(project, media_id=[video])
    api.delete_localization_list(project, media_id=[video])
