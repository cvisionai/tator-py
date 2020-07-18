import os
from ..openapi import tator_openapi

def get_api(host='https://www.tatorapp.com', token=os.getenv('TATOR_TOKEN')):
    """ Retrieves a :class:`tator.api` instance using the given host and token.

    :param host: URL of host. Default is https://www.tatorapp.com.
    :param token: API token.
    :returns: :class:`tator.api` object.
    """
    config = tator_openapi.Configuration()
    config.host = host
    if token:
        config.api_key['Authorization'] = token
        config.api_key_prefix['Authorization'] = 'Token'
    return tator_openapi.TatorApi(tator_openapi.ApiClient(config))
