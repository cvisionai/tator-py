
import logging
import os
import sys

import tator
from ._upload_file import _upload_file

logger = logging.getLogger(__name__)

def register_applet(
        host: str,
        token: str,
        project: int,
        html_file: str,
        applet_name: str,
        categories: list=[],
        description: str='') -> None:
    """ Registers a applet using the provided parameters

    This will upload the given html file, save it to tator, and the new
    server side URL will be used when registering the applet. This may change
    the filename of the uploaded file

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

    # With the applet file saved, register the applet
    spec = tator.models.Applet(
        name=applet_name,
        project=project,
        description=description,
        html_file=response.url,
        categories=categories)

    response = tator_api.register_applet(project=project, applet_spec=spec)

    log_msg = f"Applet registered with ID: {response.id}"
    logger.info(log_msg)
