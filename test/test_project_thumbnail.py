import tator
from tator.util._upload_file import _upload_file

def test_project_thumbnail(host, token, project, image_file):
    api = tator.get_api(host, token)
    for progress, upload_info in _upload_file(api, project, image_file):
        pass
    response = api.update_project(project, project_update={'thumb': upload_info.key})
    assert(isinstance(response, tator.models.MessageResponse))
