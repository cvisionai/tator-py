import os
import math
import tempfile
from uuid import uuid1
from collections import defaultdict

from urllib.parse import urlparse, urljoin

from .md5sum import md5sum
from ._download_file import _download_file

class HostTransfer:
    def __init__(self, src_api, src_project, dest_api, dest_project):
        """ Sets up authentication for transferring file.

        :param src_api: :class:`tator.TatorApi` object corresponding to source host.
        :param src_project: Unique integer identifying the source project.
        :param dest_api: :class:`tator.TatorApi` object corresponding to destination host.
        :param dest_project: Unique integer identifying the destination project.
        """
        # Set up source.
        self.src_api = src_api
        self.src_project = src_project

        # Set up destination.
        self.dest_api = dest_api
        self.dest_project = dest_project

    def __call__(self, src_url, media_id=None, return_url=False):
        """ Downloads a file from one host and uploads it to another.
        
        :param src_url: Relative URL of source file to download.
        :param media_id: Destination media ID.
        :param return_url: Return download URL if true.
        :returns: URL or path of destination file.
        """
        parsed = urlparse(src_url)
        filename = os.path.basename(parsed.path)
        with tempfile.NamedTemporaryFile() as temp:
            for _ in _download_file(self.src_api, self.src_project, src_url, temp.name):
                pass
            for _, upload_info in _upload_file(self.dest_api, self.dest_project, temp.name,
                                               media_id=media_id, filename=filename):
                pass
        out = upload_info.key
        if return_url:
            out = api.get_download_info(project, {'keys': [upload_info.key]})[0].url
        return out

