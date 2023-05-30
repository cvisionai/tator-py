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
        "type": video_type,
        "uid": upload_uid,
        "gid": upload_gid,
        "name": fname,
        "section": section,
        "md5": md5,
    }


    # Create the media.
    response = tator_api.create_media_list(project=project, body=media_spec)
    print(f"Transcoding video with existing media ID {response.id[0]}...")
    for progress, response in tator.util.upload_media(tator_api, video_type, video_file,
                                                      media_id=response.id[0]):
        print(f"Upload video progress: {progress}%")
    print(response.message)
    print(response.id)
    while True:
        transcode = tator_api.get_transcode(response.id)
        status = transcode.job.status.lower()
        if status == 'succeeded':
            break
        elif status == 'failed':
            raise Exception('Transcode of existing media failed!')
        else:
            print("Waiting for transcode of existing media to complete...")
            time.sleep(2.5)

def test_transcode_cancel(host, token, project, video_type, video_file):
    tator_api = tator.get_api(host, token)

    # Compute parameters needed to create media.
    md5 = tator.util.md5sum(video_file)
    upload_uid = str(uuid1())
    upload_gid = str(uuid1())
    fname='CancelTranscodeTest.mp4'
    section="Transcode cancel"

    # Define media spec.
    media_spec = {
        'type': video_type,
        'uid': upload_uid,
        'gid': upload_gid,
        'name': fname,
        'section': section,
        'md5': md5,
    }


    # Upload the same media multiple times.
    media_ids = []
    uids = []
    other_gid = str(uuid1())
    for idx in range(5):
        media_spec['uid'] = str(uuid1())
        if idx > 2:
            # On last two transcodes, change the group ID
            media_spec['gid'] = other_gid
        response = tator_api.create_media_list(project=project, body=[media_spec])
        media_ids.append(response.id[0])
        print(f"Transcoding video with existing media ID {response.id[0]}...")
        for progress, response in tator.util.upload_media(tator_api, video_type, video_file,
                                                          upload_uid=media_spec['uid'],
                                                          upload_gid=media_spec['gid'],
                                                          media_id=response.id[0]):
            print(f"Upload video progress: {progress}%")
        uids.append(response.id)

    # Get all transcodes for the two groups
    transcodes1 = tator_api.get_transcode_list(project, gid=upload_gid)
    transcodes2 = tator_api.get_transcode_list(project, gid=other_gid)
    assert(len(transcodes1) + len(transcodes2) == 5)

    # Cancel transcodes for one group
    before_delete = tator_api.get_transcode_list(project)
    response = tator_api.delete_transcode_list(project, gid=other_gid)
    print(response.message)
    remaining = tator_api.get_transcode_list(project)
    for transcode in remaining:
        assert(transcode.spec.gid != other_gid)
    assert(len(before_delete) - len(remaining)  >= 2)

    # Cancel individual transcode
    transcodes = tator_api.get_transcode_list(project, gid=upload_gid)
    uid = transcodes[0].spec.uid
    response = tator_api.delete_transcode(uid)
    print(response.message)
    remaining = tator_api.get_transcode_list(project, gid=upload_gid)
    assert(len(transcodes) - len(remaining) == 1)

    # Get transcodes by media
    transcodes = tator_api.get_transcode_list(project, media_id=media_ids)
    transcode = transcodes[0]
    media_id = transcode.spec.media_id
    uid = transcode.spec.uid
    transcode = tator_api.get_transcode(uid)
    assert(transcode.spec.media_id == media_id)
    response = tator_api.delete_transcode_list(project, media_id=[media_id])
    print(response.message)
    remaining = tator_api.get_transcode_list(project, media_id=media_ids)
    assert(len(transcodes) > len(remaining))
    response = tator_api.delete_transcode_list(project, media_id=media_ids)
    print(response.message)
    remaining = tator_api.get_transcode_list(project, media_id=media_ids)
    assert(len(remaining) == 0)
    
