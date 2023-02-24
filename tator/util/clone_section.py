def clone_section(src_api, src_section_id, dest_project, dest_api=None):
    """ Clone section.

    This can be used to clone sections from one project to another or from one
    host to another.

    Example for different host:

    .. code-block:: python

        src_api = tator.get_api(host, token)
        dest_api = tator.get_api(other_host, other_token)
        src_section_id = 1
        dest_project = 1
        response = tator.util.clone_section(src_api, src_section_id, dest_project, dest_api)
        print(response.message)

    Example for same host:

    .. code-block:: python

        api = tator.get_api(host, token)
        src_section_id = 1
        dest_project = 1
        response = tator.util.clone_section(src_api, src_section_id, dest_project)
        print(response.message)

    :param src_api: :class:`tator.TatorApi` object corresponding to source host or only
        host if this is a clone on same host.
    :param src_section_id: Unique integer identifying section to clone.
    :param dest_project: Unique integer identifying destination project.
    :param dest_api: :class:`tator.TatorApi` object corresponding to destination host.
    :returns: Response from section creation request.
    """
    section_obj = src_api.get_section(src_section_id)
    spec = {'name': section_obj.name}
    if section_obj.object_search:
        spec['object_search'] = section_obj.object_search
    if section_obj.tator_user_sections:
        spec['tator_user_sections'] = section_obj.tator_user_sections
    if dest_api is None:
        dest_api = src_api
    return dest_api.create_section(dest_project, section_spec=spec)
