import logging
import os
import shutil
import tempfile
import uuid
from textwrap import dedent

import pytest
import tator
from tator.util._upload_file import _upload_file

logger = logging.getLogger(__name__)

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

def _missing_upload_file(
        host: str,
        token: str,
        project: int) -> None:
    """ Test missing upload file for SaveGenericFile endpoint

    :param host: Project URL
    :param token: User token used for connecting to the host
    :param project: Unique identifier of test project
    """

    tator_api = tator.get_api(host=host, token=token)
    spec = tator.models.GenericFileSpec(name="test.html", upload_url="not_there")
    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        tator_api.save_generic_file(project=project, generic_file_spec=spec)

def _upload_test_html_file(
        host: str,
        token: str,
        project: int,
        html_file: str="test.html"):
    """ Uploads the provided manifest file

    :param host: Project URL
    :param token: User token used for connecting to the host
    :param project: Unique identifier of test project
    :param html_file: Local HTML file to be uploaded and saved
    :returns: Response from the save HTML file endpoint
    """

    # Setup the interface to tator
    tator_api = tator.get_api(host=host, token=token)

    # Create the temporary HTML file
    fd, local_file = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as file_handle:
            file_handle.write(_create_html_file_str())

        # Upload the file
        logger.info(f"Created temporary HTML file: {local_file}")
        for progress, upload_info in _upload_file(tator_api, project, local_file):
            logger.info(f"Upload progress: {progress}%")
        url = tator_api.get_download_info(project, {'keys': [upload_info.key]})[0].url

        # Save the uploaded file to the project using the save html endpoint
        spec = tator.models.GenericFileSpec(name=html_file, upload_url=url)
        response = tator_api.save_generic_file(project=project, generic_file_spec=spec)

    finally:
        os.remove(local_file)

    return response

def test_save_html_file(
        host: str,
        token: str,
        project: int) -> None:
    """ Unit test for the SaveGenericFile endpoint

    Unit testing of the save generic file endpoint involvest the following:
    - Provide something where the upload file doesn't exist
    - Upload two of the same files (have the same name, but will result in two separate files)

    :param host: Project URL
    :param token: User token used for connecting to the host
    :param project: Unique identifier of test project
    """

    _missing_upload_file(host=host, token=token, project=project)

    response_1 = _upload_test_html_file(
        host=host, token=token, project=project, html_file='test_nodupe.html')
    assert os.path.basename(response_1.url) != "test_nodupe.html"
    url_1 = os.path.basename(response_1.url)
    response_2 = _upload_test_html_file(
        host=host, token=token, project=project, html_file='test_nodupe.html')
    assert os.path.basename(response_2.url) != "test_nodupe.html"
    url_2 = os.path.basename(response_2.url)
    assert url_1 != url_2

def test_dashboard_endpoint(host: str, token: str, project: int) -> None:
    """ Unit tests for the dashboard endpoint

    :param host: Project URL
    :param token: User token used for connecting to the host
    :param project: Unique identifier of test project
    """

    tator_api = tator.get_api(host=host, token=token)

    # Test creating dashboards
    response = _upload_test_html_file(host=host, token=token, project=project)
    spec = tator.models.Applet(
        name="Test Dashboard 1",
        project=project,
        description="",
        html_file=response.url,
        categories=[])

    response = tator_api.register_applet(project=project, applet_spec=spec)
    dashboard = tator_api.get_applet(id=response.id)
    assert dashboard.name == spec.name
    assert dashboard.project == spec.project
    assert dashboard.description == spec.description
    assert dashboard.categories == spec.categories

    response = _upload_test_html_file(host=host, token=token, project=project)
    spec = tator.models.Applet(
        name="Test Dashboard 2",
        project=project,
        description="Test Dashboard 2",
        html_file=response.url,
        categories=["category"])

    response = tator_api.register_applet(project=project, applet_spec=spec)
    dashboard = tator_api.get_applet(id=response.id)
    assert dashboard.name == spec.name
    assert dashboard.project == spec.project
    assert dashboard.description == spec.description
    assert dashboard.categories == spec.categories

    response = _upload_test_html_file(host=host, token=token, project=project)
    spec = tator.models.Applet(
        name="Test Dashboard 3",
        project=project,
        description="Test Dashboard 3",
        html_file=response.url,
        categories=["test1", "test2"])

    response = tator_api.register_applet(project=project, applet_spec=spec)
    dashboard = tator_api.get_applet(id=response.id)
    assert dashboard.name == spec.name
    assert dashboard.project == spec.project
    assert dashboard.description == spec.description
    assert dashboard.categories == spec.categories

    # Test retrieving the dashboard list
    dashboards = tator_api.get_applet_list(project=project)
    assert len(dashboards) == 3

    # Test patching a dashboard's fields
    response = _upload_test_html_file(host=host, token=token, project=project)
    html_url = response.url
    dashboard_id = dashboard.id
    original = tator_api.get_applet(id=dashboard.id)
    update = {
      "name": "Another name",
      "description": "Another description",
      "categories": ["a","b","c","d"],
      "html_file": html_url}
    tator_api.update_applet(id=dashboard_id, applet_spec=update)
    dashboard = tator_api.get_applet(id=dashboard_id)
    assert dashboard.name == update["name"]
    assert dashboard.description == update["description"]
    assert dashboard.categories == update["categories"]
    assert dashboard.html_file != original.html_file

    # Test deleting a dashboard
    tator_api.delete_applet(id=dashboard.id)
    dashboards = tator_api.get_applet_list(project=project)
    assert len(dashboards) == 2
