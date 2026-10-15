""" Tests for streaming/archival encoder arguments. These don't need a Tator server. """

import json
import os
import shutil
import subprocess

import pytest

import tator.transcode.encoder_args as encoder_args_module
from tator.transcode.encoder_args import (
    encoder_args,
    parse_streaming_config,
    require_encoder,
    resolve_pixel_format,
    source_bit_depth,
)
from tator.transcode.transcode import _streaming_command


def _ffmpeg_has(kind, name):
    if shutil.which("ffmpeg") is None:
        return False
    output = subprocess.run(["ffmpeg", "-hide_banner", f"-{kind}"], capture_output=True,
                            text=True).stdout
    return any(line.split()[1:2] == [name] for line in output.splitlines() if line.strip())


requires_ffmpeg = pytest.mark.skipif(shutil.which("ffmpeg") is None, reason="ffmpeg not found")
requires_svtav1 = pytest.mark.skipif(not _ffmpeg_has("encoders", "libsvtav1"),
                                     reason="ffmpeg without libsvtav1")
requires_x265 = pytest.mark.skipif(not _ffmpeg_has("encoders", "libx265"),
                                   reason="ffmpeg without libx265")


def test_parse_legacy_config_strings():
    config = parse_streaming_config("720:23:h264")
    assert (config["resolution"], config["crf"], config["vcodec"]) == (720, "23", "h264")
    assert config["preset"] == ""
    assert config["pixel_format"] == "yuv420p"
    assert config["match_source_bit_depth"] is False

    config = parse_streaming_config("1080:34:av1:5:yuv420p10le")
    assert (config["preset"], config["pixel_format"]) == ("5", "yuv420p10le")


def test_parse_config_mapping_fills_missing_fields():
    config = parse_streaming_config({"resolution": "1080", "vcodec": "av1", "crf": 34,
                                     "preset": None, "match_source_bit_depth": True})
    assert config["resolution"] == 1080
    assert config["preset"] == ""
    assert config["pixel_format"] == "yuv420p"
    assert config["match_source_bit_depth"] is True
    assert config["encoder_params"] is None


@requires_ffmpeg
@pytest.mark.parametrize("pix_fmt,depth", [
    ("yuv420p", 8), ("yuvj420p", 8), ("nv12", 8), ("yuv420p10le", 10), ("yuv422p10le", 10),
    ("p010le", 10), ("yuv422p12le", 12), ("yuva444p12le", 12), ("gbrp10le", 10), (None, 8),
])
def test_source_bit_depth(pix_fmt, depth):
    assert source_bit_depth(pix_fmt) == depth


@pytest.mark.parametrize("encoder,pixel_format,match,depth,expected", [
    ("libsvtav1", "yuv420p", True, 8, "yuv420p"),
    ("libsvtav1", "yuv420p", True, 10, "yuv420p10le"),
    ("libsvtav1", "yuv420p", True, 12, "yuv420p10le"),
    ("libsvtav1", "yuv420p10le", True, 8, "yuv420p"),
    ("libsvtav1", "yuv420p", False, 10, "yuv420p"),
    ("libsvtav1", "yuv420p10le", False, 8, "yuv420p10le"),
    # H.264 keeps its pixel format; browsers don't decode High 10.
    ("libx264", "yuv420p", True, 10, "yuv420p"),
    ("h264_vaapi", "yuv420p", True, 10, "yuv420p"),
    ("h264_qsv", "yuv420p", True, 10, "yuv420p"),
    ("libx265", "yuv422p", True, 10, "yuv422p10le"),
])
def test_resolve_pixel_format(encoder, pixel_format, match, depth, expected):
    assert resolve_pixel_format(encoder, pixel_format, match, depth) == expected


def test_svtav1_args_use_svtav1_params_not_tune():
    args = encoder_args("libsvtav1", 34, "5", None, "yuv420p")
    assert args == ["-c:v", "libsvtav1", "-preset", "5", "-crf", "34",
                    "-svtav1-params", "irefresh-type=2", "-pix_fmt", "yuv420p"]

    args = encoder_args("libsvtav1", 34, 5, "vq", "yuv420p10le", {"fast-decode": 1})
    assert "-tune" not in args
    assert args[args.index("-svtav1-params") + 1] == "irefresh-type=2:tune=0:fast-decode=1"

    args = encoder_args("libsvtav1", 34, 5, None, "yuv420p", "hierarchical-levels=3")
    assert args[args.index("-svtav1-params") + 1] == "irefresh-type=2:hierarchical-levels=3"


