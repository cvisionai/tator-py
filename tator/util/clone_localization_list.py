def _convert_for_post(loc, dest_type, media_mapping, version_mapping):
    # Check for media mapping.
    media_id = loc.media
    if media_id in media_mapping:
        media_id = media_mapping[media_id]
    else:
        raise ValueError(f"Source media ID {media_id} missing from media_mapping!")
    # Check for version mapping.
    version_id = loc.version
    if version_id in version_mapping:
        version_id = version_mapping[version_id]
    else:
        raise ValueError(f"Source version ID {version_id} missing from version_mapping!")
    # Fill in required fields for post.
    return {'type': dest_type,
            'version': version_id,
            'media_id': media_id,
            'x': loc.x,
            'y': loc.y,
            'width': loc.width,
            'height': loc.height,
            'u': loc.u,
            'v': loc.v,
            'frame': loc.frame,
            **loc.attributes}

def clone_localization_list(src_api, query_params, dest_project, media_mapping, version_mapping,
                            dest_type=-1, dest_api=None):
    """ Clone localization list.

    This can be used to clone localizations from one project to another or from one
    host to another.

    Example for different host:

    .. code-block:: python

        src_api = tator.get_api(host, token)
        dest_api = tator.get_api(other_host, other_token)
        query_params = {'project': 1, 'media_id': [1]}
        media_mapping = {1: 10} # Source media ID -> Dest media ID
        version_mapping = {1: 10} # Source version ID -> Dest version ID
        dest_project = 1
        dest_type = -1
        created_ids = []
        generator = clone_localization_list(src_api, query_params, dest_project, media_mapping,
                                            version_mapping, dest_type, dest_api)
        for num_created, num_total, response in generator:
            print(f"Created {num_created} of {num_total} localizations...")
            created_ids.append(response.id)
        print(f"Finished creating {num_created} localizations!")

    Example for same host:

    .. code-block:: python

        api = tator.get_api(host, token)
        query_params = {'media_id': [1]}
        dest_project = 1
        media_mapping = {1: 10}
        version_mapping = {1: 10}
        created_ids = []
        for num_created, num_total, response in clone_localization_list(src_api, query_params,
                                                                        dest_project, media_mapping,
                                                                        version_mapping):
            print(f"Created {num_created} of {num_total} localizations...")
            created_ids += response.id
        print(f"Finished creating {num_created} localizations!")

    :param src_api: :class:`tator.TatorApi` object corresponding to source host or only
        host if this is a clone on same host.
    :param query_params: Dictionary containing query parameters for source localization list.
    :param dest_project: Unique integer identifying destination project.
    :param media_mapping: Dictionary mapping source media IDs to destination media IDs. If the
        source localization list contains a media ID for which a destination media is not supplied, 
        an exception is raised.
    :param version_mapping: Dictionary mapping source version IDs to destination version IDs. If the
        source localization list contains a version ID for which a destination version is not supplied, 
        an exception is raised.
    :param dest_type: Unique integer identifying destination localization type. If set to
        -1, the localization type is set to the first localization type in the project.
    :param dest_version: Unique integer identifying destination version. If set to
        -1, the version is set to the lowest number version in the project.
    :param dest_api: :class:`tator.TatorApi` object corresponding to destination host.
    :returns: Generator containing number of localizations created, number of localizations total,
        most recent response from localization creation operation, and mapping between original IDs
        and created IDs.
    """
    # Make sure query has a project.
    if 'project' not in query_params:
        raise Exception("Query parameters must include a project!")

    # Set the dest_api if not given.
    if dest_api is None:
        dest_api = src_api

    # Guess the localization type if it was not given.
    if dest_type == -1:
        loc_types = dest_api.get_localization_type_list(dest_project)
        if len(loc_types) == 0:
            raise Exception('Specified project does not have any localization types!')
        dest_type = loc_types[0].id

    # Start by getting list of localizations to be cloned.
    locs = src_api.get_localization_list(**query_params)

    # Convert to new spec.
    spec = [_convert_for_post(loc, dest_type, media_mapping, version_mapping) for loc in locs]

    # Create the localizations.
    created_ids = []
    total_localizations = len(spec)
    for idx in range(0, total_localizations, 500):
        response = dest_api.create_localization_list(dest_project,
                                                     localization_spec=spec[idx:idx+500])
        created_ids += response.id
        id_map = {src.id: dest_id for src, dest_id in zip(locs[idx:idx+500], response.id)}
        yield (len(created_ids), total_localizations, response, id_map)

