import tator
from uuid import uuid1

def test_clone_version_same_host(host, token, project, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator_api.create_version(project=project, version_spec={'name': str(uuid1())})
    version = response.id
    response = tator.util.clone_version(tator_api, version, clone_project)
    assert(isinstance(response, tator.models.CreateResponse))

def test_clone_version_different_host(host, token, project, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator_api.create_version(project=project, version_spec={'name': str(uuid1())})
    version = response.id
    response = tator.util.clone_version(tator_api, version, clone_project, tator_api)
    assert(isinstance(response, tator.models.CreateResponse))

