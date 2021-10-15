import os
import subprocess
import tempfile
import uuid
from textwrap import dedent

import tator

def _create_html_file_str() -> str:
    """ Creates a HTML file used by the unit tests in this file
    """

    return dedent("""\
<html>
<head>
<title>CVisionAI Tator Test</title>
</head>
<body>
<p>Hi! This is a test HTML file for CVisionAI's tator-py bindings</p>
</body>
</html>
        """)

def test_register_and_update_dashboard(host: str, token: str, project: int):

    fd, local_file = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as file_handle:
        file_handle.write(_create_html_file_str())

    fd, local_file2 = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as file_handle:
        file_handle.write(_create_html_file_str())

    try:
        cmd = [
            'python3',
            'examples/register_dashboard.py',
            '--host', host,
            '--token', token,
            '--project', str(project),
            '--html-file', local_file,
            '--name', 'dashboard_test',
            '--description', 'test description',
            '--categories', "categoryA", "categoryB"
        ]

        subprocess.run(cmd, check=True)

    finally:

        tator_api = tator.get_api(host=host, token=token)
        dashboards = tator_api.get_dashboard_list(project=project)

        assert dashboards[-1].name == "dashboard_test"

        new_name = "dashboard_test2"
        new_description = "test description2"
        new_categories = ["categoryC"]

        try:
            cmd = [
                'python3',
                'examples/update_dashboard.py',
                '--host', host,
                '--token', token,
                '--dashboard-id', str(dashboards[-1].id),
                '--html-file', local_file2,
                '--name', new_name,
                '--description', new_description,
                '--categories', new_categories[0]
            ]

            subprocess.run(cmd, check=True)

        finally:

            dashboards = tator_api.get_dashboard_list(project=project)
            assert dashboards[-1].name == new_name
            assert dashboards[-1].description == new_description
            assert dashboards[-1].categories == new_categories

        tator_api.delete_dashboard(id=dashboards[-1].id)

    os.remove(local_file)
    os.remove(local_file2)
