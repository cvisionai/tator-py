import datetime
import random
import uuid
import time

import tator
from tator.util import chunked_create
from tator.util import to_dataframe
from ._common import assert_close_enough

def random_localization(project, box_type, video_obj, post=False):
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
    if post:
        out = {**out, **attributes}
    else:
        out['attributes'] = attributes
    return out

def test_localization_crud(url, token, project, video_type, video, box_type):
    tator_api = tator.get_api(url, token)
    video_obj = tator_api.get_media(video)

    # These fields will not be checked for object equivalence after patch.
    exclude = ['project', 'type', 'media_id', 'id', 'meta', 'user']

    # Test bulk create.
    num_localizations = random.randint(2000, 10000)
    boxes = [
        random_localization(project, box_type, video_obj, post=True)
        for _ in range(num_localizations)
    ]
    box_ids = chunked_create(tator_api.create_localization_list,
                             project, localization_spec=boxes)
    assert len(box_ids) == len(boxes)
    print(f"Created {len(box_ids)} boxes!")

    # Test single create.
    box = random_localization(project, box_type, video_obj, post=True)
    response = tator_api.create_localization_list(project, localization_spec=[box])
    assert isinstance(response, tator.CreateListResponse)
    box_id = response.id[0]

    # Patch single box.
    patch = random_localization(project, box_type, video_obj)
    response = tator_api.update_localization(box_id, localization_update=patch)
    assert isinstance(response, tator.MessageResponse)
    print(response.message)

    # Get single box.
    updated_box = tator_api.get_localization(box_id)
    assert_close_enough(patch, updated_box, exclude)
    
    # Delete single box.
    response = tator_api.delete_localization(box_id)
    assert isinstance(response, tator.MessageResponse)
    print(response.message)

    # ES can be slow at indexing so wait for a bit.
    time.sleep(5)

    # Bulk update box attributes.
    bulk_patch = random_localization(project, box_type, video_obj)
    bulk_patch = {'attributes': bulk_patch['attributes']}
    params = {'media_id': [video], 'type': box_type}
    response = tator_api.update_localization_list(project, **params,
                                                  attribute_bulk_update=bulk_patch)
    assert isinstance(response, tator.MessageResponse)
    print(response.message)

    # Verify all boxes have been updated.
    boxes = tator_api.get_localization_list(project, **params)
    dataframe = to_dataframe(boxes)
    assert(len(boxes)==len(dataframe))
    for box in boxes:
        assert_close_enough(bulk_patch, box, exclude)
    
    # Delete all boxes.
    response = tator_api.delete_localization_list(project, **params)
    assert isinstance(response, tator.MessageResponse)
    time.sleep(1)

    # Verify all boxes are gone.
    boxes = tator_api.get_localization_list(project, **params)
    assert boxes == []
