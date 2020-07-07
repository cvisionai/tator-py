import logging
import os
import shutil
import tempfile
from textwrap import dedent

from tusclient.client import TusClient

import tator
from tator.util.upload_file import upload_file

logger = logging.getLogger(__name__)

def _create_valid_yaml_file_str() -> str:
    """ Returns a string that can be written out to a .yaml file that is valid syntax
    """

    return dedent("""\
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: hello-world-
spec:
  entrypoint: pipeline
  ttlStrategy:
    secondsAfterCompletion: 300 # Time to live after workflow is completed, replaces ttlSecondsAfterFinished
    secondsAfterSuccess: 300    # Time to live after workflow is successful
    secondsAfterFailure: 3600   # Time to live after workflow fails
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
    - - name: hello
        template: hello
    - - name: goodbye
        template: goodbye
  - name: hello
    script:
      image: localhost:5000/hello_world
      resources:
        limits:
          cpu: 1000m
          memory: 500Mi
      command: [python]
      args: [/hello.py]
  - name: goodbye
    script:
      image: localhost:5000/hello_world
      resources:
        limits:
          cpu: 1000m
          memory: 500Mi
      command: [python]
      args: [/goodbye.py]
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
        break_yaml_file: bool=False) -> str:
    """ Uploads the provided manifest file

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project

    Returns:
        Manifest file URL
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

    response_1 = _upload_test_algorithm_manifest(host=host, token=token, project=project, manifest_name='test.yaml')
    assert os.path.basename(response_1.server_url) == 'test.yaml'

    response_2 = _upload_test_algorithm_manifest(host=host, token=token, project=project, manifest_name='test.yaml')
    assert os.path.basename(response_2.server_url) == 'test_0.yaml'

'''
def test_register_algorithm(
        host: str,
        token: str,
        project: int) -> None:
    """ Unit test for the ReigsterAlgorithm endpoint

    Unit testing of the algortihm registration endpoint involves the following:
    - Create a request body that has missing pieces
    - Create a request body that's fine, but has bad syntax for the .yaml file
    - Create a request body for a .yaml file that doesn't exist

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project

    """
'''