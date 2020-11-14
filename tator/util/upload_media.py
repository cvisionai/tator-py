from uuid import uuid1
import mimetypes
import os
import math

from tusclient.client import TusClient
from urllib.parse import urljoin

from .md5sum import md5sum

def upload_media(api, type_id, path, md5=None, section=None, fname=None,
                 upload_gid=None, upload_uid=None,chunk_size=2*1024*1024,
                 attributes=None, media_id=None):
    """ Uploads a single media file.

    Example:

    .. code-block:: python

        api = tator.get_api(host, token)
        for progress, response in tator.util.upload_media(api, type_id, path):
            print(f"Upload progress: {progress}%")
        print(response.message)

    :param api: :class:`tator.TatorApi` object.
    :param type_id: Unique integer identifying a media type.
    :param path: Path to the media file.
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
        md5 = md5sum(path)
    if upload_uid is None:
        upload_uid = str(uuid1())
    if upload_gid is None:
        upload_gid = str(uuid1())
    if fname is None:
        fname=os.path.basename(path)
    if section is None:
        section="New Files"

    host = api.api_client.configuration.host
    token = api.api_client.configuration.api_key['Authorization']
    prefix = api.api_client.configuration.api_key_prefix['Authorization']
    tusURL = urljoin(host, "files/")
    tus = TusClient(tusURL, headers={'Authorization': f'{prefix} {token}',
                                     'Upload-Uid': f'{upload_uid}'})
    uploader = tus.uploader(path, chunk_size=chunk_size,
                            retries=10, retry_delay=15)
    num_chunks=math.ceil(uploader.get_file_size()/chunk_size)

    last_progress = 0
    yield (last_progress, None)

    for chunk_count in range(num_chunks):
        uploader.upload_chunk()
        this_progress = round((chunk_count / num_chunks) *100,1)
        if this_progress != last_progress:
            yield (this_progress, None)
            last_progress = this_progress

    mime,_ = mimetypes.guess_type(fname)
    response = api.get_media_type(type_id)
    project_id = response.project
    spec = {
        'type': type_id,
        'uid': upload_uid,
        'gid': upload_gid,
        'url': uploader.url,
        'name': fname,
        'section': section,
        'md5': md5,
        'attributes': attributes,
        'media_id': media_id,
    }
    # Initiate transcode or save image.
    if mime.find('video') >= 0:
        response = api.transcode(project_id, transcode_spec=spec)
    else:
        response = api.create_media(project_id, media_spec=spec)
    yield (100, response)
