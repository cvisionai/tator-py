import subprocess
import tempfile

import tator

def test_download_temporary_file(host, token, project):
    tator_api = tator.get_api(host, token)

    with tempfile.NamedTemporaryFile(mode='w',suffix=".txt") as temp:
        temp.write("foo")
        temp.flush()
        for progress, response in tator.util.upload_temporary_file(tator_api, project, temp.name):
            print(f"Temporary file upload progress: {progress}%")
        print(response.message)
        temporary_file_id = response.id

    # Run the example.
    cmd = [
        'python3',
        'examples/download_temporary_file.py',
        '--host', host,
        '--token', token,
        '--temporary_file_id', str(temporary_file_id),
        '--file_path', '/tmp/asdf',
    ]
    subprocess.run(cmd, check=True)

