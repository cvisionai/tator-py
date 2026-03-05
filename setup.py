import json
from setuptools import setup, find_packages

REQUIRES = [
    "Pillow >= 10.3.0",
    "progressbar2 >= 3.51.4",
    "psutil >= 5.9.5",
    "pyyaml >= 5.4",
    "requests >= 2.32.4",
]

CONFIG_FILENAME = 'config.json'

def get_version():
    with open(CONFIG_FILENAME, 'r') as f:
        config = json.load(f)
    return config['packageVersion']

setup(
    name="tator",
    version=get_version(),
    description="Python client for Tator",
    author="CVision AI, Inc.",
    author_email="info@cvisionai.com",
    url="https://github.com/cvisionai/tator-py",
    keywords=["OpenAPI", "Tator"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    package_data={"tator": ["tator/util/tator-symbol.png", "tator/util/tator-symbol.gif"]},
    include_package_data=True,
    long_description="""\
    Python client for Tator.
    """
)
