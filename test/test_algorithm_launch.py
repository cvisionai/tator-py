import glob
import logging
import os
import shutil
import tempfile
import time
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

            for media_id in media_ids:
                media=tator_api.get_media(media_id)
                increment = media.attributes.get('test_int',0)+1
                tator_api.update_media(media.id, {'attributes':{'test_int': increment}})

        if __name__ == '__main__':
            main()
        """)

def _create_workflow_manifest(
        host: str,
        token: str,
        project: int) -> str:
    """ Creates the argo workflow manifest file used by the tests in this module

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project

    Returns:
        URL to uploaded and saved algorithm manifest file
    """
    tator_api = tator.get_api(host=host, token=token)

    fd, local_yaml_file = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as file_handle:
            file_handle.write(_create_yaml_file_str())

        for progress, upload_info in _upload_file(tator_api, project, local_yaml_file):
            pass
        url = tator_api.get_download_info(project, {'keys': [upload_info.key]})[0].url

        # Save the uploaded file using the save algorithm manifest endpoint
        spec = tator.models.AlgorithmManifestSpec(name='workflow.yaml', upload_url=url)
        response = tator_api.save_algorithm_manifest(project=project, algorithm_manifest_spec=spec)

    finally:
        os.remove(local_yaml_file)

    return response.url

@pytest.fixture(scope='module')
def algorithm_name(request, project: int) -> str:
    """ Pytest fixture used to create a registered algorithm used by the tests in this module

    Yields:
        Unique algorithm name to be used for the registered algorithms in this test
        Deletes the registered algorithm once context switches back to this method
    """

    import uuid
    import tator

    # Get the user ID
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host=host, token=token)
    user = tator_api.whoami()

    # Create the workflow manifest that will be used when testing the algorithm launch endpoint
    manifest_url = _create_workflow_manifest(host=host, token=token, project=project)

    # Register the algorithm using the unique name
    algorithm_name = 'test_algorithm_launch_workflow'

    spec = tator.models.Algorithm(
        name=algorithm_name,
        project=project,
        user=user.id,
        description=None,
        manifest=manifest_url,
        cluster=None,
        files_per_job=100)

    response = tator_api.register_algorithm(project=project, algorithm_spec=spec)

    yield algorithm_name

    # Once we're done with the tests in this module, delete the algorithm
    # (and subsequently its unique name)
    _ = tator_api.delete_algorithm(id=response.id)

def _assert_algorithm_workflow_results(
    tator_api: tator.api,
    project: int,
    expected_count: int,
    media_ids: list) -> None:
    """ Polls the tator database waiting for the argo workflow to complete its database inserts

    Performs assert on if the count of analysis entries matches the provided expected count

    Args:
        tator_api: Interface to tator
        project: Unique identifier of test project
        expected_analysis_count: Expected number of analysis entries with test_media_id data query
    """

    MAX_RETRIES = 10
    num_retries = 0
    matched_analysis_count = False

    while True:
        media = tator_api.get_media_list(project, media_id=media_ids)
        analysis_count = 0
        log_msg = f'num_retries: {num_retries}'
        print(log_msg)
        all_good=True
        for m in media:
          if m.attributes.get('test_int',0) != expected_count:
            all_good = False

        if all_good:
          break

        num_retries += 1
        if num_retries < MAX_RETRIES:
            time.sleep(10)
        else:
            log_msg = f'Number of detected analysis entries from workflow: {analysis_count}'
            logger.error(log_msg)
            logger.error('Reached maximum retries')
            break

    for m in media:
      assert m.attributes.get('test_int',0) == expected_count

def test_algorithm_launch(
        host: str,
        token: str,
        project: int,
        algorithm_name: str,
        image_type: int,
        image_set: str) -> None:
    """ Unit tests the Jobs POST method

    Performs the following unit tests:
    - Add a bunch of images, register the workflow that writes entries to the Analysis model
      and check to see if the number of entries match in a given amount of processing time.
    - Provide a specific media list, launch the workflow, 
      and perform the analysis entry counting as above
    - Provide a blank media list and ensure no workflow was launched (using the uid)
    - Provide a media query, launch the workflow,
      and perform the analysis entry counting as above 

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project
        algorithm_name: Unique algorithm name of a registered workflow to be used by this test
        image_type: Unique identifier of the media type related to images saved to this project
        image_set: List of paths to temporary images that can be uploaded to tator
    """
    tator_api = tator.get_api(host=host, token=token)
    number_of_media = 10

    # Get the media that's already in the project (perhaps added from other tests)
    medias = tator_api.get_media_list(project=project)
    number_of_media += len(medias)

    # Add some media to the project
    paths = glob.glob(image_set + '/**/*.jpg', recursive=True)
    paths = [os.path.join(image_set, path) for path in paths]
    paths = paths[:10]

    for image_file in paths:
        for progress, response in tator.util.upload_media(tator_api, image_type, image_file):
            log_msg = f"Upload image {image_file} - progress: {progress}%"
            logger.info(log_msg)

    num_retries = 0
    max_retries = 30
    while True:
        medias = tator_api.get_media_list(project=project)
        if len(medias) == number_of_media:
            break

        num_retries += 1
        if num_retries >= max_retries:
            break
        time.sleep(0.5)

    assert len(medias) == number_of_media
    all_ids = [m.id for m in medias]

    # Now, launch the algorithm again with an arbitrary set of media and test the results
    media_ids = [medias[0].id, medias[1].id]
    print(f"Providing following media list: {media_ids}")
    spec = tator.models.JobSpec(algorithm_name=algorithm_name, media_ids=media_ids)
    response = tator_api.create_job_list(project=project, job_spec=spec)
    assert len(response.id) == 1
    _assert_algorithm_workflow_results(
        tator_api=tator_api,
        project=project,
        expected_count=1,
        media_ids=media_ids)

    # Next, launch the algorithm again with a blank set of media ids and test the results
    # - This shouldn't launch the argo workflow
    media_ids = []
    spec = tator.models.JobSpec(algorithm_name=algorithm_name, media_ids=media_ids)
    response = tator_api.create_job_list(project=project, job_spec=spec)
    assert len(response.id) == 0
