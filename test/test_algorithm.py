import logging
import os
import shutil
import tempfile
from textwrap import dedent

from tusclient.client import TusClient

import tator

logger = logging.getLogger(__name__)

def _create_valid_yaml_file_str() -> str:
    """ Returns a string that can be written out to a .yaml file that is valid syntax
    """

    return dedent("""\
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: find-edges-
spec:
  entrypoint: pipeline
  ttlSecondsAfterFinished: 30
  volumeClaimTemplates:
  - metadata:
      name: workdir
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: nfs-client
      resources:
        requests:
          storage: 100Mi
  templates:
  - name: pipeline
    steps:
    - - name: setup
        template: setup
    - - name: find-edges
        template: find-edges
    - - name: teardown
        template: teardown
  - name: setup
    script:
      image: localhost:5000/tator_algo_marshal
      resources:
        limits:
          cpu: 250m
          memory: 100Mi
      env:
      - name: TATOR_MEDIA_IDS
        value: "{{workflow.parameters.media_ids}}"
      - name: TATOR_API_SERVICE
        value: "{{workflow.parameters.rest_url}}"
      - name: TATOR_AUTH_TOKEN
        value: "{{workflow.parameters.rest_token}}"
      - name: TATOR_PROJECT_ID
        value: "{{workflow.parameters.project_id}}"
      volumeMounts:
      - name: workdir
        mountPath: /work
      command: [python]
      source: |
        #!/usr/bin/env python

        import os
        import logging
        import pytator
        import time

        log = logging.getLogger(__name__)

        if __name__ == '__main__':

            # Grab necessary environment variables.
            media_ids = os.getenv('TATOR_MEDIA_IDS')
            rest_svc = os.getenv('TATOR_API_SERVICE')
            token = os.getenv('TATOR_AUTH_TOKEN')
            project = os.getenv('TATOR_PROJECT_ID')
            work_dir = '/work'

            # Iterate through media IDs.
            tator = pytator.Tator(rest_svc, token, project)
            medias = tator.Media
            for media_id in media_ids.split(','):

                # Get the media objects.
                media = medias.byId(media_id)
                print(f"media = {media}, media_id = {media_id}")
                time.sleep(2)
                # Download media to working directory.
                fname = media['file'].split('/')[-1]
                out_path = os.path.join(work_dir, fname)
                medias.downloadFile(media, out_path)
  - name: find-edges
    script:
      image: localhost:5000/find_edges
      resources:
        limits:
          cpu: 1000m
          memory: 500Mi
      env:
      - name: TATOR_MEDIA_IDS
        value: "{{workflow.parameters.media_ids}}"
      - name: TATOR_API_SERVICE
        value: "{{workflow.parameters.rest_url}}"
      - name: TATOR_AUTH_TOKEN
        value: "{{workflow.parameters.rest_token}}"
      - name: TATOR_PROJECT_ID
        value: "{{workflow.parameters.project_id}}"
      - name: TATOR_WORK_DIR
        value: /work
      volumeMounts:
      - name: workdir
        mountPath: /work
      command: [python]
      args: [/find_edges.py]
  - name: teardown
    script:
      image: localhost:5000/tator_algo_marshal
      resources:
        limits:
          cpu: 250m
          memory: 100Mi
      env:
      - name: TATOR_MEDIA_IDS
        value: "{{workflow.parameters.media_ids}}"
      - name: TATOR_API_SERVICE
        value: "{{workflow.parameters.rest_url}}"
      - name: TATOR_AUTH_TOKEN
        value: "{{workflow.parameters.rest_token}}"
      - name: TATOR_PROJECT_ID
        value: "{{workflow.parameters.project_id}}"
      - name: TATOR_TUS_SERVICE
        value: "{{workflow.parameters.tus_url}}"
      volumeMounts:
      - name: workdir
        mountPath: /work
      command: [python]
      source: |
        #!/usr/bin/env python

        import os
        import subprocess

        if __name__ == '__main__':

            # Grab necessary environment variables.
            tus_svc = os.getenv('TATOR_TUS_SERVICE')
            rest_svc = os.getenv('TATOR_API_SERVICE')
            token = os.getenv('TATOR_AUTH_TOKEN')
            project_id = os.getenv('TATOR_PROJECT_ID')
            work_dir = '/work'

            # Use ingestor to upload files.
            obj = subprocess.Popen([
                "python",
                "ingestor.py",
                "media",
                "--directory", work_dir,
                "--typeId", "59",
                "--url", rest_svc,
                "--token", token,
                "--project", project_id,
                "--extension", "jpg",
            ], cwd='/')
            obj.wait()
        """)

