from difflib import get_close_matches
from functools import partial
import logging
import re
from typing import Optional


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

        # Set up function with all shared arguments as a partial function
        get_page = partial(self._fn, **kwargs)

        # Initialize progress tracking variables
        page_count = self._batch_size
        page_num = 0
        cum_count = 0
        last_id = None
        msg = self._name + " returned page {} ({} cumulative results)."

        # Loop until a page smaller than the desired `_batch_size` is returned, this signals the end
        # of the list
        while page_count == self._batch_size:
            page = get_page(after=last_id, start=0, stop=self._batch_size)
            page_count = len(page)
            cum_count += page_count
            page_num += 1
            logger.info(msg.format(page_num, cum_count))
            yield page

            # Update `last_id` for next page
            next_last_id = None
            while page:
                try:
                    next_last_id = page[-1].id
                except Exception:
                    logger.warning("Could not get ID from last result in page", exc_info=True)
                    page.pop()
                else:
                    break
            if next_last_id is not None:
                last_id = next_last_id
            else:
                raise RuntimeError("Could not find an object in the last page with an id")


def get_paginator(api, func_name: str, batch_size: Optional[int] = 1000):
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
    :raises: ValueError if the `func_name` does not match the expected pattern or if it does not
             exist.
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
