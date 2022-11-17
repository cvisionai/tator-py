from difflib import get_close_matches
from functools import partial


class Paginator:
    def __init__(self, fn, name, batch_size):
        self.fn = fn
        self.name = name
        self.batch_size = batch_size

    def paginate(self, **kwargs):
        func = partial(self.fn, **kwargs)
        page_results = self.batch_size
        page_num = 0
        msg = self.name + " returned page {} ({} cumulative results)."

        while page_results == self.batch_size:
            start = page_num * self.batch_size
            page = func(start=start, stop=start + self.batch_size)
            page_results = len(page)
            logger.info(msg.format(page_num + 1, page_results + start))
            page_num += 1
            yield page


def get_paginator(api, func_name, batch_size=1000):
    try:
        fn = getattr(api, func_name)
    except AttributeError:
        similar = get_close_matches(func_name, dir(api), n=1)[0]
        raise ValueError(f"TatorApi has no function '{func_name}', did you mean '{similar}'?")
    return Paginator(fn, name, batch_size)
