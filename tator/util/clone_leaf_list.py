def _convert_for_post(leaf, leaf_type_mapping, parent_mapping):
    # Swap parent IDs.
    parent_id = leaf.parent
    if parent_id:
        if parent_id in parent_mapping:
             parent_id = parent_mapping[parent_id]
        else:
            raise ValueError(f"Source parent ID {parent_id} missing from parent_mapping!")
    # Swap leaf type IDs.
    leaf_type_id = leaf.type
    if leaf_type_id in leaf_type_mapping:
        leaf_type_id = leaf_type_mapping[leaf_type_id]
    else:
        raise ValueError(f"Source leaf_type ID {leaf_type_id} missing from "
                          "leaf_type_mapping!")
    # Fill in required fields for post.
    spec = {'name': leaf.name,
            'type': leaf_type_id,
            'parent': parent_id,
            **leaf.attributes}
    spec = {key:spec[key] for key in spec if spec[key] is not None}
    return spec

def clone_leaf_list(src_api, query_params, dest_project, parent_mapping,
                    leaf_type_mapping, dest_api=None):
    """ Clone leaf list.

    This can be used to clone leaves from one project to another or from one
    host to another.

    Example for different host:

    .. code-block:: python

        src_api = tator.get_api(host, token)
        dest_api = tator.get_api(other_host, other_token)
        query_params = {'project': 1, 'depth': 1}
        dest_project = 1
        created_ids = []
        parent_mapping = {1: 10} # Mapping of parent leaf IDs
        leaf_type_mapping = {1: 10} # Source leaf type ID -> Dest leaf type ID
        generator = clone_leaf_list(src_api, query_params, dest_project, parent_mapping,
                                    leaf_type_mapping, dest_api)
        for num_created, num_total, response, id_map in generator:
            print(f"Created {num_created} of {num_total} leafs...")
            created_ids.append(response.id)
        print(f"Finished creating {num_created} leafs!")

    Example for same host:

    .. code-block:: python

        api = tator.get_api(host, token)
        query_params = {'project': 1, 'depth': 1}
        dest_project = 1
        parent_mapping = {1: 10}
        leaf_type_mapping = {1: 10} # Source leaf type ID -> Dest leaf type ID
        created_ids = []
        generator = clone_leaf_list(api, query_params, dest_project, parent_mapping)
        for num_created, num_total, response, id_map in generator:
            print(f"Created {num_created} of {num_total} leafs...")
            created_ids += response.id
        print(f"Finished creating {num_created} leafs!")

    :param src_api: :class:`tator.TatorApi` object corresponding to source host or only
        host if this is a clone on same host.
    :param query_params: Dictionary containing query parameters for source leaf list.
    :param dest_project: Unique integer identifying destination project.
    :param parent_mapping: Dictionary mapping source parent leaf IDs to destination parent leaf
        IDs. If the source leaf list contains a parent ID for which a destination parent ID is
        not supplied, an exception is raised.
    :param leaf_type_mapping: Dictionary mapping source leaf type IDs to destination 
        leaf_type IDs. If the source leaf list contains a leaf type ID for which a
        destination leaf type ID is not supplied, an exception is raised.
    :param dest_api: :class:`tator.TatorApi` object corresponding to destination host.
    :returns: Generator containing number of leafs created, number of leafs total,
        most recent response from leaf creation operation, and mapping between
        original IDs and created IDs.
    """
    # Make sure query has a project.
    if 'project' not in query_params:
        raise Exception("Query parameters must include a project!")

    # Set the dest_api if not given.
    if dest_api is None:
        dest_api = src_api

    # Start by getting list of leafs to be cloned.
    leafs = src_api.get_leaf_list(**query_params)

    # Convert to new spec.
    spec = [_convert_for_post(leaf, leaf_type_mapping, parent_mapping)
            for leaf in leafs]

    # Create the leafs.
    created_ids = []
    total_leafs = len(spec)
    for idx in range(0, total_leafs, 500):
        response = dest_api.create_leaf_list(dest_project, body=spec[idx:idx+500])
        created_ids += response.id
        id_map = {src.id: dest_id for src, dest_id in zip(leafs[idx:idx+500], response.id)}
        yield (len(created_ids), total_leafs, response, id_map)

