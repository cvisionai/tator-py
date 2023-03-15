import os
import math
import tempfile
import logging
from uuid import uuid1
from collections import defaultdict
from urllib.parse import urlparse, urljoin

import progressbar

from .md5sum import md5sum
from ._download_file import _download_file
from ._upload_file import _upload_file

logger = logging.getLogger(__name__)

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
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = os.path.join(temp_dir, filename)
            print(f"Downloading {filename}")
            bar = progressbar.ProgressBar(max_value=100)
            for progress in _download_file(self.src_api, self.src_project, src_url, temp):
                bar.update(progress)
            bar.update(100)
            print(f"Uploading {filename}")
            bar = progressbar.ProgressBar(max_value=100)
            for progress, upload_info in _upload_file(self.dest_api, self.dest_project, temp,
                                               media_id=media_id, filename=filename):
                bar.update(progress)
            bar.update(100)
            out = upload_info.key
        if return_url:
            out = self.dest_api.get_download_info(self.dest_project,
                                                  {'keys': [upload_info.key]})[0].url
        return out

def clone_media_list(src_api, query_params, dest_project, media_mapping={}, dest_type=-1,
                     dest_section='', dest_api=None, ignore_transfer=False):
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
            created_ids.append(response.id[0])
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
            created_ids += response.id[0] # This response is from the CloneMedia endpoint.
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
    :param ignore_transfer: True if media files should not be transferred. Media object will still be created.
        Paths in media_files will be invalid.
    :returns: Generator containing number of files created, number of files total,
        most recent response from media creation operation, and mapping between original IDs
        and created IDs.
    """
    # Make sure query has a project.
    if 'project' not in query_params:
        raise Exception("Query parameters must include a project!")
    src_project = query_params['project']

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
    try:
        medias = src_api.get_media_list(**query_params, presigned=86400)
    except:
        # Support legacy api
        medias = src_api.get_media_list(**query_params)
    total_files = len(medias)

    # Clone the media.
    created_ids = []
    if (dest_api is None) or (dest_api is src_api):
        for idx in range(0, len(medias), 100): # Go in batches of 100
            # Clone media locally.
            media_ids = [media.id for media in medias[idx:idx+100]]
            response = src_api.clone_media_list(src_project,
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
        if not ignore_transfer:
            transfer = HostTransfer(src_api, src_project, dest_api, dest_project)
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

            # Create the media object.
            response = dest_api.create_media_list(dest_project, body=[media_spec])
            id_map = {media.id: response.id[0]}

            # Transfer videos.
            if media.media_files:
                media_files = media.media_files.to_dict()
                for key in ['streaming', 'archival', 'audio', 'image', 'thumbnail', 'thumbnail_gif']:
                    if ignore_transfer:
                        continue
                    if media_files.get(key):
                        for item in media_files[key]:
                            media_def = {k: v for k, v in item.items()
                                         if v is not None}
                            src_path = media_def.pop('path', None)
                            media_def['path'] = transfer(src_path, media_id=response.id[0])
                            if key == 'streaming':
                                src_segments = media_def.pop('segment_info', None)
                                media_def['segment_info'] = transfer(src_segments, media_id=response.id[0])
                            if key in ['streaming', 'archival']:
                                dest_api.create_video_file(response.id[0], role=key,
                                                           video_definition=media_def)
                            elif key in ['image', 'thumbnail', 'thumbnail_gif']:
                                dest_api.create_image_file(response.id[0], role=key,
                                                           image_definition=media_def)
                            elif key in ['audio']:
                                dest_api.create_audio_file(response.id[0], role=key,
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
                        update['multi']['layout'] = media.media_files.layout
                    if media.media_files.quality:
                        update['multi']['quality'] = media.media_files.quality
                    dest_api.update_media(response.id[0], media_update=update)
            created_ids.append(response.id[0])
            yield (len(created_ids), total_files, response, id_map)
