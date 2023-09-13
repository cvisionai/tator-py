import logging
from math import floor
from typing import Callable
import time

logger = logging.getLogger(__name__)


def chunked_create(func: Callable, project: int, chunk_size: int = 500, **kwargs):
    """Breaks a create_*_list operation into chunks.

    Example:

    .. code-block:: python

        created_ids = [
            new_id
            for response in tator.util.chunked_create(
                api.create_localization_list, chunk_size=100, body=my_long_list
            )
            for new_id in response.id
        ]

    :param func: Function to call on each chunk.
    :param project: Unique integer identifying a project.
    :param chunk_size: [Optional] Sets the size of the chunks, defaults to 500.
    :param kwargs: Exactly one keyword argument should be set, which contains the list of specs to
                   create and is passed to `func`
    :returns: Generator that yields a response.
    """
    if len(kwargs) != 1:
        raise RuntimeError(f"Expects exactly one keyword argument")

    key = list(kwargs.keys())[0]
    spec = kwargs[key]
    n_specs = len(spec)
    while chunk_size > 0 and spec:
        n_created = 0
        try:
            for idx in range(0, len(spec), chunk_size):
                try:
                    response = func(project, **{key: spec[idx : idx + chunk_size]})
                    n_created += len(response.id)
                    yield response
                except Exception:
                    # Back-off once, wait 5 seconds, and try again. This helps work around
                    # if we trip a DDOS firewall in a bulk import
                    time.sleep(5)
                    response = func(project, **{key: spec[idx : idx + chunk_size]})
                    n_created += len(response.id)
                    yield response
        except Exception:
            chunk_size = floor(chunk_size / 2)
            logger.warning("Caught exception, halving chunk size to %d", chunk_size, exc_info=True)
        spec = spec[n_created:]
    if spec:
        raise RuntimeError(f"Was not able to create {len(spec)} of {n_specs} objects")
