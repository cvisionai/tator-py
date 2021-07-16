import subprocess

import tator

def test_localizations(host, token, project, leaf_type):
    cmd = [
        'python3',
        'examples/leaf.py',
        '--host', host,
        '--token', token,
        '--type_id', str(leaf_type),
        '--input', 'examples/leaf.yaml',
    ]
    subprocess.run(cmd, check=True)
