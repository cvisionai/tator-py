import os

import tator
from tator.util import download_media

def test_download_media(url, token, video):
    tator_api = tator.get_api(url, token)
    video_obj = tator_api.get_media(video)
    video_path = f'/tmp/{video_obj.name}'
    if os.path.exists(video_path):
        os.remove(video_path)
    download_media(tator_api, video_obj, video_path)
    assert os.path.exists(video_path)
    assert os.stat(video_path).st_size == 2299653
