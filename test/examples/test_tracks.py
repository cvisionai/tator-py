import subprocess

import tator

def test_tracks(host, token, video_type, video):
    cmd = [
        'python3',
        'examples/tracks.py',
        '--host', host,
        '--token', token,
        '--video_type_id', str(video_type),
        '--video_id', str(video),
    ]
    subprocess.run(cmd, check=True)
