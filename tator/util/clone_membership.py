def clone_membership(src_api, src_membership_id, dest_project, user_mapping=None, dest_api=None):
    """ Clone membership.

    This can be used to clone memberships from one project to another or from one
    host to another.

    Example for different host:

    .. code-block:: python

        src_api = tator.get_api(host, token)
        dest_api = tator.get_api(other_host, other_token)
        src_membership_id = 1
        dest_project = 1
        user_mapping = {1: 10} # Mapping between user ID on source host and destination host.
        response = tator.util.clone_membership(src_api, src_membership_id, dest_project,
                                               user_mapping, dest_api)
        print(response.message)

    Example for same host:

    .. code-block:: python

        api = tator.get_api(host, token)
        src_membership_id = 1
        dest_project = 1
        response = tator.util.clone_membership(src_api, src_membership_id, dest_project)
        print(response.message)

    :param src_api: :class:`tator.TatorApi` object corresponding to source host or only
        host if this is a clone on same host.
    :param src_membership_id: Unique integer identifying membership to clone.
    :param dest_project: Unique integer identifying destination project.
    :param user_mapping: If cloning to different host, the mapping between source and destination
        user IDs.
    :param dest_api: :class:`tator.TatorApi` object corresponding to destination host.
    :returns: Response from membership creation request.
    """
    membership_obj = src_api.get_membership(src_membership_id)
    spec = {'permission': membership_obj.permission}
    if dest_api is None:
        spec['user'] = membership_obj.user
    else:
        if membership_obj.user in user_mapping:
            spec['user'] = user_mapping[membership_obj.user]
        else:
            raise ValueError(f"User ID {membership_obj.user} not specified in user mapping!")
    if dest_api is None:
        dest_api = src_api
    return dest_api.create_membership(dest_project, membership_spec=spec)
