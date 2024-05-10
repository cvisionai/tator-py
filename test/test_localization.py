from pprint import pformat
import datetime
import random
from time import sleep
import uuid
from collections import Counter
import pytest

import tator
from ._common import assert_close_enough


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


def comparison_query(tator_api, project, box_ids, exclude):
    """Runs a random query and compares results with ES enabled and disabled."""
    bool_value = random.choice([True, False])
    int_lower = random.randint(-1000, 0)
    int_upper = random.randint(0, 1000)
    float_lower = random.uniform(-1000.0, 0.0)
    float_upper = random.uniform(0.0, 1000.0)
    enum_value = random.choice(["a", "b", "c"])
    localization_id_query = {"ids": box_ids}
    attribute_filter = [
        f"test_bool::{'true' if bool_value else 'false'}",
        f"test_enum::{enum_value}",
    ]
    attribute_lte_filter = [f"test_int::{int_upper}"]
    attribute_gte_filter = [f"test_int::{int_lower}"]
    attribute_lt_filter = [f"test_float::{float_upper}"]
    attribute_gt_filter = [f"test_float::{float_lower}"]
    print("Starting PSQL query...")
    t0 = datetime.datetime.now()
    from_psql = tator_api.get_localization_list_by_id(
        project,
        localization_id_query=localization_id_query,
        attribute=attribute_filter,
        attribute_lte=attribute_lte_filter,
        attribute_gte=attribute_gte_filter,
        attribute_lt=attribute_lt_filter,
        attribute_gt=attribute_gt_filter,
    )
    psql_time = datetime.datetime.now() - t0
    print("Starting ES query...")
    t0 = datetime.datetime.now()
    from_es = tator_api.get_localization_list_by_id(
        project,
        localization_id_query=localization_id_query,
        attribute=attribute_filter,
        attribute_lte=attribute_lte_filter,
        attribute_gte=attribute_gte_filter,
        attribute_lt=attribute_lt_filter,
        attribute_gt=attribute_gt_filter,
    )
    es_time = datetime.datetime.now() - t0

    print("Checking PSQL and ES ids...")
    psql_ids = [ele.id for ele in from_psql]
    es_ids = [ele.id for ele in from_es]
    assert Counter(psql_ids) == Counter(es_ids)

    print("Checking PSQL and ES values...")
    assert len(from_psql) == len(from_es)
    for psql, es in zip(from_psql, from_es):
        assert_close_enough(psql, es, exclude)
        assert psql.attributes["test_bool"] == bool_value
        assert psql.attributes["test_int"] <= int_upper
        assert psql.attributes["test_int"] >= int_lower
        assert psql.attributes["test_float"] < float_upper
        assert psql.attributes["test_float"] > float_lower
        assert psql.attributes["test_enum"] == enum_value
    return psql_time, es_time


