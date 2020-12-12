def clone_media_type(src_api, src_type_id, dest_project, dest_api=None):
    """ Clone media type.

    This can be used to clone media types from one project to another or from one
    host to another.

    Example for different host:

    .. code-block:: python

        src_api = tator.get_api(host, token)
        dest_api = tator.get_api(other_host, other_token)
        src_type_id = 1
        dest_project = 1
        response = tator.util.clone_media_type(src_api, src_type_id, dest_project, dest_api)
        print(response.message)

    Example for same host:

    .. code-block:: python

        api = tator.get_api(host, token)
        src_type_id = 1
        dest_project = 1
        response = tator.util.clone_media_type(src_api, src_type_id, dest_project)
        print(response.message)

    :param src_api: :class:`tator.TatorApi` object corresponding to source host or only
        host if this is a clone on same host.
    :param src_type_id: Unique integer identifying media type to clone.
    :param dest_project: Unique integer identifying destination project.
    :param dest_api: :class:`tator.TatorApi` object corresponding to destination host.
    :returns: Response from media type creation request.
    """
    type_obj = src_api.get_media_type(src_type_id)
    spec = {'name': type_obj.name,
            'description': type_obj.description,
            'dtype': type_obj.dtype,
            'default_volume': type_obj.default_volume,
            'attribute_types': type_obj.attribute_types}
    if type_obj.file_format:
        spec['file_format'] = type_obj.file_format
    if type_obj.overlay_config:
        spec['overlay_config'] = type_obj.overlay_config
    if type_obj.streaming_config:
        spec['streaming_config'] = type_obj.streaming_config
    if type_obj.archive_config:
        spec['archive_config'] = type_obj.archive_config
    if dest_api is None:
        dest_api = src_api
    return dest_api.create_media_type(dest_project, media_type_spec=spec)
