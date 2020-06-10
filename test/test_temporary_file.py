import tempfile
import os

import tator
from tator.util import upload_temporary_file
from tator.util import download_temporary_file

def test_temporary_file(url, token, project):
    tator_api = tator.get_api(url, token)

    all_temps = tator_api.get_temporary_file_list(project)
    assert  all_temps is not None
    assert len(all_temps) == 0
    
    with tempfile.NamedTemporaryFile(mode='w',suffix=".txt") as temp:
        temp.write("foo")
        temp.flush()
        upload_temporary_file(tator_api, project, temp.name)
        all_temps = tator_api.get_temporary_file_list(project)
        assert len(all_temps) == 1

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_fp = os.path.join(temp_dir, "foo.txt")
        temp_element = tator_api.get_temporary_file_list(project)[0]
        download_temporary_file(tator_api, temp_element, temp_fp)
        with open(temp_fp, 'r') as temp_file:
            contents = temp_file.read()
            assert contents == "foo"
