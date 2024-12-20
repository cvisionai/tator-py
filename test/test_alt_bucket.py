# Test alternate bucket upload, only runs on compose
import pytest
import tator
from tator.util._upload_file import _upload_file
from tator.transcode.transcode import make_video_definition
import tempfile
import requests
import os


def test_alt_bucket_upload(alt_bucket, host, token, project, video_type):
    api = tator.get_api(host, token)

    media_specs = [
        {
            "type": video_type,
            "section": "alt_bucket",
            "name": f"count.mp4",
            "md5": "foo",
        }
    ]

    response = api.create_media_list(project, body=media_specs)
    media_id = response.id[0]

    VIDEO_URL = "https://github.com/cvisionai/rgb_test_videos/raw/v0.0.3/samples/count.mp4"

    file_size = 0
    with tempfile.TemporaryDirectory() as td:
        r = requests.get(VIDEO_URL)
        video_path = os.path.join(td, "count.mp4")
        f = open(video_path, "wb")
        for chunk in r.iter_content(chunk_size=1 * 1024 * 1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
        f.close()
        file_size = os.path.getsize(video_path)

        filename = "count.mp4"
        for _, upload_info in _upload_file(
            api,
            project,
            video_path,
            media_id=media_id,
            filename=filename,
            chunk_size=0x10000000,
            bucket_id=alt_bucket,
        ):
            pass
        media_def = {
            **make_video_definition(video_path),
            "path": upload_info.key,
            "bucket_id": alt_bucket,
        }
        # Patch in video file with the api.
        response = api.create_video_file(media_id, role="archival", video_definition=media_def)

    # Check that the video file was uploaded to alt_bucket
    media = api.get_media(media_id, presigned=3600)
    path = media.media_files.archival[0].path
    assert path.find("tator-alt") >= 0

    with tempfile.TemporaryDirectory() as td:
        download_path = os.path.join(td, "count.mp4")
        with open(download_path, "wb") as f:
            r = requests.get(path)
            for chunk in r.iter_content(chunk_size=1 * 1024 * 1024):
                f.write(chunk)

        assert os.path.getsize(download_path) == file_size
