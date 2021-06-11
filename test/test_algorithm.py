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

def _create_yaml_file_str() -> str:
    """ Creates a argo manifest file used by the unit tests in this file
    """

    return dedent("""\
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: test-algorithm-launcher-
spec:
  entrypoint: pipeline
  ttlStrategy:
    secondsAfterCompletion: 300 # Time to live after workflow is completed, replaces ttlSecondsAfterFinished
    secondsAfterSuccess: 300 # Time to live after workflow is successful
    secondsAfterFailure: 600 # Time to live after workflow fails
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
    - - name: test
        template: test
  - name: test
    script:
      image: cvisionai/tator_transcoder #localhost:5000/tator_transcoder
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
        value: "/work"
      resources:
        limits:
          cpu: 1000m
          memory: 500Mi
      volumeMounts:
      - name: workdir
        mountPath: /work
      command: [python3]
      source: |
        #!/usr/bin/env python3

        import os
        import tator

        def main():
            host = os.path.dirname(os.getenv('TATOR_API_SERVICE'))
            token = os.getenv('TATOR_AUTH_TOKEN')
            project = int(os.getenv('TATOR_PROJECT_ID'))
            media_ids = os.getenv('TATOR_MEDIA_IDS')
            media_ids = [int(m) for m in media_ids.split(',')]

            tator_api = tator.get_api(host=host, token=token)

            print(f'{host} {token} {project} {media_ids}')

            for media in media_ids:
                name = f'test_media_{media}'
                dq = f'test_media_id:{media}'
                spec = tator.models.AnalysisSpec(name=name, data_query=dq)
                _ = tator_api.create_analysis(project=project, analysis_spec=spec)

        if __name__ == '__main__':
            main()
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
    spec = tator.models.AlgorithmManifestSpec(name='test.yaml', upload_url='not_there')
    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        tator_api.save_algorithm_manifest(project = project, algorithm_manifest_spec=spec)

def _upload_test_algorithm_manifest(
        host: str,
        token: str,
        project: int,
        manifest_name: str='test_manifest.yaml',
        break_yaml_file: bool=False) -> tator.models.AlgorithmManifest:
    """ Uploads the provided manifest file

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project
        manifest_name: Local argo workflow manifest file to be uploaded and saved
        break_yaml_file: True if a syntax error is added to the given yaml.
            False leaves the yaml file untouched.

    Returns:
        Response from the save algorithm manifest endpoint
    """

    # Setup the interface to tator
    tator_api = tator.get_api(host=host, token=token)

    # Create the temporary manifest file
    fd, local_yaml_file = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as file_handle:
            file_handle.write(_create_yaml_file_str())

            if break_yaml_file:
                file_handle.write('RANDOM_TEXT!!!!!')

        # Upload the manifest file with tus first
        logger.info(f"Created temporary manifest file: {local_yaml_file}")
        for progress, upload_info in _upload_file(tator_api, project, local_yaml_file):
            logger.info(f"Upload progress: {progress}%")
        url = tator_api.get_download_info(project, {'keys': [upload_info.key]})[0].url

        # Save the uploaded file using the save algorithm manifest endpoint
        spec = tator.models.AlgorithmManifestSpec(name=manifest_name, upload_url=url)
        response = tator_api.save_algorithm_manifest(project=project, algorithm_manifest_spec=spec)

    finally:
        os.remove(local_yaml_file)

    return response

def test_save_algorithm_manifest(
        host: str,
        token: str,
        project: int) -> None:
    """ Unit test for the SaveAlgorithmManifest endpoint

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
        host=host, token=token, project=project, manifest_name='test_nodupe.yaml')
    assert os.path.basename(response_1.url) == 'test_nodupe.yaml'

    response_2 = _upload_test_algorithm_manifest(
        host=host, token=token, project=project, manifest_name='test_nodupe.yaml')
    assert os.path.basename(response_2.url) == 'test_nodupe_0.yaml'

