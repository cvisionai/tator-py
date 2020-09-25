import os
import time
import tempfile
from textwrap import dedent

import tator
import uuid

def test_algorithm_cancel(host, token, project, image):
    ALGORITHM_NAME = f'Sleepy time {uuid.uuid1()}'

    # Register an algorithm that sleeps.
    workflow_spec = dedent("""\
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: sleep-
spec:
  entrypoint: sleep
  ttlStrategy:
    secondsAfterCompletion: 0
  templates:
  - name: sleep
    terminationGracePeriodSeconds: 0
    container:
      image: busybox
      command: [sleep]
      args: ["1000"]
      resources:
        limits:
          memory: 32Mi
          cpu: 100m
""")
    manifest_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
    manifest_file.write(workflow_spec)
    manifest_file.close()
    tator.util.register_algorithm(
        host=host,
        token=token,
        project=project,
        manifest=manifest_file.name,
        algorithm_name=ALGORITHM_NAME,
        files_per_job=1,
        description='sleeps for testing purposes',
        cluster_id=None)
    os.remove(manifest_file.name)

    # Launch some workflows.
    tator_api = tator.get_api(host=host, token=token)
    spec = tator.models.AlgorithmLaunchSpec(
        algorithm_name=ALGORITHM_NAME,
        media_ids=[image])
    responses = [tator_api.algorithm_launch(project=project,
                                            algorithm_launch_spec=spec)
                 for _ in range(10)]

    # Cancel by UID.
    uid = responses[0].uid[0]
    job = tator_api.get_job(uid)
    assert isinstance(job, tator.models.Job)
    print(f"Cancelling job with uid {uid}...")
    response = tator_api.delete_job(uid)
    # TODO: Job deletions are taking a really long time to go through,
    # at least partially because the progress container is taking so long.
    # When websockets are removed, switch cancel operation to delete
    # rather than patching with stop (delete is almost instantaneous).
    """
    print("Cancel done, waiting 30 sec...")
    #time.sleep(30)
    try:
        found = True
        response = tator_api.get_job(uid)
    except tator.exceptions.ApiException as exc:
        found = False
        assert exc.status == 404
    assert found == False
    """

    # Cancel by GID.
    gid = responses[1].gid
    jobs = tator_api.get_job_list(project, gid=gid)
    assert isinstance(jobs[0], tator.models.Job)
    print(f"Cancelling job with gid {gid}...")
    tator_api.delete_job_list(project, gid=gid)
    """
    print("Cancel done, waiting 60 sec...")
    time.sleep(60)
    jobs = tator_api.get_job_list(project, gid=gid)
    assert len(jobs) == 0
    """

    # Cancel all jobs in project.
    jobs = tator_api.get_job_list(project)
    assert len(jobs) >= 8
    print("Cancelling all jobs in project...")
    tator_api.delete_job_list(project)
    """
    print("Cancel done, waiting 60 sec...")
    time.sleep(60)
    jobs = tator_api.get_job_list(project)
    assert len(jobs) == 0
    """

