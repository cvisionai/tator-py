import tator
import time
from uuid import uuid1

def test_transcode_fault_handling(host, token, project):
    """ Verify Error Handling occurs for transcode endpoint """
    tator_api = tator.get_api(host, token)
    exception = False
    try:
        video_obj = tator_api.transcode(project,
                                        transcode_spec={'gid':str(uuid1()),
                                                        'md5':"1234",
                                                        'name':"blah",
                                                        'section':"blah",
                                                        'type':200,
                                                        'uid':str(uuid1()),
                                                        'url':"blah"})
    except Exception as e:
        exception = True
        code = e.status

    assert(exception)
    assert(code == 400)

def test_transcode_existing_media(host, token, project, video_type, video_file):
    tator_api = tator.get_api(host, token)

    # Compute parameters needed to create media.
    md5 = tator.util.md5sum(video_file)
    upload_uid = str(uuid1())
    upload_gid = str(uuid1())
    fname='ExistingMediaTranscodeTest.mp4'
    section="Transcoded with Existing Media"

    # Define media spec.
    media_spec = {
        'type': video_type,
        'uid': upload_uid,
        'gid': upload_gid,
        'name': fname,
        'section': section,
        'md5': md5,
    }

    # Create the media.
    response = tator_api.create_media(project=project, media_spec=media_spec)
    print(f"Transcoding video with existing media ID {response.id}...")
    for progress, response in tator.util.upload_media(tator_api, video_type, video_file,
                                                      media_id=response.id):
        print(f"Upload video progress: {progress}%")
    print(response.message)
    while True:
        job = tator_api.get_job(response.uid)
        if job.status == 'Succeeded':
            break
        elif job.status == 'Failed':
            raise Exception('Transcode of existing media failed!')
        else:
            print("Waiting for transcode of existing media to complete...")
            time.sleep(2.5)

