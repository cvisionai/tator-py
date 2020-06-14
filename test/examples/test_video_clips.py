import subprocess
import tempfile

import tator

def test_video_clips(host, token, project, video):

    # Run the example.
    cmd = [
        'python3',
        'examples/video_clips.py',
        '--host', host,
        '--token', token,
        '--video_id', str(video),
        '--file_path', '/tmp/asdf',
    ]
    subprocess.run(cmd, check=True)

