def chunked_file_list(paths, chunk_size=100):
    """ Breaks file list into chunks for upload via media archive.

    Example:

    .. code-block:: python

        api = tator.get_api(host, token)
        batch_num = 0
        for batch in tator.util.chunked_file_list(paths):
            print(f"Uploading file {batch_num*100} / {len(paths)}")
            for progress, response in tator.util.upload_media_archive(api, project_id, batch):
                print(f"Upload progress: {progress}%")
            print(response.message)
            batch_num += 1

    :param paths: List of file paths.
    :param chunk_size: [Optional] Size of batches for file upload. Archive uploads are created in
        memory, so this should be set to a reasonable value based on file size. Default
        is 100.
    :returns: Generator that yields batches of file paths.
    """
    for idx in range(0, len(paths), chunk_size):
        yield paths[idx:idx+chunk_size]
