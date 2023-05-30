import logging
import os
import hashlib

logger = logging.getLogger(__name__)

def make_live_stream(api, type_id, layout, name, section, feedInfo):
    """ Make a live stream tator media object.

    :param api: :class:`tator.TatorApi` object.
    :param type_id: Unique integer identifying a multi-stream media type.
    :param layout: 2 element list of integers defining layout as [rows, cols].
    :param name: Name of the file to use
    :param section: Section name. If this section does not exist it will be created.
    :param feed_info: maybeList of :class:`tator.models.LiveDefinition` object or dictionary.
    :returns: Response from media object creation.
    """

    # Fetch the stuff we need to download files
    config = api.api_client.configuration
    host = config.host
    token = config.api_key['Authorization']
    prefix = config.api_key_prefix['Authorization']

    # use a live extension, if one is not specified
    if os.path.splitext(name)[1] == '':
        name += ".live"

    if type(feedInfo) is list:
        pass
    else:
        feedInfo = [feedInfo]

    # Fetch the media type
    live_stream_type = api.get_media_type(type_id)
    project = live_stream_type.project

    assert(len(feedInfo) == layout[0]*layout[1])

    # Calculate md5sum of configuration
    digest = hashlib.md5()
    digest.update(f"{feedInfo}".encode())
    md5_of_config = digest.hexdigest()


    media_spec = {
        "name": name,
        "type": type_id,
        "section": section,
        "md5": md5_of_config,
    }
    create_resp = api.create_media_list(project, [media_spec])

    patch_object = {"live": {"layout": layout, "streams": feedInfo}}
    return api.update_media(create_resp.id[0], patch_object)

