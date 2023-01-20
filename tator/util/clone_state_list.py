def _convert_for_post(state, version_mapping, media_mapping, localization_mapping,
                      state_type_mapping):
    # Swap version IDs.
    version_id = state.version
    if version_id in version_mapping:
        version_id = version_mapping[version_id]
    else:
        raise ValueError(f"Source version ID {version_id} missing from version_mapping!")
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
    # Swap state type IDs.
    state_type_id = state.type
    if state_type_id in state_type_mapping:
        state_type_id = state_type_mapping[state_type_id]
    else:
        raise ValueError(f"Source state_type ID {state_type_id} missing from "
                          "state_type_mapping!")
    # Fill in required fields for post.
    spec = {'type': state_type_id,
            'version': version_id,
            'media_ids': media_ids,
            'localization_ids': localization_ids,
            **state.attributes}
    if state.frame is not None:
        spec['frame'] = state.frame
    spec = {key:spec[key] for key in spec if spec[key] is not None}
    return spec

def clone_state_list(src_api, query_params, dest_project, version_mapping, media_mapping,
                     localization_mapping, state_type_mapping, dest_api=None):
    """ Clone state list.

    This can be used to clone states from one project to another or from one
    host to another.

    Example for different host:

    .. code-block:: python

        src_api = tator.get_api(host, token)
        dest_api = tator.get_api(other_host, other_token)
        query_params = {'project': 1, 'media_id': [1]}
        version_mapping = {1: 10} # Source version ID -> Dest version ID
        media_mapping = {1: 10} # Source media ID -> dest media ID
        localization_mapping = {} # For tracks, source localization ID -> dest localization ID
        state_type_mapping = {1: 10} # Source state type ID -> Dest state type ID
        dest_project = 1
        dest_version = -1
        created_ids = []
        generator = clone_state_list(src_api, query_params, dest_project, version_mapping,
                                     media_mapping, localization_mapping, state_type_mapping,
                                     dest_api)
        for num_created, num_total, response, id_map in generator:
            print(f"Created {num_created} of {num_total} states...")
            created_ids.append(response.id)
        print(f"Finished creating {num_created} states!")

    Example for same host:

    .. code-block:: python

        api = tator.get_api(host, token)
        query_params = {'media_id': [1]}
        dest_project = 1
        version_mapping = {1: 10} # Source version ID -> Dest version ID
        media_mapping = {1: 10}
        localization_mapping = {}
        state_type_mapping = {1: 10} # Source state type ID -> Dest state type ID
        created_ids = []
        generator = clone_state_list(src_api, query_params, dest_project, version_mapping,
                                     media_mapping, localization_mapping, state_type_mapping)
        for num_created, num_total, response, id_map in generator:
            print(f"Created {num_created} of {num_total} states...")
            created_ids += response.id
        print(f"Finished creating {num_created} states!")

    :param src_api: :class:`tator.TatorApi` object corresponding to source host or only
        host if this is a clone on same host.
    :param query_params: Dictionary containing query parameters for source state list.
    :param dest_project: Unique integer identifying destination project.
    :param version_mapping: Dictionary mapping source version IDs to destination version IDs. If the
        source localization list contains a version ID for which a destination version is not supplied, 
        an exception is raised.
    :param media_mapping: Dictionary mapping source media IDs to destination media IDs. If the
        source state list contains a media ID for which a destination media is not supplied, 
        an exception is raised.
    :param localization_mapping: Dictionary mapping source localization IDs to destination 
        localization IDs. If the source state list contains a localization ID for which a
        destination localization ID is not supplied, an exception is raised.
    :param state_type_mapping: Dictionary mapping source state type IDs to destination 
        state_type IDs. If the source state list contains a state type ID for which a
        destination state type ID is not supplied, an exception is raised.
    :param dest_api: :class:`tator.TatorApi` object corresponding to destination host.
    :returns: Generator containing number of states created, number of states total,
        most recent response from state creation operation, and mapping between
        original IDs and created IDs.
    """
    # Make sure query has a project.
    if 'project' not in query_params:
        raise Exception("Query parameters must include a project!")

    # Set the dest_api if not given.
    if dest_api is None:
        dest_api = src_api

    # Start by getting list of states to be cloned.
    if 'state_id_query' in query_params:
        states = src_api.get_state_list_by_id(**query_params)
    else:
        states = src_api.get_state_list(**query_params)

    # Convert to new spec.
    spec = [_convert_for_post(state, version_mapping, media_mapping, localization_mapping,
                              state_type_mapping) for state in states]

    # Create the states.
    created_ids = []
    total_states = len(spec)
    for idx in range(0, total_states, 500):
        response = dest_api.create_state_list(dest_project, body=spec[idx:idx+500])
        created_ids += response.id
        id_map = {src.id: dest_id for src, dest_id in zip(states[idx:idx+500], response.id)}
        yield (len(created_ids), total_states, response, id_map)

