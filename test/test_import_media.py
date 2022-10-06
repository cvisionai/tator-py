import tator
import time

def test_import_image(host, token, project, image_type):
    api = tator.get_api(host, token)
    url = 'https://www.cvisionai.com/static/74822662b430b97b6d86bb74beab1666/fb5f3/open-em-image.png'
    response = tator.util.import_media(api, image_type, url)
    assert(isinstance(response, tator.models.CreateResponse))

def test_import_video(host, token, project, video_type):
    api = tator.get_api(host, token)
    url = 'http://www.ballastmedia.com/wp-content/uploads/AudioVideoSyncTest_BallastMedia.mp4'
    response = tator.util.import_media(api, video_type, url)
    print(response.message)
    while True:
        job = api.get_job(response.uid)
        if job.status == 'Succeeded':
            break
        elif job.status == 'Failed':
            raise Exception('Media import failed!')
        else:
            print("Waiting for transcode of imported media to complete...")
            time.sleep(2.5)

    # Attempt to import the same video to the same media id, no additional transcodes should occur
    initial_obj = api.get_media(response.media_id)
    response = tator.util.import_media(api, video_type, url, media_id=response.media_id)
    print(response.message)
    while True:
        job = api.get_job(response.uid)
        if job.status == "Succeeded":
            break
        elif job.status == "Failed":
            raise Exception("Media import failed!")
        else:
            print("Waiting for transcode of imported media to complete...")
            time.sleep(2.5)
    final_obj = api.get_media(response.media_id)

    media_fields = ["archival", "_audio", "_streaming", "_thumbnail", "_thumbnail_gif"]

    for field in media_fields:
        assert (
            len(getattr(initial_obj.media_files, field)) ==
            len(getattr(final_obj.media_files, field))
        )
