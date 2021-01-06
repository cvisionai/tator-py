import pytest
from uuid import uuid4

import tator

allowed_mutations = {
    "bool": ["bool", "enum", "string"],
    "int": ["int", "float", "enum", "string"],
    "float": ["int", "float", "enum", "string"],
    "enum": ["enum", "string"],
    "string": ["enum", "string"],
    "datetime": ["enum", "string", "datetime"],
    "geopos": ["enum", "string", "geopos"],
}


def mutation_helper(tator_api, type_getter, type_id, params):
    uid = f" {uuid4()}"
    source_name = params["source_name"]
    dest_name = params.get("dest_name", source_name)
    source_name += uid
    dest_name += uid
    source_dtype = params["source_dtype"]
    dest_dtype = params.get("dest_dtype", source_dtype)
    assert_cnt = 0

    entity_type = type_getter(type_id)
    addition = {
        "entity_type": f"{type(entity_type).__name__}",
        "addition": {"name": source_name, "dtype": source_dtype},
    }
    if source_dtype == "enum":
        addition["addition"]["choices"] = ["a", "b", "c"]
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
        "new_attribute_type": {"name": dest_name, "dtype": dest_dtype},
    }
    if dest_dtype == "enum":
        mutation["new_attribute_type"]["choices"] = ["a", "b", "c"]

    # A type mutation not in the list of allowed mutations will raise an `ApiException` and the
    # expected `dtype` will be the same as `source_dtype`
    if dest_dtype in allowed_mutations[source_dtype]:
        expected_dtype = dest_dtype
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


@pytest.mark.parametrize("source_dtype", allowed_mutations.keys())
@pytest.mark.parametrize("dest_dtype", allowed_mutations.keys())
def test_box_type_dtype_change(host, token, project, box_type, source_dtype, dest_dtype):
    tator_api = tator.get_api(host, token)
    params = {
        "source_name": f"{source_dtype} attribute to modify",
        "source_dtype": source_dtype,
        "dest_dtype": dest_dtype,
        "expected_asserts": 4,
    }
    mutation_helper(tator_api, tator_api.get_localization_type, box_type, params)


@pytest.mark.parametrize("dtype", allowed_mutations.keys())
def test_box_type_invalid_dtype_change(host, token, project, box_type, dtype):
    tator_api = tator.get_api(host, token)
    params = {
        "source_name": f"{dtype} attribute to modify",
        "source_dtype": dtype,
        "dest_dtype": "unknown",
        "expected_asserts": 4,
    }
    mutation_helper(tator_api, tator_api.get_localization_type, box_type, params)


@pytest.mark.parametrize("dtype", allowed_mutations.keys())
def test_state_type_invalid_dtype_change(host, token, project, state_type, dtype):
    tator_api = tator.get_api(host, token)
    params = {
        "source_name": f"{dtype} attribute to modify",
        "source_dtype": dtype,
        "dest_dtype": "unknown",
        "expected_asserts": 4,
    }
    mutation_helper(tator_api, tator_api.get_state_type, state_type, params)


@pytest.mark.parametrize("dtype", allowed_mutations.keys())
def test_video_type_invalid_dtype_change(host, token, project, video_type, dtype):
    tator_api = tator.get_api(host, token)
    params = {
        "source_name": f"{dtype} attribute to modify",
        "source_dtype": dtype,
        "dest_dtype": "unknown",
        "expected_asserts": 4,
    }
    mutation_helper(tator_api, tator_api.get_media_type, video_type, params)


@pytest.mark.parametrize("dtype", allowed_mutations.keys())
def test_box_type_name_change(host, token, project, box_type, dtype):
    tator_api = tator.get_api(host, token)
    params = {
        "source_name": f"{dtype} attribute to rename",
        "source_dtype": dtype,
        "dest_name": f"renamed {dtype} attribute",
        "expected_asserts": 5,
    }
    mutation_helper(tator_api, tator_api.get_localization_type, box_type, params)


