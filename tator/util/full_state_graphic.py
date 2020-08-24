import itertools

import tator

def full_state_graphic(api, state_id, force_scale=None):
    """ Retrieves all detection images for a state.

    Example:

    .. code-block:: python

        state_graphic = full_state_graphic(api, state_id)

    :param api: :class:`tator.TatorApi` object.
    :param state_id: Unique integer identifying a localization-associated state.
    :param force_scale: (Optional) wxh to force each tile prior to stitch.
    :returns: List containing all detection images in this state.
    """
    BATCH_SIZE = 30
    state = api.get_state(state_id)
    graphics = []
    for offset in range(0, len(state.localizations), BATCH_SIZE):
        kwargs = dict(mode='tile', length=BATCH_SIZE, offset=offset)
        if force_scale is not None:
            kwargs['force_scale'] = force_scale
        path = api.get_state_graphic(state_id, **kwargs)
        num_images = len(state.localizations[offset:offset+BATCH_SIZE])
        graphics.append(tator.util.get_images(path, state, num_images))
    return list(itertools.chain.from_iterable(graphics))
