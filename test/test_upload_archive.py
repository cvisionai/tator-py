import os

import tator

def test_upload_archive(host, token, project, image_type, image_set):
    tator_api = tator.get_api(host, token)
    paths = os.listdir(image_set)
    paths = [os.path.join(image_set, path) for path in paths]
    paths = paths[:100] # Only upload the first 100 files.
    batch_num = 0
    for batch in tator.util.chunked_file_list(paths):
        print(f"Uploading file {batch_num*10} / {len(paths)}")
        for progress, response in tator.util.upload_media_archive(tator_api, project, batch):
            print(f"Archive upload progress: {progress}%")
        batch_num += 1
        assert isinstance(response, tator.models.Transcode)
        print(response.message)
    
