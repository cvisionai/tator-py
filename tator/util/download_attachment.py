import os
import math

from ._download_file import _download_file

def _is_none_or_eq(variable, match):
    """  :returns: True if `variable` is None or equals `match` """
    return variable is None or variable == match

def download_attachment(api, media, out_path, index=0):
    """ Download an attachment from Tator to an off-line location.

    Example:

    .. code-block:: python

        api = tator.get_api(host, token)
        media = api.get_media(media_id)
        out_path = f'/tmp/{media.name}'
        for progress in tator.util.download_attachment(api, media, out_path):
            print(f"Download progress: {progress}%")

        #download second attachment
        for progress in tator.util.download_attachment(api, media, out_path, index=1):
            print(f"Download progress: {progress}%")

    :param api: :class:`tator.TatorApi` object.
    :param media: :class:`tator.Media` object.
    :param path-like out_path: Path to where to download.
    :param index: Integer indicating which attachment to download.
    :returns: Generator that yields progress (0-100).
    """
    if media.media_files is not None:
        attachment = media.media_files.attachment
        if (attachment is None) or (len(attachment) <= index):
            raise ValueError(f"Media {media.id} does not have an attachment at index {index}!")
        else:
            url = attachment[index].path
    return _download_file(api, media.project, url, out_path)

