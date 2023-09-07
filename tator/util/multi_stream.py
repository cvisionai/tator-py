from math import inf
import os
import tempfile
import logging
from uuid import uuid1

from PIL import Image

from ._upload_file import _upload_file
from ._download_file import _download_file
from ..openapi.tator_openapi.models import MessageResponse

logger = logging.getLogger(__name__)
GIF_SZ = 256

PLACEHOLDER_THUMB_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "tator-symbol.png"
)
PLACEHOLDER_THUMB_GIF_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "tator-symbol.gif"
)


def _crop_and_resize(image):
    # Determine largest square crop
    # width, height = image.size
    # if width > height:
    #     left = (width - height) / 2
    #     right = width - left
    #     top = 0
    #     bottom = height
    # else:
    #     top = (height - width) / 2
    #     bottom = height - top
    #     left = 0
    #     right = width

    # Crop and resize the image
    # image = image.crop((left, top, right, bottom))
    image = image.resize((GIF_SZ, GIF_SZ), Image.LANCZOS)

    return image


def _merge_gifs(layout, gif_list, output_filename) -> bool:
    # Calculate the dimensions of the merged GIF
    merged_height = 256 * layout[0]
    merged_width = 256 * layout[1]

    # Create a new image for the merged GIF
    merged = Image.new("RGB", (merged_width, merged_height))

    # Resize and paste the GIFs into the merged image
    duration = inf  # in milliseconds
    for i, gif_path in enumerate(gif_list):
        gif = Image.open(gif_path)
        duration = min(duration, gif.info.get("duration", duration))

        # Crop and resize to 256x256 while maintaining aspect ratio
        gif = _crop_and_resize(gif)

        x = (i % layout[0]) * 256
        y = (i // layout[0]) * 256
        merged.paste(gif, (x, y))

    if duration == inf:
        return False

    # Save the merged GIF
    try:
        merged.save(
            output_filename,
            save_all=True,
            append_images=gif_list,
            duration=duration,
        )
    except Exception:
        logger.warning(
            "Could not save merged gif '%s', using placeholder", output_filename, exc_info=True
        )
        return False
    return True


def make_multi_stream(
    api, type_id, layout, name, media_ids, section, quality=None, frame_offset=None
):
    """Creates a multiview from the given arguments

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
    tiled_thumb_filename = "tiled_thumb.jpg"
    tiled_gif_filename = "tiled_gif.gif"
    thumb_path = PLACEHOLDER_THUMB_PATH
    thumb_gif_path = PLACEHOLDER_THUMB_GIF_PATH

    # use a multi extension
    name += ".multi"

    # Fetch the media type
    multi_stream_type = api.get_media_type(type_id)
    project = multi_stream_type.project

    # Fetch the section. If it does not exist, create it.
    sections = api.get_section_list(project, name=section)
    if len(sections) == 0:
        section_spec = {"name": section, "tator_user_sections": str(uuid1())}
        response = api.create_section(project, section_spec=section_spec)
        section_obj = api.get_section_list(project, name=section)[0]
    else:
        section_obj = sections[0]

    n_ids = len(media_ids)
    n_spots = layout[0] * layout[1]
    if n_ids != n_spots:
        raise RuntimeError(
            f"{layout[0]} by {layout[1]} layout requires {n_spots} videos, received {n_ids}"
        )

    media_objects = api.get_media_list(project, media_id=media_ids)
    n_objs = len(media_objects)
    if n_objs != n_ids:
        raise RuntimeError(f"Requested {n_ids} media objects, but only found {n_objs}")
    media_lookup = {media.id: media for media in media_objects}

    attributes = {}
    if section:
        attributes.update({"tator_user_sections": section_obj.tator_user_sections})

    # Download the thumbnails into a temporary directory
    with tempfile.TemporaryDirectory() as d:
        input_files = []
        md5 = ""
        for pos, media_id in enumerate(media_ids):
            media = media_lookup[media_id]
            md5 = media.md5
            thumbnail_gifs = media.media_files.thumbnail_gif
            if thumbnail_gifs:
                thumb_gif = thumbnail_gifs[0].path
                thumb_name = os.path.join(d, f"gif_{pos:09d}.gif")
                try:
                    for _ in _download_file(api, media.project, thumb_gif, thumb_name):
                        pass
                except Exception:
                    logger.warning(
                        "Could not download thumbnail gif from %d", media_id, exc_info=True
                    )
                else:
                    input_files.append(thumb_name)

        new_thumb_gif_path = os.path.join(d, tiled_gif_filename)
        if len(input_files) == n_ids and _merge_gifs(
            layout=layout, gif_list=input_files, output_filename=new_thumb_gif_path
        ):
            thumb_gif_path = new_thumb_gif_path
            try:
                new_thumb_path = os.path.join(d, tiled_thumb_filename)
                with Image.open(thumb_gif_path) as img:
                    first_frame = img.convert("RGB")
                    first_frame.save(new_thumb_path)
            except Exception:
                logger.warning("Could not create thumbnail image from gif", exc_info=True)
            else:
                thumb_path = new_thumb_path

        media_spec = {
            "attributes": attributes,
            "name": name,
            "md5": md5,
            "section": section_obj.name,
            "type": type_id,
        }
        try:
            resp = api.create_media_list(project, [media_spec])
        except Exception as exc:
            raise RuntimeError("Could not create multiview") from exc

        thumbnail_info = None
        for progress, thumbnail_info in _upload_file(
            api, project, thumb_path, media_id=resp.id[0], filename=tiled_thumb_filename
        ):
            logger.info(f"Thumbnail upload progress: {progress}%")
        if not thumbnail_info:
            raise RuntimeError("Did not receive thumbnail info after upload")

        thumbnail_gif_info = None
        for progress, thumbnail_gif_info in _upload_file(
            api, project, thumb_gif_path, media_id=resp.id[0], filename=tiled_gif_filename
        ):
            logger.info(f"Thumbnail gif upload progress: {progress}%")
        if not thumbnail_gif_info:
            raise RuntimeError("Did not receive thumbnail gif info after upload")

        # Open images to get output resolution.
        thumb_image = Image.open(thumb_path)
        thumb_gif_image = Image.open(thumb_gif_path)

        # Create image definitions for thumbnails.
        thumb_def = {
            "path": thumbnail_info.key,
            "size": os.stat(thumb_path).st_size,
            "resolution": [thumb_image.height, thumb_image.width],
            "mime": f"image/{thumb_image.format.lower()}",
        }
        thumb_gif_def = {
            "path": thumbnail_gif_info.key,
            "size": os.stat(thumb_gif_path).st_size,
            "resolution": [thumb_gif_image.height, thumb_gif_image.width],
            "mime": f"image/{thumb_gif_image.format.lower()}",
        }

        response = api.create_image_file(resp.id[0], role="thumbnail", image_definition=thumb_def)
        if not isinstance(response, MessageResponse):
            raise RuntimeError(f"Unexpected response type '{type(response)}'")
        response = api.create_image_file(
            resp.id[0], role="thumbnail_gif", image_definition=thumb_gif_def
        )
        if not isinstance(response, MessageResponse):
            raise RuntimeError(f"Unexpected response type '{type(response)}'")

        # Add the multi definition.
        multi_def = {"layout": layout, "ids": media_ids}
        if quality:
            multi_def.update({"quality": quality})
        if frame_offset:
            if len(frame_offset) != n_ids:
                raise RuntimeError("Length of frame offsets did not match length of media IDs!")
            multi_def.update({"frameOffset": frame_offset})
        api.update_media(resp.id[0], {"multi": multi_def})

        return resp
