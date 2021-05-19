import tempfile
import os

import tator

def test_attachment(host, token, project, video):
    tator_api = tator.get_api(host, token)

    with tempfile.NamedTemporaryFile(mode='w',suffix=".txt") as temp:
        temp.write("foo")
        temp.flush()
        for progress, response in tator.util.upload_attachment(tator_api, video, temp.name):
            print(f"Attachment upload progress: {progress}%")
        assert isinstance(response, tator.models.MessageResponse)
        print(f"Message: {response.message}")

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_fp = os.path.join(temp_dir, "foo.txt")
        media_obj = tator_api.get_media(video)
        for progress in tator.util.download_attachment(tator_api, media_obj, temp_fp):
            print(f"Attachment download progress: {progress}%")
        with open(temp_fp, 'r') as temp_file:
            contents = temp_file.read()
            assert contents == "foo"
