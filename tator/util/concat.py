import math
import os
import requests
import subprocess
import tempfile
import logging
from uuid import uuid1

from PIL import Image

from .md5sum import md5sum
from .download_media import download_media
from ._upload_file import _upload_file
from ._download_file import _download_file
from ..openapi.tator_openapi.models import MessageResponse

logger = logging.getLogger(__name__)

def make_concat(api, name, media_ids, section, offsets=None):
    """ Uploads a single media file.

    :param api: :class:`tator.TatorApi` object.
    :param name: Name of the file to use
    :param media_ids: List of media_ids to multi-stream
    :param section: Section name. If this section does not exist it will be created.
    :param offsets: Section name. If this section does not exist it will be created.
    :returns: Response from media object creation.
    """
    media_obj = api.get_media(media_ids[0], presigned=86400)
    type_id = media_obj.type;
    project = media_obj.project;
    # if offsets aren't supplied make them
    all_media = api.get_media_list_by_id(project, {"ids": media_ids})

    # use a concat extension
    name += ".concat"
   
    # Fetch the section. If it does not exist, create it. 
    sections = api.get_section_list(project, name=section)
    if len(sections) == 0:
        section_spec = {'name': section, 'tator_user_sections': str(uuid1())}
        response = api.create_section(project, section_spec=section_spec)
        section_obj = api.get_section_list(project, name=section)[0]
    else:
        section_obj = sections[0]


    attributes={}
    if section:
        attributes.update({"tator_user_sections": section_obj.tator_user_sections})

    if offsets == None:
        offsets = [0]
        for media in all_media[0:len(all_media)-1]:
            offsets.append(media.num_frames / media.fps)


    md5 = media_obj.md5 # doesn't matter
    media_spec = {'attributes': attributes,
                  'name': name,
                  'md5': md5,
                  'section': section_obj.name,
                  'fps': media_obj.fps,
                  'num_frames': media_obj.num_frames,
                  'type': type_id,
                  'width': media_obj.width,
                  'height': media_obj.height}

    resp = api.create_media_list(project, [media_spec])
    print(f"Created {resp.id[0]}")

    # Copy thumbnails from first media
    with tempfile.TemporaryDirectory() as d:
        thumb_path = os.path.join(d,'tiled_thumb.jpg')
        thumb_gif_path = os.path.join(d,'tiled_gif.gif')

        for progress in download_media(api, media_obj, thumb_path, None, 'thumbnail'):
            pass
        for progress in download_media(api, media_obj, thumb_gif_path, None, 'thumbnail_gif'):
            pass

        for progress, thumbnail_info in _upload_file(api, project, thumb_path,
                                                     media_id=resp.id[0], filename='tiled_thumb.jpg'):
            logger.info(f"Thumbnail upload progress: {progress}%")
        for progress, thumbnail_gif_info in _upload_file(api, project, thumb_gif_path,
                                                         media_id=resp.id[0], filename='tiled_gif.gif'):
            logger.info(f"Thumbnail gif upload progress: {progress}%")

        # Open images to get output resolution.
        thumb_image = Image.open(thumb_path)
        thumb_gif_image = Image.open(thumb_gif_path)

        # Create image definitions for thumbnails.
        thumb_def = {'path': thumbnail_info.key,
                     'size': os.stat(thumb_path).st_size,
                     'resolution': [thumb_image.height, thumb_image.width],
                     'mime': f'image/{thumb_image.format.lower()}'}
        thumb_gif_def = {'path': thumbnail_gif_info.key,
                         'size': os.stat(thumb_gif_path).st_size,
                         'resolution': [thumb_gif_image.height, thumb_gif_image.width],
                         'mime': f'image/{thumb_gif_image.format.lower()}'}

        response = api.create_image_file(resp.id[0], role='thumbnail', image_definition=thumb_def)
        assert isinstance(response, MessageResponse)
        response = api.create_image_file(resp.id[0], role='thumbnail_gif', image_definition=thumb_gif_def)
        assert isinstance(response, MessageResponse)

    concat_def = [{"id": media_id, "timestampOffset": offset} for media_id,offset in zip(media_ids, offsets)]
    api.update_media(resp.id[0], {"concat": concat_def})

    return resp

