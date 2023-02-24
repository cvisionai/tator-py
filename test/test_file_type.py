import logging
import os
import tempfile

import pytest
import tator
from tator.util._upload_file import _upload_file

logger = logging.getLogger(__name__)


def _upload_generic_file(
    host: str, token: str, project: int, file_id: int, file_path: str = "test.file"
):
    """Uploads the provided manifest file

    :param host: Project URL
    :param token: User token used for connecting to the host
    :param project: Unique identifier of test project
    :param file_id: Unique identifier of associated file
    :param file_path: Local file to be uploaded and saved
    :returns: Associated key of uploaded file
    """

    # Setup the interface to tator
    tator_api = tator.get_api(host=host, token=token)

    # Create the temporary file
    fd, local_file = tempfile.mkstemp()
    try:
        with os.fdopen(fd, "w") as file_handle:
            file_handle.write("Yo!")

        # Upload the file
        logger.info(f"Created temporary file: {local_file}")
        for progress, upload_info in _upload_file(
            api=tator_api, project=project, path=local_file, file_id=file_id
        ):
            logger.info(f"Upload progress: {progress}%")

    finally:
        os.remove(local_file)

    return upload_info.key


def test_file_type_delete(host: str, token: str, project: int) -> None:
    # Setup the interface to Tator
    tator_api = tator.get_api(host=host, token=token)

    # Test creating FileType objects with all available fields
    response = tator_api.create_file_type(
        project=project,
        file_type_spec={
            "name": "file_type_with_attrs",
            "description": "Test file type with attributes",
            "project": project,
            "attribute_types": [{"name": "test_bool", "dtype": "bool", "default": True}],
        },
    )
    file_type = response.id
    assert file_type >= 0

    # Verify no files exist to start
    response = tator_api.get_file_list(project, type=file_type)
    assert len(response) == 0

    file_ids = []
    for idx in range(10):
        file_spec = {
            "name": f"File_A_{idx}",
            "description": "hey",
            "type": file_type,
            "attributes": {"test_bool": True},
        }
        response = tator_api.create_file(project=project, file_spec=file_spec)
        key = _upload_generic_file(
            host=host, token=token, project=project, file_id=response.id, file_path="test.data"
        )
        tator_api.update_file(id=response.id, file_update={"path": key})
        file_ids.append({"file_id": response.id, "key": key})

    assert len(file_ids) == 10

    # Verify list is the right length
    response = tator_api.get_file_list(project, type=file_type)
    assert len(response) == 10

    response = tator_api.delete_file_type(file_type)

    assert str(file_type) in response.message, "File type id not found in delete response"
    assert "10" in response.message, "File count not found in delete response"

    try:
        caught_it = False
        response = tator_api.get_file_list(project, type=file_type)
    except:
        caught_it=True
    finally:
        assert caught_it
