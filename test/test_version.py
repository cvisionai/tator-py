import tator

def test_version_crud(url, token, project):
    tator_api = tator.get_api(url, token)

    # Test single create.
    response = tator_api.create_version(project, version_spec={
        'name': 'Test Version',
        'description': 'A version for testing',
    })
    assert isinstance(response, tator.CreateResponse)
    print(response.message)
    pk = response.id

    # Test patch.
    response = tator_api.update_version(pk, version_update={'name': 'Updated Version'})
    assert isinstance(response, tator.MessageResponse)
    print(response.message)

    # Compare with get results.
    updated = tator_api.get_version(pk)
    assert isinstance(updated, tator.Version)
    assert updated.name == 'Updated Version'

    # Test delete.
    response = tator_api.delete_version(pk)
    assert isinstance(response, tator.MessageResponse)
    print(response.message)
