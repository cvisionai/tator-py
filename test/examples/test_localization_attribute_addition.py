import subprocess
from uuid import uuid4

import tator


def test_localization_attribute_addition(host, token, project, box_type):
    cmd = [
        "python3",
        "examples/localization_attribute_addition.py",
        "--host", host,
        "--token", token,
        str(project),
        str(box_type),
        f'{{"name": "test {uuid4()}", "dtype": "int", "default": 42}}',
    ]
    subprocess.run(cmd, check=True)
