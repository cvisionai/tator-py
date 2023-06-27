
import logging
import os
import requests
import tempfile

import pytest
import tator
from tator.util._upload_file import _upload_file
import json
import base64

logger = logging.getLogger(__name__)

def _missing_upload_file(
        host: str,
        token: str,
        project: int) -> None:
    """ Test missing upload file for SaveGenericFile endpoint

    :param host: Project URL
    :param token: User token used for connecting to the host
    :param project: Unique identifier of test project
    """

    tator_api = tator.get_api(host=host, token=token)
    spec = tator.models.GenericFileSpec(name="test.file", upload_url="not_there")
    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        tator_api.save_generic_file(project=project, generic_file_spec=spec)

def _upload_generic_file(
        host: str,
        token: str,
        project: int,
        file_id: int,
        file_path: str="test.file"):
    """ Uploads the provided manifest file

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
        with os.fdopen(fd, 'w') as file_handle:
            file_handle.write("Yo!")

        # Upload the file
        logger.info(f"Created temporary file: {local_file}")
        for progress, upload_info in _upload_file(api=tator_api, project=project, path=local_file, file_id=file_id):
            logger.info(f"Upload progress: {progress}%")

    finally:
        os.remove(local_file)

    return upload_info.key

def _make_all_attribute_types() -> list:
    """ Taken from conftest.py
    :returns: One of each possible attribute dtype with generic values
    """
    return [
        dict(
            name='test_bool',
            dtype='bool',
            default=True,
        ),
        dict(
            name='test_int',
            dtype='int',
            default=0,
            minimum=-1000,
            maximum=1000,
        ),
        dict(
            name='test_float',
            dtype='float',
            default=0.0,
            minimum=-1000.0,
            maximum=1000.0,
        ),
        dict(
            name='test_enum',
            dtype='enum',
            choices=['a', 'b', 'c'],
            default='a',
        ),
        dict(
            name='test_string',
            dtype='string',
            default='asdf',
        ),
        dict(
            name='test_datetime',
            dtype='datetime',
            use_current=True,
        ),
        dict(
            name='test_geopos',
            dtype='geopos',
            default=[-179.0, -89.0],
        ),
        dict(
            name='test_float_array',
            dtype='float_array',
            default=[0.0, 0.0, 0.0],
            size=3,
        )
    ]

def test_file_type_crud(
        host: str,
        token: str,
        project: int) -> None:
    """ Test the get, post, patch, and delete FileType endpoints

    :param host: Project URL
    :param token: User token used for connecting to the host
    :param project: Unique identifier of test project

    """

    # Setup the interface to Tator
    tator_api = tator.get_api(host=host, token=token)

    # Test creating FileType objects with all available fields
    response = tator_api.create_file_type(project=project, file_type_spec={
        "name": "file_type_with_attrs",
        "description": "Test file type with attributes",
        "project": project,
        "attribute_types": _make_all_attribute_types()
    })
    file_type_id_1 = response.id
    assert file_type_id_1 >= 0

    # Test creating FileType object without attribute and description
    response = tator_api.create_file_type(project=project, file_type_spec={
        "name": "file_type_without_attrs",
        "project": project,
    })
    file_type_id_2 = response.id
    assert file_type_id_2 >= 0

    # Test retrieval by ID and list
    files_types = tator_api.get_file_type_list(project=project)
    found_file_type_id_1 = False
    found_file_type_id_2 = False
    for file_type in files_types:
        if file_type.id == file_type_id_1:
            found_file_type_id_1 = True
        elif file_type.id == file_type_id_2:
            found_file_type_id_2 = True

    assert found_file_type_id_1
    assert found_file_type_id_2

    file_type = tator_api.get_file_type(id=file_type_id_1)
    assert file_type.id == file_type_id_1

    file_type = tator_api.get_file_type(id=file_type_id_2)
    assert file_type.id == file_type_id_2

    # Update the FileType object
    tator_api.update_file_type(id=file_type_id_2, file_type_update={
        "name": "Another name",
        "description": "Another description"
    })
    file_type = tator_api.get_file_type(id=file_type_id_2)
    assert file_type.name == "Another name"
    assert file_type.description == "Another description"

    # Test deleting
    tator_api.delete_file_type(id=file_type_id_2)

    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        file_type = tator_api.get_file_type(id=file_type_id_2)

def test_file_crud(
        host: str,
        token: str,
        project: int) -> None:
    """ Test the get, post, patch, and delete File endpoints. Also test attribute type updates.

    :param host: Project URL
    :param token: User token used for connecting to the host
    :param project: Unique identifier of test project

    FileTypeA
    LabelA - string dtype
    LabelB - int dtype

    FileTypeB
    LabelA - string dtype

    This will have 10 different File objects with FileType - A.
    This will have 100 different File objects with FileType - B.

    """

    # Setup the interface to Tator
    tator_api = tator.get_api(host=host, token=token)

    # Create two FileTypes so we can test searching
    response = tator_api.create_file_type(project=project, file_type_spec={
        "name": "file_type_without_attrs",
        "project": project,
        "attribute_types": [
            dict(
                name="LabelA",
                dtype="int",
                default=0,
                minimum=-1000,
                maximum=1000,
            ),
            dict(
                name="LabelB",
                dtype="string",
                default="",
            ),
        ]
    })
    file_type_a_id = response.id

    response = tator_api.create_file_type(project=project, file_type_spec={
        "name": "file_type_without_attrs",
        "project": project,
        "attribute_types": [
            dict(
                name="LabelA",
                dtype="int",
                default=0,
                minimum=-1000,
                maximum=1000,
            ),
            dict(
                name="LabelB",
                dtype="string",
                default="",
            ),
        ]
    })
    file_type_b_id = response.id

    # Create the files of each type
    file_a_ids = []
    for idx in range(10):
        response = tator_api.create_file(project=project, file_spec=dict(
            name=f"File_A_{idx}",
            description="hey",
            type=file_type_a_id,
            attributes=dict(
                LabelA=idx,
                LabelB="seeya"
            )
        ))
        key = _upload_generic_file(
            host=host, token=token, project=project, file_id=response.id, file_path="test.data")
        tator_api.update_file(id=response.id, file_update={"path": key})
        file_a_ids.append({
            "file_id": response.id,
            "key": key
        })

    file_b_ids = []
    for idx in range(50):
        response = tator_api.create_file(project=project, file_spec=dict(
            name=f"File_B_{idx}",
            description="hey",
            type=file_type_b_id,
            attributes=dict(
                LabelB="bye"
            )
        ))
        key = _upload_generic_file(
            host=host, token=token, project=project, file_id=response.id, file_path="test.data")
        tator_api.update_file(id=response.id, file_update={"path": key})
        file_b_ids.append({
            "file_id": response.id,
            "key": key
        })

    # Get all the files
    file_list = tator_api.get_file_list(project=project)
    file_a_count = 0
    file_b_count = 0
    for file_obj in file_list:
        for file_info in file_a_ids:
            if file_obj.id == file_info["file_id"]:
                file_a_count += 1
                break

        for file_info in file_b_ids:
            if file_obj.id == file_info["file_id"]:
                file_b_count += 1
                break

    assert file_a_count == len(file_a_ids)
    assert file_b_count == len(file_b_ids)

    # Grab only the data associated with the FileTypes
    files = tator_api.get_file_list(project=project, type=file_type_a_id)
    assert len(files) == len(file_a_ids)

    files = tator_api.get_file_list(project=project, type=file_type_b_id)
    assert len(files) == len(file_b_ids)

    files = tator_api.get_file_list(project=project, attribute=["LabelB::seeya"])
    assert len(files) == len(file_a_ids)

    blob=base64.b64encode(json.dumps({'attribute': 'LabelB', 'operation': 'eq', 'value': 'seeya'}).encode('ascii'))
    files = tator_api.get_file_list(project=project, encoded_search=blob)
    assert len(files) == len(file_a_ids)

    # Update a bunch of the entries and verify the updates are valid and
    # the search still works correctly
    for info in file_a_ids:
        current_id = info["file_id"]
        tator_api.update_file(id=current_id, file_update={
            "name": "new_name",
            "description": "new_description",
            "attributes": {"LabelA": -100}
        })
    files = tator_api.get_file_list(project=project, type=file_type_a_id)
    for file_obj in files:
        update_check = \
            file_obj.name == "new_name" and \
            file_obj.description == "new_description" and \
            file_obj.attributes["LabelA"] == -100 and \
            file_obj.attributes["LabelB"] == "seeya"
        if not update_check:
            print(file_obj)
            break

    assert update_check

    blob=base64.b64encode(json.dumps({'attribute': 'LabelA', 'operation': 'lt', 'value': 0}).encode('ascii'))
    files = tator_api.get_file_list(project=project, encoded_search=blob)
    assert len(files) == len(file_a_ids)

    # Check to see if pagination works
    page_size = 10
    num_pages = (len(file_b_ids) / page_size) - 1
    start = 0
    stop = page_size
    page = 0
    all_files = set()
    files = tator_api.get_file_list(project=project, type=file_type_b_id, start=start, stop=stop)
    for file in files:
        all_files.add(file.id)
    files = tator_api.get_file_list(project=project, type=file_type_b_id, start=start+(page*page_size), stop=stop+(page*page_size))
    while files:
        for file in files:
            all_files.add(file.id)
        page += 1
        files = tator_api.get_file_list(project=project, type=file_type_b_id, start=start+(page*page_size), stop=stop+(page*page_size))

    files = tator_api.get_file_list(project=project, type=file_type_b_id)
    blah = [file.id for file in files]
    assert len(all_files) == len(file_b_ids)

    # Delete 2 entries from each file group. Verify they were deleted.
    tator_api.delete_file(id=file_a_ids[0]["file_id"])
    tator_api.delete_file(id=file_a_ids[-1]["file_id"])
    tator_api.delete_file(id=file_b_ids[0]["file_id"])
    tator_api.delete_file(id=file_b_ids[-1]["file_id"])
    file_list = tator_api.get_file_list(project=project)
    file_a_count = 0
    file_b_count = 0
    for file_obj in file_list:
        for file_info in file_a_ids:
            if file_obj.id == file_info["file_id"]:
                file_a_count += 1
                break

        for file_info in file_b_ids:
            if file_obj.id == file_info["file_id"]:
                file_b_count += 1
                break

    assert file_a_count == len(file_a_ids) - 2
    assert file_b_count == len(file_b_ids) - 2


def test_upload_generic_file(host, token, project):
    TEST_STR = b"foo"
    # Setup the interface to Tator
    tator_api = tator.get_api(host=host, token=token)

    # Create a FileType
    response = tator_api.create_file_type(
        project=project,
        file_type_spec={
            "name": "generic_upload_file_type",
            "project": project,
            "attribute_types": [
                {"name": "test", "dtype": "int", "default": 0, "minimum": -1000, "maximum": 1000}
            ],
        },
    )
    type_id = response.id

    # Create a file locally and test uploading/downloading
    with tempfile.NamedTemporaryFile() as temp_file:
        path = temp_file.name
        fname = os.path.basename(path)

        temp_file.write(TEST_STR)
        temp_file.flush()

        for progress, response in tator.util.upload_generic_file(tator_api, type_id, path, "File description", fname):
            print(f"Progress: {progress}%")
    assert response.name == fname
    download_info = tator_api.get_download_info(project=project, download_info_spec={"keys": [response.path]})

    assert len(download_info) == 1
    assert download_info[0].key == response.path
    response = requests.get(download_info[0].url, stream=True)
    assert response.content == TEST_STR
