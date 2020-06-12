import subprocess
import os

import tator

def test_upload_media(host, token, video_type, video_file):

    # Run the example.
    cmd = [
        'python3',
        'examples/upload_media.py',
        '--host', host,
        '--token', token,
        '--type_id', str(video_type),
        '--media_path', video_file,
    ]
    subprocess.run(cmd, check=True)

