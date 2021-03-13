def clone_localization_type(src_api, src_type_id, dest_project, media_type_mapping, dest_api=None):
    """ Clone localization type.

    This can be used to clone localization types from one project to another or from one
    host to another.

    Example for different host:

    .. code-block:: python

        src_api = tator.get_api(host, token)
        dest_api = tator.get_api(other_host, other_token)
        src_type_id = 1
        dest_project = 1
        media_type_mapping = {1: 10}
        response = tator.util.clone_localization_type(src_api, src_type_id, dest_project,
                                                      media_type_mapping, dest_api)
        print(response.message)

    Example for same host:

    .. code-block:: python

        api = tator.get_api(host, token)
        src_type_id = 1
        dest_project = 1
        response = tator.util.clone_localization_type(src_api, src_type_id, dest_project,
                                                      media_type_mapping)
        print(response.message)

    :param src_api: :class:`tator.TatorApi` object corresponding to source host or only
        host if this is a clone on same host.
    :param src_type_id: Unique integer identifying localization type to clone.
    :param dest_project: Unique integer identifying destination project.
    :param media_type_mapping: Dictionary mapping source media types to destination media types.
    :param dest_api: :class:`tator.TatorApi` object corresponding to destination host.
    :returns: Response from localization type creation request.
    """
    type_obj = src_api.get_localization_type(src_type_id)
    spec = {'name': type_obj.name,
            'description': type_obj.description,
            'dtype': type_obj.dtype,
            'grouping_default': type_obj.grouping_default,
            'color_map': type_obj.color_map,
            'line_width': type_obj.line_width,
            'visible': type_obj.visible,
            'attribute_types': type_obj.attribute_types}
    dest_media_types = set()
    for src_media_type in type_obj.media:
        if src_media_type in media_type_mapping:
            dest_media_types.add(media_type_mapping[src_media_type])
        else:
            raise ValueError(f"Media type mapping does not contain source media ID {src_media_type}!")
    spec['media_types'] = list(dest_media_types)
    if dest_api is None:
        dest_api = src_api
    return dest_api.create_localization_type(dest_project, localization_type_spec=spec)
