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

    :param api: :class:`tator.TatorApi` object.
    :param project: Unique integer identifying a project.
    :param paths: List of paths to the media files.
    :param section: [Optional] Media section to upload to.
    :param chunk_size: [Optional] Chunk size in bytes. Default is 2MB.
    :returns: Response object from :meth:`tator.TatorApi.save_video` or
        :meth:`tator.TatorApi.transcode`.
    """
    upload_uid = str(uuid1())
    upload_gid = str(uuid1())
    in_mem_buf = io.BytesIO()
    host = api.api_client.configuration.host
    tusURL = urljoin(host, "files/")
    tus = TusClient(tusURL)
    in_mem_tar = tarfile.TarFile(mode='w', fileobj=in_mem_buf)
    for idx,fp in enumerate(paths):
        in_mem_tar.add(fp, os.path.basename(fp))

    uploader = tus.uploader(file_stream=in_mem_buf, chunk_size=chunk_size,
                            retries=10, retry_delay=15)
    last_progress = 0
    num_chunks=math.ceil(uploader.get_file_size()/chunk_size)
    for chunk_count in range(num_chunks):
        uploader.upload_chunk()
        this_progress = round((chunk_count / num_chunks) *100,1)
        if this_progress != last_progress:
            last_progress = this_progress

    # Initiate transcode.
    spec = {
        'type': -1, #Tar-based inport
        'uid': upload_uid,
        'gid': upload_gid,
        'url': uploader.url,
        'name': "archive.tar",
        'section': section,
        'md5': "N/A",
    }
    response = api.transcode(project, transcode_spec=spec)
    return response
