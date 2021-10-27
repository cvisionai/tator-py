
import logging
import os
import tempfile

import pytest
import tator
from tator.util._upload_file import _upload_file

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
        file_path: str="test.file"):
    """ Uploads the provided manifest file

    :param host: Project URL
    :param token: User token used for connecting to the host
    :param project: Unique identifier of test project
    :param file_path: Local file to be uploaded and saved
    :returns: Response from the save file endpoint
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
        for progress, upload_info in _upload_file(tator_api, project, local_file):
            logger.info(f"Upload progress: {progress}%")
        url = tator_api.get_download_info(project, {'keys': [upload_info.key]})[0].url

        # Save the uploaded file to the project using the save generic file endpoint
        spec = tator.models.GenericFileSpec(name=file_path, upload_url=url)
        response = tator_api.save_generic_file(project=project, generic_file_spec=spec)

    finally:
        os.remove(local_file)

    return response


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

def test_file_upload(
        host: str,
        token: str,
        project: int) -> None:
    """ Unit test for the SaveGenericFile endpoint

    Unit testing of the save file endpoint involvest the following:
    - Provide something where the upload file doesn't exist
    - Upload two of the same files (have the same name, but will result in two separate files)

    :param host: Project URL
    :param token: User token used for connecting to the host
    :param project: Unique identifier of test project
    """

    _missing_upload_file(host=host, token=token, project=project)

    response_1 = _upload_generic_file(
        host=host, token=token, project=project, file_path='test_nodupe.txt')
    response_2 = _upload_generic_file(
        host=host, token=token, project=project, file_path='test_nodupe.txt')

    assert "test_nodupe" in response_1.url
    assert "test_nodupe" in response_2.url
    assert response_1.url != response_2.url

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
        response = _upload_generic_file(
            host=host, token=token, project=project, file_path="test.data")
        file_url = response.url
        response = tator_api.create_file(project=project, file_spec=dict(
            name=f"File_A_{idx}",
            path=file_url,
            description="hey",
            meta=file_type_a_id,
            attributes=dict(
                LabelA=idx,
                LabelB="seeya"
            )
        ))
        file_a_ids.append(response.id)

    file_b_ids = []
    for idx in range(50):
        response = _upload_generic_file(
            host=host, token=token, project=project, file_path="test.data")
        file_url = response.url
        response = tator_api.create_file(project=project, file_spec=dict(
            name=f"File_B_{idx}",
            path=file_url,
            description="hey",
            meta=file_type_b_id,
            attributes=dict(
                LabelB="bye"
            )
        ))
        file_b_ids.append(response.id)
    file_b_url = file_url

    # Get all the files
    file_list = tator_api.get_file_list(project=project)
    file_a_count = 0
    file_b_count = 0
    for file_obj in file_list:
        if file_obj.id in file_a_ids:
            file_a_count += 1

        elif file_obj.id in file_b_ids:
            file_b_count += 1

    assert file_a_count == len(file_a_ids)
    assert file_b_count == len(file_b_ids)

    # Grab only the data associated with the FileTypes
    files = tator_api.get_file_list(project=project, meta=file_type_a_id)
    assert len(files) == len(file_a_ids)

    files = tator_api.get_file_list(project=project, meta=file_type_b_id, force_es=1)
    assert len(files) == len(file_b_ids)

    # Grab file objects matching the search string (force_es and not)
    files = tator_api.get_file_list(project=project, attribute=["LabelB::seeya"], force_es=0)
    assert len(files) == len(file_a_ids)

    files = tator_api.get_file_list(project=project, attribute=["LabelB::seeya"], force_es=1)
    assert len(files) == len(file_a_ids)

    files = tator_api.get_file_list(project=project, search="LabelB:seeya")
    assert len(files) == len(file_a_ids)
    
    # Update a bunch of the entries and verify the updates are valid and
    # the search still works correctly
    for current_id in file_a_ids:
        tator_api.update_file(id=current_id, file_update={
            "name": "new_name",
            "description": "new_description",
            "path": file_b_url,
            "attributes": {"LabelA": -100}
        })
    files = tator_api.get_file_list(project=project, meta=file_type_a_id)
    for file_obj in files:
        update_check = \
            file_obj.name == "new_name" and \
            file_obj.description == "new_description" and \
            file_b_url in file_obj.path and \
            file_obj.attributes["LabelA"] == -100 and \
            file_obj.attributes["LabelB"] == "seeya"
        if not update_check:
            print(file_obj)
            break

    assert update_check

    files = tator_api.get_file_list(project=project, search="LabelA:<0")
    assert len(files) == len(file_a_ids)

    # Check to see if pagination works
    page_size = 10
    num_pages = (len(file_b_ids) / page_size) - 1
    start = 0
    stop = page_size
    page = 0
    all_files = set()
    files = tator_api.get_file_list(project=project, meta=file_type_b_id, start=start, stop=stop, force_es=1)
    for file in files:
        all_files.add(file.id)
    while page < num_pages:
        after = max(all_files)
        files = tator_api.get_file_list(project=project, meta=file_type_b_id, start=start, stop=stop, after=after)
        if len(files) == 0:
            break
        for file in files:
            all_files.add(file.id)
        page += 1

    files = tator_api.get_file_list(project=project, meta=file_type_b_id, force_es=1)
    blah = [file.id for file in files]
    print(blah)
    print(all_files)
    print(file_b_ids)
    assert len(all_files) == len(file_b_ids)

    # Delete 2 entries from each file group. Verify they were deleted.
    tator_api.delete_file(id=file_a_ids[0])
    tator_api.delete_file(id=file_a_ids[-1])
    tator_api.delete_file(id=file_b_ids[0])
    tator_api.delete_file(id=file_b_ids[-1])
    file_list = tator_api.get_file_list(project=project)
    file_a_count = 0
    file_b_count = 0
    for file_obj in file_list:
        if file_obj.id in file_a_ids:
            file_a_count += 1

        elif file_obj.id in file_b_ids:
            file_b_count += 1

    assert file_a_count == len(file_a_ids) - 2
    assert file_b_count == len(file_b_ids) - 2