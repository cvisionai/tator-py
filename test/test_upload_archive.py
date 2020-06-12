import os

import tator

def test_upload_archive(host, token, project, image_type, image_set):
    tator_api = tator.get_api(host, token)
    paths = os.listdir(image_set)
    paths = [os.path.join(image_set, path) for path in paths]
    batch_num = 0
    for batch in tator.chunked_file_list(paths):
        print(f"Uploading file {batch_num*100} / {len(paths)}")
        for progress, response in tator.upload_media_archive(tator_api, project, batch):
            print(f"Archive upload progress: {progress}%")
        batch_num += 1
        assert isinstance(response, tator.Transcode)
        print(response.message)
    