def _missing_upload_file(
        host: str,
        token: str,
        project: int) -> None:
    """ Test missing upload file for SaveAlgorithManifest endpoint

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project
    """

    tator_api = tator.get_api(host=host, token=token)

    try:
        caught_exception = False
        spec = tator.models.AlgorithmManifestSpec(name='test.yaml', upload_url='not_there')
        response = tator_api.save_algorithm_manifest(name=basename, algorithm_manifest_spec=spec)
    except:
        caught_exception = True

    assert caught_exception

def _upload_test_algorithm_manifest(
        host: str,
        token: str,
        project: int,
        manifest_name: str='test_manifest.yaml',
        break_yaml_file: bool=False):
    """ Uploads the provided manifest file

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project

    Returns:
        Response
    """

    # Setup the interface to tator
    tator_api = tator.get_api(host=host, token=token)

    # Create the temporary manifest file
    local_yaml_file = 'test.yaml'
    with open(local_yaml_file, 'w') as file_handle:
        file_handle.write(_create_valid_yaml_file_str())

        if break_yaml_file:
            file_handle.write('RANDOM_TEXT!!!!!')

    # Upload the manifest file with tus first
    logger.info(f"Created temporary manifest file: {local_yaml_file}")
    for progress, url in tator.util.upload_file(api=tator_api, project=project, path=local_yaml_file):
        logger.info(f'Manifest file upload progress: {progress}')

    # Save the uploaded file using the save algorithm manifest endpoint
    spec = tator.models.AlgorithmManifestSpec(name=manifest_name, upload_url=url)
    response = tator_api.save_algorithm_manifest(project=project, algorithm_manifest_spec=spec)

    return response


def test_save_algorithm_manifest(
        host: str,
        token: str,
        project: int) -> None:
    """ Unit test for the SaveAlgorithManifest endpoint

    Unit testing of the save algorithm endpoint involvest the following:
    - Provide something where the upload file doesn't exist
    - Upload two of the same files (have the same name, but will result in two separate files)

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project

    """

    _missing_upload_file(host=host, token=token, project=project)

    response_1 = _upload_test_algorithm_manifest(
        host=host, token=token, project=project, manifest_name='test.yaml')
    assert os.path.basename(response_1.url) == 'test.yaml'

    response_2 = _upload_test_algorithm_manifest(
        host=host, token=token, project=project, manifest_name='test.yaml')
    assert os.path.basename(response_2.url) == 'test_0.yaml'

