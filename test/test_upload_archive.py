import os
import tarfile

import requests
import tator

def test_upload_archive(url, token, project, image_type):
    tator_api = tator.get_api(url, token)
    out_path = '/tmp/lfw.tgz'
    extract_path = '/tmp/lfw'

    # Download Labeled Faces in the Wild dataset.
    if not os.path.exists(out_path):
        url = 'http://vis-www.cs.umass.edu/lfw/lfw.tgz'
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(out_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

    # Extract the images.
    if not os.path.exists(extract_path):
        os.makedirs(extract_path, exist_ok=True)
        tar = tarfile.open(out_path)
        for item in tar:
            tar.extract(item, extract_path)

    paths = os.listdir(extract_path)
    paths = [os.path.join(extract_path, path) for path in paths]
    response = tator.upload_media_archive(tator_api, project, paths)
    assert isinstance(response, tator.Transcode)
    print(response.message)
    
