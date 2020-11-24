
def clone_localization_list(src_api, query_params, dest_project, media_mapping, dest_type=-1, 
                            dest_api=None):
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
        created_ids = []
        for num_created, num_total, response in clone_localization_list(src_api, query_params,
                                                                        dest_project, media_mapping,
                                                                        dest_type, dest_api):
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
        source media list contains a media ID for which a destination media is not supplied, 
        an exception is raised.
    :param dest_type: Unique integer identifying destination localization type. If set to
        -1, the localization type is set to the first localization type in the project.
    :param dest_api: :class:`tator.TatorApi` object corresponding to destination host.
    :returns: Generator containing number of localizations created, number of localizations total,
        and most recent response from localization creation operation.
    """
    # Make sure query has a project.
    if 'project' not in query_params:
        raise Exception("Query parameters must include a project!")

    # Check for no pagination parameters.
    has_pagination = 'after' in query_params or 'start' in query_params or 'stop' in query_params
    if has_pagination:
        raise Exception("This utility does pagination internally and does not accept pagination "
                        "parameters as inputs!")

    # Guess the localization type if it was not given.
    if dest_type == -1:
        if dest_api is None:
            loc_types = src_api.get_localization_type_list(dest_project)
        else:
            loc_types = dest_api.get_localization_type_list(dest_project)
        if len(loc_types) == 0:
            raise Exception('Specified project does not have any localization types!')
        dest_type = loc_types[0]

    # Start by getting total number of localizations to be cloned.
    total_localizations = src_api.get_localization_count(**query_params)

    # Clone the localizations.
    created_ids = []
    after = None
    query_params['stop'] = 500
    query_params['start'] = 0
    while len(created_ids) < total_localizations:
        # Get paginated localizations.
        locs = src_api.get_localization_list(**query_params)
        # Set after parameter for next iteration.
        query_params['after'] = locs[-1].id
        if 'start' in query_params:
            query_params.pop('start', None)
        if dest_api is None:
            dest_api = src_api
        # Update media and type fields.
        for loc in locs:
            loc = loc.to_dict()
            loc.pop('meta', None)
            loc['type'] = dest_type
            if loc['media'] in media_mapping:
                loc['media'] = media_mapping[loc['media']]
            else:
                raise ValueError(f"Source media ID {loc['media']} missing from media_mapping!")
        # Create this batch.
        response = dest_api.create_localization_list(query_params['project'],
                                                     localization_spec=locs)
        created_ids += response.id
        yield (len(created_ids), total_files, response)
