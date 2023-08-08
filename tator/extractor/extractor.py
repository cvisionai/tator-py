import os
import subprocess
import tempfile
import traceback
import shutil
import sys
import uuid


from collections import defaultdict
import numpy as np

try:
    import cv2
except:
    print("Unable to import cv2, required for extractor")
    traceback.print_exc()
    sys.exit(-1)


import tator
from tator.transcode.make_thumbnails import make_thumbnails
from tator.transcode.transcode import make_video_definition
from tator.transcode.transcode import convert_streaming
from tator.transcode.transcode import default_archival_upload

from tator.openapi.tator_openapi.models import CreateResponse



def import_media(api,
                 project,
                 media_type_id,
                 path,
                 fname,
                 section,
                 upload_gid,
                 work_dir):

    md5sum = tator.util.md5sum(path)
    media_spec = [
        {
            "type": media_type_id,
            "section": section,
            "name": fname,
            "md5": md5sum,
            "gid": upload_gid,
            "uid": str(uuid.uuid1()),
        },
    ]
    response = api.create_media_list(project, media_spec)
    assert isinstance(response, CreateResponse)
    media_id = response.id[0]

    # Peel apart api to get host/token combo (TODO: not great)
    host = api.api_client.configuration.host
    token = api.api_client.configuration.api_key['Authorization']
    with tempfile.TemporaryDirectory(dir=work_dir) as td:
        try:
            thumb_path = os.path.join(td, f"{uuid.uuid4()}.jpg")
            thumb_gif_path = os.path.join(td, f"{uuid.uuid4()}.gif")
            make_thumbnails(host, token, media_id,
                            path, thumb_path, thumb_gif_path)

            video_definition = make_video_definition(path)
            video_height = video_definition["resolution"][0]
            video_width = video_definition["resolution"][1]

            # Now transcode to streaming at a fixed resolution
            convert_streaming(host,
                              token,
                              media_id,
                              path,
                              td,
                              video_width,
                              video_height,
                              [f"{video_height}:23:h264"])

            default_archival_upload(api,
                                    host,
                                    media_id,
                                    path,
                                    True)
        except Exception as e:
            print(f"Error {e}")
            api.delete_media(media_id)
            traceback.print_exc()
            return None

    return media_id

