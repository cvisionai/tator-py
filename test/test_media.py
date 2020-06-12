import tempfile
import os

import tator

from._common import assert_vector_equal

def test_get_file(host, token, project, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    with tempfile.TemporaryDirectory() as temp_dir:
        outpath = os.path.join(temp_dir, "video.mp4")
        for progress in tator.download_media(tator_api, video_obj, outpath):
            print(f"Video download progress: {progress}%")
        assert(os.path.exists(outpath))

def test_get_audio(host, token, project, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    audio = video_obj.media_files.audio
    assert len(audio) > 0
    assert audio[0].codec == 'aac'

