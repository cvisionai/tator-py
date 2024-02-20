import time
import pytest
import tator

def test_algo_template(host, token, organization, project, video):
    api = tator.get_api(host, token)
    response = api.create_hosted_template(organization, {
        "name": "echo",
        "url": "https://raw.githubusercontent.com/cvisionai/tator/dev/500-hosted-workflows-applets/doc/examples/workflow_template/echo.yaml",
        "headers": [],
        "tparams": [{"name": "message", "value": "Hello from the tator-py tests"}]
    })
    
    response = api.register_algorithm(project, {
        "name": "echo",
        "user": api.whoami().id,
        "files_per_job": 10000,
        "template": response.id,
    })
    print(response.message)

    response = api.create_job_list(project, {
        "algorithm_name": "echo",
        "media_ids": [video],
    })
    job_id = response.id[0]

    while True:
        print("Waiting for job to complete...")
        time.sleep(5)
        response = api.get_job(job_id)
        if response.status == 'Succeeded':
            break
        elif response.status == 'Failed':
            raise RuntimeError("Workflow template failed!")
          
def test_applet_template(host, token, organization, project):
    api = tator.get_api(host, token)
    response = api.create_hosted_template(organization, {
        "name": "echo",
        "url": "https://raw.githubusercontent.com/cvisionai/tator/dev/500-hosted-workflows-applets/doc/examples/applet_template/echo.html",
        "headers": [],
        "tparams": [{"name": "message", "value": "Hello from the tator-py tests"}]
    })

    response = api.register_applet(project, {
        "name": "echo",
        "description": "test for templated applets",
        "template": response.id,
    })

