import subprocess

import tator
import uuid

def test_setup_project(host, token):
    temp_name = f"Test Project {uuid.uuid1()}"
    cmd = [
        'python3',
        'examples/setup_project.py',
        '--host', host,
        '--token', token,
        '--name', temp_name,
    ]
    subprocess.run(cmd, check=True)
    tator_api = tator.get_api(host, token)
    projects = tator_api.get_project_list()
    for project in projects:
        if project.name == temp_name:
            project_id = project.id
            break
    tator_api.delete_project(project_id)    

