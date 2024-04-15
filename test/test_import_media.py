import tator
import time

def test_import_image(host, token, project, image_type):
    api = tator.get_api(host, token)
    url = 'https://www.cvisionai.com/static/74822662b430b97b6d86bb74beab1666/fb5f3/open-em-image.png'
    response = tator.util.import_media(api, image_type, url)
    assert(isinstance(response, tator.models.CreateListResponse))


def wait_for_transcode(api, transcode_id):
    while True:
        transcode = api.get_transcode(uid=transcode_id)
        status = transcode.job.status.lower()
        if status == "succeeded":
            break
        elif status == "failed":
            raise Exception("Media import failed!")
        else:
            print("Waiting for transcode of imported media to complete...")
            time.sleep(2.5)

def test_import_video(host, token, project, video_type):
    api = tator.get_api(host, token)
    url = 'http://www.ballastmedia.com/wp-content/uploads/AudioVideoSyncTest_BallastMedia.mp4'
    response = tator.util.import_media(api, video_type, url, _request_timeout=30)
    print(response.message)
    wait_for_transcode(api, response.id)

    # Attempt to import the same video to the same media id, no additional transcodes should occur
    media_id = response.object['spec']['media_id']
    initial_obj = api.get_media(media_id)
    response = tator.util.import_media(api, video_type, url, media_id=media_id, _request_timeout=30)
    print(response.message)
    wait_for_transcode(api, response.id)
    final_obj = api.get_media(media_id)

    media_fields = ["archival", "_audio", "_streaming", "_thumbnail", "_thumbnail_gif"]

    for field in media_fields:
        assert (
            len(getattr(initial_obj.media_files, field)) ==
            len(getattr(final_obj.media_files, field))
        )

def test_import_video_to_section_id(host, token, project, video_type):
    api = tator.get_api(host, token)
    url = 'http://www.ballastmedia.com/wp-content/uploads/AudioVideoSyncTest_BallastMedia.mp4'
    section_id = api.create_section(project, {"name":"Video import to section ID"}).id
    response = tator.util.import_media(api, video_type, url, _request_timeout=30, section_id=section_id)
    print(response.message)
    wait_for_transcode(api, response.id)

    # Attempt to import the same video to the same media id, no additional transcodes should occur
    media_id = response.object['spec']['media_id']
    initial_obj = api.get_media(media_id)
    response = tator.util.import_media(api, video_type, url, media_id=media_id, _request_timeout=30)
    print(response.message)
    wait_for_transcode(api, response.id)
    final_obj = api.get_media(media_id)

    media_fields = ["archival", "_audio", "_streaming", "_thumbnail", "_thumbnail_gif"]

    for field in media_fields:
        assert (
            len(getattr(initial_obj.media_files, field)) ==
            len(getattr(final_obj.media_files, field))
        )
