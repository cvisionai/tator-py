import os
import tempfile

import tator

def test_download_image(host, token, image):
    tator_api = tator.get_api(host, token)
    image_obj = tator_api.get_media(image)

    image_files = image_obj.media_files.image
    thumbnail = image_obj.media_files.thumbnail

    assert len(image_files) > 0, "Must have at least 1 image file!"

    available = [x.resolution[0] for x in image_files]
    best = max(available)
    best_idx = available.index(best)

    with tempfile.TemporaryDirectory() as td:
        image_path = os.path.join(td, image_obj.name)
        for progress in tator.download_media(
                tator_api,
                image_obj,
                image_path,
                quality=None,
                media_type=None):
            print(f"Media download progress: {progress}%")
        assert os.path.exists(image_path)
        assert os.stat(image_path).st_size == image_files[best_idx].size

    available = [x.resolution[0] for x in thumbnail]
    best = max(available)
    best_idx = available.index(best)
    with tempfile.TemporaryDirectory() as td:
        image_path = os.path.join(td, image_obj.name)
        for progress in tator.download_media(
                tator_api,
                image_obj,
                image_path,
                quality=None,
                media_type='thumbnail'):
            print(f"Media download progress: {progress}%")
        assert os.path.exists(image_path)
        assert os.stat(image_path).st_size == thumbnail[best_idx].size


    for image_file in image_files:
        with tempfile.TemporaryDirectory() as td:
            image_path = os.path.join(td, image_obj.name)
            for progress in tator.download_media(
                    tator_api,
                    image_obj,
                    image_path,
                    quality=image_file.resolution[0],
                    media_type=None,
                    codec_or_mime=image_file.mime):
                print(f"Media download progress: {progress}%")
            assert os.path.exists(image_path)
            assert os.stat(image_path).st_size == image_file.size

def test_download_video(host, token, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    archival = video_obj.media_files.archival
    streaming = video_obj.media_files.streaming
    thumbnail = video_obj.media_files.thumbnail
    thumbnail_gif = video_obj.media_files.thumbnail_gif

    available = [x.resolution[0] for x in archival]
    best = max(available)
    best_idx = available.index(best)

    # Verify we get the best archival when we ask
    with tempfile.TemporaryDirectory() as td:
        video_path = os.path.join(td, video_obj.name)
        for progress in tator.download_media(
                tator_api,
                video_obj,
                video_path,
                quality=None,
                media_type=None):
            print(f"Media download progress: {progress}%")
        assert os.path.exists(video_path)
        assert os.stat(video_path).st_size == archival[best_idx].size

    for idx,video_file in enumerate(archival):
        with tempfile.TemporaryDirectory() as td:
            video_path = os.path.join(td, video_obj.name)
            for progress in tator.download_media(
                    tator_api,
                    video_obj,
                    video_path,
                    quality=video_file.resolution[0],
                    media_type='archival'):
                print(f"Media download progress: {progress}%")
            assert os.path.exists(video_path)
            assert os.stat(video_path).st_size == video_file.size



    # Verify we can download the best when we ask (streaming)
    available = [x.resolution[0] for x in streaming]
    best = max(available)
    best_idx = available.index(best)

    # Verify we get the best streaming when we ask
    with tempfile.TemporaryDirectory() as td:
        video_path = os.path.join(td, video_obj.name)
        for progress in tator.download_media(
                tator_api,
                video_obj,
                video_path,
                quality=None,
                media_type='streaming'):
            print(f"Media download progress: {progress}%")
        assert os.path.exists(video_path)
        assert os.stat(video_path).st_size == streaming[best_idx].size


    # Verify we can download each file size
    for video_file in streaming:
        with tempfile.TemporaryDirectory() as td:
            video_path = os.path.join(td, video_obj.name)
            for progress in tator.download_media(
                    tator_api,
                    video_obj,
                    video_path,
                    quality=video_file.resolution[0],
                    media_type='streaming'):
                print(f"Media download progress: {progress}%")
            assert os.path.exists(video_path)
            assert os.stat(video_path).st_size == video_file.size


    available = [x.resolution[0] for x in thumbnail]
    best = max(available)
    best_idx = available.index(best)
    with tempfile.TemporaryDirectory() as td:
        image_path = os.path.join(td, video_obj.name)
        for progress in tator.download_media(
                tator_api,
                video_obj,
                image_path,
                quality=None,
                media_type='thumbnail'):
            print(f"Media download progress: {progress}%")
        assert os.path.exists(image_path)
        assert os.stat(image_path).st_size == thumbnail[best_idx].size

    available = [x.resolution[0] for x in thumbnail_gif]
    best = max(available)
    best_idx = available.index(best)
    with tempfile.TemporaryDirectory() as td:
        image_path = os.path.join(td, video_obj.name)
        for progress in tator.download_media(
                tator_api,
                video_obj,
                image_path,
                quality=None,
                media_type='thumbnail_gif'):
            print(f"Media download progress: {progress}%")
        assert os.path.exists(image_path)
        assert os.stat(image_path).st_size == thumbnail_gif[best_idx].size
