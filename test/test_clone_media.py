import tempfile
import os
import time

import tator

from._common import assert_vector_equal

def test_clone_multi(host, token, project, multi_type, multi):
    tator_api = tator.get_api(host, token)
    multi_obj = tator_api.get_media(multi)
    response = tator_api.clone_media_list(project=project,
                                          media_id=[multi],
                                          clone_media_spec={'dest_project': project,
                                                            'dest_section': 'Cloned multi',
                                                            'dest_type': multi_type})
    assert isinstance(response, tator.models.CreateListResponse)
    assert len(response.id) == 1

def test_clone_videos(host, token, project, video_type, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    response = tator_api.clone_media_list(project=project,
                                          media_id=[video],
                                          clone_media_spec={'dest_project': project,
                                                            'dest_section': 'Cloned video',
                                                            'dest_type': video_type})
    assert isinstance(response, tator.models.CreateListResponse)
    assert len(response.id) == 1

    cloned_video = tator_api.get_media(response.id[0])
    with tempfile.TemporaryDirectory() as temp_dir:
        outpath = os.path.join(temp_dir, "video.mp4")
        for progress in tator.download_media(tator_api, cloned_video, outpath):
            print(f"Cloned video download progress: {progress}%")
        assert(os.path.exists(outpath))

def test_clone_images(host, token, project, image_type, image):
    tator_api = tator.get_api(host, token)
    image_obj = tator_api.get_media(image)

    response = tator_api.clone_media_list(project=project,
                                          media_id=[image],
                                          clone_media_spec={'dest_project': project,
                                                            'dest_section': 'Cloned image',
                                                            'dest_type': image_type})
    assert isinstance(response, tator.models.CreateListResponse)
    assert len(response.id) == 1

    cloned_image = tator_api.get_media(response.id[0])
    with tempfile.TemporaryDirectory() as temp_dir:
        outpath = os.path.join(temp_dir, "image.jpg")
        for progress in tator.download_media(tator_api, cloned_image, outpath):
            print(f"Cloned image download progress: {progress}%")
        assert(os.path.exists(outpath))

def test_clone_multi_util_same_host(host, token, project, multi_type, multi):
    tator_api = tator.get_api(host, token)
    query_params = {'project': project, 'media_id': [multi]}
    section = 'Cloned media util same host'
    created_ids = []
    generator = tator.util.clone_media_list(tator_api, query_params, project, {}, multi_type,
                                            section)
    for num_created, num_total, response, id_map in generator:
        print(f"Created {num_created} of {num_total} files...")
        created_ids.append(response.id[0])
    print(f"Finished creating {num_created} files!")
    assert len(created_ids) == 1

def test_clone_videos_util_same_host(host, token, project, video_type, video):
    tator_api = tator.get_api(host, token)
    query_params = {'project': project, 'media_id': [video]}
    section = 'Cloned media util same host'
    created_ids = []
    generator = tator.util.clone_media_list(tator_api, query_params, project, {}, video_type,
                                            section)
    for num_created, num_total, response, id_map in generator:
        print(f"Created {num_created} of {num_total} files...")
        created_ids.append(response.id[0])
    print(f"Finished creating {num_created} files!")
    assert len(created_ids) == 1

def test_clone_images_util_same_host(host, token, project, image_type, image):
    tator_api = tator.get_api(host, token)
    query_params = {'project': project, 'media_id': [image]}
    section = 'Cloned media util same host'
    created_ids = []
    generator = tator.util.clone_media_list(tator_api, query_params, project, {}, image_type,
                                            section)
    for num_created, num_total, response, id_map in generator:
        print(f"Created {num_created} of {num_total} files...")
        created_ids.append(response.id[0])
    print(f"Finished creating {num_created} files!")
    assert len(created_ids) == 1

def test_clone_multi_util_different_host(host, token, project, multi_type, multi, video):
    tator_api = tator.get_api(host, token)
    dest_api = tator.get_api(host, token)
    assert tator_api is not dest_api
    query_params = {'project': project, 'media_id': [multi]}
    section = 'Cloned media util different host'
    created_ids = []
    generator = tator.util.clone_media_list(tator_api, query_params, project, {video:video},
                                            multi_type, section, dest_api)
    for num_created, num_total, response, id_map in generator:
        print(f"Created {num_created} of {num_total} files...")
        created_ids.append(response.id[0])
    print(f"Finished creating {num_created} files!")
    tator.util.clone_media_list(tator_api, query_params, project, multi_type,
                                'Cloned media util different host', tator_api)
    assert len(created_ids) == 1

def test_clone_videos_util_different_host(host, token, project, video_type, video):
    tator_api = tator.get_api(host, token)
    dest_api = tator.get_api(host, token)
    assert tator_api is not dest_api
    query_params = {'project': project, 'media_id': [video]}
    section = 'Cloned media util different host'
    created_ids = []
    generator = tator.util.clone_media_list(tator_api, query_params, project, {}, video_type,
                                            section, dest_api)
    for num_created, num_total, response, id_map in generator:
        print(f"Created {num_created} of {num_total} files...")
        created_ids.append(response.id[0])
    print(f"Finished creating {num_created} files!")
    tator.util.clone_media_list(tator_api, query_params, project, video_type,
                                'Cloned media util different host', tator_api)
    assert len(created_ids) == 1

def test_clone_images_util_different_host(host, token, project, image_type, image):
    tator_api = tator.get_api(host, token)
    dest_api = tator.get_api(host, token)
    assert tator_api is not dest_api
    query_params = {'project': project, 'media_id': [image]}
    section = 'Cloned media util different host'
    created_ids = []
    generator = tator.util.clone_media_list(tator_api, query_params, project, {}, image_type,
                                            section, dest_api)
    for num_created, num_total, response, id_map in generator:
        print(f"Created {num_created} of {num_total} files...")
        created_ids.append(response.id[0])
    print(f"Finished creating {num_created} files!")
    assert len(created_ids) == 1
