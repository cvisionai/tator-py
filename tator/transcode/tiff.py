import json
import logging
import os
import shutil
import subprocess
import numpy as np
from osgeo import gdal

from ..util._upload_file import _upload_file
from ..util.get_api import get_api

logger = logging.getLogger(__name__)
import tator.exceptions

DEFAULT_WEBP_QUALITY = 85
DEFAULT_ZSTD_LEVEL = 9
DEFAULT_DEFLATE_LEVEL = 6
DEFAULT_LZMA_LEVEL = 6

def _clamp_int(value, minimum, maximum):
    try:
        numeric = int(value)
    except (TypeError, ValueError):
        numeric = minimum
    return max(minimum, min(maximum, numeric))


def _append_cog_compression_options(cmd, compression, compression_quality_raw):
    compression_upper = (compression or "").upper()

    if compression_upper == "WEBP":
        webp_quality = _clamp_int(
            compression_quality_raw if compression_quality_raw is not None else DEFAULT_WEBP_QUALITY,
            1,
            100,
        )
        cmd.extend(["-co", f"QUALITY={webp_quality}"])
    elif compression_upper == "ZSTD":
        zstd_level = _clamp_int(
            compression_quality_raw if compression_quality_raw is not None else DEFAULT_ZSTD_LEVEL,
            1,
            22,
        )
        cmd.extend(["-co", f"LEVEL={zstd_level}"])
    elif compression_upper == "DEFLATE":
        deflate_level = _clamp_int(
            compression_quality_raw if compression_quality_raw is not None else DEFAULT_DEFLATE_LEVEL,
            1,
            12,
        )
        cmd.extend(["-co", f"LEVEL={deflate_level}"])
    elif compression_upper == "LZMA":
        lzma_level = _clamp_int(
            compression_quality_raw if compression_quality_raw is not None else DEFAULT_LZMA_LEVEL,
            1,
            9,
        )
        cmd.extend(["-co", f"LEVEL={lzma_level}"])
    elif compression_upper == "LZW":
        # LZW does not use a compression level option in GDAL COG creation options.
        pass


