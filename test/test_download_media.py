import os

import tator

def test_download_media(host, token, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)
    video_path = f'/tmp/{video_obj.name}'
    if os.path.exists(video_path):
        os.remove(video_path)
    for progress in tator.download_media(tator_api, video_obj, video_path):
        print(f"Media download progress: {progress}%")
    assert os.path.exists(video_path)
    assert os.stat(video_path).st_size == 2299653
