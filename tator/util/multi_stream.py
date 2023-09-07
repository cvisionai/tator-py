import os
import tempfile
import logging
from uuid import uuid1

from PIL import Image, ImageSequence

from ._upload_file import _upload_file
from ._download_file import _download_file
from ..openapi.tator_openapi.models import MessageResponse

logger = logging.getLogger(__name__)
GIF_SZ = 256

PLACEHOLDER_DIR = os.path.dirname(os.path.abspath(__file__))
PLACEHOLDER_THUMB_PATH = os.path.join(PLACEHOLDER_DIR, "tator-symbol.png")
PLACEHOLDER_THUMB_GIF_PATH = os.path.join(PLACEHOLDER_DIR, "tator-symbol.gif")


def _merge_gifs(layout, gif_list, output_filename) -> bool:
    # Calculate the dimensions of the merged GIF
    gifs = []
    try:
        # Open all
        frame_iters = []
        for gif_path in gif_list:
            gifs.append(Image.open(gif_path))
            frame_iters.append(ImageSequence.Iterator(gifs[-1]))

        merged_frames = []
        rows, columns = layout
        merged_height = 256 * rows
        merged_width = 256 * columns
        for single_frames in zip(*frame_iters):
            merged_frames.append(Image.new("RGB", (merged_width, merged_height)))
            for idx, single_frame in enumerate(single_frames):
                y_offset = GIF_SZ * (idx // rows)
                x_offset = 2 * GIF_SZ * (idx % rows)
                merged_frames[-1].paste(
                    single_frame.resize((2 * GIF_SZ, GIF_SZ), Image.LANCZOS), (x_offset, y_offset)
                )
        # Save the merged GIF
        try:
            merged_frames[0].save(
                output_filename,
                save_all=True,
                append_images=merged_frames[1:],
            )
        except Exception:
            logger.warning(
                "Could not save merged gif '%s', using placeholder", output_filename, exc_info=True
            )
            return False
    finally:
        for gif in gifs:
            gif.close()
    return True


def make_multi_stream(
    api, type_id, layout, name, media_ids, section, quality=None, frame_offset=None
):
    """Creates a multiview from the given arguments

    :param api: The Tator client
    :type api: tator.openapi.TatorApi
    :param type_id: Unique integer identifying a multi-stream media type.
    :type type_id: int
    :param layout: 2 element list of integers defining layout as [rows, cols].
    :type layout: List[int]
    :param name: Name of the file to use
    :type name: str
    :param media_ids: List of media_ids to multi-stream
    :type media_ids: List[int]
    :param section: Section name; if it does not exist, it will be created.
    :type section: str
    :param quality: [Optional] The desired resolution to pull from the single media
    :type quality: List[int]
    :param frame_offset: [Optional] Frame offsets to apply to each stream.
    :type frame_offset: List[int]
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
        attributes["tator_user_sections"] = section_obj.tator_user_sections

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
        defs = [
            {
                "path": thumbnail_info.key,
                "size": os.stat(thumb_path).st_size,
                "resolution": [thumb_image.height, thumb_image.width],
                "mime": f"image/{thumb_image.format.lower()}",
            },
            {
                "path": thumbnail_gif_info.key,
                "size": os.stat(thumb_gif_path).st_size,
                "resolution": [thumb_gif_image.height, thumb_gif_image.width],
                "mime": f"image/{thumb_gif_image.format.lower()}",
            },
        ]
        roles = ["thumbnail", "thumbnail_gif"]

        for img_def, role in zip(defs, roles):
            response = api.create_image_file(resp.id[0], role=role, image_definition=img_def)
            if not isinstance(response, MessageResponse):
                raise RuntimeError(f"Unexpected response type '{type(response)}'")

        # Add the multi definition.
        multi_def = {"layout": layout, "ids": media_ids}
        if quality:
            multi_def["quality"] = quality
        if frame_offset:
            if len(frame_offset) != n_ids:
                raise RuntimeError("Length of frame offsets did not match length of media IDs!")
            multi_def["frameOffset"] = frame_offset
        api.update_media(resp.id[0], {"multi": multi_def})

        return resp
