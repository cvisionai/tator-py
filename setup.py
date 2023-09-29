import os
import subprocess
import shutil

from setuptools import setup, find_packages
import requests
import yaml
import json

REQUIRES = [
    "certifi >= 14.05.14",
    "Pillow >= 10.0.1",
    "progressbar2 >= 3.51.4",
    "psutil >= 5.9.5",
    "python-dateutil >= 2.5.3",
    "pyyaml >= 5.3.1",
    "requests >= 2.25",
    "six >= 1.10",
    "urllib3 >= 1.26",
]

SCHEMA_FILENAME = 'schema.yaml'
CONFIG_FILENAME = 'config.json'

def get_version():
    with open(CONFIG_FILENAME, 'r') as f:
        config = json.load(f)
    return config['packageVersion']

def remove_oneof(data):
    """ Removes oneOf key from a dict and recursively calls this function on
        other dict values.
    """
    if 'oneOf' in data:
        del data['oneOf']
    for key in data:
        if isinstance(data[key], dict):
            remove_oneof(data[key])
    return data

class NoAliasDumper(yaml.Dumper):
    def ignore_aliases(self, data):
        return True

def codegen():
    """ Fetches a schema from cloud.tator.io if one does not exist, then 
        use openapi-generator to generate openapi code from it.
    """
    # Retrieve schema if it does not exist.
    if not os.path.exists(SCHEMA_FILENAME):
        response = requests.get("https://cloud.tator.io/schema")
        assert response.status_code == 200
        with open(SCHEMA_FILENAME, 'wb') as f:
            f.write(response.content)

    # Remove any oneOf entries from the schema, as they are not handled
    # well by openapi generator.
    with open(SCHEMA_FILENAME, 'r') as f:
        schema = yaml.safe_load(f)
    schema = remove_oneof(schema)
    with open(SCHEMA_FILENAME, 'w') as f:
        yaml.dump(schema, f, Dumper=NoAliasDumper)

    # Get the git SHA ID.
    cmd = ['git', 'rev-parse', 'HEAD']
    git_rev = subprocess.check_output(cmd).strip().decode('utf-8')

    # Generate code using openapi generator docker image.
    pwd = os.path.dirname(os.path.abspath(__file__))
    cmd = [
        'docker', 'run', '--rm',
        '-v', f"{pwd}:/pwd",
        '-v', f"{pwd}/out:/out",
        'openapitools/openapi-generator-cli:v4.3.1', 'generate',
        '-c', f'/pwd/{CONFIG_FILENAME}',
        '-i', f'/pwd/{SCHEMA_FILENAME}',
        '-g', 'python',
        '-o', f'/out/tator-py-{git_rev}',
        '-t', '/pwd/templates',
    ]
    subprocess.run(cmd, check=True)

    # Remove the schema.
    os.remove(SCHEMA_FILENAME)

    # Copy relevant directories into openapi.
    out_dir = os.path.join(pwd, 'tator/openapi')
    os.makedirs(out_dir, exist_ok=True)
    for subpath in ['README.md', 'tator_openapi', 'docs']:
        src = f'{pwd}/out/tator-py-{git_rev}/{subpath}'
        dst = os.path.join(out_dir, f'{subpath}')
        if os.path.isfile(src):
            shutil.copy(src, dst)
        else:
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
    pwd = os.path.dirname(os.path.abspath(__file__))

    # need to delete from within docker
    cmd = [
        'docker', 'run', '--rm',
        '-v', f"{pwd}/out:/out",
         'openapitools/openapi-generator-cli:v4.3.1',
        'rm', '-fr',
        '/out/*'
    ]
    subprocess.run(cmd, check=True)

codegen()
setup(
    name="tator",
    version=get_version(),
    description="Python client for Tator",
    author="CVision AI, Inc.",
    author_email="info@cvisionai.com",
    url="https://github.com/cvisionai/tator-py",
    keywords=["OpenAPI", "OpenAPI-Generator", "Tator"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    package_data={"tator": ["tator/util/tator-symbol.png", "tator/util/tator-symbol.gif"]},
    include_package_data=True,
    long_description="""\
    Python client for Tator.
    """
)