def test_register_algorithm(host: str, token: str, project: int, algo_project: int) -> None:
    """ Unit test for the RegisterAlgorithm endpoint

    Unit testing of the algorithm registration endpoint involves the following:
    - Create a request body that's fine, but has bad syntax for the .yaml file
    - Create a request body for a .yaml file that doesn't exist
    - Normal request body

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project
    """

    # Create a randomized unique algorithm name (that we'll end up deleting later anyway)
    ALGO_NAME = str(uuid.uuid1())

    # Get the user ID
    tator_api = tator.get_api(host=host, token=token)
    user = tator_api.whoami()
    user_id = user.id

    # Create a request body that's fine but has bad syntax for the .yaml file
    response = _upload_test_algorithm_manifest(
        host=host, token=token, project=project, manifest_name='test.yaml', break_yaml_file=True)

    spec = tator.models.Algorithm(
        name=ALGO_NAME,
        project=project,
        user=user_id,
        description='test_description',
        manifest=response.url,
        cluster=None,
        files_per_job=1)

    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        response = tator_api.register_algorithm(project=project, algorithm_spec=spec)

    # Create a request body for a .yaml file that doesn't exist
    spec = tator.models.Algorithm(
        name=ALGO_NAME,
        project=project,
        user=user_id,
        description='test_description',
        manifest='ghost',
        cluster=None,
        files_per_job=1)

    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        response = tator_api.register_algorithm(project=project, algorithm_spec=spec)

    # Create a normal algorithm workflow
    response = _upload_test_algorithm_manifest(
        host=host, token=token, project=project, manifest_name='test.yaml')

    manifest_url = response.url

    spec = tator.models.Algorithm(
        name=ALGO_NAME,
        project=project,
        user=user_id,
        description='test_description',
        manifest=manifest_url,
        cluster=None,
        files_per_job=1,
        categories=['category1, category2, category3'],
        parameters=[{'name':'param1', 'value':'bool'}])

    response = tator_api.register_algorithm(project=project, algorithm_spec=spec)

    # Get the algorithm info
    algorithm_id = response.id
    algorithm_info = tator_api.get_algorithm(id=algorithm_id)
    spec.id = algorithm_id
    assert algorithm_info == spec

    # Try to register a second algorithm with the same name
    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        tator_api.register_algorithm(project=project, algorithm_spec=spec)

    # Attempt to patch the algorithm info and make sure it has been updated
    # Note: the cluster field is ignored in the patch operation
    spec = tator.models.Algorithm(
        name=str(uuid.uuid1()),
        project=project,
        user=user_id,
        description='new_test_description',
        manifest='coolfile.yaml',
        files_per_job=2,
        categories=['categoryA, categoryB'],
        parameters=[{'name': 'paramA', 'value':'int'}, {'name':'paramB', 'value':'string'}])
    response = tator_api.update_algorithm(id=algorithm_id, algorithm_spec=spec)
    algorithm_info = tator_api.get_algorithm(id=algorithm_id)
    spec.id = algorithm_id
    assert algorithm_info == spec

    # Create another algorithm workflow and verify retrieving both algorithm objects
    # using the get list method
    algorithm_ids = [algorithm_id]

    new_spec = tator.models.Algorithm(
        name=str(uuid.uuid1()),
        project=project,
        user=user_id,
        description='test_description',
        manifest=manifest_url,
        cluster=None,
        files_per_job=1)

    response = tator_api.register_algorithm(project=project, algorithm_spec=new_spec)

    new_spec.id = response.id
    algorithm_ids.append(new_spec.id)
    spec_list = [spec, new_spec]
    algorithm_list = tator_api.get_algorithm_list(project=project)

    for alg in algorithm_list:
        found_match = False
        for spec in spec_list:
            if spec == alg:
                found_match = True
                break

        assert found_match

    # Register algorithm with the same name for a different project
    response = _upload_test_algorithm_manifest(
        host=host, token=token, project=algo_project, manifest_name='test.yaml')

    manifest_url = response.url

    spec = tator.models.Algorithm(
        name=ALGO_NAME,
        project=algo_project,
        user=user_id,
        description='test_description',
        manifest=manifest_url,
        cluster=None,
        files_per_job=1)

    response = tator_api.register_algorithm(project=algo_project, algorithm_spec=spec)

    # Finally delete all the algorithms
    tator_api.delete_algorithm(response.id)
    algorithm_list = tator_api.get_algorithm_list(project=algo_project)
    assert len(algorithm_list) == 0

    current_number_of_algs = len(algorithm_ids)
    for alg_id in algorithm_ids:
        _ = tator_api.delete_algorithm(id=alg_id)
        algorithm_list = tator_api.get_algorithm_list(project=project)

        current_number_of_algs -= 1
        assert len(algorithm_list) == current_number_of_algs


def test_register_algorithm_with_missing_fields(
        host: str,
        token: str,
        project: int) -> None:
    """ Unit test for the RegisterAlgorithm endpoint focused on missing request body fields

    Request bodies are created with missing required fields and a workflow tries
    to be registered with these incorrect request bodies.

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project
    """

    NAME = str(uuid.uuid1())
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
    spec = tator.models.Algorithm(
        project=project,
        user=user_id,
        manifest=manifest_url,
        files_per_job=FILES_PER_JOB)

    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        tator_api.register_algorithm(project=project, algorithm_spec=spec)

    # Missing user field
    spec = tator.models.Algorithm(
        name=NAME,
        project=project,
        manifest=manifest_url,
        files_per_job=FILES_PER_JOB)

    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        tator_api.register_algorithm(project=project, algorithm_spec=spec)

    # Missing manifest
    spec = tator.models.Algorithm(
        name=NAME,
        project=project,
        user=user_id,
        files_per_job=FILES_PER_JOB)

    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        tator_api.register_algorithm(project=project, algorithm_spec=spec)

    # Missing fields per job
    spec = tator.models.Algorithm(
        name=NAME,
        project=project,
        user=user_id,
        manifest=manifest_url)

    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        tator_api.register_algorithm(project=project, algorithm_spec=spec)
