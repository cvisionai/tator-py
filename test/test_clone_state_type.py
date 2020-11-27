import tator

def test_clone_state_type_same_host(host, token, project, video_type,
                                           state_type, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator.util.clone_media_type(tator_api, video_type, clone_project)
    dest_video_type = response.id
    response = tator.util.clone_state_type(tator_api, state_type, clone_project,
                                                  {video_type: dest_video_type})
    assert(isinstance(response, tator.models.CreateResponse))

def test_clone_state_type_different_host(host, token, project, video_type,
                                                state_type, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator.util.clone_media_type(tator_api, video_type, clone_project)
    dest_video_type = response.id
    response = tator.util.clone_state_type(tator_api, state_type, clone_project,
                                                  {video_type: dest_video_type}, tator_api)
    assert(isinstance(response, tator.models.CreateResponse))

