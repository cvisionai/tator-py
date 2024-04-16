from datetime import datetime
import os
from random import randint
import tempfile
from time import sleep
from urllib.parse import parse_qs, urlparse
from uuid import uuid1
import pytest

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
    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        response = tator_api.update_media_list(project, media_id=[video], media_bulk_update=update_spec, count=2)
    response = tator_api.update_media_list(project, media_id=[video], media_bulk_update=update_spec, count=1)
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
    image_url = "https://www.gstatic.com/webp/gallery/1.jpg"
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
    created_ids = response.id
    duration = (datetime.now() - start).total_seconds()
    assert duration < 5

    assert str(len(media_specs)) in response.message
    assert len(media_specs) == len(created_ids)

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
        media_list = tator_api.get_media_list(project, type=image_type, media_id=created_ids)

        n_with_media_files = 0
        for media in media_list:
            if media.name.startswith(uuid) and media.media_files is not None:
                n_with_media_files += 1
        if n_with_media_files == n_images:
            break
    assert n_with_media_files == n_images


def parse_url(url):
    parsed_url = urlparse(url)
    return parsed_url.path, parse_qs(parsed_url.query)


def parse_media_files(media):
    return dict(
        parse_url(spec["path"])
        for file_type, file_specs in media.media_files.to_dict().items()
        if file_specs is not None
        for spec in file_specs
        if "path" in spec
    )


def test_presigned_no_cache(host, token, project, video_type, video_file):
    expires_key = "X-Amz-Expires"

    # Set up new video to ensure a clean cache
    tator_api = tator.get_api(host, token)
    uuid_val = str(uuid1())
    attributes = {"test_string": uuid_val}
    for progress, response in tator.util.upload_media(
            tator_api, video_type, video_file, attributes=attributes
    ):
        print(f"Upload video progress: {progress}%")
    print(response.message)

    while True:
        response = tator_api.get_media_list(
            project,
            name='AudioVideoSyncTest_BallastMedia.mp4',
            attribute=[f"test_string::{uuid_val}"],
        )
        print("Waiting for transcode...")
        sleep(2.5)
        if len(response) == 0:
            continue
        if response[0].media_files is None:
            continue
        streaming = response[0].media_files.streaming
        have_archival = response[0].media_files.archival is not None
        if streaming and have_archival and len(streaming) == 4:
            video_id = response[0].id
            break

    # Get initial presigned url
    original_presigned_duration = new_presigned_duration = randint(8640, 86400)
    while new_presigned_duration == original_presigned_duration:
        new_presigned_duration = randint(8640, 86400)

    video_obj = tator_api.get_media(video_id, presigned=original_presigned_duration)

    init_presigned_url = parse_media_files(video_obj)

    # Request a new duration without the `no_cache` flag and assert it returns the same urls
    video_obj = tator_api.get_media(video_id, presigned=new_presigned_duration, no_cache=False)
    no_cache_false_presigned_url = parse_media_files(video_obj)

    for path, query_params in no_cache_false_presigned_url.items():
        assert path in init_presigned_url
        assert int(query_params[expires_key][0]) == original_presigned_duration

    # Request a new duration with the `no_cache` flag and assert it returns new urls
    video_obj = tator_api.get_media(video_id, presigned=new_presigned_duration, no_cache=True)
    no_cache_false_presigned_url = parse_media_files(video_obj)

    for path, query_params in no_cache_false_presigned_url.items():
        assert path in init_presigned_url
        assert int(query_params[expires_key][0]) == new_presigned_duration

    # Request a new duration without the `no_cache` flag again and assert it returns the original
    # cached urls and not the ones from the new duration
    video_obj = tator_api.get_media(video_id, presigned=original_presigned_duration, no_cache=False)
    no_cache_false_presigned_url = parse_media_files(video_obj)

    for path, query_params in no_cache_false_presigned_url.items():
        assert path in init_presigned_url
        assert int(query_params[expires_key][0]) == original_presigned_duration

def test_upload_to_section_id(host, token, project, image_type, image_file):
    tator_api = tator.get_api(host, token)
    section_spec = {
        "name": "Section ID test",
        "tator_user_sections": str(uuid1()),
    }
    section_id = tator_api.create_section(project, section_spec).id
    attributes = {"test_string": str(uuid1())}
    for progress, response in tator.util.upload_media(
            tator_api, image_type, image_file, section_id=section_id, attributes=attributes
    ):
        print(f"Upload image to section by ID progress: {progress}%")
    print(response.message)
    media_list = tator_api.get_media_list(
        project,
        section=section_id,
    )
    assert(len(media_list) == 1)
