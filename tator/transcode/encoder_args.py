""" Encoder settings for streaming and archival transcodes.

Turns media type encode configs into ffmpeg arguments for the selected encoder, so each
encoder only receives options it actually understands.
"""

import json
import logging
import re
import subprocess
from functools import lru_cache

logger = logging.getLogger(__name__)

# Per-field defaults for streaming configs, mirroring the ResolutionConfig schema defaults.
STREAMING_FIELD_DEFAULTS = {
    "vcodec": "h264",
    "crf": 23,
    "preset": "",
    "pixel_format": "yuv420p",
    "match_source_bit_depth": False,
    "tune": None,
    "encoder_params": None,
}

# Streaming defaults applied when a config leaves preset/tune empty.
STREAMING_PRESET_DEFAULTS = {"x264": "fast", "svtav1": "5"}
STREAMING_TUNE_DEFAULTS = {"x264": "fastdecode"}

SW_TO_HW_PIXEL_FORMAT_CONVERSION = {
    'yuv420p': 'nv12', # QSV h264 supports this
    'yuv420p10le': 'p010le', # QSV h264 supports this
    'yuv422p': 'nv16', # Not sure if any hw encoders actually support this
    'yuv444p' : 'nv21' # Not sure if any hw encoders actually support this
}

TEN_BIT_PIXEL_FORMATS = {
    "yuv420p": "yuv420p10le",
    "yuvj420p": "yuv420p10le",
    "yuv422p": "yuv422p10le",
    "yuvj422p": "yuv422p10le",
    "yuv444p": "yuv444p10le",
    "yuvj444p": "yuv444p10le",
}
EIGHT_BIT_PIXEL_FORMATS = {
    "yuv420p10le": "yuv420p",
    "yuv422p10le": "yuv422p",
    "yuv444p10le": "yuv444p",
}

# SVT-AV1 only encodes 4:2:0.
SVTAV1_PIXEL_FORMATS = ("yuv420p", "yuv420p10le")

# Closed GOP, so every -g interval starts with a key frame that can begin an MP4 fragment.
SVTAV1_BASE_PARAMS = {"irefresh-type": 2}

SVTAV1_TUNES = {"vq": 0, "psnr": 1, "ssim": 2, "iq": 3, "ms-ssim": 4, "vmaf": 5}

# libsvtav1 logs and ignores svtav1-params keys it doesn't recognize, so keys are checked here.
# keyint, irefresh-type and pred-struct are left out because tator controls GOP structure.
SVTAV1_ALLOWED_PARAMS = frozenset({
    "ac-bias",
    "adaptive-film-grain",
    "aq-mode",
    "chroma-qm-max",
    "chroma-qm-min",
    "enable-cdef",
    "enable-dlf",
    "enable-intrabc",
    "enable-kf-tf",
    "enable-overlays",
    "enable-qm",
    "enable-restoration",
    "enable-tf",
    "enable-variance-boost",
    "fast-decode",
    "film-grain",
    "film-grain-denoise",
    "hbd-mds",
    "hierarchical-levels",
    "lookahead",
    "lp",
    "luminance-qp-bias",
    "max-tx-size",
    "qm-max",
    "qm-min",
    "qp-scale-compress-strength",
    "scm",
    "sharpness",
    "startup-mg-size",
    "startup-qp-offset",
    "tf-strength",
    "tile-columns",
    "tile-rows",
    "tune",
    "variance-boost-curve",
    "variance-boost-strength",
    "variance-octile",
})

_PARAM_TOKEN = re.compile(r"^[A-Za-z0-9_.+-]+$")


def parse_streaming_config(config):
    """ Normalizes a streaming config to a dict with every field set.

    :param config: A ResolutionConfig-like mapping, or the legacy string form
                   ``resolution:crf:codec[:preset[:pixel_format]]``.
    """
    if isinstance(config, str):
        parts = config.split(':')
        out = {"resolution": parts[0], "crf": parts[1], "vcodec": parts[2]}
        if len(parts) > 3:
            out["preset"] = parts[3]
        if len(parts) > 4:
            out["pixel_format"] = parts[4]
    else:
        out = {key: value for key, value in dict(config).items() if value is not None}
    out = {**STREAMING_FIELD_DEFAULTS, **out}
    out["resolution"] = int(out["resolution"])
    return out


