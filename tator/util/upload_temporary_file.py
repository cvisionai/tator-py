import os
import math

from tusclient.client import TusClient
from urllib.parse import urljoin
from urllib.parse import urlsplit

from .md5sum import md5sum

def upload_temporary_file(api, project, path, lookup=None, hours=24,
                          name=None, chunk_size=100*1024*1024):
    """ Upload a file to the temporary file storage location.

    :param api: :class:`tator.TatorApi` object.
    :param project: Unique integer identifying a project.
    :param path: Path to the file.
    :param lookup: [Optional] md5hash of lookup parameters.
    :param hours: [Optional] Number of hourse file is kept alive. Default is 24.
    :param name: [Optional] Name of temporary file in database. Defaults to basename of path.
    :param chunk_size: [Optional] Chunk size in bytes. Default is 100MB.
    """
    if name is None:
        name = os.path.basename(path)

    if lookup is None:
        lookup = name

    host = api.api_client.configuration.host
    tusURL = urljoin(host, "files/")
    tus = TusClient(tusURL)
    uploader = tus.uploader(path, chunk_size=chunk_size,
                            retries=10, retry_delay=15)
    num_chunks=math.ceil(uploader.get_file_size()/chunk_size)
    for _ in range(num_chunks):
        uploader.upload_chunk()

    response = api.create_temporary_file(project, temporary_file_spec={
        "url": uploader.url,
        "name": name,
        "lookup": lookup,
        "hours": 24,
    })

