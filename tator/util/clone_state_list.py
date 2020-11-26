def _convert_for_post(state, dest_type, dest_version, media_mapping, localization_mapping):
    # Swap media IDs.
    media_ids = state.media
    for idx, media_id in enumerate(media_ids):
        if media_id in media_mapping:
            media_ids[idx] = media_mapping[media_id]
        else:
            raise ValueError(f"Source media ID {media_id} missing from media_mapping!")
    # Swap localization IDs.
    localization_ids = state.localizations
    for idx, localization_id in enumerate(localization_ids):
        if localization_id in localization_mapping:
            localization_ids[idx] = localization_mapping[localization_id]
        else:
            raise ValueError(f"Source localization ID {localization_id} missing from "
                              "localization_mapping!")
    # Fill in required fields for post.
    return {'type': dest_type,
            'version': dest_version,
            'media_ids': media_ids,
            'localization_ids': localization_ids,
            'frame': state.frame,
            **state.attributes}

def clone_state_list(src_api, query_params, dest_project, media_mapping, localization_mapping,
                     dest_type=-1, dest_version=-1, dest_api=None):
    """ Clone state list.

    This can be used to clone states from one project to another or from one
    host to another.

    Example for different host:

    .. code-block:: python

        src_api = tator.get_api(host, token)
        dest_api = tator.get_api(other_host, other_token)
        query_params = {'project': 1, 'media_id': [1]}
        media_mapping = {1: 10} # Source media ID -> dest media ID
        localization_mapping = {} # For tracks, source localization ID -> dest localization ID
        dest_project = 1
        dest_type = -1
        dest_version = -1
        created_ids = []
        generator = clone_state_list(src_api, query_params, dest_project, media_mapping,
                                     localization_mapping, dest_type, dest_version, dest_api)
        for num_created, num_total, response in generator:
            print(f"Created {num_created} of {num_total} states...")
            created_ids.append(response.id)
        print(f"Finished creating {num_created} states!")

    Example for same host:

    .. code-block:: python

        api = tator.get_api(host, token)
        query_params = {'media_id': [1]}
        dest_project = 1
        media_mapping = {1: 10}
        localization_mapping = {}
        created_ids = []
        for num_created, num_total, response in clone_state_list(src_api, query_params,
                                                                 dest_project, media_mapping,
                                                                 localization_mapping):
            print(f"Created {num_created} of {num_total} states...")
            created_ids += response.id
        print(f"Finished creating {num_created} states!")

    :param src_api: :class:`tator.TatorApi` object corresponding to source host or only
        host if this is a clone on same host.
    :param query_params: Dictionary containing query parameters for source state list.
    :param dest_project: Unique integer identifying destination project.
    :param media_mapping: Dictionary mapping source media IDs to destination media IDs. If the
        source state list contains a media ID for which a destination media is not supplied, 
        an exception is raised.
    :param localization_mapping: Dictionary mapping source localization IDs to destination 
        localization IDs. If the source state list contains a localization ID for which a
        destination localization ID is not supplied, an exception is raised.
    :param dest_type: Unique integer identifying destination state type. If set to
        -1, the state type is set to the first state type in the project.
    :param dest_version: Unique integer identifying destination version. If set to
        -1, the version is set to the lowest number version in the project.
    :param dest_api: :class:`tator.TatorApi` object corresponding to destination host.
    :returns: Generator containing number of states created, number of states total,
        and most recent response from state creation operation.
    """
    # Make sure query has a project.
    if 'project' not in query_params:
        raise Exception("Query parameters must include a project!")

    # Set the dest_api if not given.
    if dest_api is None:
        dest_api = src_api

    # Guess the state type if it was not given.
    if dest_type == -1:
        state_types = dest_api.get_state_type_list(dest_project)
        if len(state_types) == 0:
            raise Exception('Specified project does not have any state types!')
        dest_type = state_types[0].id

    # Guess the version if it was not given.
    if dest_version == -1:
        versions = dest_api.get_version_list(dest_project)
        if len(versions) == 0:
            raise Exception('Specified project does not have any versions!')
        version = min(versions, key=lambda v: v.number)
        dest_version = version.id

    # Start by getting list of states to be cloned.
    states = src_api.get_state_list(**query_params)

    # Convert to new spec.
    spec = [_convert_for_post(state, dest_type, dest_version, media_mapping, localization_mapping)
            for state in states]

    # Create the states.
    created_ids = []
    total_states = len(spec)
    for idx in range(0, total_states, 500):
        response = dest_api.create_state_list(dest_project,
                                              state_spec=spec[idx:idx+500])
        created_ids += response.id
        yield (len(created_ids), total_states, response)

