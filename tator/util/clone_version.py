def clone_version(src_api, src_version_id, dest_project, version_mapping={}, dest_api=None):
    """ Clone version.

    This can be used to clone versions from one project to another or from one
    host to another.

    Example for different host:

    .. code-block:: python

        src_api = tator.get_api(host, token)
        dest_api = tator.get_api(other_host, other_token)
        src_version_id = 1
        dest_project = 1
        version_mapping = {} # Necessary if source version has base versions.
        response = tator.util.clone_version(src_api, src_version_id, dest_project,
                                            version_mapping, dest_api)
        print(response.message)

    Example for same host:

    .. code-block:: python

        api = tator.get_api(host, token)
        src_version_id = 1
        dest_project = 1
        response = tator.util.clone_version(src_api, src_version_id, dest_project)
        print(response.message)

    :param src_api: :class:`tator.TatorApi` object corresponding to source host or only
        host if this is a clone on same host.
    :param src_version_id: Unique integer identifying version to clone.
    :param dest_project: Unique integer identifying destination project.
    :param version_mapping: Dictionary mapping source version IDs to destination version IDs.
                            Necessary if source version defines `bases` field.
    :param dest_api: :class:`tator.TatorApi` object corresponding to destination host.
    :returns: Response from version creation request.
    """
    version_obj = src_api.get_version(src_version_id)
    spec = {'name': version_obj.name,
            'description': version_obj.description,
            'show_empty': version_obj.show_empty,
            'bases': []}
    for base in version_obj.bases:
        if base in version_mapping:
            spec['bases'].append(version_mapping[base])
        else:
            raise ValueError(f"Base version with ID {base} not contained in version mapping!")
    if dest_api is None:
        dest_api = src_api
    return dest_api.create_version(dest_project, version_spec=spec)
