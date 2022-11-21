from difflib import get_close_matches
from functools import partial
import logging
import re


logger = logging.getLogger(__name__)


class Paginator:
    """Manages retrieving pages of results for `get_*_list[_by_id]` API functions"""

    def __init__(self, fn, name, batch_size):
        self._fn = fn
        self._name = name
        self._batch_size = batch_size

    def paginate(self, **kwargs):
        """
        Passes `kwargs` to the stored function and yields pages of results with (at most)
        `_batch_size` results.
        """
        get_page = partial(self._fn, **kwargs)
        page_count = self._batch_size
        page_num = 0
        msg = self._name + " returned page {} ({} cumulative results)."

        while page_count == self._batch_size:
            start = page_num * self._batch_size
            page = get_page(start=start, stop=start + self._batch_size)
            page_count = len(page)
            logger.info(msg.format(page_num + 1, page_count + start))
            page_num += 1
            yield page


def get_paginator(api, func_name, batch_size=1000):
    """Returns a Paginator object that returns pages of results from the given `func_name`.

    Example:

    .. code-block:: python

        import tator

        api = tator.get_api(host, token)
        media_paginator = tator.util.get_paginator(api, "get_media_list")
        page_iterator = media_paginator.paginate(project=project_id)
        all_media = []
        for page in page_iterator:
            for media in page:
                all_media.append(media)

    :param api: :class:`tator.TatorApi` object.
    :param str func_name:
    :param int batch_size:
    :returns: Paginator object
    """
    if not re.search(r"^get_.+_list(_by_id)?$", func_name):
        raise ValueError(
            f"Cannot paginate '{func_name}', expected a `get_<entity>_list` or "
            f"`get_<entity>_list_by_id` method"
        )
    try:
        fn = getattr(api, func_name)
    except AttributeError:
        similar = get_close_matches(func_name, dir(api), n=1)[0]
        raise ValueError(f"TatorApi has no function '{func_name}', did you mean '{similar}'?")
    return Paginator(fn, func_name, batch_size)
