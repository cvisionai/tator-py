import subprocess

import tator

def test_setup_project(host, token):
    cmd = [
        'python3',
        'examples/setup_project.py',
        '--host', host,
        '--token', token,
    ]
    subprocess.run(cmd, check=True)
    tator_api = tator.get_api(host, token)
    projects = tator_api.get_project_list()
    for project in projects:
        if project.name == 'Test Project':
            project_id = project.id
            break
    tator_api.delete_project(project_id)    

