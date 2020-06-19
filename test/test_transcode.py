import tator
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


    

