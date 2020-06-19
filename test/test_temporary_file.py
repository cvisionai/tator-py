import tempfile
import os

import tator

def test_temporary_file(host, token, project):
    tator_api = tator.get_api(host, token)

    all_temps = tator_api.get_temporary_file_list(project)
    assert  all_temps is not None
    assert len(all_temps) == 0
    
    with tempfile.NamedTemporaryFile(mode='w',suffix=".txt") as temp:
        temp.write("foo")
        temp.flush()
        for progress, response in tator.util.upload_temporary_file(tator_api, project, temp.name):
            print(f"Temporary file upload progress: {progress}%")
        assert isinstance(response, tator.models.CreateResponse)
        print(response.message)
        all_temps = tator_api.get_temporary_file_list(project)
        assert len(all_temps) == 1

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_fp = os.path.join(temp_dir, "foo.txt")
        temp_element = tator_api.get_temporary_file_list(project)[0]
        for progress in tator.util.download_temporary_file(tator_api, temp_element, temp_fp):
            print(f"Temporary file download progress: {progress}%")
        with open(temp_fp, 'r') as temp_file:
            contents = temp_file.read()
            assert contents == "foo"