def encoder_family(encoder):
    """ Returns the argument family for an ffmpeg encoder name. """
    if encoder.endswith("_vaapi"):
        return "vaapi"
    if encoder.endswith("_qsv"):
        return "qsv"
    return {"libsvtav1": "svtav1", "libx264": "x264", "libx265": "x265"}.get(encoder, "other")


@lru_cache(maxsize=None)
def _pixel_format_depths():
    """ Maps pixel format names to their largest component bit depth.

    Uses ``ffprobe -show_pixel_formats``, which reports component depths on every FFmpeg version;
    ``ffmpeg -pix_fmts`` only gained its BIT_DEPTHS column in FFmpeg 6.
    """
    output = subprocess.run(["ffprobe", "-v", "error", "-of", "json", "-show_pixel_formats"],
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True).stdout
    depths = {}
    for pix_fmt in json.loads(output).get("pixel_formats", []):
        components = pix_fmt.get("components")
        if components:
            depths[pix_fmt["name"]] = max(component["bit_depth"] for component in components)
    return depths


@lru_cache(maxsize=None)
def _available_encoders():
    """ Returns the names of the encoders the installed ffmpeg was built with. """
    output = subprocess.run(["ffmpeg", "-hide_banner", "-encoders"], stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL, check=True).stdout.decode()
    # A legend of capability flags comes first, ending in a line of dashes
    lines = output.splitlines()
    start = next((idx + 1 for idx, line in enumerate(lines) if line.strip().startswith("---")), 0)
    return {line.split()[1] for line in lines[start:] if len(line.split()) >= 2}


def require_encoder(encoder, purpose):
    """ Raises a RuntimeError naming the encoder if the installed ffmpeg doesn't have it.

    :param purpose: What the encoder is for, used in the message, e.g. "the 720 av1 stream".
    """
    if encoder not in _available_encoders():
        raise RuntimeError(
            f"ffmpeg has no {encoder} encoder, which {purpose} needs. Use an FFmpeg built with "
            f"{encoder} (the cvisionai/svt_transcoder image has one), or a streaming profile "
            f"with a codec this ffmpeg can encode.")


def source_bit_depth(pix_fmt):
    """ Returns the bit depth of a decoded pixel format, e.g. 10 for yuv422p10le. """
    if not pix_fmt:
        return 8
    depth = _pixel_format_depths().get(pix_fmt)
    if depth is None:
        # Formats with more than 8 bits per sample end in their depth and byte order, e.g.
        # p010le. Names such as nv12 end in digits that aren't a depth.
        match = re.search(r"(9|10|12|14|16)(le|be)$", pix_fmt)
        depth = int(match.group(1)) if match else 8
    return depth


def resolve_pixel_format(encoder, pixel_format, match_source_bit_depth, source_depth):
    """ Returns the output pixel format for an encode.

    With match_source_bit_depth, the chroma layout comes from pixel_format and the bit depth from
    the source: 8-bit for sources up to 8 bits, 10-bit above that. H.264 always keeps the given
    pixel format, because browsers don't decode High 10 or 4:2:2/4:4:4 H.264.
    """
    if not match_source_bit_depth:
        return pixel_format
    if encoder_family(encoder) == "x264":
        if source_depth > 8:
            logger.info(f"Keeping {pixel_format} for {encoder} with a {source_depth}-bit source")
        return pixel_format
    if source_depth > 8:
        return TEN_BIT_PIXEL_FORMATS.get(pixel_format, pixel_format)
    return EIGHT_BIT_PIXEL_FORMATS.get(pixel_format, pixel_format)


def _encoder_params(encoder_params):
    """ Returns encoder params as an ordered dict, from a mapping or a ``key=value:...`` string. """
    if not encoder_params:
        return {}
    if isinstance(encoder_params, str):
        pairs = [item.split('=', 1) for item in encoder_params.split(':') if item]
        if any(len(pair) != 2 for pair in pairs):
            raise ValueError(f"Encoder params must be key=value pairs, got '{encoder_params}'")
        encoder_params = dict(pairs)
    params = {}
    for key, value in dict(encoder_params).items():
        if not _PARAM_TOKEN.match(str(key)) or not _PARAM_TOKEN.match(str(value)):
            raise ValueError(f"Invalid encoder param {key}={value}")
        params[str(key)] = value
    return params