@pytest.mark.parametrize("dtype", allowed_mutations.keys())
def test_state_type_name_change(host, token, project, state_type, dtype):
    tator_api = tator.get_api(host, token)
    params = {
        "source_name": f"{dtype} attribute to rename",
        "source_dtype": dtype,
        "dest_name": f"renamed {dtype} attribute",
        "expected_asserts": 5,
    }
    mutation_helper(tator_api, tator_api.get_state_type, state_type, params)


@pytest.mark.parametrize("dtype", allowed_mutations.keys())
def test_video_type_name_change(host, token, project, video_type, dtype):
    tator_api = tator.get_api(host, token)
    params = {
        "source_name": f"{dtype} attribute to rename",
        "source_dtype": dtype,
        "dest_name": f"renamed {dtype} attribute",
        "expected_asserts": 5,
    }
    mutation_helper(tator_api, tator_api.get_media_type, video_type, params)


@pytest.mark.parametrize("source_dtype", allowed_mutations.keys())
@pytest.mark.parametrize("dest_dtype", allowed_mutations.keys())
def test_box_type_full_mutation(host, token, project, box_type, source_dtype, dest_dtype):
    params = {
        "source_name": f"{source_dtype} attribute to modify",
        "source_dtype": source_dtype,
        "dest_name": f"renamed {source_dtype} -> {dest_dtype} attribute",
        "dest_dtype": dest_dtype,
        "expected_asserts": 5 if dest_dtype in allowed_mutations[source_dtype] else 4,
    }
    tator_api = tator.get_api(host, token)
    mutation_helper(tator_api, tator_api.get_localization_type, box_type, params)


@pytest.mark.parametrize("dtype", allowed_mutations.keys())
def test_video_and_image_type_name_change(host, token, project, video_type, image_type, dtype):
    uid = f"{uuid4()}"
    source_name = f"{dtype} attribute to rename {uid}"
    dest_name = f"renamed {dtype} attribute {uid}"
    source_dtype = dtype
    tator_api = tator.get_api(host, token)

    # Add attribute to video_type
    entity_type = tator_api.get_media_type(video_type)
    addition = {
        "entity_type": f"MediaType",
        "addition": {"name": source_name, "dtype": source_dtype},
    }
    if source_dtype == "enum":
        addition["addition"]["choices"] = ["a", "b", "c"]
    tator_api.add_attribute(id=video_type, attribute_type_spec=addition)
    entity_type = tator_api.get_media_type(video_type)

    # Check attribute name before changing it
    assert any(attr.name == source_name for attr in entity_type.attribute_types)

    # Add same attribute to image_type
    entity_type = tator_api.get_media_type(image_type)
    addition = {
        "entity_type": f"MediaType",
        "addition": {"name": source_name, "dtype": source_dtype},
    }
    if source_dtype == "enum":
        addition["addition"]["choices"] = ["a", "b", "c"]
    tator_api.add_attribute(id=image_type, attribute_type_spec=addition)
    entity_type = tator_api.get_media_type(image_type)

    # Check attribute name before changing it
    assert any(attr.name == source_name for attr in entity_type.attribute_types)

    # Mutate attribute on video_type
    mutation = {
        "global": "true",
        "entity_type": "MediaType",
        "old_attribute_type_name": source_name,
        "new_attribute_type": {"name": dest_name, "dtype": source_dtype},
    }
    if source_dtype == "enum":
        mutation["new_attribute_type"]["choices"] = ["a", "b", "c"]

    tator_api.rename_attribute(id=video_type, attribute_type_update=mutation)

    entity_type = tator_api.get_media_type(video_type)

    # Check new attribute name
    assert any(attr.name == dest_name for attr in entity_type.attribute_types)

    # No attributes should have the old name
    assert all(attr.name != source_name for attr in entity_type.attribute_types)

    # The image_type attribute should also have the new name
    entity_type = tator_api.get_media_type(image_type)
    assert any(attr.name == dest_name for attr in entity_type.attribute_types)
    assert all(attr.name != source_name for attr in entity_type.attribute_types)
