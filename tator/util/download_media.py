import os
import math

import requests

from ._download_file import _download_file
from ..openapi.tator_openapi.models import ImageDefinition, VideoDefinition

def _is_none_or_eq(variable, match):
    """  :returns: True if `variable` is None or equals `match` """
    return variable is None or variable == match

def _find_best_match(media_list, quality, codec_or_mime=None):
    """ Given a media list find the closest quality
        :param media_list: list of Media definitons either
                           :class:`tator.models.ImageDefinition` or
                           :class:`tator.models.VideoDefinition`.
        :param int quality: Vertical resolution to match (or None for best)
        :param str codec_or_mime: Specified codec or mime if multiple versions
                                  of 1 resolution exist. E.g. h264 or image/avif
    """
    # Without pulling in numpy we have to do this in an explicit loop
    available = [x.resolution[0] for x in media_list]

    match_idx = -1
    best_quality = max(available)
    quality = best_quality if quality is None else quality
    best_distance = best_quality+1
    for idx,val in enumerate(available):
        # Bounce out of any non matching codecs
        if codec_or_mime:
            media_info = media_list[idx]
            if type(media_info) == ImageDefinition and media_info.mime != codec_or_mime:
                continue
            if type(media_info) == VideoDefinition and media_info.codec != codec_or_mime:
                continue
        distance = abs(val-quality)
        if distance < best_distance:
            best_distance = distance
            match_idx = idx

    assert match_idx >= 0, "Unable to find match"

    return match_idx

def download_media(api, media, out_path, quality=None,media_type=None, codec_or_mime=None):
    """ Download a media file from Tator to an off-line location.

    Example:

    .. code-block:: python

        api = tator.get_api(host, token)
        media = api.get_media(media_id)
        out_path = f'/tmp/{media.name}'
        for progress in tator.util.download_media(api, media, out_path):
            print(f"Download progress: {progress}%")

        #download 720p version streaming
        for progress in tator.util.download_media(api,
                                                  media,
                                                  out_path,
                                                  720,
                                                  'streaming'):
            print(f"Download progress: {progress}%")


    :param api: :class:`tator.TatorApi` object.
    :param media: :class:`tator.Media` object.
    :param path-like out_path: Path to where to download.
    :param int quality: Attempts to fetch this resolution (defaults to best)
    :param str media_type: The desired item to download (archival, streaming,
                           image, thumbnail, or thumbnail_gif). Not all types
                           are valid for all media.
    :param str codec_or_mime: The desired codec or mime if multiple exist at
                              the same resolution. e.g. h264 for video or image/jpeg for images.
    :returns: Generator the yields progress (0-100).
    """
    assert media_type in [None,
                          'streaming',
                          'archival',
                          'image',
                          'thumbnail',
                          'thumbnail_gif']

    if media.media_files is not None:
        archival = media.media_files.archival
        archival = archival if archival else []
        streaming = media.media_files.streaming
        streaming = streaming if streaming else []
        image = media.media_files.image
        thumbnail = media.media_files.thumbnail
        thumbnail_gif = media.media_files.thumbnail_gif

        if _is_none_or_eq(media_type,"archival") and len(archival) > 0:
            url = archival[_find_best_match(archival,quality, codec_or_mime)].path
        elif _is_none_or_eq(media_type,"streaming") and len(streaming) > 0:
            url = streaming[_find_best_match(streaming,quality, codec_or_mime)].path
        elif _is_none_or_eq(media_type,"image") and image:
            url = image[_find_best_match(image,quality, codec_or_mime)].path
        elif media_type == "thumbnail":
            url = thumbnail[_find_best_match(thumbnail,quality)].path
        elif media_type == "thumbnail_gif":
            url = thumbnail_gif[_find_best_match(thumbnail_gif,quality)].path
        else:
            assert False, f"Unable to deduce download file media={media.id}"
    else:
        # Legacy way of using streaming prior to streaming
        # and images
        url = f"/media/{media.file}"
        if media.original:
            url = f"/data/raw/{media.original}"

    return _download_file(api, media.project, url, out_path)
