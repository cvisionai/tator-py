from uuid import uuid1
import mimetypes
import os
import math
import io
import tarfile
import tempfile

from urllib.parse import urljoin
from urllib.parse import urlsplit

from ._upload_file import _upload_file
from .md5sum import md5sum

def upload_media_archive(api, project, paths, section="Test Section", chunk_size=10*1024*1024):
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
    if isinstance(paths, list):
        fobj = tempfile.NamedTemporaryFile(delete=False)    
        in_mem_tar = tarfile.TarFile(mode='w', fileobj=fobj)
        for idx, fp in enumerate(paths):
            in_mem_tar.add(fp, os.path.basename(fp))
        fobj.close()
        path = fobj.name
    else:
        path = paths
    for progress, upload_info in _upload_file(api, project, path):
        yield (progress, None)
    url = api.get_download_info(project, {'keys': [upload_info.key]})[0].url

    # Initiate transcode.
    spec = {
        'type': -1, #Tar-based import
        'uid': upload_uid,
        'gid': upload_gid,
        'url': url,
        'name': "archive.tar",
        'section': section,
        'md5': "N/A",
        'size': os.stat(path).st_size,
    }
    response = api.transcode(project, transcode_spec=spec)
    yield (100, response)
