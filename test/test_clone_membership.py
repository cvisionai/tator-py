import json

import tator

def test_clone_membership_same_host(host, token, project, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator_api.whoami()
    user_id = response.id
    memberships = tator_api.get_membership_list(project)
    for membership in memberships:
        if membership.user == user_id:
            break
    try:
        response = tator.util.clone_membership(tator_api, membership.id, clone_project)
    except tator.openapi.tator_openapi.exceptions.ApiException as exc:
        assert(json.loads(exc.body)['message'].startswith('Membership already exists'))

def test_clone_membership_different_host(host, token, project, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator_api.whoami()
    user_id = response.id
    memberships = tator_api.get_membership_list(project)
    for membership in memberships:
        if membership.user == user_id:
            break
    try:
        response = tator.util.clone_membership(tator_api, membership.id, clone_project, tator_api)
    except tator.openapi.tator_openapi.exceptions.ApiException as exc:
        assert(json.loads(exc.body)['message'].startswith('Membership already exists'))

