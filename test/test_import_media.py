import tator
import time

def test_import_media(host, token, project, video_type):
    api = tator.get_api(host, token)

    url = 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4'
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
