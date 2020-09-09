from uuid import uuid1
import mimetypes
import os
import math
import io
import tarfile

from tusclient.client import TusClient
from urllib.parse import urljoin
from urllib.parse import urlsplit

from .md5sum import md5sum

def upload_media_archive(api, project, paths, section="Test Section", chunk_size=2*1024*1024):
    """ Uploads multiple media files as an archive.

    Example:

    .. code-block:: python

        api = tator.get_api(host, token)
        for progress, response in tator.util.upload_media_archive(api, project_id, paths):
            print(f"Upload progress: {progress}%")
        print(response.message)

    :param api: :class:`tator.TatorApi` object.
    :param project: Unique integer identifying a project.
    :param paths: Path to a media archive or list of paths to media files.
    :param section: [Optional] Media section to upload to.
    :param chunk_size: [Optional] Chunk size in bytes. Default is 2MB.
    :returns: Generator that yields tuple containing progress (0-100) and a
        response. The response is `None` until the last yield, when the response
        is the response object from :meth:`tator.TatorApi.transcode`.
    """
    upload_uid = str(uuid1())
    upload_gid = str(uuid1())
    host = api.api_client.configuration.host
    token = api.api_client.configuration.api_key['Authorization']
    prefix = api.api_client.configuration.api_key_prefix['Authorization']
    tusURL = urljoin(host, "files/")
    tus = TusClient(tusURL, headers={'Authorization': f'{prefix} {token}',
                                     'Upload-Uid': f'{upload_uid}'})
    if isinstance(paths, list):
        in_mem_buf = io.BytesIO()
        in_mem_tar = tarfile.TarFile(mode='w', fileobj=in_mem_buf)
        for idx,fp in enumerate(paths):
            in_mem_tar.add(fp, os.path.basename(fp))

        uploader = tus.uploader(file_stream=in_mem_buf, chunk_size=chunk_size,
                                retries=10, retry_delay=15)
    else:
        file_buf = open(paths, 'rb')
        uploader = tus.uploader(file_stream=file_buf, chunk_size=chunk_size,
                                retries=10, retry_delay=15)
    last_progress = 0
    num_chunks=math.ceil(uploader.get_file_size()/chunk_size)
    yield (last_progress, None)
    for chunk_count in range(num_chunks):
        uploader.upload_chunk()
        this_progress = round((chunk_count / num_chunks) *100,1)
        if this_progress != last_progress:
            yield (this_progress, None)
            last_progress = this_progress

    # Initiate transcode.
    spec = {
        'type': -1, #Tar-based import
        'uid': upload_uid,
        'gid': upload_gid,
        'url': uploader.url,
        'name': "archive.tar",
        'section': section,
        'md5': "N/A",
    }
    response = api.transcode(project, transcode_spec=spec)
    yield (100, response)
