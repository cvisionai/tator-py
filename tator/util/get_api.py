import os
from ..openapi import tator_openapi


def get_api(host='https://cloud.tator.io', token=os.getenv('TATOR_TOKEN')):
    """ Retrieves a :class:`tator.api` instance using the given host and token.

    :param host: URL of host. Default is https://cloud.tator.io.
    :param token: API token.
    :returns: :class:`tator.api` object.
    """
    config = tator_openapi.Configuration()
    config.host = host
    if token:
        config.api_key['Authorization'] = token
        config.api_key_prefix['Authorization'] = 'Token'

    api = tator_openapi.TatorApi(tator_openapi.ApiClient(config))

    def legacy_create_media(project, media_spec, **kwargs):
        return api.create_media_list(project, [media_spec], **kwargs)

    api.create_media = legacy_create_media
    return api