def _join_params(params):
    return ':'.join(f"{key}={value}" for key, value in params.items())


def _svtav1_args(crf, preset, tune, pixel_format, encoder_params):
    if pixel_format not in SVTAV1_PIXEL_FORMATS:
        raise ValueError(f"libsvtav1 only encodes {' and '.join(SVTAV1_PIXEL_FORMATS)}, "
                         f"got {pixel_format}")
    try:
        preset = int(preset)
    except (TypeError, ValueError):
        raise ValueError(f"libsvtav1 presets are integers from -1 to 13, got '{preset}'")
    params = _encoder_params(encoder_params)
    unknown = sorted(set(params) - SVTAV1_ALLOWED_PARAMS)
    if unknown:
        raise ValueError(f"Unsupported svtav1-params {', '.join(unknown)}")
    if tune not in (None, ''):
        tune_value = SVTAV1_TUNES.get(str(tune).lower(), tune)
        if str(tune_value) not in {str(value) for value in SVTAV1_TUNES.values()}:
            raise ValueError(f"libsvtav1 tune must be one of {', '.join(SVTAV1_TUNES)} "
                             f"or 0-5, got '{tune}'")
        params = {"tune": tune_value, **params}
    params = {**SVTAV1_BASE_PARAMS, **params}
    return ["-preset", str(preset),
            "-crf", str(crf),
            "-svtav1-params", _join_params(params),
            "-pix_fmt", pixel_format]


def _x26x_args(params_flag, crf, preset, tune, pixel_format, encoder_params):
    args = []
    if preset:
        args.extend(["-preset", str(preset)])
    if tune:
        args.extend(["-tune", str(tune)])
    args.extend(["-crf", str(crf)])
    params = _encoder_params(encoder_params)
    if params:
        args.extend([params_flag, _join_params(params)])
    args.extend(["-pix_fmt", pixel_format])
    return args


def encoder_args(encoder, crf, preset, tune, pixel_format, encoder_params=None):
    """ Returns ffmpeg output arguments for an encoder, starting with ``-c:v``.

    :param encoder: ffmpeg encoder name, e.g. libsvtav1.
    :param crf: Quality setting; sent as -crf, or -global_quality for hardware encoders.
    :param preset: Encoder preset, or empty to leave it to the encoder.
    :param tune: Encoder tune, or empty for none. For libsvtav1 this becomes svtav1-params tune.
    :param pixel_format: Software pixel format of the encoded frames.
    :param encoder_params: Extra encoder parameters as a mapping or ``key=value:...`` string,
                           passed as -svtav1-params, -x264-params or -x265-params.
    """
    family = encoder_family(encoder)
    args = ["-c:v", encoder]
    if family == "svtav1":
        args.extend(_svtav1_args(crf, preset, tune, pixel_format, encoder_params))
    elif family == "x264":
        args.extend(_x26x_args("-x264-params", crf, preset, tune, pixel_format, encoder_params))
    elif family == "x265":
        args.extend(_x26x_args("-x265-params", crf, preset, tune, pixel_format, encoder_params))
    elif family == "vaapi":
        # Frames arrive as VAAPI surfaces from hwupload, so no -pix_fmt here.
        args.extend(["-global_quality", str(crf)])
    elif family == "qsv":
        args.extend(["-global_quality", str(crf),
                     "-pix_fmt", SW_TO_HW_PIXEL_FORMAT_CONVERSION[pixel_format]])
    else:
        if preset:
            args.extend(["-preset", str(preset)])
        args.extend(["-crf", str(crf), "-pix_fmt", pixel_format])
    return args


def hwupload_filters(encoder, pixel_format):
    """ Returns the filters that upload frames for a VAAPI encoder, or an empty list. """
    if encoder_family(encoder) != "vaapi":
        return []
    return [f"format={SW_TO_HW_PIXEL_FORMAT_CONVERSION[pixel_format]}", "hwupload"]
