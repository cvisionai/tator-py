import os
from ..openapi.client import get_api as _get_api


def get_api(host='https://cloud.tator.io', token=os.getenv('TATOR_TOKEN')):
    """ Retrieves a :class:`tator.api` instance using the given host and token.

    :param host: URL of host. Default is https://cloud.tator.io.
    :param token: API token.
    :returns: :class:`tator.api` object.
    """
    return _get_api(host, token)
