import logging
import os
import sys

import tator
from ._upload_file import _upload_file

logger = logging.getLogger(__name__)

def update_applet(
        host: str,
        token: str,
        applet_id:int,
        html_file: str=None,
        applet_name: str=None,
        categories: list=None,
        description: str=None) -> None:
    """ Updates an existing applet using the provided parameters

    :param host: Host URL
    :param token: User token used for connecting to the host
    :param project: Unique identifier of project associated with algorithm
    :param html_file: Local path to applet html file
    :param applet_name: Name of the applet
    :param categories: Optional categories the applet belongs to
    :param description: Optional applet description
    """

    # Create the interface
    tator_api = tator.get_api(host=host, token=token)
    applet = tator_api.get_applet(id=applet_id)
    project = applet.project
    update = {}

    if html_file is not None:
        # Upload the file
        for progress, upload_info in _upload_file(tator_api, project, path=html_file):
            pass
        upload_url = tator_api.get_download_info(project, {'keys': [upload_info.key]})[0].url
        logger.info("Applet HTML file uploaded")

        # Save the uploaded file using the save report endpoint
        spec = tator.models.GenericFileSpec(
            name=os.path.basename(html_file),
            upload_url=upload_url)
        response = tator_api.save_generic_file(project=project, generic_file_spec=spec)
        logger.info(response)
        logger.info("Applet HTML file saved to project")

        update["html_file"] = response.url

    if applet_name is not None:
        update["name"] = applet_name

    if categories is not None:
        update["categories"] = categories

    if description is not None:
        update["description"] = description

    response = tator_api.update_applet(id=applet_id, applet_spec=update)

    log_msg = f"Applet updated (response = {response})"
    logger.info(log_msg)
