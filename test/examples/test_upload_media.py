import subprocess
import os

import pytest
import tator

@pytest.mark.flaky(reruns=3)
def test_upload_media(host, token, video_type, video_file):

    # Run the example.
    cmd = [
        'python3',
        'examples/upload_media.py',
        '--host', host,
        '--token', token,
        '--type-id', str(video_type),
        '--media-path', video_file,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        result.check_returncode()
