import os
from ..openapi import tator_openapi as pytator

def get_api(host='https://www.tatorapp.com', token=os.getenv('TATOR_TOKEN')):
    """ Retrieves a TatorApi instance using the given host and token.
    """
    config = pytator.Configuration()
    config.host = host
    config.api_key['Authorization'] = token
    config.api_key_prefix['Authorization'] = 'Token'
    return pytator.TatorApi(pytator.ApiClient(config))
