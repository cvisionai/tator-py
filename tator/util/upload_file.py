import math
import os
import shutil

from tusclient.client import TusClient
from urllib.parse import urljoin

import tator
import tator_openapi

def upload_file(
        api: tator_openapi.api.tator_api.TatorApi,
        project: int,
        path: str,
        chunk_size: int=100*1024*1024) -> str:
    """ Uploads the given file to the upload area of the specified tator server

    Args:
        api: Interface to tator server
        project: Unique project identifier
        path: Local path to file to be uploaded (but won't be saved to specific media/project)
        chunk_size: Bytes to upload per chunk via tus

    Returns:
        Generator that yields tuple containing progress (0-100) and a response.
        The response is `None~ until the last yield, when the response
        is the name of the uploaded file
    """

    # Note: This code was duplicated from upload_temporary_file.py
    # #TODO Should this just use the same code?
    host = api.api_client.configuration.host
    tusURL = urljoin(host, "files/")
    tus = TusClient(tusURL)
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

    yield (100, uploader.url)