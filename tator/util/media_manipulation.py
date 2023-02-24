""" Module for handling the boiler plate around adding media resources to existing Media objects """

from .md5sum import md5sum
from ..transcode.transcode import make_video_definition, convert_streaming, convert_archival
import tempfile
import os


def supplement_video_to_media(api,
                              media_id,
                              role,
                              configuration,
                              filepath: str,
                              force=False):
  """ This routine will transcode `filepath` based on `configuration` to `media_object`

  See :py:meth:`tator.api.delete_video_file` for information on deleting resolutions from a media object  

  :param api: An initialized tator.api project
  :param media_id: Id of the media to supplement to
  :param role: One of 'streaming' or 'archival'
  :param configuration: For 'streaming' roles, must be a tator.models.ResolutionConfig, for 'archival' roles must be a tator.models.EncodeConfig
  :param filepath: The local file path to the file to encode
  :param force: If true, will ignore any differences in the source file compared to what was previously encoded. This is very dangerous as it could result in streams of different lengths or even different files.
  
  """
  media_object = api.get_media(media_id)
  media_type_object = api.get_media_type(media_object.type)
  if media_type_object.dtype != 'video':
    raise Exception(f'{media_id} is not a video, its a {media_type_object.dtype}')
  
  if not role in ['streaming', 'archival']:
    raise Exception(f'"{role}" must be one of "streaming" or "archival"')

  md5_of_file = md5sum(filepath)

  # Do not proceed if force is false + the input file doesn't appear to match the original inputted file
  if md5_of_file != media_object.md5 and force is False:
    raise Exception(f'{media_id} has an md5 of {media_object.md5}, local file is {md5_of_file}. Need to supply force=True to bypass this safety check.')
  else:
    print("WARNING: Bypassing source uniqueness check")

  # Extract host + token from supplied api object.
  host = api.api_client.configuration.host
  token = api.api_client.configuration.api_key['Authorization']

  # Construct the raw definition to grab input file properties
  raw_definition = make_video_definition(filepath)
  height, width = raw_definition['resolution']

  if role == 'streaming':
    # In a temporary directory do all the work
    with tempfile.TemporaryDirectory() as td:
      # To be compatible with the convert_streaming routine need to stringify the configuration
      resolution = configuration.resolution
      crf = configuration.crf if configuration.crf else 23
      codec = configuration.vcodec if configuration.vcodec else 'libx264'
      preset = configuration.preset if configuration.preset else ''
      configs = [f"{resolution}:{crf}:{codec}:{preset}"]
      convert_streaming(host, token, media_id, filepath, td, width, height, configs)

      

  if role == 'archival':
    with tempfile.TemporaryDirectory() as td:
      archival_path = os.path.join(td, "archival.mp4")
      convert_archival(host, token, media_id, filepath, archival_path, width, height, None, [configuration])
