import tempfile
from time import sleep
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

    # Test default value of `archived` is "live"
    assert video_obj.archive_state == "live"

    # Test default `get_media_list` filters on `archive_lifecycle == "live"`
    response = tator_api.get_media_list(project, media_id=[video])
    assert len(response) == 1
    assert response[0].archive_state == "live"

    # Test `get_media_list` with `archive_lifecycle="archived"` doesn't return "live" objects
    response = tator_api.get_media_list(project, media_id=[video], archive_lifecycle="archived")
    assert len(response) == 0

    # Test returning subset of media that is live
    response = tator_api.get_media_list(project, media_id=[video], archive_lifecycle="live")
    assert len(response) == 1
    assert response[0].archive_state == "live"

    # Test returning subset of media that has any `archive_lifecycle` state
    response = tator_api.get_media_list(project, media_id=[video], archive_lifecycle="all")
    assert len(response) == 1
    assert response[0].archive_state == "live"

    # Mark the video to archive
    tator_api.update_media_list(project, {"archive_state": "to_archive", "ids": [video]})

    # Wait for update to propagate to ES
    sleep(2)

    # Test default `get_media_list` filters on `archive_lifecycle == "live"`
    response = tator_api.get_media_list(project, media_id=[video])
    assert len(response) == 0

    # Test `get_media_list` with `archive_lifecycle="archived"` returns archived objects
    response = tator_api.get_media_list(project, media_id=[video], archive_lifecycle="archived")
    assert len(response) == 1
    assert response[0].archive_state == "to_archive"

    # Test with force_es
    response = tator_api.get_media_list(
        project, media_id=[video], archive_lifecycle="archived", force_es=1
    )
    assert len(response) == 1
    assert response[0].archive_state == "to_archive"

    # Test returning subset of media that is live
    response = tator_api.get_media_list(project, media_id=[video], archive_lifecycle="live")
    assert len(response) == 0

    # Test with force_es
    response = tator_api.get_media_list(
        project, media_id=[video], archive_lifecycle="live", force_es=1
    )
    assert len(response) == 0

    # Test returning subset of media that has any `archive_state` state
    response = tator_api.get_media_list(project, media_id=[video], archive_lifecycle="all")
    assert len(response) == 1
    assert response[0].archive_state == "to_archive"

    # Test with force_es
    response = tator_api.get_media_list(
        project, media_id=[video], archive_lifecycle="all", force_es=1
    )
    assert len(response) == 1
    assert response[0].archive_state == "to_archive"

    # Additional attempts to set the state to `to_archive` will not change anything
    tator_api.update_media(video, {"archive_state": "to_archive"})
    video_obj = tator_api.get_media(video)
    assert video_obj.archive_state == "to_archive"

    # Setting the `archive_state` to `to_live` when a media is in the state `to_archive` should
    # result in the media's state changing to `live`
    tator_api.update_media(video, {"archive_state": "to_live"})
    video_obj = tator_api.get_media(video)
    assert video_obj.archive_state == "live"