@pytest.mark.parametrize("kwargs,message", [
    ({"pixel_format": "yuv444p"}, "only encodes"),
    ({"preset": "fast"}, "presets are integers"),
    ({"encoder_params": {"keyint": 50}}, "Unsupported svtav1-params keyint"),
    ({"tune": "fastdecode"}, "tune must be one of"),
    ({"encoder_params": {"tune": "0:lp=4"}}, "Invalid encoder param"),
])
def test_svtav1_args_reject_bad_settings(kwargs, message):
    settings = {"crf": 34, "preset": "5", "tune": None, "pixel_format": "yuv420p",
                "encoder_params": None, **kwargs}
    with pytest.raises(ValueError, match=message):
        encoder_args("libsvtav1", **settings)


def test_x26x_args():
    assert encoder_args("libx264", 23, "fast", "fastdecode", "yuv420p") == [
        "-c:v", "libx264", "-preset", "fast", "-tune", "fastdecode", "-crf", "23",
        "-pix_fmt", "yuv420p"]
    assert encoder_args("libx265", 28, "medium", None, "yuv420p10le", {"aq-mode": 3}) == [
        "-c:v", "libx265", "-preset", "medium", "-crf", "28", "-x265-params", "aq-mode=3",
        "-pix_fmt", "yuv420p10le"]


def test_hardware_args_skip_software_options():
    assert encoder_args("h264_vaapi", 23, "fast", "fastdecode", "yuv420p") == [
        "-c:v", "h264_vaapi", "-global_quality", "23"]
    assert encoder_args("h264_qsv", 23, "fast", "fastdecode", "yuv420p10le") == [
        "-c:v", "h264_qsv", "-global_quality", "23", "-pix_fmt", "p010le"]


def _make_source(path, *args, display_rotation=None, seconds=2):
    rotation = ["-display_rotation", str(display_rotation)] if display_rotation else []
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "lavfi",
                    "-i", "testsrc2=s=640x360:r=30", "-t", str(seconds), *args, str(path)],
                   check=True)
    if rotation:
        rotated = path.with_name(f"rotated_{path.name}")
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *rotation,
                        "-i", str(path), "-c", "copy", str(rotated)], check=True)
        return rotated
    return path


def _probe(path):
    output = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v",
                             "-show_entries", "stream=width,height,pix_fmt:stream_side_data",
                             "-of", "json", str(path)],
                            capture_output=True, text=True, check=True).stdout
    return json.loads(output)["streams"][0]


def _run_streaming(path, outdir, configs):
    outdir.mkdir()
    cmd, resolutions = _streaming_command(path, str(outdir), configs)
    proc = subprocess.run(cmd, capture_output=True, text=True, env={**os.environ, "SVT_LOG": "2"})
    assert proc.returncode == 0, proc.stderr
    # Every option given to an encoder must be one it actually uses.
    assert "has not been used" not in proc.stderr
    assert "Error parsing option" not in proc.stderr
    return {res: outdir / f"{res}.mp4" for res in resolutions}


LADDER = [
    {"resolution": 360, "vcodec": "av1", "crf": 40, "preset": "10", "pixel_format": "yuv420p",
     "match_source_bit_depth": True},
    {"resolution": 240, "vcodec": "h264", "crf": 30, "pixel_format": "yuv420p",
     "match_source_bit_depth": True},
    {"resolution": 144, "vcodec": "av1", "crf": 40, "preset": "10", "pixel_format": "yuv420p"},
]


@requires_svtav1
def test_streaming_8bit_source(tmp_path):
    source = _make_source(tmp_path / "src8.mp4", "-c:v", "libx264", "-pix_fmt", "yuv420p")
    outputs = _run_streaming(str(source), tmp_path / "out", LADDER)
    assert {res: _probe(path)["pix_fmt"] for res, path in outputs.items()} == {
        360: "yuv420p", 240: "yuv420p", 144: "yuv420p"}


@requires_svtav1
@requires_x265
def test_streaming_10bit_source_matches_bit_depth(tmp_path):
    source = _make_source(tmp_path / "src10.mp4", "-c:v", "libx265", "-pix_fmt", "yuv420p10le",
                          "-x265-params", "log-level=error")
    outputs = _run_streaming(str(source), tmp_path / "out", LADDER)
    # 360 matches the source; h264 stays 8-bit; 144 doesn't match.
    assert {res: _probe(path)["pix_fmt"] for res, path in outputs.items()} == {
        360: "yuv420p10le", 240: "yuv420p", 144: "yuv420p"}


@requires_svtav1
def test_streaming_rotated_source_is_upright(tmp_path):
    source = _make_source(tmp_path / "phone.mp4", "-c:v", "libx264", "-pix_fmt", "yuv420p",
                          display_rotation=90)
    outputs = _run_streaming(str(source), tmp_path / "out", LADDER[:1])
    stream = _probe(outputs[360])
    assert stream["height"] == 360
    assert stream["width"] < stream["height"]
    assert not any("rotation" in side_data for side_data in stream.get("side_data_list", []))


