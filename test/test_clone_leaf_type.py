import tator

def test_clone_leaf_type_same_host(host, token, project, leaf_type, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator.util.clone_leaf_type(tator_api, leaf_type, clone_project)
    assert(isinstance(response, tator.models.CreateResponse))

def test_clone_leaf_type_different_host(host, token, project, leaf_type, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator.util.clone_leaf_type(tator_api, leaf_type, clone_project, tator_api)
    assert(isinstance(response, tator.models.CreateResponse))

