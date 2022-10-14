from time import sleep
from uuid import uuid4
import random
from datetime import datetime
import pytest

import tator


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
        "test_string": str(uuid4()),
        "test_datetime": datetime.now().isoformat(),
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
    }
    if post:
        out = {**out, **attributes}
    else:
        out["attributes"] = attributes
    return out


allowed_mutations = {
    "bool": ["bool", "enum", "string"],
    "int": ["int", "float", "enum", "string"],
    "float": ["int", "float", "enum", "string"],
    "enum": ["enum", "string"],
    "string": ["enum", "string"],
    "datetime": ["enum", "string", "datetime"],
    "geopos": ["enum", "string", "geopos"],
    "float_array": ["float_array"],
}


def mutation_helper(tator_api, type_getter, type_id, params):
    uid = f" {uuid4()}"
    source_name = params["source_name"]
    dest_name = params.get("dest_name", source_name)
    source_name += uid
    dest_name += uid
    source_dtype = params["source_dtype"]
    dest_dtype = params.get("dest_dtype")
    assert_cnt = 0

    entity_type = type_getter(type_id)
    addition = {
        "entity_type": f"{type(entity_type).__name__}",
        "addition": {"name": source_name, "dtype": source_dtype},
    }
    if source_dtype == "enum":
        addition["addition"]["choices"] = ["a", "b", "c"]
    if source_dtype == "float_array":
        addition["addition"]["size"] = 3
    tator_api.add_attribute(id=type_id, attribute_type_spec=addition)
    entity_type = type_getter(type_id)

    # Check attribute name before changing it
    assert any(attr.name == source_name for attr in entity_type.attribute_types)
    assert_cnt += 1

    for attr in entity_type.attribute_types:
        if attr.name == source_name:
            # Check the `dtype` before changing it
            assert attr.dtype == source_dtype
            assert_cnt += 1
            break
    else:
        # If the new attribute is not found above, we should fail
        assert False

    mutation = {
        "global": "false",
        "entity_type": addition["entity_type"],
        "old_attribute_type_name": source_name,
        "new_attribute_type": {"name": dest_name},
    }
    if dest_dtype:
        mutation["new_attribute_type"]["dtype"] = dest_dtype

        if dest_dtype == "enum":
            mutation["new_attribute_type"]["choices"] = ["a", "b", "c"]
        if dest_dtype == "float_array":
            mutation["new_attribute_type"]["size"] = 3

    # A type mutation not in the list of allowed mutations will raise an `ApiException` and the
    # expected `dtype` will be the same as `source_dtype`
    if dest_dtype is None or dest_dtype in allowed_mutations[source_dtype]:
        expected_dtype = dest_dtype if dest_dtype else source_dtype
        expected_name = dest_name
        tator_api.rename_attribute(id=type_id, attribute_type_update=mutation)
    else:
        expected_dtype = source_dtype
        expected_name = source_name
        with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException) as excinfo:
            tator_api.rename_attribute(id=type_id, attribute_type_update=mutation)

    entity_type = type_getter(type_id)

    # Check new attribute name
    assert any(attr.name == expected_name for attr in entity_type.attribute_types)
    assert_cnt += 1

    # No attributes should have the old name, if we are expecting a change
    if source_name != expected_name:
        assert all(attr.name != source_name for attr in entity_type.attribute_types)
        assert_cnt += 1

    for attr in entity_type.attribute_types:
        if attr.name == expected_name:
            # Check that the `dtype` has been updated
            assert attr.dtype == expected_dtype
            assert_cnt += 1
            break
    else:
        # If the new attribute is not found above, we should fail
        assert False

    assert assert_cnt == params["expected_asserts"]

    # Delete the attribute to keep clean for other tests
    attribute_delete = {
        "entity_type": addition["entity_type"],
        "attribute_to_delete": expected_name,
    }
    tator_api.delete_attribute(id=type_id, attribute_type_delete=attribute_delete)


@pytest.mark.parametrize("source_dtype", allowed_mutations.keys())
@pytest.mark.parametrize("dest_dtype", allowed_mutations.keys())
def test_box_type_dtype_change(host, token, project, attribute_box_type, source_dtype, dest_dtype):
    tator_api = tator.get_api(host, token)
    params = {
        "source_name": f"{source_dtype} attribute to modify {uuid4()}",
        "source_dtype": source_dtype,
        "dest_dtype": dest_dtype,
        "expected_asserts": 4,
    }
    mutation_helper(tator_api, tator_api.get_localization_type, attribute_box_type, params)


@pytest.mark.parametrize("dtype", allowed_mutations.keys())
def test_box_type_invalid_dtype_change(host, token, project, attribute_box_type, dtype):
    tator_api = tator.get_api(host, token)
    params = {
        "source_name": f"{dtype} attribute to modify {uuid4()}",
        "source_dtype": dtype,
        "dest_dtype": "unknown",
        "expected_asserts": 4,
    }
    mutation_helper(tator_api, tator_api.get_localization_type, attribute_box_type, params)


