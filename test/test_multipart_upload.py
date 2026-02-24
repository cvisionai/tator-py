import math
import os
import tempfile

import requests

import tator
from tator.util._upload_file import _upload_file
from tator.util.md5sum import md5sum

BBB_URL = "https://tator-ci.s3.us-east-1.amazonaws.com/bbb_sunflower_1080p_30fps_normal.mp4"
BBB_FILENAME = "bbb_sunflower_1080p_30fps_normal.mp4"
CHUNK_SIZE = 10 * 1024 * 1024  # 10MB chunks


def test_multipart_upload(host, token, project, video_type):
    """Verify that multipart upload works with a file large enough to require multiple S3 parts."""
    tator_api = tator.get_api(host, token)

    # Download big buck bunny to a temp directory
    with tempfile.TemporaryDirectory() as td:
        video_path = os.path.join(td, BBB_FILENAME)
        print(f"Downloading {BBB_URL}...")
        with requests.get(BBB_URL, stream=True) as r:
            r.raise_for_status()
            with open(video_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)

        file_size = os.path.getsize(video_path)
        num_chunks = math.ceil(file_size / CHUNK_SIZE)
        assert num_chunks > 1, f"Expected multiple chunks but got {num_chunks} for {file_size} bytes"
        print(f"File size: {file_size} bytes, will upload in {num_chunks} chunks of {CHUNK_SIZE} bytes")

        # Create media entry
        response = tator_api.create_media_list(
            project,
            body=[
                {
                    "type": video_type,
                    "section": "Multipart Test",
                    "name": BBB_FILENAME,
                    "md5": md5sum(video_path),
                }
            ],
        )
        media_id = response.id[0]

        # Upload with multipart
        last_progress = None
        upload_info = None
        for progress, info in _upload_file(
            tator_api,
            project,
            video_path,
            media_id=media_id,
            filename=BBB_FILENAME,
            chunk_size=CHUNK_SIZE,
        ):
            last_progress = progress
            if info is not None:
                upload_info = info

        assert last_progress == 100, f"Upload did not complete, last progress: {last_progress}"
        assert upload_info is not None, "No upload info returned"
        assert upload_info.key, "Upload info missing key"
        print(f"Multipart upload completed successfully: key={upload_info.key}")
