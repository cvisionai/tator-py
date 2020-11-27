import tator

def test_clone_membership_same_host(host, token, project, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator_api.whoami()
    user_id = response.id
    response = tator_api.create_membership(project, membership_spec={'user': user_id,
                                                                     'permission': 'Full Control'})
    membership = response.id
    response = tator.util.clone_membership(tator_api, membership, clone_project)
    assert(isinstance(response, tator.models.CreateResponse))

def test_clone_membership_different_host(host, token, project, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator_api.whoami()
    user_id = response.id
    response = tator_api.create_membership(project, membership_spec={'user': user_id,
                                                                     'permission': 'Full Control'})
    membership = response.id
    response = tator.util.clone_membership(tator_api, membership, clone_project, tator_api)
    assert(isinstance(response, tator.models.CreateResponse))

