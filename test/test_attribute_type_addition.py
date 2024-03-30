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
        "attributes": attributes,
    }

    return {**out}


def add_attribute_helper(tator_api, type_getter, type_id, dtype):
    new_attr_name = f"New {dtype} {uuid4()}"
    entity_type = type_getter(type_id)

    # Make sure the new attribute does not exist already
    assert all(attr.name != new_attr_name for attr in entity_type.attribute_types)
    addition = {
        "entity_type": f"{type(entity_type).__name__}",
        "addition": {"name": new_attr_name, "dtype": dtype},
    }
    if dtype == "enum":
        addition["addition"]["choices"] = ["a", "b", "c"]
    if dtype == "float_array":
        addition["addition"]["size"] = 3
    tator_api.create_attribute_type(id=type_id, attribute_type_spec=addition)
    entity_type = type_getter(type_id)

    # Check for added attribute
    assert any(attr.name == new_attr_name for attr in entity_type.attribute_types)


def add_invalid_attribute_helper(tator_api, type_getter, type_id):
    new_attr_name = f"New invalid attribute {uuid4()}"
    entity_type = type_getter(type_id)

    # Make sure the new attribute does not exist already
    assert all(attr.name != new_attr_name for attr in entity_type.attribute_types)
    addition = {
        "entity_type": f"{type(entity_type).__name__}",
        "addition": {"name": new_attr_name, "dtype": "unknown"},
    }

    # Adding an attribute with an invalid `dtype` should raise an exception
    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException) as excinfo:
        tator_api.create_attribute_type(id=type_id, attribute_type_spec=addition)

    # Check the exeption message for expected content
    assert (
        "ValidationError: \\\"'unknown' is not one of ['bool', 'int', 'float', 'enum', 'string', 'datetime', 'geopos', 'float_array', 'blob']\\\""
        in str(excinfo.value)
    )


def test_box_type_add_invalid_attribute(host, token, project, attribute_box_type):
    tator_api = tator.get_api(host, token)
    add_invalid_attribute_helper(tator_api, tator_api.get_localization_type, attribute_box_type)


def test_state_type_add_invalid_attribute(host, token, project, state_type):
    tator_api = tator.get_api(host, token)
    add_invalid_attribute_helper(tator_api, tator_api.get_state_type, state_type)


def test_video_type_add_invalid_attribute(host, token, project, attribute_video_type):
    tator_api = tator.get_api(host, token)
    add_invalid_attribute_helper(tator_api, tator_api.get_media_type, attribute_video_type)


dtypes = ["int", "bool", "float", "string", "enum", "datetime", "geopos", "float_array"]


@pytest.mark.parametrize("dtype", dtypes)
def test_box_type_add_attribute(host, token, project, attribute_box_type, dtype):
    tator_api = tator.get_api(host, token)
    add_attribute_helper(tator_api, tator_api.get_localization_type, attribute_box_type, dtype)


@pytest.mark.parametrize("dtype", dtypes)
def test_state_type_add_attribute(host, token, project, state_type, dtype):
    tator_api = tator.get_api(host, token)
    add_attribute_helper(tator_api, tator_api.get_state_type, state_type, dtype)


@pytest.mark.parametrize("dtype", dtypes)
def test_video_type_add_attribute(host, token, project, attribute_video_type, dtype):
    tator_api = tator.get_api(host, token)
    add_attribute_helper(tator_api, tator_api.get_media_type, attribute_video_type, dtype)


def test_add_enum_without_choices(host, token, project, attribute_video_type):
    dtype = "enum"
    tator_api = tator.get_api(host, token)
    new_attr_name = f"New {dtype} {uuid4()}"
    entity_type = tator_api.get_media_type(attribute_video_type)

    # Make sure the new attribute does not exist already
    assert all(attr.name != new_attr_name for attr in entity_type.attribute_types)
    addition = {
        "entity_type": "MediaType",
        "addition": {"name": new_attr_name, "dtype": dtype},
    }

    # Adding an enum attribute without a `choices` field should raise an exception
    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException) as excinfo:
        tator_api.create_attribute_type(id=attribute_video_type, attribute_type_spec=addition)

    # Check the exeption message for expected content
    assert "enum attribute type definition missing 'choices' field" in str(
        excinfo.value
    )


def test_add_same_attribute_twice(host, token, project, line_type):
    tator_api = tator.get_api(host, token)
    new_attr_name = f"New attribute {uuid4()}"

    # Make sure the new attribute does not exist already
    entity_type = tator_api.get_localization_type(line_type)
    assert all(attr.name != new_attr_name for attr in entity_type.attribute_types)
    addition = {
        "entity_type": "LocalizationType",
        "addition": {"name": new_attr_name, "dtype": "int"},
    }
    tator_api.create_attribute_type(id=line_type, attribute_type_spec=addition)
    entity_type = tator_api.get_localization_type(line_type)

    # Check for added attribute
    assert any(attr.name == new_attr_name for attr in entity_type.attribute_types)

    # Adding the same attribute a second time should raise an exception
    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException) as excinfo:
        tator_api.create_attribute_type(id=line_type, attribute_type_spec=addition)

    # Check the exeption message for expected content
    assert "is already an attribute." in str(excinfo.value)
