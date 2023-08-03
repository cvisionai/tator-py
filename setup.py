import os
import subprocess
import shutil

from setuptools import setup, find_packages  # noqa: H301
import requests
import yaml
import json

REQUIRES = ["urllib3 >= 1.26", "six >= 1.10", "certifi", "python-dateutil",
            "requests >= 2.25", "pyyaml", "progressbar2", "pillow", "psutil"]

SCHEMA_FILENAME = 'schema.yaml'
CONFIG_FILENAME = 'config.json'
OPENAPI_GENERATOR_VERSION = "v6.6.0"

def get_version():
    with open(CONFIG_FILENAME, 'r') as f:
        config = json.load(f)
    return config['packageVersion']

class NoAliasDumper(yaml.Dumper):
    def ignore_aliases(self, _):
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

    # Get the git SHA ID.
    cmd = ['git', 'rev-parse', 'HEAD']
    git_rev = subprocess.check_output(cmd).strip().decode('utf-8')

    # Generate code using openapi generator docker image.
    pwd = os.path.dirname(os.path.abspath(__file__))
    cmd = [
        'docker', 'run', '--rm',
        '-v', f"{pwd}:/pwd",
        '-v', f"{pwd}/out:/out",
        f'openapitools/openapi-generator-cli:{OPENAPI_GENERATOR_VERSION}', 'generate',
        '-c', f'/pwd/{CONFIG_FILENAME}',
        '-i', f'/pwd/{SCHEMA_FILENAME}',
        '-g', 'python-nextgen',
        '-o', f'/out/tator-py-{git_rev}',
        '-t', '/pwd/templates',
        '--additional-properties=library=asyncio',
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

    # need to delete from within docker
    cmd = [
        'docker', 'run', '--rm',
        '-v', f"{pwd}/out:/out",
         f'openapitools/openapi-generator-cli:{OPENAPI_GENERATOR_VERSION}',
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
    include_package_data=True,
    long_description="""\
    Python client for Tator.
    """
)
