from time import sleep

import tator

def test_media_type_delete(host, token, project, image_file):
    tator_api = tator.get_api(host, token)

    response = tator_api.create_media_type(project, media_type_spec={
        'name': 'image_type',
        'description': 'Test image type',
        'project': project,
        'dtype': 'image',
        'attribute_types': [],
    })
    image_type = response.id
    n_images = 10

    # Verify no media exist to start
    count = tator_api.get_media_count(project, type=image_type)
    assert count == 0

    for idx in range(n_images):
        for progress, response in tator.util.upload_media(tator_api, image_type, image_file):
            print(f"Upload image ({idx+1} of {n_images}) progress: {progress}%")
        print(response.message)

    n_retries = 0
    max_retries = 30
    while tator_api.get_media_count(project, type=image_type) != n_images:
        num_retries += 1
        assert num_retries < max_retries, "Failed uploading media"
        sleep(0.5)

    response = tator_api.delete_media_type(image_type)

    assert str(image_type) in response.message, "Media type id not found in delete response"
    assert str(n_images) in response.message, "Media count not found in delete response"

    try:
        caught_it = False
        tator_api.get_media_count(project, type=image_type)
    except:
        caught_it=True
    finally:
        assert caught_it
