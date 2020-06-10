from uuid import uuid1
import mimetypes
import os
import math

from tusclient.client import TusClient
from urllib.parse import urljoin
from urllib.parse import urlsplit

from .md5sum import md5sum

def upload_media(api, type_id, path, md5=None, section=None, fname=None,
                 upload_gid=None, upload_uid=None, chunk_size=2*1024*1024):
    """ Uploads a single media file.

    :param api: :class:`tator.TatorApi` object.
    :param type_id: Unique integer identifying a media type.
    :param path: Path to the media file.
    :param md5: [Optional] md5 sum of the media.
    :param section: [Optional] Media section to upload to.
    :param fname: [Optional] Filename to use for upload.
    :param upload_gid: [Optional] Group ID of the upload.
    :param upload_uid: [Optional] Unique ID of the upload.
    :param chunk_size: [Optional] Chunk size in bytes. Default is 2MB.
    :returns: Response object from :meth:`tator.TatorApi.save_video` or 
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
    tusURL = urljoin(host, "files/")
    tus = TusClient(tusURL)
    uploader = tus.uploader(path, chunk_size=chunk_size,
                            retries=10, retry_delay=15)
    num_chunks=math.ceil(uploader.get_file_size()/chunk_size)

    last_progress = 0

    for chunk_count in range(num_chunks):
        uploader.upload_chunk()
        this_progress = round((chunk_count / num_chunks) *100,1)
        if this_progress != last_progress:
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
    }
    # Initiate transcode or save image.
    if mime.find('video') >= 0:
        response = api.transcode(project_id, transcode_spec=spec)
    else:
        response = api.save_image(project_id, image_spec=spec)
    return response
