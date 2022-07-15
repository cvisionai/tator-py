import tator


def test_string_attributes_bulk_update(host, token, project, video_type, video):
    tator_api = tator.get_api(host, token)

    # Put a newline character in a string attribute
    media_bulk_update = {"attributes": {"test_string": "test\nnewline"}, "ids": [video]}
    tator_api.update_media_list(project, media_bulk_update)
    video_obj = tator_api.get_media(video)
    assert video_obj.attributes["test_string"] == media_bulk_update["attributes"]["test_string"]

    # Put a backslash character in a string attribute
    media_bulk_update["attributes"]["test_string"] = "test\\backslash"
    tator_api.update_media_list(project, media_bulk_update)
    video_obj = tator_api.get_media(video)
    assert video_obj.attributes["test_string"] == media_bulk_update["attributes"]["test_string"]

    # Put a double quote character in a string attribute
    media_bulk_update["attributes"]["test_string"] = 'test "double" quotes'
    tator_api.update_media_list(project, media_bulk_update)
    video_obj = tator_api.get_media(video)
    assert video_obj.attributes["test_string"] == media_bulk_update["attributes"]["test_string"]

def test_enum_attributes_count_mismatch(host, token, project, state_type, video):
    tator_api = tator.get_api(host, token)
    media_bulk_update = {"attributes": {"test_enum": "a"}, "ids": [video]}
    tator_api.update_media_list(project, media_bulk_update)
    video_obj = tator_api.get_media(video)
    assert video_obj.attributes["test_enum"] == media_bulk_update["attributes"]["test_enum"]
    assert tator_api.get_media_count(project, attribute=["test_enum::a"], media_id=[video], force_es=0) == tator_api.get_media_count(project, attribute=["test_enum::a"], media_id=[video], force_es=1)
