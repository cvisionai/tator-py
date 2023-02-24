from uuid import uuid4
import pytest

import tator


def delete_attribute_helper(tator_api, type_getter, type_id, dtype):
    new_attr_name = f"New {dtype} {uuid4()}"
    entity_type = type_getter(type_id)

    addition = {
        "entity_type": f"{type(entity_type).__name__}",
        "addition": {"name": new_attr_name, "dtype": dtype},
    }
    if dtype == "enum":
        addition["addition"]["choices"] = ["a", "b", "c"]
    tator_api.create_attribute_type(id=type_id, attribute_type_spec=addition)
    entity_type = type_getter(type_id)

    # Check for added attribute
    assert any(attr.name == new_attr_name for attr in entity_type.attribute_types)

    # Delete attribute
    deletion = {
        "entity_type": f"{type(entity_type).__name__}",
        "name": new_attr_name,
    }
    tator_api.delete_attribute_type(id=type_id, attribute_type_delete=deletion)
    entity_type = type_getter(type_id)

    # Check that the attribute is gone
    assert all(attr.name != new_attr_name for attr in entity_type.attribute_types)


def delete_invalid_attribute_helper(tator_api, type_getter, type_id):
    new_attr_name = f"New {uuid4()}"
    entity_type = type_getter(type_id)

    # Check that the attribute does not exist
    assert all(attr.name != new_attr_name for attr in entity_type.attribute_types)

    # Delete attribute
    deletion = {
        "entity_type": f"{type(entity_type).__name__}",
        "name": new_attr_name,
    }
    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException) as excinfo:
        tator_api.delete_attribute_type(id=type_id, attribute_type_delete=deletion)

    # Check the exeption message for expected content
    assert "Could not find attribute name" in str(excinfo.value)


def test_box_type_delete_invalid_attribute(host, token, project, attribute_box_type):
    tator_api = tator.get_api(host, token)
    delete_invalid_attribute_helper(tator_api, tator_api.get_localization_type, attribute_box_type)


def test_state_type_delete_invalid_attribute(host, token, project, state_type):
    tator_api = tator.get_api(host, token)
    delete_invalid_attribute_helper(tator_api, tator_api.get_state_type, state_type)


def test_video_type_delete_invalid_attribute(host, token, project, attribute_video_type):
    tator_api = tator.get_api(host, token)
    delete_invalid_attribute_helper(tator_api, tator_api.get_media_type, attribute_video_type)


dtypes = ["int", "bool", "float", "string", "enum", "datetime", "geopos"]


@pytest.mark.parametrize("dtype", dtypes)
def test_box_type_delete_attribute(host, token, project, attribute_box_type, dtype):
    tator_api = tator.get_api(host, token)
    delete_attribute_helper(tator_api, tator_api.get_localization_type, attribute_box_type, dtype)
