def _convert_for_post(loc, dest_type, dest_version, media_mapping):
    # Check for media mapping.
    media_id = loc.media
    if media_id in media_mapping:
        media_id = media_mapping[media_id]
    else:
        raise ValueError(f"Source media ID {media_id} missing from media_mapping!")
    # Fill in required fields for post.
    return {'type': dest_type,
            'version': dest_version,
            'media_id': media_id,
            'x': loc.x,
            'y': loc.y,
            'width': loc.width,
            'height': loc.height,
            'u': loc.u,
            'v': loc.v,
            'frame': loc.frame,
            **loc.attributes}

def clone_localization_list(src_api, query_params, dest_project, media_mapping, dest_type=-1, 
                            dest_version=-1, dest_api=None):
    """ Clone localization list.

    This can be used to clone localizations from one project to another or from one
    host to another.

    Example for different host:

    .. code-block:: python

        src_api = tator.get_api(host, token)
        dest_api = tator.get_api(other_host, other_token)
        query_params = {'project': 1, 'media_id': [1]}
        media_mapping = {1: 10} # Source media ID -> Dest media ID
        dest_project = 1
        dest_type = -1
        dest_version = -1
        created_ids = []
        generator = clone_localization_list(src_api, query_params, dest_project, media_mapping,
                                            dest_type, dest_version, dest_api)
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
        created_ids = []
        for num_created, num_total, response in clone_localization_list(src_api, query_params,
                                                                        dest_project, media_mapping):
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
    :param dest_type: Unique integer identifying destination localization type. If set to
        -1, the localization type is set to the first localization type in the project.
    :param dest_version: Unique integer identifying destination version. If set to
        -1, the version is set to the lowest number version in the project.
    :param dest_api: :class:`tator.TatorApi` object corresponding to destination host.
    :returns: Generator containing number of localizations created, number of localizations total,
        and most recent response from localization creation operation.
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

    # Guess the version if it was not given.
    if dest_version == -1:
        versions = dest_api.get_version_list(dest_project)
        if len(versions) == 0:
            raise Exception('Specified project does not have any versions!')
        version = min(versions, key=lambda v: v.number)
        dest_version = version.id

    # Start by getting list of localizations to be cloned.
    locs = src_api.get_localization_list(**query_params)

    # Convert to new spec.
    spec = [_convert_for_post(loc, dest_type, dest_version, media_mapping) for loc in locs]

    # Create the localizations.
    created_ids = []
    total_localizations = len(spec)
    for idx in range(0, total_localizations, 500):
        response = dest_api.create_localization_list(dest_project,
                                                     localization_spec=spec[idx:idx+500])
        created_ids += response.id
        yield (len(created_ids), total_localizations, response)

