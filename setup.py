from setuptools import setup, find_packages  # noqa: H301
import tator

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil",
            "requests", "tuspy"]

setup(
    name="tator",
    version=tator.__version__,
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
