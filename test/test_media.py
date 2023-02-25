from datetime import datetime
import os
import tempfile
from time import sleep
from uuid import uuid1

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
    count = tator_api.get_media_count_by_id(project, {'ids': [video]})
    assert(count == 1)

def test_archive(host, token, project, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    # Test default value of `archived` is "live"
    assert video_obj.archive_state == "live"

    # Test default `get_media_list` filters on `archive_lifecycle == "all"`
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

    # Test default `get_media_list` filters on `archive_lifecycle == "all"`
    response = tator_api.get_media_list(project, media_id=[video])
    assert len(response) == 1
    assert response[0].archive_state == "to_archive"

    # Test `get_media_list` with `archive_lifecycle="archived"` returns archived objects
    response = tator_api.get_media_list(project, media_id=[video], archive_lifecycle="archived")
    assert len(response) == 1
    assert response[0].archive_state == "to_archive"

    # Test returning subset of media that is live
    response = tator_api.get_media_list(project, media_id=[video], archive_lifecycle="live")
    assert len(response) == 0

    # Test returning subset of media that has any `archive_state` state
    response = tator_api.get_media_list(project, media_id=[video], archive_lifecycle="all")
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

def test_section(host, token, project, video):
    tator_api = tator.get_api(host, token)

    # Create test section
    section_spec = {"name": "Test Section", "tator_user_sections": str(uuid1())}
    response = tator_api.create_section(project, section_spec=section_spec)

    # Update media `tator_user_sections` attribute
    update_spec = {"attributes": {"tator_user_sections": section_spec["tator_user_sections"]}}
    response = tator_api.update_media(
        video, update_spec
    )
    media = tator_api.get_media(video)
    assert media.attributes["tator_user_sections"] == section_spec["tator_user_sections"]

    # Unset media `tator_user_sections` attribute
    response = tator_api.update_media(
        video, {"attributes": {"tator_user_sections": ""}}
    )
    media = tator_api.get_media(video)
    assert media.attributes["tator_user_sections"] == ""

    # Update media `tator_user_sections` attribute with a bulk update
    response = tator_api.update_media_list(project, media_id=[video], media_bulk_update=update_spec)
    media = tator_api.get_media(video)
    assert media.attributes["tator_user_sections"] == section_spec["tator_user_sections"]

    # Unset media `tator_user_sections` attribute with a bulk update
    response = tator_api.update_media_list(
        project,
        media_id=[video],
        media_bulk_update={"attributes": {"tator_user_sections": ""}},
    )
    media = tator_api.get_media(video)
    assert media.attributes["tator_user_sections"] == ""


def test_import_multiple_images(host, token, project, image_type):
    tator_api = tator.get_api(host, token)
    image_url = "https://s3.amazonaws.com/tator-ci/landscape.jpg"
    n_images = 5
    uuid = str(uuid1())

    project_media_count = tator_api.get_media_count(project, type=image_type)

    media_specs = [
        {
            "type": image_type,
            "section": "Multiple image upload",
            "name": f"{uuid}_{idx}.jpg",
            "url": image_url,
            "md5": "",
        }
        for idx in range(n_images)
    ]

    start = datetime.now()
    response = tator_api.create_media_list(project, body=media_specs)
    duration = (datetime.now() - start).total_seconds()
    assert duration < 5

    assert str(len(media_specs)) in response.message

    new_project_media_count = -1
    desired_project_media_count = project_media_count + len(media_specs)
    for _ in range(30):
        sleep(1)
        new_project_media_count = tator_api.get_media_count(project, type=image_type)
        if new_project_media_count == desired_project_media_count:
            break
    assert new_project_media_count == desired_project_media_count
    for _ in range(30):
        sleep(1)
        media_list = tator_api.get_media_list(project, type=image_type)

        n_with_media_files = 0
        for media in media_list:
            if media.name.startswith(uuid) and media.media_files is not None:
                n_with_media_files += 1
        if n_with_media_files == n_images:
            break
    assert n_with_media_files == n_images
