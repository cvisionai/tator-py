""" Media manipulation routines

Example:

import tator
api = tator.get_api(token=token)
media = api.get_media(media_id,presigned=3600)
util = tator.util.MediaUtil()

# This load takes a tator object
util.load_from_media_object(media, quality=None)

# path now contains a disk path to an mp4 in the temporary staging area
# containing the frames AT LEAST the frames 25,49
# clip_info can be used to interrogate what frames are present
path, clip_info = util.get_clip([(25,49)])

# Example output:
# ('/tmp/concat.mp4', [{'frame_start': 25, 'num_frames': 25},
#                      {'frame_start': 50, 'num_frames': 25}])

"""
import os
import json
import subprocess
import math
import io
import sys

import requests


def _check_is_presigned(path):
  if path.startswith('http') is False:
    raise Exception("Media object doesn't appear to have presigned URLs present.")
  return path

class MediaUtil:
  """ Top-level class to construct to handle per-media manipulations """
  def __init__(self, temp_dir):
    """ :param temp_dir: Path top use as a working directory for temporary files """
    self._temp_dir = temp_dir
    # If available we only attempt to fetch
    # the part of the file we need to

    # Initialize privates
    self._segment_info = None
    self._fps = None
    self._video_file = None
    self._external_fetch = None
    self._height = None
    self._width = None
    self._start_bias_frame = None
    self._moof_data = None

  def load_from_url(self, video_url, segment_url, height, width, fps):
    """ Setup the MediaUtil instance with primitive types

    :param video_url: Publically accessible URL to the raw segmented mp4 file to use
    :param segment_url: Publically accessible URL for the segmentation map file. 
    :param height: The vertical resolution of the video
    :param width: The horizontal resolution of the video
    :param fps: The frames per second of the video
    """
    self._video_file = video_url
    f_p = io.BytesIO()
    download_request = requests.get(segment_url)
    for chunk in download_request.iter_content(chunk_size=1*1024*1024):
      f_p.write(chunk)
    f_p.seek(0)
    self._segment_info = json.loads(f_p.getvalue().decode('utf-8'))
    self._moof_data = [(i, x) for i, x in enumerate(self._segment_info
                                                        ['segments']) if x['name'] == 'moof']
    self._start_bias_frame = 0
    if self._moof_data[0][1]["frame_start"] > 0:
      self._start_bias_frame = self._moof_data[0][1]["frame_start"]
    self._height = height
    self._width = width
    self._fps = fps

  def load_from_media_object(self, media_obj, quality=None):
    """ Initialize the MediaUtil with a tator media object (loaded with presigned URLs)

      - image or video, no live or multi

      :param media_obj: The a :ref models.Media: object with presigned URLs
      :param quality: Vertical resolution to use as source, will find closest match. 
                      Defaults to highest.
    """
    media = media_obj.to_dict()
    if "streaming" in media['media_files']:
      self._fps = media['fps']
      if quality is None:
        # Select highest quality if not specified
        highest_res = -1
        quality_idx = 0
        for idx, media_info in enumerate(media['media_files']["streaming"]):
          if media_info['resolution'][0] > highest_res:
            highest_res = media_info['resolution'][0]
            quality_idx = idx
      else:
        max_delta = sys.maxsize
        for idx, media_info in enumerate(media['media_files']["streaming"]):
          delta = abs(quality-media_info['resolution'][0])
          if delta < max_delta:
            max_delta = delta
            quality_idx = idx
      if 'hls' in media['media_files']["streaming"][quality_idx]:
        self._external_fetch = 'hls'
        self._video_file = media['media_files']["streaming"][quality_idx]["hls"]
      else:
        video_file = _check_is_presigned(media['media_files']["streaming"][quality_idx]["path"])
        height = media['media_files']["streaming"][quality_idx]["resolution"][0]
        width = media['media_files']["streaming"][quality_idx]["resolution"][1]
        segment_file = _check_is_presigned(media['media_files']["streaming"][quality_idx]["segment_info"])
        self.load_from_url(video_file, segment_file, height, width, media['fps'])
    elif "image" in media['media_files']:
      # Select highest quality image that is non AVIF (no ffmpeg support)
      highest_res = -1
      quality_idx = 0
      # only process non AVIF sources
      images = media['media_files']["image"]
      images = [i for i in images if i['mime'] != 'image/avif']
      for idx, media_info in enumerate(images):
        if media_info['resolution'][0] > highest_res:
          highest_res = media_info['resolution'][0]
          quality_idx = idx
      # Image
      self._video_file = images[quality_idx]["path"]
      self._height = media['height']
      self._width = media['width']
    else:
      raise RuntimeError(f"Media {media.id} does not have streaming or image media!")

  def get_clip(self, frame_ranges):
    """ Given a list of frame ranges generate a temporary mp4

      :param frame_ranges: tuple or list of tuples representing (begin,
                                     end) -- range is inclusive!
    """
    if isinstance(frame_ranges, tuple):
      frame_ranges = [frame_ranges]
    if self._external_fetch == 'hls':
      lookup = {}
      segment_info = [] # There are no segment
      for idx,frange in enumerate(frame_ranges):
        temp_out = os.path.join(self._temp_dir, f"{frange[0]}_{frange[1]}.mp4")
        ffmpeg_args = ["ffmpeg",
                       "-f", "hls",
                       "-y",
                       "-i", self._video_file,
                       "-ss", self._frame_to_time_str(frange[0], None),
                       "-frames:v", str(frange[1]-frange[0]),
                       temp_out]
        proc = subprocess.run(ffmpeg_args, check=True, capture_output=True)
        lookup = {"{frange[0]}_{frange[1]}.mp4": (None, temp_out)}
    else:
      impacted_segments = self._get_impacted_segments_from_ranges(frame_ranges)
      assert not impacted_segments is None, "Unable to calculate impacted video segments"
      lookup, segment_info = self._make_temporary_videos(impacted_segments)

    with open(os.path.join(self._temp_dir, "vid_list.txt"), "w") as vid_list:
      for idx, (_, f_p) in enumerate(lookup.values()):
        mux_0 = os.path.join(self._temp_dir, f"{idx}_0.mp4")
        args = ["ffmpeg",
                "-y",
                "-i", f_p,
                "-c", "copy",
                "-muxpreload", "0",
                "-muxdelay", "0",
                mux_0]
        proc = subprocess.run(args, check=True, capture_output=True)
        vid_list.write(f"file '{mux_0}'\n")

    output_file = os.path.join(self._temp_dir, "concat.mp4")
    args = ["ffmpeg",
            "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", os.path.join(self._temp_dir, "vid_list.txt"),
            "-c", "copy",
            output_file]
    proc = subprocess.run(args, check=True, capture_output=True)
    return output_file, segment_info

  def get_tile_image(self, frames, rois=None, tile_size=None,
                     render_format="jpg", force_scale=None):
    """ Generate a tile jpeg of the given frame/rois """
    # Compute tile size if not supplied explicitly
    try:
      if tile_size is not None:
        # check supplied tile size makes sense
        comps = tile_size.split('x')
        if len(comps) != 2:
          raise Exception("Bad Tile Size")
        if int(comps[0])*int(comps[1]) < len(frames):
          raise Exception("Bad Tile Size")
    except Exception as e:
      tile_size = None
      # compute the required tile size
    if tile_size is None:
      width = math.ceil(math.sqrt(len(frames)))
      height = math.ceil(len(frames) / width)
      tile_size = f"{width}x{height}"

    if not self._generate_frame_images(frames, 
                                       rois,
                                       render_format=render_format,
                                       force_scale=force_scale):
      return None

    output_file = None
    if len(frames) > 1:
      # Make a tiled jpeg
      tile_args = ["ffmpeg",
                   "-y",
                   "-i", os.path.join(self._temp_dir, f"%d.{render_format}"),
                   "-vf", f"tile={tile_size}",
                   "-q:v", "3",
                   os.path.join(self._temp_dir, f"tile.{render_format}")]
      proc = subprocess.run(tile_args, check=True, capture_output=True)
      if proc.returncode == 0:
        output_file = os.path.join(self._temp_dir, f"tile.{render_format}")
    else:
      output_file = os.path.join(self._temp_dir, f"0.{render_format}")

    return output_file

  def get_animation(self, frames, fps, roi=None, render_format='mp4', force_scale=None):
    """ Return an animation of frames at a given FPS.

        :param  frames: list of frames
        :param fps: FPS of output animation """
    if not self._generate_frame_images(frames, roi,
                                       render_format="jpg",
                                       force_scale=force_scale):
      return None

    mp4_args = ["ffmpeg",
                "-y",
                "-framerate", str(fps),
                "-i", os.path.join(self._temp_dir, "%d.jpg"),
                os.path.join(self._temp_dir, "temp.mp4")]
    proc = subprocess.run(mp4_args, check=True, capture_output=True)

    if render_format == 'mp4':
      return os.path.join(self._temp_dir, "temp.mp4")

    # Convert temporary mp4 into a gif
    gif_args = ["ffmpeg",
                "-y",
                "-i", os.path.join(self._temp_dir, "temp.mp4"),
                "-filter_complex", "[0:v] split [a][b];[a] palettegen"
                " [p];[b][p] paletteuse",
                os.path.join(self._temp_dir, "animation.gif")]
    proc = subprocess.run(gif_args, check=True, capture_output=True)
    return os.path.join(self._temp_dir, "animation.gif")

  def _get_impacted_segments(self, frames):
    """ (Internal function) Return the segment info for the requested frame

    :param frames: List of frames
    """
    if self._segment_info is None and self._external_fetch != None:
      return None

    segment_list = []
    for frame_str in frames:
      frame_seg = set()
      frame_seg.add(0)
      frame_seg.add(1)
      # We already load the header so ignore those segments
      frame = int(frame_str)
      min_idx = 0
      max_idx = len(self._moof_data)-1
      # Handle frames and files with frame biases
      if frame < self._moof_data[0][1]['frame_start']:
        # Force add the first two segments and all the data in between
        frame_seg.add(self._moof_data[0][0])
        for data_idx in range(self._moof_data[0][0] + 1, self._moof_data[1][0], 1):
          frame_seg.add(data_idx)
        frame_seg.add(self._moof_data[1][0])
        frame_seg = list(frame_seg)
        frame_seg.sort()
        segment_list.append((frame, frame_seg))
        continue

      last_segment = self._moof_data[max_idx][1] #Frame start/stop is in the moof
      if frame >= last_segment['frame_start'] + last_segment['frame_samples']:
        continue

      # Do a binary search for the segment in question
      while min_idx <= max_idx:
        guess_idx = math.floor((max_idx + min_idx) / 2)
        moof = self._moof_data[guess_idx][1]
        if frame < moof['frame_start']:
          max_idx = max_idx - 1
        elif frame >= moof['frame_start'] + moof['frame_samples']:
          min_idx = min_idx + 1
        else:
          frame_seg.add(self._moof_data[guess_idx][0])
          frame_seg.add(self._moof_data[guess_idx][0]+1)
          if frame - moof['frame_start'] > moof['frame_samples'] - 5:
            # Handle boundary conditions
            if guess_idx + 1 in self._moof_data:
              frame_seg.add(self._moof_data[guess_idx+1][0])
              frame_seg.add(self._moof_data[guess_idx+1][0]+1)
          break

      frame_seg = list(frame_seg)
      frame_seg.sort()
      segment_list.append((frame, frame_seg))
    return segment_list

  def _get_impacted_segments_from_ranges(self, frame_ranges):
    """ (Internal function) Return the segment info for the requested frame ranges

    :param frames: List of frame range tuples
    """
    segment_list = []
    for frame_range in frame_ranges:
      begin = frame_range[0]
      end = frame_range[1]
      begin_segments = self._get_impacted_segments([begin])
      end_segments = self._get_impacted_segments([end])
      range_segment_set = set()
      for _, frame_seg in [*begin_segments, *end_segments]:
        for segment in frame_seg:
          range_segment_set.add(segment)
      start_missing = begin_segments[0][1][-1]
      end_missing = end_segments[0][1][2]
      for frame_seg in range(start_missing, end_missing):
        range_segment_set.add(frame_seg)
      range_segment = list(range_segment_set)
      range_segment.sort()
      segment_list.append((frame_range, range_segment))
    return segment_list

  def _make_temporary_videos(self, segment_list):
    """ Return a temporary mp4 for each impacted segment to limit IO to
      cloud storage """
    lookup = {}
    segment_info = []
    for frame, segments in segment_list:
      temp_video = os.path.join(self._temp_dir, f"{frame}.mp4")
      sc_graph = [(0, 0)]
      segment_frame_start = sys.maxsize
      # create a scatter/gather
      for segment_idx in segments:
        segment = self._segment_info['segments'][segment_idx]
        last_io = sc_graph[len(sc_graph)-1]
        if segment.get('frame_start', sys.maxsize) < segment_frame_start:
          segment_frame_start = segment['frame_start']

        if 'frame_samples' in segment:
          segment_info.append({
              'frame_start': segment['frame_start'],
              'num_frames': segment['frame_samples']})

        if last_io[0] + last_io[1] == segment['offset']:
          # merge contigous blocks
          sc_graph[len(sc_graph)-1] = (last_io[0], last_io[1] + segment['size'])
        else:
          # A new block
          sc_graph.append((segment['offset'], segment['size']))

      if segment_frame_start == sys.maxsize:
        segment_frame_start = frame
      lookup[frame] = (segment_frame_start, temp_video)

      with open(temp_video, "wb") as out_fp:
        for scatter in sc_graph:
          start = scatter[0]
          stop = scatter[0] + scatter[1] - 1 # Byte range is inclusive
          download_request = requests.get(self._video_file, 
                                          headers={'range': f'bytes={start}-{stop}'})
          for chunk in download_request.iter_content(chunk_size=1*1024*1024):
            out_fp.write(chunk)

    return lookup, segment_info

  def _frame_to_time_str(self, frame, relative_to=None):
    """ Convert a frame number to a time reference """
    if relative_to:
      frame -= relative_to

    if frame < 0:
      frame += self._start_bias_frame

    total_seconds = frame / self._fps
    hours = math.floor(total_seconds / 3600)
    minutes = math.floor((total_seconds % 3600) / 60)
    seconds = total_seconds % 60
    return f"{hours}:{minutes}:{seconds}"

  def _generate_frame_images(self, frames, rois=None, render_format="jpg", force_scale=None):
    """ Generate a jpg for each requested frame and store in the working directory """
    BATCH_SIZE = 30
    frame_idx = 0
    procs = []
    for idx in range(0, len(frames), BATCH_SIZE):
      batch = [int(frame) for frame in frames[idx:idx+BATCH_SIZE]]
      crop_filter = None
      if rois:
        crop_filter = []
        for c in rois: #pylint: disable=invalid-name
          w = max(0,min(round(c[0]*self._width),self._width)) #pylint: disable=invalid-name
          h = max(0,min(round(c[1]*self._height),self._height)) #pylint: disable=invalid-name
          x = max(0,min(round(c[2]*self._width),self._width)) #pylint: disable=invalid-name
          y = max(0,min(round(c[3]*self._height),self._height)) #pylint: disable=invalid-name
          crop_filter.append(f"crop={w}:{h}:{x}:{y}")
      scale_filter = None
      if force_scale:
        scale_w = force_scale[0]
        scale_h = force_scale[1]
        scale_filter = f"scale={scale_w}:{scale_h}"

      args = ["ffmpeg", "-y"]
      inputs = []
      outputs = []

      # attempt to make a temporary file in a fast manner to speed up AWS access
      impacted_segments = self._get_impacted_segments(batch)
      lookup = {}
      if impacted_segments:
        lookup, _ = self._make_temporary_videos(impacted_segments)

      for batch_idx, frame in enumerate(batch):
        outputs.extend(["-map", f"{batch_idx}:v","-frames:v", "1", "-q:v", "3"])
        video_filters = []
        if crop_filter:
          video_filters.append(crop_filter[frame_idx])
        if scale_filter:
          video_filters.append(scale_filter)
        if video_filters:
          outputs.extend(["-vf", ",".join(video_filters)])

        outputs.append(os.path.join(self._temp_dir,f"{frame_idx}.{render_format}"))
        if frame in lookup:
          inputs.extend(["-ss", self._frame_to_time_str(frame, lookup[frame][0]),
                         "-i", lookup[frame][1]])
        elif self._external_fetch == 'hls':
          inputs.extend(["-ss", self._frame_to_time_str(frame, None),
                         "-f", "hls",
                         "-i", self._video_file])
        else:
          raise ValueError("Failed to find frame {frame} in segmented mp4!")
        frame_idx += 1

      # Now add all the cmds in
      args.extend(inputs)
      args.extend(outputs)
      procs.append(subprocess.run(args, check=True, capture_output=True))
    return any([proc.returncode == 0 for proc in procs])