def clone_media_list(src_api, query_params, dest_project, media_mapping={}, dest_type=-1,
                     dest_section='', dest_api=None):
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
        media_mapping = {} # Only required if query contains multi media types
        dest_project = 1
        dest_type = -1
        dest_section = 'My cloned media'
        created_ids = []
        generator = clone_media_list(src_api, query_params, dest_project, media_mapping,
                                     dest_type, dest_section, dest_api)
        for num_created, num_total, response, id_map in generator:
            print(f"Created {num_created} of {num_total} files...")
            created_ids.append(response.id)
        print(f"Finished creating {num_created} files!")

    Example for same host:

    .. code-block:: python

        api = tator.get_api(host, token)
        query_params = {'media_id': [1]}
        dest_project = 1
        created_ids = []
        generator = clone_media_list(src_api, query_params, dest_project)
        for num_created, num_total, response, id_map in generator:
            print(f"Created {num_created} of {num_total} files...")
            created_ids += response.id # This response is from the CloneMedia endpoint.
        print(f"Finished creating {num_created} files!")

    :param src_api: :class:`tator.TatorApi` object corresponding to source host or only
        host if this is a clone on same host.
    :param query_params: Dictionary containing query parameters for source media list.
    :param dest_project: Unique integer identifying destination project.
    :param media_mapping: Mapping between source and destination media IDs. Only used
        if the media list contains multi media types and the clone is being done for
        different hosts.
    :param dest_type: Unique integer identifying destination media type. If set to
        -1, the media type is set to the first media type in the project.
    :param dest_section: Name of destination section.
    :param dest_api: :class:`tator.TatorApi` object corresponding to destination host.
    :returns: Generator containing number of files created, number of files total,
        most recent response from media creation operation, and mapping between original IDs
        and created IDs.
    """
    # Make sure query has a project.
    if 'project' not in query_params:
        raise Exception("Query parameters must include a project!")

    # Guess the media type if it was not given.
    if dest_type == -1:
        if dest_api is None:
            media_types = src_api.get_media_type_list(dest_project)
        else:
            media_types = dest_api.get_media_type_list(dest_project)
        if len(media_types) == 0:
            raise Exception('Specified project does not have any media types!')
        dest_type = media_types[0].id

    # Get medias.
    medias = src_api.get_media_list(**query_params)
    total_files = len(medias)

    # Clone the media.
    created_ids = []
    if (dest_api is None) or (dest_api is src_api):
        for idx in range(0, len(medias), 100): # Go in batches of 100
            # Clone media locally.
            media_ids = [media.id for media in medias[idx:idx+100]]
            response = src_api.clone_media_list(query_params['project'],
                                                media_id=media_ids,
                                                clone_media_spec={
                                                    'dest_project': dest_project,
                                                    'dest_section': dest_section,
                                                    'dest_type': dest_type,
                                                })
            created_ids += response.id
            id_map = {src_id: dest_id for src_id, dest_id in zip(media_ids, response.id)}
            yield (len(created_ids), total_files, response, id_map)
    else:
        # Clone media to another host.
        transfer = HostTransfer(src_api, dest_api, dest_project)
        for media in medias:
            # Set up media spec.
            attributes = media.attributes
            if 'tator_user_sections' in attributes:
                attributes.pop('tator_user_sections', None)
            media_spec = {
                'type': dest_type,
                'name': media.name,
                'md5': media.md5,
                'fps': media.fps,
                'num_frames': media.num_frames,
                'codec': media.codec,
                'width': media.width,
                'height': media.height,
                'attributes': attributes,
                'section': dest_section if dest_section else media.section,
            }
            if media.gid:
                media_spec['gid'] = media.gid
            if media.uid:
                media_spec['uid'] = media.uid
            # Transfer thumbnails and image.
            media_spec['thumbnail_url'] = transfer(f'/media/{media.thumbnail}', return_url=True)

            if media.thumbnail_gif:
                media_spec['thumbnail_gif_url'] = transfer(f'/media/{media.thumbnail_gif}',
                                                           return_url=True)

            if media.file:
                media_spec['url'] = transfer(f'/media/{media.file}', return_url=True)

            # Create the media object.
            response = dest_api.create_media(dest_project, media_spec=media_spec)
            id_map = {media.id: response.id}

            # Transfer videos.
            if media.media_files:
                if media.media_files.archival:
                    for archival in media.media_files.archival:
                        media_def = {k: v for k, v in archival.to_dict().items()
                                     if v is not None}
                        media_def.pop('path', None)
                        media_def['path'] = transfer(archival.path, media_id=response.id)
                        dest_api.create_video_file(response.id, role='archival',
                                                   video_definition=media_def)
                if media.media_files.streaming:
                    for streaming in media.media_files.streaming:
                        media_def = {k: v for k, v in streaming.to_dict().items()
                                     if v is not None}
                        media_def.pop('path', None)
                        media_def['path'] = transfer(streaming.path, media_id=response.id)
                        media_def['segment_info'] = transfer(streaming.segment_info, media_id=response.id)
                        dest_api.create_video_file(response.id, role='streaming',
                                                   video_definition=media_def)
                if media.media_files.audio:
                    for audio in media.media_files.audio:
                        media_def = {k: v for k, v in audio.to_dict().items()
                                     if v is not None}
                        media_def.pop('path', None)
                        media_def['url'] = transfer(audio.path, media_id=response.id)
                        dest_api.create_audio_file(response.id, role='audio',
                                                   audio_definition=media_def)
                if media.media_files.ids:
                    dest_ids = []
                    for id_ in media.media_files.ids:
                        if id_ in media_mapping:
                            dest_ids.append(media_mapping[id_])
                        else:
                            raise Exception(f"Source media ID {id_} does not exist in media "
                                             "mapping! Individual videos should be migrated "
                                             "before multi videos.")
                    update = {'multi': {'ids': dest_ids}}
                    if media.media_files.layout:
                        update['media_files']['layout'] = media.media_files.layout
                    if media.media_files.quality:
                        update['media_files']['quality'] = media.media_files.quality
                    dest_api.update_media(response.id, media_update=update)
            created_ids.append(response.id)
            yield (len(created_ids), total_files, response, id_map)
