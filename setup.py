import os
import subprocess
import shutil
import urllib.request

from setuptools import setup, find_packages
import requests
import yaml
import json

REQUIRES = [
    "certifi >= 14.05.14",
    "Pillow >= 10.3.0",
    "progressbar2 >= 3.51.4",
    "psutil >= 5.9.5",
    "python-dateutil >= 2.5.3",
    "pyyaml >= 5.4",
    "requests >= 2.32.4",
    "six >= 1.10",
    "urllib3 >= 2.5.0",
]

SCHEMA_FILENAME = 'schema.yaml'
CONFIG_FILENAME = 'config.json'
OPENAPI_GENERATOR_VERSION = '4.3.1'
OPENAPI_GENERATOR_JAR = f'openapi-generator-cli-{OPENAPI_GENERATOR_VERSION}.jar'
OPENAPI_GENERATOR_URL = f'https://tator-ci.s3.us-east-1.amazonaws.com/{OPENAPI_GENERATOR_JAR}'

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

def ensure_java():
    """Check if Java is installed, if not, provide instructions."""
    try:
        result = subprocess.run(['java', '-version'], capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError("Java is not installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("ERROR: Java is required to run OpenAPI Generator")
        print("Please install Java 8 or later:")
        print("  Ubuntu/Debian: sudo apt-get install openjdk-11-jre")
        print("  macOS: brew install openjdk@11")
        print("  Or download from: https://adoptium.net/")
        return False

def download_openapi_generator():
    """Download the OpenAPI Generator JAR if it doesn't exist."""
    if not os.path.exists(OPENAPI_GENERATOR_JAR):
        print(f"Downloading OpenAPI Generator {OPENAPI_GENERATOR_VERSION}...")
        urllib.request.urlretrieve(OPENAPI_GENERATOR_URL, OPENAPI_GENERATOR_JAR)
        print(f"Downloaded {OPENAPI_GENERATOR_JAR}")

def codegen():
    """ Fetches a schema from cloud.tator.io if one does not exist, then 
        use openapi-generator to generate openapi code from it.
    """
    # Check Java is available
    if not ensure_java():
        raise RuntimeError("Java is required but not found")
    
    # Download OpenAPI Generator JAR if needed
    pwd = os.path.dirname(os.path.abspath(__file__))
    jar_path = os.path.join(pwd, OPENAPI_GENERATOR_JAR)
    if not os.path.exists(jar_path):
        print(f"Downloading OpenAPI Generator {OPENAPI_GENERATOR_VERSION}...")
        urllib.request.urlretrieve(OPENAPI_GENERATOR_URL, jar_path)
        print(f"Downloaded {OPENAPI_GENERATOR_JAR}")
    
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

    # Generate code using OpenAPI Generator JAR (works natively on all architectures)
    # Use temp directory to avoid permission issues
    import tempfile
    temp_out = tempfile.mkdtemp(prefix='tator-py-')
    out_dir = os.path.join(temp_out, f'tator-py-{git_rev}')
    
    # Ensure output directory exists
    os.makedirs(out_dir, exist_ok=True)
    
    cmd = [
        'java', '-jar', jar_path, 'generate',
        '-c', CONFIG_FILENAME,
        '-i', SCHEMA_FILENAME,
        '-g', 'python',
        '-o', out_dir,
        '-t', os.path.join(pwd, 'templates'),
    ]
    
    import platform
    print(f"Running OpenAPI Generator on {platform.machine()} architecture...")
    subprocess.run(cmd, check=True, cwd=pwd)

    # Remove the schema.
    os.remove(SCHEMA_FILENAME)

    # Copy relevant directories into openapi.
    openapi_dir = os.path.join(pwd, 'tator/openapi')
    os.makedirs(openapi_dir, exist_ok=True)
    for subpath in ['README.md', 'tator_openapi', 'docs']:
        src = os.path.join(out_dir, subpath)
        dst = os.path.join(openapi_dir, subpath)
        if os.path.isfile(src):
            shutil.copy(src, dst)
        else:
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
    
    # Clean up temp directory
    shutil.rmtree(temp_out)

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
