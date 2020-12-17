from uuid import uuid1
import mimetypes
import os
import math
import tempfile
import logging

import requests

from .md5sum import md5sum

logger = logging.getLogger(__name__)

def _hosted_md5(url):
    """ Downloads only enough of file to compute md5 of first part of file
        to a temporary path, then returns md5.
    """
    CHUNK_SIZE = 2 * 1024 * 1024
    MAX_CHUNKS = 5 # Download a maximum of 10MB.
    MAX_RETRIES = 10
    for attempt in range(MAX_RETRIES):
        try:
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                total_size = int(r.headers['Content-Length'])
                total_chunks = math.ceil(total_size / CHUNK_SIZE)
                chunk_count = 0
                with tempfile.NamedTemporaryFile(mode='wb') as temp:
                    for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                        if chunk:
                            chunk_count += 1
                            temp.write(chunk)
                        if chunk_count >= MAX_CHUNKS:
                            break
                    # Compute the md5 using file size from header and first 100MB.
                    md5 = md5sum(temp.name, total_size)
            break
        except Exception as ex:
            print(ex)
            logger.info(f"Failed to download {url} on attempt {attempt}...")
            pass
    return md5

def import_media(api, type_id, url, md5=None, section=None, fname=None,
                 upload_gid=None, upload_uid=None,chunk_size=2*1024*1024,
                 attributes=None, media_id=None):
    """ Imports a hosted media file.

    Example:

    .. code-block:: python

        api = tator.get_api(host, token)
        response = tator.util.import_media(api, type_id, url)
        print(response.message)

    :param api: :class:`tator.TatorApi` object.
    :param type_id: Unique integer identifying a media type.
    :param url: URL of the hosted media file.
    :param md5: [Optional] md5 sum of the media.
    :param section: [Optional] Media section to upload to.
    :param fname: [Optional] Filename to use for upload.
    :param upload_gid: [Optional] Group ID of the upload.
    :param upload_uid: [Optional] Unique ID of the upload.
    :param chunk_size: [Optional] Chunk size in bytes. Default is 2MB.
    :param attributes: [Optional] Attributes to apply to media object.
    :param media_id: [Optional] Unique ID of existing media object.
    :returns: Generator that yields tuple containing progress (0-100) and a
        response. The response is `None` until the last yield, when the response
        is the response object from :meth:`tator.TatorApi.create_media` or 
        :meth:`tator.TatorApi.transcode`.
    """
    if md5==None:
        # To compute md5, download the first 10MB to temporary file.
        md5 = _hosted_md5(url)
    if upload_uid is None:
        upload_uid = str(uuid1())
    if upload_gid is None:
        upload_gid = str(uuid1())
    if fname is None:
        fname=os.path.basename(url)
    if section is None:
        section="Imported Files"

    host = api.api_client.configuration.host
    token = api.api_client.configuration.api_key['Authorization']
    prefix = api.api_client.configuration.api_key_prefix['Authorization']
    mime,_ = mimetypes.guess_type(fname)
    response = api.get_media_type(type_id)
    project_id = response.project
    spec = {
        'type': type_id,
        'uid': upload_uid,
        'gid': upload_gid,
        'url': url,
        'name': fname,
        'section': section,
        'md5': md5,
        'attributes': attributes,
        'media_id': media_id,
    }
    # Initiate transcode.
    if mime.find('video') >= 0:
        response = api.transcode(project_id, transcode_spec=spec)
    else:
        raise NotImplementedError("Media import not supported for images.")
    return response
