
import logging
import os
import sys

import tator
from ._upload_file import _upload_file

logger = logging.getLogger(__name__)

def register_algorithm(
    host: str,
    token: str,
    project: int,
    manifest: str,
    algorithm_name: str,
    files_per_job: int,
    categories: list=[],
    description: str='',
    cluster_id: int=None) -> None:
    """ Registers an algorithm argo workflow using the provided parameters

    This will upload the given manifest file, save it to tator, and the new
    server side URL will be used when registering the workflow. This may change
    the filename of the manifest file.

    Args:
        host: Host URL
        token: User token used for connecting to the host
        project: Unique identifier of project associated with algorithm
        manifest: Local path to argo workflow manifest file to upload, save,
            and register the algorithm with
        algorithm_name: Unique name of the workflow
        files_per_job: Number of media to process per workflow created
        description: Optional description of workflow
        cluster_id: Optional unique integer identifying the job cluster
    """

    # Create the interface
    tator_api = tator.get_api(host=host, token=token)
    user = tator_api.whoami()
    user_id = user.id

    # Upload the manifest file
    for progress, upload_info in _upload_file(tator_api, project, path=manifest):
        pass
    manifest_upload_url = tator_api.get_download_info(project, {'keys': [upload_info.key]})[0].url

    # Save the uploaded file using the save algorithm manifest endpoint
    spec = tator.models.AlgorithmManifestSpec(
        name=os.path.basename(manifest),
        upload_url=manifest_upload_url)
    response = tator_api.save_algorithm_manifest(project=project, algorithm_manifest_spec=spec)
            
    # Register the algorithm argo workflow
    spec = tator.models.Algorithm(
        name=algorithm_name,
        project=project,
        user=user_id,
        description=description,
        manifest=response.url,
        cluster=cluster_id,
        files_per_job=files_per_job,
        categories=categories)

    response = tator_api.register_algorithm(project=project, algorithm_spec=spec)

    log_msg = f"Algorithm registered with ID: {response.id}"
    logger.info(log_msg)