@pytest.mark.parametrize("dtype", allowed_mutations.keys())
def test_box_type_name_change(host, token, project, attribute_box_type, dtype):
    tator_api = tator.get_api(host, token)
    params = {
        "source_name": f"{dtype} attribute to rename {uuid4()}",
        "source_dtype": dtype,
        "dest_name": f"renamed {dtype} attribute",
        "expected_asserts": 5,
    }
    mutation_helper(tator_api, tator_api.get_localization_type, attribute_box_type, params)


@pytest.mark.parametrize("source_dtype", allowed_mutations.keys())
@pytest.mark.parametrize("dest_dtype", allowed_mutations.keys())
def test_box_type_full_mutation(host, token, project, attribute_box_type, source_dtype, dest_dtype):
    params = {
        "source_name": f"{source_dtype} attribute to modify {uuid4()}",
        "source_dtype": source_dtype,
        "dest_name": f"renamed {source_dtype} -> {dest_dtype} attribute",
        "dest_dtype": dest_dtype,
        "expected_asserts": 5 if dest_dtype in allowed_mutations[source_dtype] else 4,
    }
    tator_api = tator.get_api(host, token)
    mutation_helper(tator_api, tator_api.get_localization_type, attribute_box_type, params)


@pytest.mark.skip(reason="Will be reinstated with the removal of ES")
@pytest.mark.parametrize("dtype", allowed_mutations.keys())
def test_video_and_image_type_name_change(
    host, token, project, attribute_video_type, image_type, dtype
):
    uid = f"{uuid4()}"
    source_name = f"{dtype} attribute to rename {uid}"
    dest_name = f"renamed {dtype} attribute {uid}"
    source_dtype = dtype
    tator_api = tator.get_api(host, token)

    # Add attribute to attribute_video_type
    entity_type = tator_api.get_media_type(attribute_video_type)
    addition = {
        "entity_type": "MediaType",
        "addition": {"name": source_name, "dtype": source_dtype},
    }
    if source_dtype == "enum":
        addition["addition"]["choices"] = ["a", "b", "c"]
    if source_dtype == "float_array":
        addition["addition"]["size"] = 3
    tator_api.add_attribute(id=attribute_video_type, attribute_type_spec=addition)
    entity_type = tator_api.get_media_type(attribute_video_type)

    # Check attribute name before changing it
    assert any(attr.name == source_name for attr in entity_type.attribute_types)

    # Add same attribute to image_type
    entity_type = tator_api.get_media_type(image_type)
    addition = {
        "entity_type": "MediaType",
        "addition": {"name": source_name, "dtype": source_dtype},
    }
    if source_dtype == "enum":
        addition["addition"]["choices"] = ["a", "b", "c"]
    if source_dtype == "float_array":
        addition["addition"]["size"] = 3
    tator_api.add_attribute(id=image_type, attribute_type_spec=addition)
    entity_type = tator_api.get_media_type(image_type)

    # Check attribute name before changing it
    assert any(attr.name == source_name for attr in entity_type.attribute_types)

    # Mutate attribute on attribute_video_type
    mutation = {
        "global": "true",
        "entity_type": "MediaType",
        "old_attribute_type_name": source_name,
        "new_attribute_type": {"name": dest_name, "dtype": source_dtype},
    }
    if source_dtype == "enum":
        mutation["new_attribute_type"]["choices"] = ["a", "b", "c"]
    if source_dtype == "float_array":
        mutation["new_attribute_type"]["size"] = 3

    tator_api.rename_attribute(id=attribute_video_type, attribute_type_update=mutation)

    entity_type = tator_api.get_media_type(attribute_video_type)

    # Check new attribute name
    assert any(attr.name == dest_name for attr in entity_type.attribute_types)

    # No attributes should have the old name
    assert all(attr.name != source_name for attr in entity_type.attribute_types)

    # The image_type attribute should also have the new name
    entity_type = tator_api.get_media_type(image_type)
    assert any(attr.name == dest_name for attr in entity_type.attribute_types)
    assert all(attr.name != source_name for attr in entity_type.attribute_types)

    # Delete the attribute to keep clean for other tests
    attribute_delete = {
        "entity_type": "MediaType",
        "attribute_to_delete": dest_name,
    }
    tator_api.delete_attribute(id=attribute_video_type, attribute_type_delete=attribute_delete)
    tator_api.delete_attribute(id=image_type, attribute_type_delete=attribute_delete)


