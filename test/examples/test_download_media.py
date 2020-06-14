import subprocess
import os

import tator

def test_download_media(host, token, project, video):

    # Get project and video.
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)
    project_obj = tator_api.get_project(project)

    # Clear the media on disk if it exists.
    expected_path = os.path.join('/tmp', video_obj.name)
    if os.path.exists(expected_path):
        os.remove(expected_path)

    # Run the example.
    cmd = [
        'python3',
        'examples/download_media.py',
        '--host', host,
        '--token', token,
        '--media_name', video_obj.name,
        '--project_name', project_obj.name,
        '--save_path', '/tmp',
    ]
    subprocess.run(cmd, check=True)

    # Assert the download exists.
    assert os.path.exists(expected_path)
