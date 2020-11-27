import tator
from uuid import uuid1

def test_clone_section_same_host(host, token, project, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator_api.create_section(project=project, section_spec={'name': str(uuid1())})
    section = response.id
    response = tator.util.clone_section(tator_api, section, clone_project)
    assert(isinstance(response, tator.models.CreateResponse))

def test_clone_section_different_host(host, token, project, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator_api.create_section(project=project, section_spec={'name': str(uuid1())})
    section = response.id
    response = tator.util.clone_section(tator_api, section, clone_project, tator_api)
    assert(isinstance(response, tator.models.CreateResponse))

