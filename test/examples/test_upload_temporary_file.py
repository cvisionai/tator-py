import subprocess

import tator

def test_upload_temporary_file(host, token, project, video_file):

    # Run the example.
    cmd = [
        'python3',
        'examples/upload_temporary_file.py',
        '--host', host,
        '--token', token,
        '--project_id', str(project),
        '--file_path', video_file,
    ]
    subprocess.run(cmd, check=True)

