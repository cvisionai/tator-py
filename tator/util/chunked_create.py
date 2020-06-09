def chunked_create(func, project, **kwargs):
    """ Breaks a create_*_list operation into chunks.

    Example:
    .. highlight:: python
    .. code-block:: python
        ids = chunked_create(api.create_localization_list,
                             1, localization_spec=my_long_list)

    :param func: Function to call on each chunk.
    :param project: Unique integer identifying a project.
    :returns: List of created IDs.
    """
    ids = []
    for key in kwargs:
        spec = kwargs[key]
    for idx in range(0, len(spec), 500):
        response = func(project, **{key: spec[idx:idx+500]})
        ids += response.id
    return ids
