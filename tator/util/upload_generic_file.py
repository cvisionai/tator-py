import os

from ._upload_file import _upload_file


def upload_generic_file(
    api, file_type, path, description, name=None, attributes=None, timeout=None
):
    """Upload a file to the File storage location.

    Example:

    .. code-block:: python

        api = tator.get_api(host, token)
        for progress, response in tator.util.upload_generic_file(api, project_id, path):
            print(f"Upload progress: {progress}%")
        print(response)

    :param api: :class:`tator.TatorApi` object.
    :param file_type: Unique integer identifying a `FileType`.
    :param path: Path to the file.
    :param description: Description of the file to be uploaded.
    :param name: [Optional] Name of temporary file in database. Defaults to basename of path.
    :param attributes: [Optional] Attributes to set on the uploaded file.
    :param timeout: [Optional] Timeout for the :meth:`tator.util._upload_file._upload_file`
                    operation.
    :returns: Generator that yields tuple containing progress (0-100) and a response. The response
              is `None` until the last yield, when the response is the updated response object from
              :meth:`tator.util.TatorApi.get_file`.
    """
    project = api.get_file_type(file_type).project
    if name is None:
        name = os.path.basename(path)
    file_spec = {"name": name, "type": file_type, "description": description}
    if attributes is not None:
        file_spec["attributes"] = attributes

    response = api.create_file(project=project, file_spec=file_spec)
    file_id = response.id
    upload_kwargs = {
        "api": api,
        "project": project,
        "path": path,
        "file_id": file_id,
    }
    if timeout is not None:
        upload_kwargs["timeout"] = timeout

    for progress, upload_info in _upload_file(**upload_kwargs):
        yield (progress, None)

    api.update_file(id=file_id, file_update={"path": upload_info.key})
    response = api.get_file(file_id)
    yield (100, response)