@requires_svtav1
def test_streaming_concatenates_segments(tmp_path):
    first = _make_source(tmp_path / "a.mp4", "-c:v", "libx264", "-pix_fmt", "yuv420p")
    second = _make_source(tmp_path / "b.mp4", "-c:v", "libx264", "-pix_fmt", "yuv420p")
    outputs = _run_streaming([str(first), str(second)], tmp_path / "out", LADDER[:1])
    output = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-count_packets",
                             "-show_entries", "stream=nb_read_packets", "-of", "csv=p=0",
                             str(outputs[360])], capture_output=True, text=True, check=True)
    assert int(output.stdout.strip()) >= 120


@requires_svtav1
def test_streaming_av1_key_frames_every_gop(tmp_path):
    source = _make_source(tmp_path / "src.mp4", "-c:v", "libx264", "-pix_fmt", "yuv420p",
                          seconds=4)
    outputs = _run_streaming(str(source), tmp_path / "out", LADDER[:1])
    output = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v",
                             "-show_entries", "packet=flags", "-of", "csv=p=0",
                             str(outputs[360])], capture_output=True, text=True, check=True)
    flags = output.stdout.split()
    key_frames = [idx for idx, flag in enumerate(flags) if flag.startswith("K")]
    assert key_frames[:5] == [0, 25, 50, 75, 100]


ENCODERS_OUTPUT = """Encoders:
 V..... = Video
 A..... = Audio
 ------
 V....D libx264              libx264 H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 (codec h264)
 V..... libsvtav1            SVT-AV1(Scalable Video Technology for AV1) encoder (codec av1)
 A....D aac                  AAC (Advanced Audio Coding)
"""


def test_available_encoders_reads_encoder_names(monkeypatch):
    def run(cmd, **kwargs):
        return subprocess.CompletedProcess(cmd, 0, ENCODERS_OUTPUT.encode())
    monkeypatch.setattr(encoder_args_module, "subprocess",
                        type("FakeSubprocess", (), {"run": staticmethod(run), "PIPE": None,
                                                    "DEVNULL": None}))
    encoder_args_module._available_encoders.cache_clear()
    try:
        assert encoder_args_module._available_encoders() == {"libx264", "libsvtav1", "aac"}
    finally:
        encoder_args_module._available_encoders.cache_clear()


@requires_ffmpeg
def test_available_encoders_match_ffmpeg():
    encoders = encoder_args_module._available_encoders()
    assert "=" not in encoders
    for name in ("libx264", "libx265", "libsvtav1"):
        assert (name in encoders) == _ffmpeg_has("encoders", name)


def test_require_encoder_names_the_missing_encoder(monkeypatch):
    monkeypatch.setattr(encoder_args_module, "_available_encoders", lambda: {"libx264"})
    require_encoder("libx264", "the 720 h264 stream")
    with pytest.raises(RuntimeError, match="no libsvtav1 encoder, which the 720 av1 stream needs"):
        require_encoder("libsvtav1", "the 720 av1 stream")


@requires_ffmpeg
def test_streaming_fails_clearly_without_the_encoder(tmp_path, monkeypatch):
    source = _make_source(tmp_path / "src.mp4", "-c:v", "libx264", "-pix_fmt", "yuv420p")
    monkeypatch.setattr(encoder_args_module, "_available_encoders", lambda: {"libx264"})
    with pytest.raises(RuntimeError, match="no libsvtav1 encoder, which the 360 av1 stream needs"):
        _streaming_command(str(source), str(tmp_path), LADDER)


@requires_ffmpeg
@pytest.mark.skipif(_ffmpeg_has("encoders", "libsvtav1"), reason="ffmpeg has libsvtav1")
def test_streaming_av1_on_ffmpeg_without_svtav1_fails_clearly(tmp_path):
    source = _make_source(tmp_path / "src.mp4", "-c:v", "libx264", "-pix_fmt", "yuv420p")
    with pytest.raises(RuntimeError, match="no libsvtav1 encoder"):
        _streaming_command(str(source), str(tmp_path), LADDER)


@requires_ffmpeg
def test_streaming_keeps_zero_preset_and_tune(tmp_path, monkeypatch):
    source = _make_source(tmp_path / "src.mp4", "-c:v", "libx264", "-pix_fmt", "yuv420p")
    monkeypatch.setattr(encoder_args_module, "_available_encoders", lambda: {"libsvtav1"})
    config = {"resolution": 144, "vcodec": "av1", "crf": 40, "preset": 0, "tune": 0}
    cmd, _ = _streaming_command(str(source), str(tmp_path), [config])
    preset = cmd.index("-preset")
    assert cmd[preset + 1] == "0"
    assert "tune=0" in cmd[cmd.index("-svtav1-params") + 1].split(":")

