import os
import tempfile

import tator

def test_get_clip(host, token, project, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    frame_ranges = ['0:100']
    clip = tator_api.get_clip(video, frame_ranges=frame_ranges)
    with tempfile.TemporaryDirectory() as td:
        video_path = os.path.join(td, 'video_clip_test.mp4')
        for progress in tator.util.download_temporary_file(tator_api, clip.file, video_path):
            print(f"Video clip download progress: {progress}%")
    tator_api.delete_temporary_file(clip.file.id)