def test_box_type_attribute_mutation_es(host, token, project, attribute_video, attribute_box_type):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(attribute_video)

    num_localizations = 2
    boxes = [
        random_localization(project, attribute_box_type, video_obj, post=True)
        for _ in range(num_localizations)
    ]
    box_ids = [
        box_id
        for response in tator.util.chunked_create(
            tator_api.create_localization_list, project, localization_spec=boxes
        )
        for box_id in response.id
    ]

    assert len(box_ids) == len(boxes)

    # ES can be slow at indexing so wait for a bit.
    sleep(2)

    # Make sure the new attribute does not exist already
    value = str(uuid4()).lower()
    new_attr_name = f"New enum {value}"
    entity_type = tator_api.get_localization_type(attribute_box_type)
    assert all(attr.name != new_attr_name for attr in entity_type.attribute_types)
    addition = {
        "entity_type": "LocalizationType",
        "addition": {"name": new_attr_name, "dtype": "enum", "default": value, "choices": [value]},
    }
    tator_api.add_attribute(id=attribute_box_type, attribute_type_spec=addition)
    entity_type = tator_api.get_localization_type(attribute_box_type)

    # Check for added attribute
    assert any(attr.name == new_attr_name for attr in entity_type.attribute_types)

    # ES can be slow at indexing so wait for a bit.
    sleep(2)

    # Check for default value on existing instances
    params = {
        "type": attribute_box_type,
        "attribute": [f"{new_attr_name}::{str(value).lower()}"],
        "force_es": 1,
    }
    boxes = tator_api.get_localization_list(project, **params)

    assert len(box_ids) == len(boxes)

    for box in boxes:
        assert box.attributes[new_attr_name] == value

    # Change attribute type
    newer_attr_name = f"New string {value}"
    mutation = {
        "global": "false",
        "entity_type": "LocalizationType",
        "old_attribute_type_name": new_attr_name,
        "new_attribute_type": {"name": newer_attr_name, "dtype": "string"},
    }
    tator_api.rename_attribute(id=attribute_box_type, attribute_type_update=mutation)

    # Check for mutated attribute
    entity_type = tator_api.get_localization_type(attribute_box_type)
    for attr in entity_type.attribute_types:
        if attr.name == newer_attr_name:
            assert attr.dtype == "string"
            break
    else:
        assert False, f"Attribute {newer_attr_name} not found"

    # ES can be slow at indexing so wait for a bit.
    sleep(2)

    # Check for default value on existing instances
    params = {
        "type": attribute_box_type,
        "attribute": [f"{newer_attr_name}::{str(value).lower()}"],
        "force_es": 1,
    }
    boxes = tator_api.get_localization_list(project, **params)

    assert len(box_ids) == len(boxes)

    for box in boxes:
        assert box.attributes[newer_attr_name] == value

    # Clean up
    params = {"media_id": [attribute_video], "type": attribute_box_type}
    tator_api.delete_localization_list(project, **params)

    # Delete the attribute to keep clean for other tests
    attribute_delete = {
        "entity_type": "LocalizationType",
        "attribute_to_delete": newer_attr_name,
    }
    tator_api.delete_attribute(id=attribute_box_type, attribute_type_delete=attribute_delete)


def test_box_type_attribute_mutation_fail(
        host, token, project, attribute_video, attribute_box_type
):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(attribute_video)

    # Create localizations, but less than 100
    num_localizations = 75
    boxes = [
        random_localization(project, attribute_box_type, video_obj, post=True)
        for _ in range(num_localizations)
    ]
    box_ids = [
        box_id
        for response in tator.util.chunked_create(
            tator_api.create_localization_list, project, localization_spec=boxes
        )
        for box_id in response.id
    ]

    assert len(box_ids) == len(boxes)

    # Make sure the new attribute does not exist already
    value = str(uuid4()).lower()
    new_attr_name = f"New int {value}"
    entity_type = tator_api.get_localization_type(attribute_box_type)
    assert all(attr.name != new_attr_name for attr in entity_type.attribute_types)
    addition = {
        "entity_type": "LocalizationType",
        "addition": {"name": new_attr_name, "dtype": "int", "default": 0},
    }
    tator_api.add_attribute(id=attribute_box_type, attribute_type_spec=addition)
    entity_type = tator_api.get_localization_type(attribute_box_type)

    # Check for added attribute
    assert any(attr.name == new_attr_name for attr in entity_type.attribute_types)

    # Attempt to change attribute type with low `max_instances`, call to `rename_attribute` should
    # raise
    mutation = {
        "entity_type": "LocalizationType",
        "old_attribute_type_name": new_attr_name,
        "new_attribute_type": {"name": new_attr_name, "dtype": "float"},
        "max_instances": 50,
    }
    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException) as excinfo:
        tator_api.rename_attribute(id=attribute_box_type, attribute_type_update=mutation)

    assert "too many Localizations" in str(excinfo.value)

    # Change attribute type with higher `max_instances` should succeed
    mutation = {
        "entity_type": "LocalizationType",
        "old_attribute_type_name": new_attr_name,
        "new_attribute_type": {"name": new_attr_name, "dtype": "float"},
        "max_instances": 100,
    }
    tator_api.rename_attribute(id=attribute_box_type, attribute_type_update=mutation)

    # Check for mutated attribute
    entity_type = tator_api.get_localization_type(attribute_box_type)
    for attr in entity_type.attribute_types:
        if attr.name == new_attr_name:
            assert attr.dtype == "float"
            break
    else:
        assert False, f"Attribute {new_attr_name} not found"

    # Clean up
    params = {"media_id": [attribute_video], "type": attribute_box_type}
    tator_api.delete_localization_list(project, **params)

    # Delete the attribute to keep clean for other tests
    attribute_delete = {
        "entity_type": "LocalizationType",
        "attribute_to_delete": new_attr_name,
    }
    tator_api.delete_attribute(id=attribute_box_type, attribute_type_delete=attribute_delete)
