""" Tests for filter graph construction. These need neither ffmpeg nor a Tator server. """

import pytest

from tator.transcode.filtergraph import (
    build_streaming_filtergraph,
    filter_chain,
    render_filter,
    render_filtergraph,
    streaming_input_chains,
)

DEINTERLACE = "bwdif=mode=send_frame:deint=interlaced"


def test_render_filter_forms():
    assert render_filter("scale=-2:720") == "scale=-2:720"
    assert render_filter({"name": "hwupload"}) == "hwupload"
    assert render_filter({"name": "scale", "args": [-2, 720]}) == "scale=-2:720"
    assert render_filter({"name": "bwdif", "options": {"mode": "send_frame", "deint": "interlaced"}}) \
        == "bwdif=mode=send_frame:deint=interlaced"


def test_render_filter_rejects_values_that_need_escaping():
    with pytest.raises(ValueError, match="needs escaping"):
        render_filter({"name": "drawtext", "options": {"text": "a:b"}})


def test_render_filtergraph():
    chains = [
        filter_chain(["0:v:0"], ["setsar=1", {"name": "fps", "args": [30]}], ["a"]),
        filter_chain(["a"], ["split=2"], ["b", "c"]),
    ]
    assert render_filtergraph(chains) == "[0:v:0]setsar=1,fps=30[a];[a]split=2[b][c]"
    with pytest.raises(ValueError, match="no filters"):
        render_filtergraph([filter_chain(["a"], [], ["b"])])


def test_single_segment_single_output():
    graph = build_streaming_filtergraph(1, 1920, 1080, 30.0, [{"resolution": 720}], DEINTERLACE)
    assert graph.split(";") == [
        f"[0:v:0]{DEINTERLACE},setsar=1,fps=30.0[vid0]",
        "[1:v:0]scale=1920:1080,setsar=1,fps=30.0[bv]",
        "[vid0][bv]concat=n=2:v=1:a=0[concatenated]",
        "[concatenated]scale=-2:720,pad=ceil(iw/2)*2:ceil(ih/2)*2[outv0]",
    ]


def test_segments_and_outputs_with_hardware_upload():
    outputs = [{"resolution": 1080, "filters": ["format=nv12", "hwupload"]}, {"resolution": 144}]
    graph = build_streaming_filtergraph(2, 1280, 720, 25.0, outputs, DEINTERLACE)
    assert graph.split(";") == [
        f"[0:v:0]{DEINTERLACE},setsar=1,fps=25.0[vid0]",
        f"[1:v:0]{DEINTERLACE},setsar=1,fps=25.0[vid1]",
        "[2:v:0]scale=1280:720,setsar=1,fps=25.0[bv]",
        "[vid0][vid1][bv]concat=n=3:v=1:a=0[concatenated]",
        "[concatenated]split=2[split0][split1]",
        "[split0]scale=-2:1080,pad=ceil(iw/2)*2:ceil(ih/2)*2,format=nv12,hwupload[outv0]",
        "[split1]scale=-2:144,pad=ceil(iw/2)*2:ceil(ih/2)*2[outv1]",
    ]


def test_custom_input_stage_as_chains():
    # e.g. an external project inserting an overlay before the default concat
    chains = streaming_input_chains(1, 640, 360, "{fps}", DEINTERLACE)
    chains[0]["filters"].append("drawbox=x=0:y=0:w=64:h={height}")
    graph = build_streaming_filtergraph(1, 640, 360, 15.0, [{"resolution": 360}], DEINTERLACE,
                                        filter_complex=chains)
    assert graph.split(";")[0] == f"[0:v:0]{DEINTERLACE},setsar=1,fps=15.0,drawbox=x=0:y=0:w=64:h=360[vid0]"
    assert graph.endswith("[concatenated]scale=-2:360,pad=ceil(iw/2)*2:ceil(ih/2)*2[outv0]")


def test_custom_input_stage_must_produce_concatenated():
    chains = [filter_chain(["0:v:0"], ["fps={fps}"], ["video"])]
    with pytest.raises(ValueError, match="exactly once"):
        build_streaming_filtergraph(1, 640, 360, 30.0, [{"resolution": 360}], DEINTERLACE,
                                    filter_complex=chains)


def test_custom_input_stage_as_string_template():
    template = "[0:v:0]fps={fps}{hw_upload}[concatenated];"
    graph = build_streaming_filtergraph(1, 640, 360, 30.0, [{"resolution": 360}], DEINTERLACE,
                                        filter_complex=template)
    assert graph == ("[0:v:0]fps=30.0[concatenated];"
                     "[concatenated]scale=-2:360,pad=ceil(iw/2)*2:ceil(ih/2)*2[outv0]")
    with pytest.raises(ValueError, match="must output"):
        build_streaming_filtergraph(1, 640, 360, 30.0, [{"resolution": 360}], DEINTERLACE,
                                    filter_complex="[0:v:0]fps={fps}[out]")


@pytest.mark.parametrize("value,expected", [
    ('[{"inputs": ["0:v"], "filters": ["null"], "outputs": ["concatenated"]}]',
     [{"inputs": ["0:v"], "filters": ["null"], "outputs": ["concatenated"]}]),
    # Pretty-printed JSON, as json.dumps(chains, indent=2) writes it
    ('[\n  {\n    "inputs": ["0:v"],\n    "filters": ["null"],\n    "outputs": ["concatenated"]\n  }\n]',
     [{"inputs": ["0:v"], "filters": ["null"], "outputs": ["concatenated"]}]),
    ("[0:v]fps={fps}[concatenated]", "[0:v]fps={fps}[concatenated]"),
    (None, None),
])
def test_parse_filter_complex(value, expected):
    from tator.transcode.__main__ import _parse_filter_complex
    assert _parse_filter_complex(value) == expected

