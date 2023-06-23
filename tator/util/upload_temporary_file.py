import os

from ._upload_file import _upload_file

def upload_temporary_file(
    api, project, path, lookup=None, hours=24, name=None, chunk_size=100*1024*1024
):
    """ Upload a file to the temporary file storage location.

    Example:

    .. code-block:: python

        api = tator.get_api(host, token)
        for progress, response in tator.util.upload_temporary_file(api, project_id, path):
            print(f"Upload progress: {progress}%")
        print(response.message)

    :param api: :class:`tator.TatorApi` object.
    :param project: Unique integer identifying a project.
    :param path: Path to the file.
    :param lookup: [Optional] md5hash of lookup parameters.
    :param hours: [Optional] Number of hourse file is kept alive. Default is 24.
    :param name: [Optional] Name of temporary file in database. Defaults to basename of path.
    :param chunk_size: [Optional] Chunk size in bytes. Default is 100MB.
    :returns: Generator that yields tuple containing progress (0-100) and a
        response. The response is `None` until the last yield, when the response
        is the response object from :meth:`tator.util.TatorApi.create_temporary_file`.
    """
    if name is None:
        name = os.path.basename(path)

    if lookup is None:
        lookup = name

    for progress, upload_info in _upload_file(api, project, path, chunk_size=chunk_size):
        yield (progress, None)
    url = api.get_download_info(project, {'keys': [upload_info.key]})[0].url

    response = api.create_temporary_file(
        project, temporary_file_spec={"url": url, "name": name, "lookup": lookup, "hours": hours}
    )
    yield (100, response)
