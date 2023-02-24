import datetime
import random
import string
import uuid

import tator
from ._common import assert_close_enough

def random_leaf(project, leaf_type, parent_obj=None, post=False):
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
    name = "".join(random.choice(string.ascii_letters) for _ in range(10))
    out = {
        'project': project,
        'type': leaf_type,
        'name': name,
        'attributes': attributes
    }
    if parent_obj:
        out['parent'] = parent_obj.id
    return {**out}

def test_leaf_crud(host, token, project, clone_project, leaf_type, clone_leaf_type):
    tator_api = tator.get_api(host, token)

    # Create root leaf.
    root_spec = random_leaf(project, leaf_type, None, True)
    response = tator_api.create_leaf_list(project=project, body=root_spec)
    assert(isinstance(response, tator.models.CreateListResponse))
    prev_ids = response.id

    # Create three additional layers.
    for _ in range(3):
        new_ids = []
        for parent_id in prev_ids:
            parent_obj = tator_api.get_leaf(parent_id)
            leaf_spec = [random_leaf(project, leaf_type, parent_obj, True)
                         for _ in range(3)] # 3 children per parent
            response = tator_api.create_leaf_list(project=project, body=leaf_spec)
            assert(isinstance(response, tator.models.CreateListResponse))
            new_ids += response.id
        prev_ids = list(new_ids)

    # Clone the layers.
    parent_mapping = {}
    for depth in range(4):
        leaves = tator_api.get_leaf_list(project=project, depth=depth)
        # Check leaf retrieval by ID.
        leaves_by_id = tator_api.get_leaf_list_by_id(project, {'ids': [leaf.id for leaf in leaves]})
        count = tator_api.get_leaf_count_by_id(project, {'ids': [leaf.id for leaf in leaves]})
        assert(len(leaves_by_id) == count)
        assert len(leaves) == len(leaves_by_id)
        for leaf, leaf_by_id in zip(leaves, leaves_by_id):
            assert_close_enough(leaf, leaf_by_id)
        print(f"Cloning Depth {depth}: {leaves}")
        generator = tator.util.clone_leaf_list(tator_api, {'project': project, 'depth': depth},
                                               clone_project, parent_mapping,
                                               {leaf_type: leaf_type})
        created_ids = []
        num_created = 0
        for num_created, num_total, response, id_map in generator:
            print(f"Created {num_created} of {num_total} leafs...")
            created_ids += response.id
        parent_mapping = {**parent_mapping,
                          **{src.id: dst for src, dst in zip(leaves, created_ids)}}
        print(f"Finished creating {num_created} leafs!")
    for src_id in parent_mapping:
        src = tator_api.get_leaf(src_id)
        dst = tator_api.get_leaf(parent_mapping[src_id])
        assert(src.path.split('.', 1)[1] == dst.path.split('.', 1)[1])