def process_file(api,
                 project,
                 media_file,
                 media_el,
                 mode,
                 metadata,
                 output_dir,
                 tator_section_output=None,
                 output_type_id=None,
                 upload_gid=str(uuid.uuid1()),
                 work_dir=None):
    """
    Run the extractor on on a given file. Can optionally upload the extraction
    data to Tator if `tator_section_output` and `output_type_id` are given. Else
    the extractions are placed in `output_dir` for further use.

    :param api: Iniitalized :class:`tator.TatorApi` object
    :param project: Project ID
    :param media_file: Path to local copy of media file
    :param media_el: :class:`tator.models.Media` Media element
    :param mode: str choice of
                 - state : Whole frame capture based on state's frame
                 - localization_keyframe : Whole frame on localization frame
                 - localization_thumbnail : Thumbnail of localization
                 - track_thumbnail : Thumbnail of track (mp4)
    :param metadata: list of metadata to process for this media on a given mode
    :param output_dir: path to output extraction files
    :param tator_section_output: Name of section to output to in project
                                 (optional)
    :param output_type_id: Type ID of media to use for extraction data
                           (optional)
    :param upload_gid: str representation of a unique task id (optional)
    """
    grouped_by_frame = defaultdict(lambda: [])
    if mode == "track_thumbnail":

        # First get the localization_type id
        random_local = api.get_localization(metadata[0].localizations[0])
        localization_type = random_local.type
        localizations = api.get_localization_list(project,
                                                  media_id=[media_el.id],
                                                  type=localization_type)
        localizations = [x.to_dict() for x in localizations]
        for l in localizations:
            found = False
            for entry in metadata:
                found = True
                l['track'] = entry.id
            if found:
                grouped_by_frame[l['frame']].append(l)
    else:
        for entry in metadata:
            frame = entry.frame
            grouped_by_frame[frame].append(entry.to_dict())

    vid = cv2.VideoCapture(media_file)
    if cv2.__version__ >= "3.2.0":
        vid_len = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    else:
        vid_len = int(vid.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))

    frame_num = 0
    if len(grouped_by_frame.keys()) > 0:
        max_frame = np.max(list(grouped_by_frame.keys()))
    else:
        print("Nothing to extract")
        max_frame = 0

    fail_count = 0
    while frame_num <= max_frame:
        ok, image = vid.read()
        if not ok:
            fail_count += 1
            if fail_count >= 10:
                raise RuntimeError("Failed to grab video frame")
        else:
            fail_count = 0
            if frame_num in grouped_by_frame:
                print(f"Extracting metadata from {media_file}:{frame_num} of {max_frame}")
                if mode == 'state' or mode == 'localization_keyframe':
                    output_name = media_el.name
                    output_name += f"_{frame_num}.png"
                    output_fp = os.path.join(output_dir, output_name)
                    cv2.imwrite(output_fp, image)
                else:
                    _extract_thumbnails(image,
                                        grouped_by_frame[frame_num],
                                        output_dir)
            else:
                pass #print(f"Skipping {frame_num} of {max_frame}")
        frame_num += 1

    # Handle uploads
    if mode == 'track_thumbnail':
        print("Generating track thumbnails")
        for track in metadata:
            print(f"Making track {track.id}")
            track_dir = os.path.join(output_dir,
                                     str(track.id))
            os.makedirs(track_dir)
            local_ids = track.localizations
            track_locals = [local for local in localizations if local['id'] in local_ids]
            track_locals.sort(key=lambda x: x['frame'])
            for idx, track_local in enumerate(track_locals):
                shutil.copyfile(os.path.join(output_dir, f"{track_local['id']}.png"),
                                os.path.join(track_dir, f"{idx:05d}.png"))
            ffmpeg_cmd = ["ffmpeg",
                          "-r", "1",
                          "-v", "error",
                          "-f", "image2",
                          "-i", os.path.join(track_dir, "%05d.png"),
                          "-crf", "23",
                          os.path.join(track_dir, "clip.mp4")
                          ]
            subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            print(f"Uploading Clip for {track.id}")
            if tator_section_output and output_type_id:
                # Upload the media and update the track object
                media_id = import_media(api,
                                        project,
                                        output_type_id,
                                        os.path.join(track_dir, "clip.mp4"),
                                        fname=f"{track.id}.mp4",
                                        section=tator_section_output,
                                        upload_gid=upload_gid,
                                        work_dir=work_dir)
                if media_id:
                    api.update_state(track.id, {"attributes": {"_extracted": media_id}})
                    print(f"Uploaded Track({track.id}) Extraction to {media_id}")
    elif mode == 'localization_thumbnail' and tator_section_output and output_type_id:
        for root, _, files in os.walk(output_dir):
            for fp in files:
                full_path = os.path.join(root, fp)
                for _, resp in tator.util.upload_media(api, output_type_id, full_path,
                                                       section=tator_section_output,
                                                       upload_gid=upload_gid):
                    pass
                try:
                    local_id = int(os.path.splitext(fp)[0])
                    media_id = resp.id
                    api.update_localization(local_id, {"attributes": {"_extracted": media_id}})
                except:
                    print(f"Unable to update '_extracted' attribute")
    else:
        if tator_section_output and output_type_id:
            ep = api.create_state_list if mode == 'state' else api.create_localization_list
            for root, _, files in os.walk(output_dir):
                for fp in files:
                    full_path = os.path.join(root, fp)
                    for _, resp in tator.util.upload_media(
                            api,
                            output_type_id,
                            full_path,
                            section=tator_section_output,
                            upload_gid=upload_gid):
                        pass
                    # Now duplicate state or localization(s) that caused the extraction
                    # into new media
                    media_id = resp.id
                    frame_str = os.path.splitext(fp.split('_')[-1])[0]
                    frame = int(frame_str)
                    new_meta=[]
                    for metadata in grouped_by_frame[frame]:
                        new_obj = {
                            'frame': 0,
                            'type': metadata['type'],
                            **metadata['attributes']
                        }
                        if mode == 'state':
                            new_obj.update({'media_ids':[media_id]})
                        else:
                            new_obj.update({'media_id':media_id,
                                            'x': metadata['x'],
                                            'y': metadata['y'],
                                            'width': metadata['width'],
                                            'height': metadata['height']})
                        new_meta.append(new_obj)
                        print(f"{frame} {new_meta}")
                    ep(project, new_meta)



def _extract_thumbnails(image, localizations, outputDir):
    for localization in localizations:
        output_name = f"{localization['id']}.png"
        output_fp = os.path.join(outputDir, output_name)

        # Now get the image data from the image
        height = image.shape[0]
        width = image.shape[1]

        # Check for annotations starting off screen
        if localization.get('x') < 0:
            localization['x'] = 0
        if localization.get('y') < 0:
            localization['y'] = 0

        thumb_height = int(height * localization['height'])
        thumb_width = int(width * localization['width'])
        thumb_y = int(height * localization['y'])
        thumb_x = int(width * localization['x'])

        # Check for annotations extending off screen
        if thumb_x + thumb_width > width:
            thumb_width = width - thumb_x
        if thumb_y + thumb_height > height:
            thumb_height = height - thumb_y

        thumbnail = image[thumb_y:thumb_y+thumb_height,
                          thumb_x:thumb_x+thumb_width,
                          :]
        cv2.imwrite(output_fp, thumbnail)
