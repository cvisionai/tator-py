import tator
import time

def test_import_image(host, token, project, image_type):
    api = tator.get_api(host, token)
    url = 'https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png'
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

