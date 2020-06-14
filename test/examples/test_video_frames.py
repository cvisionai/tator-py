import subprocess

import tator

def test_video_frames(host, token, project, video):

    # Run the example.
    cmd = [
        'python3',
        'examples/video_frames.py',
        '--host', host,
        '--token', token,
        '--video_id', str(video),
    ]
    subprocess.run(cmd, check=True)

