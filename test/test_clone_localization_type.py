import tator

def test_clone_localization_type_same_host(host, token, project, image_type, video_type,
                                           box_type, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator.util.clone_media_type(tator_api, video_type, clone_project)
    dest_video_type = response.id
    response = tator.util.clone_media_type(tator_api, image_type, clone_project)
    dest_image_type = response.id
    response = tator.util.clone_localization_type(tator_api, box_type, clone_project,
                                                  {video_type: dest_video_type,
                                                   image_type: dest_image_type})
    assert(isinstance(response, tator.models.CreateResponse))

def test_clone_localization_type_different_host(host, token, project, image_type, video_type,
                                                box_type, clone_project):
    tator_api = tator.get_api(host, token)
    response = tator.util.clone_media_type(tator_api, video_type, clone_project)
    dest_video_type = response.id
    response = tator.util.clone_media_type(tator_api, image_type, clone_project)
    dest_image_type = response.id
    response = tator.util.clone_localization_type(tator_api, box_type, clone_project,
                                                  {video_type: dest_video_type,
                                                   image_type: dest_image_type}, tator_api)
    assert(isinstance(response, tator.models.CreateResponse))

