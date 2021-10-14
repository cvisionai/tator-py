
import logging
import os
import sys

import tator
from ._upload_file import _upload_file

logger = logging.getLogger(__name__)

def update_dashboard(
        host: str,
        token: str,
        dashboard_id:int,
        html_file: str=None,
        dashboard_name: str=None,
        categories: list=None,
        description: str=None) -> None:
    """ Updates an existing dashboard using the provided parameters

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
    dashboard = tator_api.get_dashboard(id=dashboard_id)
    project = dashboard.project
    update = {}

    if html_file is not None:
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

        update["html_file"] = response.url

    if dashboard_name is not None:
        update["name"] = dashboard_name

    if categories is not None:
        update["categories"] = categories

    if description is not None:
        update["description"] = description

    response = tator_api.update_dashboard(id=dashboard_id, dashboard_spec=update)

    log_msg = f"Dashboard updated (response = {response})"
    logger.info(log_msg)
