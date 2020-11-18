import os
import tempfile

from urllib.parse import urljoin

from ._download_file import _download_file

def clone_media_list(src_api, query_params, dest_project, dest_section='', dest_media_type=-1,
                     dest_api=None):
    """ Clone media list.

    This can be used to clone media from one project to another or from one
    host to another. In the case of the same host, the media files are not
    copied. If the destination host is different (`dest_api` is a :class:`tator.TatorApi`
    object), the transcoded files for each media object is downloaded and then
    uploaded to the other host, and a new :class:`tator.Media` object is created.

    Example for different host:

    .. code-block:: python

        src_api = tator.get_api(host, token)
        dest_api = tator.get_api(other_host, other_token)
        query_params = {'project': 1, 'media_id': [1]}
        dest_project = 1
        dest_media_type = -1
        dest_section = 'My cloned media'
        created_ids = []
        for num_created, num_total, response in clone_media_list(src_api, query_params,
                                                                 dest_project, dest_media_type,
                                                                 dest_section, dest_api):
            print(f"Created {num_created} of {num_total} files...")
            created_ids.append(response.id)
        print(f"Finished creating {num_created} files!")

    Example for same host:

    .. code-block:: python

        api = tator.get_api(host, token)
        query_params = {'media_id': [1]}
        dest_project = 1
        created_ids = []
        for num_created, num_total, response in clone_media_list(src_api, query_params,
                                                                 dest_project):
            print(f"Created {num_created} of {num_total} files...")
            created_ids += response.id # This response is from the CloneMedia endpoint.
        print(f"Finished creating {num_created} files!")

    :param api: :class:`tator.TatorApi` object.
    :param query_params: Dictionary containing query parameters for source media list.
    :param dest_project: Unique integer identifying destination project.
    :param dest_media_type: Unique integer identifying destination media type. If set to
        -1, the media type is set to the first media type in the project found with
        the proper dtype for the files.
    :returns: Generator containing number of files created, number of files total, and
        most recent response from media creation operation.
    """
    # Start by getting total number of files to be cloned.
    total_files = src_api.media_count(**query_params)

    # Check for no pagination parameters.
    has_pagination = 'after' in query_params or 'start' in query_params or 'stop' in query_params
    if has_pagination:
        raise Exception("This utility does pagination internally and does not accept pagination "
                        "parameters as inputs!")

    # Make sure query has a project.
    if 'project' not in query_params:
        raise Exception("Query parameters must include a project!")

    # Get auth info for downloading media.
    host = config.host
    token = config.api_key['Authorization']
    prefix = config.api_key_prefix['Authorization']
    headers = {
        'Authorization': f'{prefix} {token}',
        'Content-Type': f'application/json',
        'Accept-Encoding': 'gzip',
    }

    # Guess the media type if it was not given.
    if dest_media_type == -1:
        mime,_ = mimetypes.guess_type(fname)
        if dest_api is None:
            media_types = dest_api.get_media_type_list(dest_project)
            for media_type in media_types:
                response = api.get_media_type(type_id)
                project_id = response.project
                

    # Clone the media.
    created_ids = []
    after = None
    while len(created_ids) < total_files:
        if after is None:
            query_params['start'] = 0
        else:
            if 'start' in query_params:
                query_params.pop('start', None)
            query_params['after'] = after
        if dest_api is None:
            # Clone media locally.
            response = src_api.clone_media_list(**query_params, clone_spec={
                'dest_project': dest_project,
                'dest_section': dest_section,
                'dest_media_type': dest_media_type,
            })
            created_ids += response.id
            yield (len(created_ids), total_files, response)
        else:
            # Clone media to another host.
            medias = src_api.get_media_list(**query_params)
            
            for media in medias:
                with tempfile.TemporaryDirectory() as temp_dir:
                    # Download media to a temporary directory. 
                    media_paths = defaultdict(list)
                    def _download_to_temp(path, key):
                        url = urljoin(host, path)
                        out_path = os.path.join(temp_dir, os.path.basename(path))
                        _download_file(url, headers, out_path)
                        media_paths[key].append(out_path)
                    if media.media_files:
                        if media.media_files.archival:
                            for archival in media.media_files.archival:
                                _download_to_temp(archival.path, 'archival')
                        if media.media_files.streaming:
                            for streaming in media.media_files.streaming:
                                _download_to_temp(streaming.path, 'streaming')
                        if media.media_files.audio:
                            for audio in media.media_files.audio:
                                _download_to_temp(audio.path, 'audio')
                    if media.file:
                        _download_to_temp(media.file, 'file')
                    if media.original:
                        _download_to_temp(media.original, 'archival')

                    # Upload media.
                    for key in media_paths:
                        tus_url = urljoin(host, 'files/')
    tusURL = urljoin(host, "files/")
                        tus = TusClient(tus_url, headers={'Authorization': f'{prefix} {token}',
                                                          'Upload-Uid': f'{upload_uid}'})
                        uploader = tus.uploader(path, chunk_size=chunk_size,
                                                retries=10, retry_delay=15)
                        num_chunks = math.ceil(uploader.get_file_size()/chunk_size)
                        for chunk_count in range(num_chunks):
                            uploader.upload_chunk()
                        spec = {
                            'type': type_id,
                            'uid': upload_uid,
                            'gid': upload_gid,
                            'url': uploader.url,
                            'name': fname,
                            'section': section,
                            'md5': md5,
                            'attributes': attributes,
                            'media_id': media_id,
                        }
                        # Initiate transcode or save image.
                        if mime.find('video') >= 0:
                            response = api.transcode(project_id, transcode_spec=spec)
                        else:
                            response = api.create_media(project_id, media_spec=spec)
                        yield (100, response)
