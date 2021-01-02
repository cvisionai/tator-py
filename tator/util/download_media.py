import os
import math

import requests

from ._download_file import _download_file

def download_media(api, media, out_path):
    """ Download a media file from Tator to an off-line location.

    Example:

    .. code-block:: python

        api = tator.get_api(host, token)
        media = api.get_media(media_id)
        out_path = f'/tmp/{media.name}'
        for progress in tator.util.download_media(api, media, out_path):
            print(f"Download progress: {progress}%")

    :param api: :class:`tator.TatorApi` object.
    :param media: :class:`tator.Media` object.
    :param path-like out_path: Path to where to download.
    :returns: Generator the yields progress (0-100).
    """
    if media.media_files is not None:
        archival = media.media_files.archival
        streaming = media.media_files.streaming
        image = media.media_files.image
        if archival and len(archival) > 0:
            url = archival[0].path
        elif streaming and len(streaming) > 0:
            url = streaming[0].path
        elif image:
            url = image[0].path
    else:
        # Legacy way of using streaming prior to streaming
        # and images
        url = f"/media/{media.file}"
        if media.original:
            url = f"/data/raw/{media.original}"

    return _download_file(api, media.project, url, out_path)
