import logging
import tator

import os
import requests
import tempfile

logger = logging.getLogger(__name__)

def test_media_manipulation(host: str,
                            token: str,
                            count_video: int):
  api = tator.get_api(host, token)
  media = api.get_media(count_video)
  
  original_streamer_count = len(media.media_files.streaming)
  original_archival_count = len(media.media_files.archival if media.media_files.archival else [])

  patch_in_res = media.media_files.streaming[0].resolution[0] - 16

  with tempfile.TemporaryDirectory() as td:
    VIDEO_URL = "https://github.com/cvisionai/rgb_test_videos/raw/v0.0.3/samples/count.mp4"
    r = requests.get(VIDEO_URL)
    video_path = os.path.join(td, "count.mp4")
    f = open(video_path, 'wb')
    for chunk in r.iter_content(chunk_size=1*1024*1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()

    # Check ability to patch in a streaming file
    configuration = tator.models.ResolutionConfig(resolution=patch_in_res)
    tator.util.supplement_video_to_media(api, count_video, "streaming", configuration, video_path, force=False)
    media = api.get_media(count_video)
    new_streamer_count = len(media.media_files.streaming)
    assert new_streamer_count == original_streamer_count + 1

    found_it = False
    for streamer in media.media_files.streaming:
      if streamer.resolution[0] == patch_in_res:
        found_it = True
    assert(found_it)


    encode_configuration = tator.models.EncodeConfig(crf=40)
    archive_configuration = tator.models.ArchiveConfig(encode=encode_configuration)
    tator.util.supplement_video_to_media(api,count_video, "archival", archive_configuration, video_path, force=False)
    media = api.get_media(count_video)
    new_archival_count = len(media.media_files.archival)
    assert(new_archival_count == original_archival_count + 1)



