import math
import os
import requests
import subprocess
import tempfile
import logging
from uuid import uuid1

from PIL import Image

from .md5sum import md5sum
from ._upload_file import _upload_file
from ._download_file import _download_file
from ..openapi.tator_openapi.models import MessageResponse

logger = logging.getLogger(__name__)

def make_multi_stream(api, type_id, layout, name, media_ids, section,
                      quality=None, frame_offset=None):
    """ Uploads a single media file.

    :param api: :class:`tator.TatorApi` object.
    :param type_id: Unique integer identifying a multi-stream media type.
    :param layout: 2 element list of integers defining layout as [rows, cols].
    :param name: Name of the file to use
    :param media_ids: List of media_ids to multi-stream
    :param section: Section name. If this section does not exist it will be created.
    :param quality: [Optional] Media section to upload to.
    :param frame_offset: [Optional] Frame offsets to apply to each stream.
    :returns: Response from media object creation.
    """

    # Fetch the stuff we need to download files
    config = api.api_client.configuration
    host = config.host
    token = config.api_key['Authorization']
    prefix = config.api_key_prefix['Authorization']

    # use a multi extension
    name += ".multi"

    # Fetch the media type
    multi_stream_type = api.get_media_type(type_id)
    project = multi_stream_type.project
   
    # Fetch the section. If it does not exist, create it. 
    sections = api.get_section_list(project, name=section)
    if len(sections) == 0:
        section_spec = {'name': section, 'tator_user_sections': str(uuid1())}
        response = api.create_section(project, section_spec=section_spec)
        section_obj = api.get_section_list(project, name=section)[0]
    else:
        section_obj = sections[0]

    assert(len(media_ids) == layout[0]*layout[1])

    media_objects = api.get_media_list(project, media_id=media_ids)
    assert(len(media_objects) == len(media_ids))

    media_lookup={}
    for media in media_objects:
        media_lookup[media.id] = media

    attributes={}
    if section:
        attributes.update({"tator_user_sections": section_obj.tator_user_sections})

    headers = {
        'Authorization': f'{prefix} {token}',
        'Content-Type': f'application/json',
        'Accept-Encoding': 'gzip',
    }

    # Download the thumbnails into a temporary
    with tempfile.TemporaryDirectory() as d:
        try:
            for pos, media_id in enumerate(media_ids):
                media = media_lookup[media_id]
                md5=media.md5
                thumbnail_gifs = media.media_files.thumbnail_gif
                if thumbnail_gifs:
                    thumb_gif = thumbnail_gifs[0].path
                for _ in _download_file(api, media.project, thumb_gif,
                                        os.path.join(d, f"gif_{pos:09d}.gif")):
                    pass

            input_files=[]
            rows=layout[0]
            cols=layout[1]
            filter_graph=""
            for row in range(rows):
                # Resize each input to a square prior to grid
                for col in range(cols):
                    filter_graph += f"[{col}:v]scale=256:256[resize{col}];"
                for col in range(cols):
                    filter_graph += f"[resize{col}]"
                    if cols > 1 and col + 1 == cols:
                        filter_graph += f"hstack=inputs={cols}[r{row}];"
            for row in range(rows):
                if cols > 1:
                    filter_graph += f"[r{row}]"
            if rows > 1 and row + 1 == rows:
                filter_graph+=f'vstack=inputs={rows}[tiled_gif];[tiled_gif]'
            filter_graph+=f'scale=256:-1[raw];[raw]split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse[final]'
            print(filter_graph)
            for pos,_ in enumerate(media_ids):
                input_files.extend(['-i', f'gif_{pos:09d}.gif'])

            # Create GIF
            cmd = ["ffmpeg",
                "-y",
                *input_files,
                "-filter_complex", filter_graph,
                "-map", "[final]",
                "-shortest",
                "tiled_gif.gif"]
            subprocess.run(cmd, cwd=d, check=True)

            # Create thumbnail from first frame of GIF
            cmd = ["ffmpeg",
                "-y",
                "-i", "tiled_gif.gif",
                "-vf",f"select=eq(n\\,0)",
                "-q:v", "3",
                os.path.join(d,"tiled_thumb.jpg")]
            subprocess.run(cmd,cwd=d,check=True)

            thumb_path = os.path.join(d,'tiled_thumb.jpg')
            thumb_gif_path = os.path.join(d,'tiled_gif.gif')
        except:
            thumb_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tator-symbol.png")
            thumb_gif_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tator-symbol.gif")

        media_spec = {'attributes': attributes,
                'name': name,
                'md5': md5,
                'section': section_obj.name,
                'type': type_id}
        resp = api.create_media_list(project, [media_spec])
        print(f"Created {resp.id[0]}")
        
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

        # Add the multi definition.
        multi_def = {"layout": layout,
                     "ids": media_ids}
        if quality:
            multi_def.update({"quality": quality})
        if frame_offset:
            assert len(frame_offset) == len(media_ids), "Length of frame offsets did not match length of media IDs!"
            multi_def.update({"frameOffset": frame_offset})
        api.update_media(resp.id[0], {"multi": multi_def})

        return resp

