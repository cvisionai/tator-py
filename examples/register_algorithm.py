""" This examples uploads an algorithm manifest file and registers an algorithm workflow
"""

import logging
import os
import sys

import tator
from tator.transcode.upload import upload_file

logger = logging.getLogger(__name__)

def register_algorithm(
    host: str,
    token: str,
    project: int,
    manifest: str,
    algorithm_name: str,
    files_per_job: int,
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
    manifest_upload_url = upload_file(path=manifest, host=host)

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
        files_per_job=files_per_job)

    response = tator_api.register_algorithm(project=project, algorithm_spec=spec)

    log_msg = f"Algorithm registered with ID: {response.id}"
    logger.info(log_msg)

def main() -> None:
    """ Main routine of this script
    """

    # Set the arguments and grab them
    parser = tator.get_parser()
    parser.add_argument(
        '--project',
        help='Unique project ID associated with the argo workflow',
        required=True,
        type=int)
    parser.add_argument(
        '--manifest',
        help='Path to the argo manifest .yaml file to be uploaded',
        required=True)
    parser.add_argument(
        '--algorithm_name',
        help='Unique name of algorithm argo workflow',
        required=True)
    parser.add_argument(
        '--files_per_job',
        help='Number of files to process per job batch',
        type=int)
    parser.add_argument(
        '--description',
        help='Description of algorithm workflow')
    parser.add_argument(
        '--cluster_id',
        help='Cluster ID to run the workflow on',
        type=int)
    args = parser.parse_args()

    register_algorithm(
        host=args.host,
        token=args.token,
        project=args.project,
        manifest=args.manifest,
        algorithm_name=args.algorithm_name,
        files_per_job=args.files_per_job,
        description=args.description,
        cluster_id=args.cluster_id)

if __name__ == "__main__":
    main()