def test_register_algorithm(
        host: str,
        token: str,
        project: int) -> None:
    """ Unit test for the ReigsterAlgorithm endpoint

    Unit testing of the algortihm registration endpoint involves the following:
    - Create a request body that has missing pieces
    - Create a request body that's fine, but has bad syntax for the .yaml file
    - Create a request body for a .yaml file that doesn't exist
    - Normal request body

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project

    """

    # Get the user ID
    tator_api = tator.get_api(host=host, token=token)
    user = tator_api.whoami()
    user_id = user.id

    # Create a request body that has missing pieces

    # Create a request body that's fine but has bad syntax for the .yaml file
    caught_exception = False
    try:
        response = _upload_test_algorithm_manifest(
            host=host, token=token, project=project, manifest_name='test.yaml', break_yaml_file=True)

        spec = tator.models.Algorithm(
            name='test_algo',
            project=project,
            user=user_id,
            description='test_description',
            manifest=response.url,
            cluster=None,
            files_per_job=1)

        response = tator_api.register_algorithm(project=project, algorithm_spec=spec)
            
    except:
        caught_exception = True

    assert caught_exception

    # Create a request body for a .yaml file that doesn't exist
    caught_exception = False
    try:
        spec = tator.models.Algorithm(
            name='test_algo',
            project=project,
            user=user_id,
            description='test_description',
            manifest='ghost',
            cluster=None,
            files_per_job=1)

        response = tator_api.register_algorithm(project=project, algorithm_spec=spec)
            
    except:
        caught_exception = True

    assert caught_exception

    # Create a normal registration
    response = _upload_test_algorithm_manifest(
        host=host, token=token, project=project, manifest_name='test.yaml')

    spec = tator.models.Algorithm(
        name='test_algo',
        project=project,
        user=user_id,
        description='test_description',
        manifest=response.url,
        cluster=None,
        files_per_job=1)

    response = tator_api.register_algorithm(project=project, algorithm_spec=spec)

    # Then attempt to delete it
    _ = tator_api.delete_algorithm(id=response.id)

def test_register_algorithm_with_missing_fields(
        host: str,
        token: str,
        project: int) -> None:
    """
    """

    NAME = 'test_algorithm_workflow'
    DESCRIPTION = 'description'
    CLUSTER = 1
    FILES_PER_JOB = 1
    
    # Setup the interface to tator and get the user ID
    tator_api = tator.get_api(host=host, token=token)
    user = tator_api.whoami()
    user_id = user.id

    # Upload a manifest file
    response = _upload_test_algorithm_manifest(
        host=host, token=token, project=project, manifest_name='test.yaml')
    manifest_url = response.url

    # Missing name field
    caught_exception = False
    try:
        spec = tator.models.Algorithm(
            project=project,
            user=user_id,
            description=DESCRIPTION,
            manifest=manifest_url,
            cluster=CLUSTER,
            files_per_job=FILES_PER_JOB)

        response = tator_api.register_algorithm(project=project, algorithm_spec=spec)
    except:
        caught_exception = True

    assert caught_exception

    # Missing user field
    caught_exception = False
    try:
        spec = tator.models.Algorithm(
            name=NAME,
            project=project,
            description=DESCRIPTION,
            manifest=manifest_url,
            cluster=CLUSTER,
            files_per_job=FILES_PER_JOB)

        response = tator_api.register_algorithm(project=project, algorithm_spec=spec)
    except:
        caught_exception = True

    assert caught_exception

    # Missing description field
    caught_exception = False
    try:
        spec = tator.models.Algorithm(
            name=NAME,
            project=project,
            user=user_id,
            description=DESCRIPTION,
            manifest=manifest_url,
            cluster=CLUSTER,
            files_per_job=FILES_PER_JOB)

        response = tator_api.register_algorithm(project=project, algorithm_spec=spec)
    except:
        caught_exception = True

    assert caught_exception

    # Missing manifest
    caught_exception = False
    try:
        spec = tator.models.Algorithm(
            name=NAME,
            project=project,
            user=user_id,
            description=DESCRIPTION,
            cluster=CLUSTER,
            files_per_job=FILES_PER_JOB)

        response = tator_api.register_algorithm(project=project, algorithm_spec=spec)
    except:
        caught_exception = True

    assert caught_exception

    # Missing fields per job
    caught_exception = False
    try:
        spec = tator.models.Algorithm(
            name=NAME,
            project=project,
            user=user_id,
            description=DESCRIPTION,
            manifest=manifest_url,
            cluster=CLUSTER)

        response = tator_api.register_algorithm(project=project, algorithm_spec=spec)
    except:
        caught_exception = True

    assert caught_exception