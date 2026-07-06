import json
import logging
import os
import subprocess

from ..util._upload_file import _upload_file
from ..util.get_api import get_api

logger = logging.getLogger(__name__)
import tator.exceptions


def tiff_transcode_logic(args, path, paths, media_id):
    """Transcode a TIFF file into a COG and upload the outputs."""
    # We use gdal_translate subprocess to 'transcode' tiff files into COGs
    cpu_count = os.cpu_count() or 1

    # The formula of the command is:
    # gdal_translate <input> <output> -of COG     -co COMPRESS=ZSTD     -co BLOCKSIZE=512     -co OVERVIEWS=AUTO     -co NUM_THREADS=<cpu_count> -co BIGTIFF=yes

    basename = os.path.basename(path)
    comps = os.path.splitext(basename)
    output_path = os.path.join(paths['transcoded'], f"{comps[0]}_cog.tif")

    api = get_api(args.host, args.token)

    cmd = [
        "gdal_translate",
        path,
        output_path,
        "-of", "COG",
        "-co", "COMPRESS=ZSTD",
        "-co", "BLOCKSIZE=512",
        "-co", "OVERVIEWS=AUTO",
        "-co", f"NUM_THREADS={cpu_count}",
        "-co", "BIGTIFF=yes",
    ]

    proc = subprocess.run(cmd, check=True)

    if proc.returncode != 0:
        raise RuntimeError(f"gdal_translate failed with return code {proc.returncode}!")

    # Use gdal translate to make the thumbnail because we can't use the normal ffmpeg path for TIFF files.
    cmd = [
        "gdal_translate",
        output_path,
        paths["thumbnail"],
        "-of", "PNG",
        "-outsize", "256", "256",
    ]

    # Upload the thumbnail
    proc = subprocess.run(cmd, check=True)

    for progress, thumbnail_info in _upload_file(
        api,
        args.project,
        paths['thumbnail'],
        media_id=media_id,
        filename=os.path.basename(paths['thumbnail']),
        bucket_id=args.bucket_id,
    ):
        pass

    thumbnail_def = {
        "path": thumbnail_info.key,
        "size": os.stat(paths['thumbnail']).st_size,
        "resolution": [256, 256],
        "mime": "image/png",
    }

    api.create_image_file(media_id, role="thumbnail", image_definition=thumbnail_def, bucket_id=args.bucket_id)

    # Upload the cog file and update the media
    for progress, cog_info in _upload_file(
        api,
        args.project,
        output_path,
        media_id=media_id,
        filename=os.path.basename(output_path),
        bucket_id=args.bucket_id,
    ):
        pass

    # use gdalinfo -json to get the metadata for the cog, which we will use to fill in the media_file information for the media
    cmd = [
        "gdalinfo",
        "-json",
        output_path,
    ]
    output = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout
    gdal_info = json.loads(output)

    width, height = gdal_info['size']

    image_def = {
        "path": cog_info.key,
        "size": os.stat(output_path).st_size,
        "resolution": [height, width],
        "mime": "image/tiff",
    }

    api.create_image_file(media_id, role="image", image_definition=image_def, bucket_id=args.bucket_id)

    # Fetch the media object to verify it has the required type information
    media_obj = api.get_media(media_id)
    media_type_obj = api.get_media_type(media_obj.type)


    try:
        resp = api.create_attribute_type(media_obj.type, {"entity_type": "MediaType", "addition": {"name": "GDALInfo", "dtype": "blob", 'visible': False}})
    except tator.exceptions.ApiException as e:
        if e.status == 400 and "already an attribute" in str(e):
            pass
        else:
            raise

    gdal_info = {'cornerCoordinates': gdal_info.get('cornerCoordinates', {}), 'geoTransform': gdal_info.get('geoTransform',[])}

    # Update the media record with the height / width
    api.update_media(media_id, media_update={"height": height, "width": width, "attributes": {"GDALInfo": gdal_info}})
