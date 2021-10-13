import logging
import os
import sys

import tator
from ._upload_file import _upload_file

logger = logging.getLogger(__name__)

def register_report(
        host: str,
        token: str,
        project: int,
        name: str,
        html_file: str,
        description: str) -> None:
    """
    """

    # Connect to the Tator instance
    tator_api = tator.get_api(host=host, token=token)
    user = tator_api.whoami()
    user_id = user.id

    # Upload the report file
    for progress, upload_info in _upload_file(tator_api, project, path=html_file):
        pass
    upload_url = tator_api.get_download_info(project, {'keys': [upload_info.key]})[0].url
    logger.info("Report file uploaded")

    # Save the uploaded file using the save report endpoint
    spec = tator.models.HTMLFileSpec(
        name=os.path.basename(html_file),
        upload_url=upload_url)
    response = tator_api.save_html_file(project=project, html_file_spec=spec)
    logger.info(response)
    logger.info("Report file saved to project location")

    # With the report file saved, finally create the report entry
    spec = {
        "name": name,
        "project": project,
        "description": description,
        "html_file": response.url
    }
    response = tator_api.register_report(project=project, report_spec=spec)
    logger.info(f"Report file reigstered with ID: {response.id}")