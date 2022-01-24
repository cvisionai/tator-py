from datetime import datetime, timezone

import tator


def test_date_before_now(host, token, project, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)
    assert datetime.now(timezone.utc) > video_obj.archive_status_date


def test_date_after_change(host, token, project, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)
    original_status_date = video_obj.archive_status_date

    tator_api.update_media(video, media_update={"archive_state": "to_archive"})
    video_obj = tator_api.get_media(video)
    to_archive_date = video_obj.archive_status_date
    assert datetime.now(timezone.utc) > to_archive_date > original_status_date

    tator_api.update_media(video, media_update={"archive_state": "to_live"})
    video_obj = tator_api.get_media(video)
    assert datetime.now(timezone.utc) > video_obj.archive_status_date > to_archive_date

def test_date_after_unrelated_change(host, token, project, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)
    original_status_date = video_obj.archive_status_date
    original_name = video_obj.name

    tator_api.update_media(video, media_update={"name": "new_name"})
    video_obj = tator_api.get_media(video)
    assert video_obj.archive_status_date == original_status_date

    tator_api.update_media(video, media_update={"name": original_name})
    video_obj = tator_api.get_media(video)
    assert video_obj.archive_status_date == original_status_date
