import os
import subprocess
import tempfile
import uuid
from textwrap import dedent

import tator

def _create_yaml_file_str() -> str:
    """ Creates a argo manifest file
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


def test_register_algorithm(host: str, token: str, project: int):

    ALGORITHM_NAME = str(uuid.uuid1())

    # Create a temporary file
    fd, local_yaml_file = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as file_handle:
            file_handle.write(_create_yaml_file_str())

        # Run the example.
        cmd = [
            'python3',
            'examples/register_algorithm.py',
            '--host', host,
            '--token', token,
            '--project', str(project),
            '--manifest', local_yaml_file,
            '--algorithm_name', ALGORITHM_NAME,
            '--files_per_job', '100'
        ]

        subprocess.run(cmd, check=True)

    finally:
        os.remove(local_yaml_file)

        tator_api = tator.get_api(host=host, token=token)
        algorithms = tator_api.get_algorithm_list(project=project)
        for alg in algorithms:
            if alg.name == ALGORITHM_NAME:
                tator_api.delete_algorithm(id=alg.id)
                print(f'Deleting algorithm: {alg.name}')
                break