import subprocess

import tator

def test_activities(host, token, video_type, video):
    cmd = [
        'python3',
        'examples/activities.py',
        '--host', host,
        '--token', token,
        '--video_type_id', str(video_type),
        '--video_id', str(video),
    ]
    subprocess.run(cmd, check=True)
