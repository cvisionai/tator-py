import os

from ._upload_file import _upload_file

def upload_attachment(api, media, path, name=None, chunk_size=100*1024*1024):
    """ Upload a file as an attachment to a media object.

    Example:

    .. code-block:: python

        api = tator.get_api(host, token)
        for progress, response in tator.util.upload_attachment(api, media_id, path):
            print(f"Upload progress: {progress}%")
        print(response.message)

    :param api: :class:`tator.TatorApi` object.
    :param media: Unique integer identifying a media.
    :param path: Path to the file.
    :param name: [Optional] Name of file in database. Defaults to basename of path.
    :param chunk_size: [Optional] Chunk size in bytes. Default is 100MB.
    :returns: Generator that yields tuple containing progress (0-100) and a
        response. The response is `None` until the last yield, when the response
        is the response object from :meth:`tator.util.TatorApi.create_auxiliary_file`.
    """
    size = os.stat(path).st_size
    media_obj = api.get_media(media)

    if name is None:
        name = os.path.basename(path)

    for progress, upload_info in _upload_file(api, media_obj.project, path, media_id=media,
                                              filename=name):
        yield (progress, None)

    file_def = {'size': os.stat(path).st_size,
                'path': upload_info.key,
                'name': name}

    response = api.create_auxiliary_file(media, role='attachment', auxiliary_file_definition=file_def)
    yield (100, response)
