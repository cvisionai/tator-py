import os

import tator

def test_download_media(url, token, video):
    tator_api = tator.get_api(url, token)
    video_obj = tator_api.get_media(video)
    tator.download_media(video_obj, '/tmp')
    assert os.path.exists(f'/tmp/{video_obj.name}')
    assert os.stat(f'/tmp/{video_obj.name}').st_size == 2299653
