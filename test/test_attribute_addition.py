from uuid import uuid4
import pytest

import tator


def add_attribute_helper(tator_api, type_getter, type_id, dtype):
    new_attr_name = f"New {dtype} {uuid4()}"
    entity_type = type_getter(type_id)

    # Make sure the new attribute does not exist already
    assert all(attr.name != new_attr_name for attr in entity_type.attribute_types)
    addition = {
        "entity_type": f"{type(entity_type).__name__}",
        "addition": {"name": new_attr_name, "dtype": dtype},
    }
    tator_api.add_attribute(id=type_id, attribute_addition=addition)
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
        tator_api.add_attribute(id=type_id, attribute_addition=addition)

    # Check the exeption message for expected content
    assert (
        "ValidationError: \\\"'unknown' is not one of ['bool', 'int', 'float', 'enum', 'string', 'datetime', 'geopos']\\\""
        in str(excinfo.value)
    )


def test_box_type_add_invalid_attribute(host, token, project, box_type):
    tator_api = tator.get_api(host, token)
    add_invalid_attribute_helper(tator_api, tator_api.get_localization_type, box_type)


def test_state_type_add_invalid_attribute(host, token, project, state_type):
    tator_api = tator.get_api(host, token)
    add_invalid_attribute_helper(tator_api, tator_api.get_state_type, state_type)


def test_video_type_add_invalid_attribute(host, token, project, video_type):
    tator_api = tator.get_api(host, token)
    add_invalid_attribute_helper(tator_api, tator_api.get_media_type, video_type)


dtypes = ["int", "bool", "float", "string", "enum", "datetime", "geopos"]


@pytest.mark.parametrize("dtype", dtypes)
def test_box_type_add_attribute(host, token, project, box_type, dtype):
    tator_api = tator.get_api(host, token)
    add_attribute_helper(tator_api, tator_api.get_localization_type, box_type, dtype)


@pytest.mark.parametrize("dtype", dtypes)
def test_state_type_add_attribute(host, token, project, state_type, dtype):
    tator_api = tator.get_api(host, token)
    add_attribute_helper(tator_api, tator_api.get_state_type, state_type, dtype)


@pytest.mark.parametrize("dtype", dtypes)
def test_video_type_add_attribute(host, token, project, video_type, dtype):
    tator_api = tator.get_api(host, token)
    add_attribute_helper(tator_api, tator_api.get_media_type, video_type, dtype)