def test_localization_crud(host, token, project, video_type, video_temp, box_type):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video_temp)

    # These fields will not be checked for object equivalence after patch.
    exclude = ["project", "type", "media_id", "id", "type", "user", "ids", "in_place"]
    mapping = {"new_version": "version"}

    # Test bulk create.
    num_localizations = random.randint(2000, 10000)
    existing = len(tator_api.get_localization_list(project, type=box_type, media_id=[video_temp]))
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

    # Verify list is the right length
    response = tator_api.get_localization_list(project, type=box_type, media_id=[video_temp])
    assert len(response) == num_localizations + existing

    # Test media retrieval by localization ID.
    response = tator_api.get_media_list_by_id(project, {"localization_ids": box_ids})
    assert len(response) == 1
    assert response[0].id == video_temp

    # Test box retrieval by media ID.
    response = tator_api.get_localization_list_by_id(project, {"media_ids": [video_temp]})
    assert len(response) == len(box_ids)

    # Test single create.
    box = random_localization(project, box_type, video_obj, post=True)
    response = tator_api.create_localization_list(project, body=box)
    assert isinstance(response, tator.models.CreateListResponse)
    box_id = response.id[0]
    response = tator_api.get_localization(box_id)
    version_id = response.version
    elemental_id = response.elemental_id

    # Patch single box (in-place)
    patch = random_localization(project, box_type, video_obj)
    update_msg = {**patch, "in_place": 1}
    response = tator_api.update_localization(box_id, localization_update=update_msg)
    assert "message" in response.to_dict()
    print(response.message)

    # Get single box.
    updated_box = tator_api.get_localization(box_id)
    assert_close_enough(patch, updated_box, exclude)

    # Get box by ID.
    box_by_id = tator_api.get_localization_list_by_id(project, {"ids": [box_id]})
    assert len(box_by_id) == 1
    box_by_id = box_by_id[0]
    assert_close_enough(updated_box, box_by_id, exclude)

    # Patch single box via eid
    patch = random_localization(project, box_type, video_obj)
    response = tator_api.update_localization_by_elemental_id(
        version_id, elemental_id, localization_update=patch
    )
    assert "message" in response.to_dict()
    print(response.message)

    # Get single box.
    updated_box = tator_api.get_localization_by_elemental_id(version_id, elemental_id)
    assert_close_enough(patch, updated_box, exclude)

    # Delete single box.
    response = tator_api.delete_localization_by_elemental_id(version_id, elemental_id)
    assert "message" in response.to_dict()
    print(response.message)

    params = {"media_id": [video_temp], "type": box_type}
    assert tator_api.get_localization_count(project, **params) == len(boxes) + existing

    # Bulk update box attributes.
    response = tator_api.create_version(
        project,
        version_spec={
            "name": "Test Version",
            "description": "A version for testing",
        },
    )
    new_version = response.id
    bulk_patch = random_localization(project, box_type, video_obj)
    bulk_patch = {"attributes": bulk_patch["attributes"], "new_version": new_version, "in_place": 1}
    count = tator_api.get_localization_count(project, **params)
    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        response = tator_api.update_localization_list(
            project, **params, localization_bulk_update=bulk_patch, count=count + 1)
    response = tator_api.update_localization_list(
        project, **params, localization_bulk_update=bulk_patch, count=count
    )
    assert isinstance(response, tator.models.MessageResponse)
    print(response.message)

    # Bulk update specified boxes by ID.
    boxes = tator_api.get_localization_list(project, type=box_type, media_id=[video_obj.id])
    id_bulk_patch = random_localization(project, box_type, video_obj)
    box_ids = [x.id for x in boxes]
    update_ids = random.choices(box_ids, k=100)
    id_bulk_patch = {
        "attributes": id_bulk_patch["attributes"],
        "ids": update_ids,
        "new_version": new_version,
        "in_place": 1,
    }
    response = tator_api.update_localization_list(
        project, **params, localization_bulk_update=id_bulk_patch
    )
    assert isinstance(response, tator.models.MessageResponse)
    print(response.message)

    # Verify all boxes have been updated.
    boxes = tator_api.get_localization_list(project, **params, version=[new_version])
    dataframe = tator.util.to_dataframe(boxes)
    assert len(boxes) == len(dataframe)
    for box in boxes:
        if box.id in update_ids:
            assert_close_enough(id_bulk_patch, box, exclude, mapping)
        else:
            assert_close_enough(bulk_patch, box, exclude, mapping)

    # Clone boxes to same media.
    version_mapping = {version.id: version.id for version in tator_api.get_version_list(project)}
    generator = tator.util.clone_localization_list(
        tator_api,
        {**params, "project": project},
        project,
        version_mapping,
        {video_temp: video_temp},
        {box_type: box_type},
        tator_api,
    )
    for num_created, num_total, response, id_map in generator:
        print(f"Created {num_created} of {num_total} localizations...")
    print(f"Finished creating {num_created} localizations!")
    assert tator_api.get_localization_count(project, **params) == 2 * (len(boxes) + existing)

    # Delete all boxes.
    count = tator_api.get_localization_count(project, **params)
    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        response = tator_api.delete_localization_list(project, **params, count=count + 1)
    response = tator_api.delete_localization_list(project, **params, count=count)
    assert isinstance(response, tator.models.MessageResponse)

    # Verify all boxes are gone.
    boxes = tator_api.get_localization_list(project, **params)
    assert boxes == []

    boxes = tator_api.get_localization_list(project, **params, show_deleted=1, show_all_marks=1)
    assert boxes != []

    response = tator_api.delete_localization_list(
        project,
        **params,
        show_deleted=1,
        merge=0,
        show_all_marks=1,
        localization_bulk_delete={"prune": 1},
    )
    assert isinstance(response, tator.models.MessageResponse)

    # Clean up test version
    tator_api.delete_version(new_version)
