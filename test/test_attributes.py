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