def add_alpha_to_webp(input_path, output_path, webp_quality=85):
    """Add a fully-opaque alpha band to a 3-band TIFF and write a 4-band COG.

    This is used to convert RGB WEBP-compressed TIFFs to RGBA so browser decode
    paths can use fast hardware-accelerated routines.
    """
    src = gdal.Open(input_path)
    if src is None:
        raise RuntimeError(f"Could not open input TIFF: {input_path}")

    if src.RasterCount < 3:
        raise RuntimeError(
            f"Expected at least 3 input bands for RGB, got {src.RasterCount}"
        )

    driver = gdal.GetDriverByName("GTiff")
    if driver is None:
        raise RuntimeError("GTiff driver is not available in GDAL.")

    gdal.SetConfigOption("GDAL_NUM_THREADS", "ALL_CPUS")

    temp_rgba_path = f"{output_path}.tmp_rgba.tif"

    out = driver.Create(
        temp_rgba_path,
        src.RasterXSize,
        src.RasterYSize,
        4,
        gdal.GDT_Byte,
        options=[
            "COMPRESS=ZSTD",
            "ZSTD_LEVEL=1",
            "NUM_THREADS=ALL_CPUS",
            "INTERLEAVE=PIXEL",
            "TILED=YES",
            "BLOCKXSIZE=512",
            "BLOCKYSIZE=512",
            "BIGTIFF=YES",
        ],
    )
    if out is None:
        raise RuntimeError(f"Could not create output TIFF: {output_path}")

    out.SetGeoTransform(src.GetGeoTransform())
    out.SetProjection(src.GetProjection())

    out.GetRasterBand(1).SetColorInterpretation(gdal.GCI_RedBand)
    out.GetRasterBand(2).SetColorInterpretation(gdal.GCI_GreenBand)
    out.GetRasterBand(3).SetColorInterpretation(gdal.GCI_BlueBand)
    out.GetRasterBand(4).SetColorInterpretation(gdal.GCI_AlphaBand)

    tile_size = 512
    tiles_x = (src.RasterXSize + tile_size - 1) // tile_size
    tiles_y = (src.RasterYSize + tile_size - 1) // tile_size
    total_tiles = tiles_x * tiles_y

    # Reuse full-alpha tiles by shape to reduce allocations on edge tiles.
    alpha_cache = {}

    # Print status roughly every 5% and always at completion.
    print_interval = max(1, total_tiles // 20)
    processed_tiles = 0

    for y in range(0, src.RasterYSize, tile_size):
        h = min(tile_size, src.RasterYSize - y)
        for x in range(0, src.RasterXSize, tile_size):
            w = min(tile_size, src.RasterXSize - x)

            rgb = src.ReadAsArray(x, y, w, h)
            if rgb is None:
                raise RuntimeError(
                    f"Failed to read source tile x={x}, y={y}, w={w}, h={h}"
                )

            out.GetRasterBand(1).WriteArray(rgb[0], x, y)
            out.GetRasterBand(2).WriteArray(rgb[1], x, y)
            out.GetRasterBand(3).WriteArray(rgb[2], x, y)

            key = (h, w)
            if key not in alpha_cache:
                alpha_cache[key] = np.full((h, w), 255, dtype=np.uint8)
            out.GetRasterBand(4).WriteArray(alpha_cache[key], x, y)

            processed_tiles += 1
            if processed_tiles % print_interval == 0 or processed_tiles == total_tiles:
                pct = (processed_tiles / total_tiles) * 100.0
                print(
                    f"add_alpha_to_webp: {processed_tiles}/{total_tiles} tiles ({pct:.1f}%)"
                )

    out.FlushCache()
    out = None
    src = None

    try:
        cmd = [
            "gdal_translate",
            temp_rgba_path,
            output_path,
            "-of", "COG",
            "-co", "COMPRESS=WEBP",
            "-co", f"QUALITY={_clamp_int(webp_quality, 1, 100)}",
            "-co", "BLOCKSIZE=512",
            "-co", "OVERVIEWS=AUTO",
            "-co", "NUM_THREADS=ALL_CPUS",
            "-co", "BIGTIFF=YES",
        ]
        proc = subprocess.run(cmd, check=True)
        if proc.returncode != 0:
            raise RuntimeError(f"gdal_translate failed with return code {proc.returncode}!")
    finally:
        try:
            os.remove(temp_rgba_path)
        except OSError:
            pass

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

    cmd = ["gdalinfo", "-json", path]
    output = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout
    gdal_info = json.loads(output)

    # SKIP COG if the file is already COG
    image_structure_format = gdal_info.get('metadata', {}).get('IMAGE_STRUCTURE', {}).get('LAYOUT', '')
    image_compression = gdal_info.get('metadata', {}).get('IMAGE_STRUCTURE', {}).get('COMPRESSION', '')
    image_interleave = gdal_info.get('metadata', {}).get('IMAGE_STRUCTURE', {}).get('INTERLEAVE', '')
    overview_count = len(gdal_info.get('bands',[])[0].get('overviews', [])) if gdal_info.get('bands',[]) else 0
    band_count = len(gdal_info.get('bands', []))

    media_type_obj = api.get_media_type(api.get_media(media_id).type)
    # WEBP is much faster than ZSTD for RGBA images. Unless the media type specifies using ZSTD we should
    # favor WEBP for performance reasons
    preferred_multiband_compression = media_type_obj.extended_info.get('preferred_multiband_compression', 'WEBP')
    compression_quality_raw = media_type_obj.extended_info.get('compression_quality')

    preferred_compression = "WEBP" if preferred_multiband_compression == 'WEBP' and band_count > 1 else "ZSTD"

    # If the image is a COG, in the preferred compression format, has overviews, and is band interleaved by pixel then we can skip transcoding and 
    # just copy the file. 
    #
    # Otherwise we need to transcode it to ensure it is in the optimal format for our viewer.
    if image_structure_format == 'COG' and \
        overview_count > 0 and \
            band_count in [1,4] and \
                image_compression == preferred_compression and \
                    image_interleave == 'PIXEL':
        shutil.copy(path, output_path)
    else:
        if band_count == 3 and preferred_compression == "WEBP":
            # We need to add an alpha channel to the image at this point. While webp can support 3 band RGB images, the 
            # browser decode stack expects 4 channel rgba webp images. This ensures we use hardware-based decode of the webp images
            # for optimal performance.
            webp_quality = _clamp_int(
                compression_quality_raw if compression_quality_raw is not None else DEFAULT_WEBP_QUALITY,
                1,
                100,
            )
            add_alpha_to_webp(path, output_path, webp_quality=webp_quality)
        else:
            # Because we are doing something more humdrum here, we can just use gdal_translate directly.
            # While the python bindings don't add much overhead, it'd be more code to maintain, so we will use a simple
            # subprocess-based transcode for the cases we don't have to add an alpha channel.
            cmd = [
                "gdal_translate",
                path,
                output_path,
                "-of", "COG",
                "-co", f"COMPRESS={preferred_compression}",
                "-co", "BLOCKSIZE=512",
                "-co", "OVERVIEWS=AUTO",
                "-co", f"NUM_THREADS={cpu_count}",
                "-co", "BIGTIFF=yes",
            ]

            _append_cog_compression_options(
                cmd,
                preferred_compression,
                compression_quality_raw,
            )

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
