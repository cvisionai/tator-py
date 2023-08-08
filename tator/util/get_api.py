import os
from ..openapi import tator_openapi
from ..openapi.tator_openapi.models import CreateResponse


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
        """
        Provides a matching legacy interface to the create media endpoint that returns a
        :class:`tator.openapi.tator_openapi.models.CreateResponse` object instead of
        :class:`tator.openapi.tator_openapi.models.CreateListResponse`
        """

        response = api.create_media_list(project, [media_spec], **kwargs)
        return CreateResponse(
            id=response.id[0], message=response.message, object=response.object[0]
        )

    api.create_media = legacy_create_media
    return api
