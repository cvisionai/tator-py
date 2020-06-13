import subprocess

import tator

def test_localizations(host, token, project, video, box_type):
    cmd = [
        'python3',
        'examples/localizations.py',
        '--host', host,
        '--token', token,
        '--video_id', str(video),
        '--type_id', str(box_type),
    ]
    subprocess.run(cmd, check=True)
