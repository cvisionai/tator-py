import logging

logger = logging.getLogger(__name__)

def _convert_for_post(loc, localization_type_mapping, version_mapping, media_mapping,
                      parent_mapping={}):
    # Check for version mapping.
    version_id = loc.version
    if version_id in version_mapping:
        version_id = version_mapping[version_id]
    else:
        raise ValueError(f"Source version ID {version_id} missing from version_mapping!")
    # Check for media mapping.
    media_id = loc.media
    if media_id in media_mapping:
        media_id = media_mapping[media_id]
    else:
        raise ValueError(f"Source media ID {media_id} missing from media_mapping!")
    # Swap localization type IDs.
    localization_type_id = loc.type
    if localization_type_id in localization_type_mapping:
        localization_type_id = localization_type_mapping[localization_type_id]
    else:
        raise ValueError(f"Source localization_type ID {localization_type_id} missing from "
                          "localization_type_mapping!")
    # Check for parent mapping.
    parent_id = loc.parent
    if parent_id:
        parent_id = int(parent_id)
        if parent_id in parent_mapping:
            parent_id = parent_mapping[parent_id]
        else:
            logger.warning(f"Source parent ID {parent_id} missing from parent_mapping! Not "
                           f"setting parent for source localization {loc.id}...")
            parent_id = None
    # Fill in required fields for post.
    spec = {'type': localization_type_id,
            'version': version_id,
            'media_id': media_id,
            'x': loc.x,
            'y': loc.y,
            'width': loc.width,
            'height': loc.height,
            'u': loc.u,
            'v': loc.v,
            'frame': loc.frame,
            'attributes': loc.attributes}
    if parent_id:
        spec['parent'] = parent_id
    spec = {key:spec[key] for key in spec if spec[key] is not None}
    return spec

def clone_localization_list(src_api, query_params, dest_project, version_mapping, media_mapping,
                            localization_type_mapping, dest_api=None):
    """ Clone localization list.

    This can be used to clone localizations from one project to another or from one
    host to another.

    Example for different host:

    .. code-block:: python

        src_api = tator.get_api(host, token)
        dest_api = tator.get_api(other_host, other_token)
        query_params = {'project': 1, 'media_id': [1]}
        version_mapping = {1: 10} # Source version ID -> Dest version ID
        media_mapping = {1: 10} # Source media ID -> Dest media ID
        localization_type_mapping = {1: 10} # Source localization type ID -> Dest type ID
        dest_project = 1
        created_ids = []
        generator = clone_localization_list(src_api, query_params, dest_project, version_mapping,
                                            media_mapping, localization_type_mapping, dest_api)
        for num_created, num_total, response, id_map in generator:
            print(f"Created {num_created} of {num_total} localizations...")
            created_ids.append(response.id)
        print(f"Finished creating {num_created} localizations!")

    Example for same host:

    .. code-block:: python

        api = tator.get_api(host, token)
        query_params = {'media_id': [1]}
        dest_project = 1
        version_mapping = {1: 10}
        media_mapping = {1: 10}
        localization_type_mapping = {1: 10} # Source localization type ID -> Dest type ID
        created_ids = []
        generator = clone_localization_list(src_api, query_params, dest_project, version_mapping,
                                            media_mapping, localization_type_mapping)
        for num_created, num_total, response, id_map in generator:
            print(f"Created {num_created} of {num_total} localizations...")
            created_ids += response.id
        print(f"Finished creating {num_created} localizations!")

    :param src_api: :class:`tator.TatorApi` object corresponding to source host or only
        host if this is a clone on same host.
    :param query_params: Dictionary containing query parameters for source localization list.
    :param dest_project: Unique integer identifying destination project.
    :param version_mapping: Dictionary mapping source version IDs to destination version IDs. If the
        source localization list contains a version ID for which a destination version is not supplied, 
        an exception is raised.
    :param media_mapping: Dictionary mapping source media IDs to destination media IDs. If the
        source localization list contains a media ID for which a destination media is not supplied, 
        an exception is raised.
    :param localization_type_mapping: Dictionary mapping source localization type IDs to destination 
        localization_type IDs. If the source localization list contains a localization type ID for
        which a destination localization type ID is not supplied, an exception is raised.
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

    # Start by getting list of localizations to be cloned.
    if 'localization_id_query' in query_params:
        locs = src_api.get_localization_list_by_id(**query_params)
    else:
        locs = src_api.get_localization_list(**query_params)

    # Find parent localizations.
    parent_ids = [int(loc.parent) for loc in locs if loc.parent]
    parent_locs = [loc for loc in locs if loc.id in parent_ids]
    child_locs = [loc for loc in locs if loc.id not in parent_ids]

    # Create spec for parent localizations.
    parent_spec = [_convert_for_post(loc, localization_type_mapping, version_mapping,
                                     media_mapping)
                   for loc in parent_locs]

    # Create parent localizations first.
    created_ids = []
    total_localizations = len(locs)
    parent_mapping = {}
    for idx in range(0, len(parent_locs), 500):
        response = dest_api.create_localization_list(dest_project, body=parent_spec[idx:idx+500])
        created_ids += response.id
        id_map = {src.id: dest_id for src, dest_id in zip(parent_locs[idx:idx+500], response.id)}
        parent_mapping = {**parent_mapping, **id_map}
        yield (len(created_ids), total_localizations, response, id_map)

    # Convert spec for child localizations.
    child_spec = [_convert_for_post(loc, localization_type_mapping, version_mapping,
                                    media_mapping, parent_mapping)
                  for loc in child_locs]

    # Create the localizations.
    for idx in range(0, len(child_locs), 500):
        response = dest_api.create_localization_list(dest_project, body=child_spec[idx:idx+500])
        created_ids += response.id
        id_map = {src.id: dest_id for src, dest_id in zip(locs[idx:idx+500], response.id)}
        yield (len(created_ids), total_localizations, response, id_map)

