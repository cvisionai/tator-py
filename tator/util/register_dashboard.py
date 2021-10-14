
import logging
import os
import sys

import tator
from ._upload_file import _upload_file

logger = logging.getLogger(__name__)

def register_dashboard(
        host: str,
        token: str,
        project: int,
        html_file: str,
        dashboard_name: str,
        categories: list=[],
        description: str='') -> None:
    """ Registers a dashboard using the provided parameters

    This will upload the given html file, save it to tator, and the new
    server side URL will be used when registering the dashboard. This may change
    the filename of the uploaded file

    :param host: Host URL
    :param token: User token used for connecting to the host
    :param project: Unique identifier of project associated with algorithm
    :param html_file: Local path to dashboard html file
    :param dashboard_name: Name of the dashboard
    :param categories: Optional categories the dashboard belongs to
    :param description: Optional dashboard description
    """

    # Create the interface
    tator_api = tator.get_api(host=host, token=token)

    # Upload the file
    for progress, upload_info in _upload_file(tator_api, project, path=html_file):
        pass
    upload_url = tator_api.get_download_info(project, {'keys': [upload_info.key]})[0].url
    logger.info("Dashboard HTML file uploaded")

    # Save the uploaded file using the save report endpoint
    spec = tator.models.HTMLFileSpec(
        name=os.path.basename(html_file),
        upload_url=upload_url)
    response = tator_api.save_html_file(project=project, html_file_spec=spec)
    logger.info(response)
    logger.info("Dashboard HTML file saved to project")

    # With the dashboard file saved, register the dashboard
    spec = tator.models.Dashboard(
        name=dashboard_name,
        project=project,
        description=description,
        html_file=response.url,
        categories=categories)

    response = tator_api.register_dashboard(project=project, dashboard_spec=spec)

    log_msg = f"Dashboard registered with ID: {response.id}"
    logger.info(log_msg)
