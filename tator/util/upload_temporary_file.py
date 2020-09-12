import os
import math
from uuid import uuid1

from tusclient.client import TusClient
from urllib.parse import urljoin
from urllib.parse import urlsplit

from .md5sum import md5sum

def upload_temporary_file(api, project, path, lookup=None, hours=24,
                          name=None, chunk_size=100*1024*1024):
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

    host = api.api_client.configuration.host
    token = api.api_client.configuration.api_key['Authorization']
    prefix = api.api_client.configuration.api_key_prefix['Authorization']
    tusURL = urljoin(host, "files/")
    tus = TusClient(tusURL, headers={'Authorization': f'{prefix} {token}',
                                     'Upload-Uid': f'{str(uuid1())}'})
    uploader = tus.uploader(path, chunk_size=chunk_size,
                            retries=10, retry_delay=15)
    last_progress = 0
    yield (last_progress, None)
    num_chunks=math.ceil(uploader.get_file_size()/chunk_size)
    for chunk_count in range(num_chunks):
        uploader.upload_chunk()
        this_progress = round((chunk_count / num_chunks) *100,1)
        if this_progress != last_progress:
            yield (this_progress, None)
            last_progress = this_progress

    response = api.create_temporary_file(project, temporary_file_spec={
        "url": uploader.url,
        "name": name,
        "lookup": lookup,
        "hours": 24,
    })
    yield (100, response)

