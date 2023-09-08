import tator
from tator.openapi.tator_openapi import CreateListResponse


def test_make_multi_stream(host, token, project, video, video_temp, multi_type):
    tator_api = tator.get_api(host, token)
    assert video != video_temp
    multi_ids = [video, video_temp]
    response = tator.util.make_multi_stream(
        tator_api, multi_type, [1, 2], 'Test multi', multi_ids, 'Multi Videos'
    )

    assert isinstance(response, CreateListResponse)
    multi_obj = tator_api.get_media(response.id[0])
    assert multi_obj.media_files.ids == multi_ids


def test_missing_gif(host, token, project, video, video_temp, multi_type):
    tator_api = tator.get_api(host, token)
    assert video != video_temp

    # Remove the gifs and mock get_media_list
    video_obj = tator_api.get_media(video)
    video_temp_obj = tator_api.get_media(video_temp)
    video_temp_obj.media_files.thumbnail_gif = []
    video_obj.media_files.thumbnail_gif = []
    def get_media_list(*_, **__):
        return [video_temp_obj, video_obj]
    original_get_media_list = tator_api.get_media_list
    tator_api.get_media_list = get_media_list

    multi_ids = [video_temp, video]
    response = tator.util.make_multi_stream(
        tator_api, multi_type, [1, 2], 'Test multi', multi_ids, 'Multi Videos'
    )

    # Replace get_media_list
    tator_api.get_media_list = original_get_media_list

    assert isinstance(response, CreateListResponse)
    multi_obj = tator_api.get_media(response.id[0])
    assert multi_obj.media_files.ids == multi_ids
