""" ffmpeg filter graphs as data.

A graph is a list of chains, each a dict::

    {"inputs": ["0:v:0"], "filters": ["setsar=1", {"name": "fps", "args": [30]}], "outputs": ["vid0"]}

:func:`render_filtergraph` turns that into the string ``-filter_complex`` expects. A streaming
transcode's graph has two stages: an input stage from the source segments and the black tail clip
to ``[concatenated]`` (:func:`streaming_input_chains`), and an output stage from
``[concatenated]`` to one ``[outvN]`` per resolution (:func:`streaming_output_chains`). Callers
can replace the input stage with their own chains, as long as it produces ``[concatenated]``.
"""

CONCATENATED = "concatenated"

# Characters with meaning in filter graph or filter option syntax.
_SPECIAL_CHARACTERS = set("[];,:='\\")


def filter_chain(inputs, filters, outputs):
    """ Returns a chain dict. Labels are given without brackets. """
    return {"inputs": list(inputs), "filters": list(filters), "outputs": list(outputs)}


def _render_value(value):
    text = str(value)
    if _SPECIAL_CHARACTERS & set(text):
        raise ValueError(f"Filter option value {text!r} needs escaping; give the filter as a "
                         "rendered string instead")
    return text


def render_filter(spec):
    """ Renders one filter.

    :param spec: A rendered string such as ``"scale=-2:720"``, used as is, or a dict with
                 ``name`` and optional positional ``args`` and named ``options``.
    """
    if isinstance(spec, str):
        return spec
    parts = [_render_value(arg) for arg in spec.get("args", [])]
    parts.extend(f"{key}={_render_value(value)}" for key, value in spec.get("options", {}).items())
    return f"{spec['name']}={':'.join(parts)}" if parts else spec["name"]


def render_filtergraph(chains):
    """ Renders a list of chain dicts as a -filter_complex string. """
    rendered = []
    for chain in chains:
        if not chain.get("filters"):
            raise ValueError(f"Filter chain {chain} has no filters")
        inputs = "".join(f"[{label}]" for label in chain.get("inputs", []))
        outputs = "".join(f"[{label}]" for label in chain.get("outputs", []))
        rendered.append(inputs + ",".join(render_filter(spec) for spec in chain["filters"])
                        + outputs)
    return ";".join(rendered)


def format_chains(chains, **values):
    """ Returns a copy of chains with str.format(**values) applied to labels and string filters.

    Lets externally generated chains use placeholders such as ``{fps}``, ``{width}``,
    ``{height}`` and ``{num_segments}``. Write literal braces as ``{{`` and ``}}``.
    """
    def fmt(item):
        return item.format(**values) if isinstance(item, str) else item
    return [
        filter_chain([fmt(label) for label in chain.get("inputs", [])],
                     [fmt(spec) for spec in chain.get("filters", [])],
                     [fmt(label) for label in chain.get("outputs", [])])
        for chain in chains
    ]


def check_input_stage(chains):
    """ Raises ValueError unless the chains produce [concatenated] exactly once. """
    produced = [label for chain in chains for label in chain.get("outputs", [])]
    if produced.count(CONCATENATED) != 1:
        raise ValueError(f"A streaming input stage must output [{CONCATENATED}] exactly once, "
                         f"got outputs {produced}")


def streaming_input_chains(num_segments, width, height, fps, deinterlace):
    """ Chains from source segments 0..n-1 and the black tail clip (input n) to [concatenated].

    :param width: Width of the decoded (autorotated) source frames.
    :param height: Height of the decoded (autorotated) source frames.
    :param deinterlace: Deinterlace filter applied to each segment.
    """
    chains = [
        filter_chain([f"{idx}:v:0"], [deinterlace, "setsar=1", f"fps={fps}"], [f"vid{idx}"])
        for idx in range(num_segments)
    ]
    # Scale the black clip to the source resolution prior to concating and scaling back down.
    chains.append(filter_chain([f"{num_segments}:v:0"],
                               [f"scale={width}:{height}", "setsar=1", f"fps={fps}"],
                               ["bv"]))
    chains.append(filter_chain([f"vid{idx}" for idx in range(num_segments)] + ["bv"],
                               [f"concat=n={num_segments + 1}:v=1:a=0"],
                               [CONCATENATED]))
    return chains


def streaming_output_chains(outputs):
    """ Chains from [concatenated] to [outv0] .. [outvN-1], one per output.

    :param outputs: Dicts with a ``resolution`` and optional ``filters`` to run after scaling,
                    such as hardware upload.
    """
    tails = [
        [f"scale=-2:{output['resolution']}", "pad=ceil(iw/2)*2:ceil(ih/2)*2",
         *output.get("filters", [])]
        for output in outputs
    ]
    if len(outputs) == 1:
        # Single resolution - no split needed, pipe directly from [concatenated]
        return [filter_chain([CONCATENATED], tails[0], ["outv0"])]
    split = filter_chain([CONCATENATED], [f"split={len(outputs)}"],
                         [f"split{ridx}" for ridx in range(len(outputs))])
    return [split] + [filter_chain([f"split{ridx}"], tail, [f"outv{ridx}"])
                      for ridx, tail in enumerate(tails)]


def build_streaming_filtergraph(num_segments, width, height, fps, outputs, deinterlace,
                                filter_complex=None):
    """ Returns the -filter_complex string for a streaming transcode.

    :param filter_complex: Optional replacement for the input stage. Either chain dicts (see
                           :func:`format_chains` for placeholders) or a string template using
                           ``{fps}`` (and ``{hw_upload}``, now always empty) that ends in
                           ``[concatenated]``.
    """
    output_graph = render_filtergraph(streaming_output_chains(outputs))
    if filter_complex is None:
        input_chains = streaming_input_chains(num_segments, width, height, fps, deinterlace)
    elif isinstance(filter_complex, str):
        # Hardware upload now happens per output, so {hw_upload} is always empty.
        input_graph = filter_complex.format(fps=fps, hw_upload='').strip().rstrip(';')
        if f"[{CONCATENATED}]" not in input_graph:
            raise ValueError(f"filter_complex must output [{CONCATENATED}]")
        return f"{input_graph};{output_graph}"
    else:
        input_chains = format_chains(filter_complex, fps=fps, width=width, height=height,
                                     num_segments=num_segments)
    check_input_stage(input_chains)
    return f"{render_filtergraph(input_chains)};{output_graph}"
