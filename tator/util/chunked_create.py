def chunked_create(func, project, **kwargs):
    """ Breaks a create_*_list operation into chunks.

    Example:

    .. code-block:: python

        created_ids = []
        for response in tator.util.chunked_create(api.create_localization_list, 1,
                                                  localization_spec=my_long_list):
            created_ids += response.id

    :param func: Function to call on each chunk.
    :param project: Unique integer identifying a project.
    :returns: Generator that yields a response.
    """
    for key in kwargs:
        spec = kwargs[key]
    for idx in range(0, len(spec), 500):
        response = func(project, **{key: spec[idx:idx+500]})
        yield response
