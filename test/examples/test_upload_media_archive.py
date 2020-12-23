import subprocess
import os

import tator

def test_upload_media_archive(host, token, project, image_set, image_type):

    # Run the example.
    cmd = [
        'python3',
        'examples/upload_media_archive.py',
        '--host', host,
        '--token', token,
        '--project_id', str(project),
        '--media_dir', image_set,
    ]
    subprocess.run(cmd, check=True)

