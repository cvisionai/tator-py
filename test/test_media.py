import tempfile
import os

import tator

def test_get_file(host, token, project, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    with tempfile.TemporaryDirectory() as temp_dir:
        outpath = os.path.join(temp_dir, "video.mp4")
        for progress in tator.download_media(tator_api, video_obj, outpath):
            print(f"Video download progress: {progress}%")
        assert(os.path.exists(outpath))

def test_get_audio(host, token, project, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    audio = video_obj.media_files.audio
    assert len(audio) > 0
    assert audio[0].codec == 'aac'

def test_get_by_id(host, token, project, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)
    other_obj = tator_api.get_media_list_by_id(project, {'ids': [video]})[0]
    assert video_obj.id == other_obj.id
    other_obj = tator_api.get_media_list_by_id(project, {'ids': [video]}, force_es=1)[0]
    assert video_obj.id == other_obj.id

def test_archive(host, token, project, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    # Test default value of `archived` is False
    assert video_obj.archived == False

    # Test default `get_media_list` filters on `archived == False`
    response = tator_api.get_media_list(project, media_id=[video])
    assert len(response) == 1
    assert response[0].archived == False

    # Test `get_media_list` with `archive_state="archived"` returns only `archived == True`
    # objects
    response = tator_api.get_media_list(project, media_id=[video], archive_state="archived")
    assert len(response) == 0

    # Test returning subset of media that is live
    response = tator_api.get_media_list(project, media_id=[video], archive_state="live")
    assert len(response) == 1
    assert response[0].archived == False

    # Test returning subset of media that has any `archived` state
    response = tator_api.get_media_list(project, media_id=[video], archive_state="all")
    assert len(response) == 1
    assert response[0].archived == False

    # Archive the video
    bulk_update = {"archived": True, "ids": [video]}
    tator_api.update_media_list(project, bulk_update)

    # Test default `get_media_list` filters on `archived == False`
    response = tator_api.get_media_list(project, media_id=[video])
    assert len(response) == 0

    # Test `get_media_list` with `archive_state="archived"` returns only `archived == True` objects
    response = tator_api.get_media_list(project, media_id=[video], archive_state="archived")
    assert len(response) == 1
    assert response[0].archived == True

    # Test returning subset of media that is live
    response = tator_api.get_media_list(project, media_id=[video], archive_state="live")
    assert len(response) == 0

    # Test returning subset of media that has any `archived` state
    response = tator_api.get_media_list(project, media_id=[video], archive_state="all")
    assert len(response) == 1
    assert response[0].archived == True

    # Clean up
    single_update = {"archived": False}
    tator_api.update_media(video, single_update)
    video_obj = tator_api.get_media(video)
    assert video_obj.archived == False
