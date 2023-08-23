"""Adds locally transcoded file to a media.

- Currently only supported to add a streaming config
- Must delete existing resolution. This tool does not replace, just add.

"""

import argparse
import datetime
import os

import tator
from tator.util._upload_file import _upload_file
from tator.transcode.transcode import make_video_definition
from tator.transcode.make_fragment_info import make_fragment_info

def parse_args() -> argparse.Namespace:
    """Parse script's arguments
    """

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--host", type=str, default="https://cloud.tator.io")
    parser.add_argument("--token", type=str, required=True)
    parser.add_argument("--media-id", type=int, required=True, help="Destination media ID to place media file in.")
    parser.add_argument("--transcoded-file", type=str, required=True, help="Locally transcoded file")
    parser.add_argument("--description", type=str, help="Description of transcode", default="Locally transcoded file")
    parser.add_argument("--resolution", type=int, required=True, description="Resolution to add as")
    args = parser.parse_args()
    return args

def script_main() -> None:
    """Main entrypoint
    """

    args = parse_args()

    #
    # GET MEDIA
    #
    # Verify the media does not have an existing resolution
    #
    tator_api = tator.get_api(host=args.host, token=args.token)
    media = tator_api.get_media(id=args.media_id)
    if media.media_files:
        streaming = media.media_files.streaming
    else:
        streaming = []
    available_resolutions = [x.resolution[0] for x in streaming]
    for res in available_resolutions:
        assert res != args.resolution, f"Resolution of {args.resolution} already exists!"

    print(f"[{datetime.datetime.now()}] {media.name} (ID: {media.id}) - Adding {args.resolution} streaming resolution")

    #
    # MAKE SEGMENTS FILE
    #
    print(f"[{datetime.datetime.now()}] Making segments file for {args.transcoded_file}")
    assert os.path.exists(args.transcoded_file), f"Could not find {args.transcoded_file}"
    segments_file = os.path.join(os.path.dirname(args.transcoded_file), "segments_{resolution}.json")
    make_fragment_info(args.transcoded_file, segments_file)

    #
    # UPLOAD FILES
    #
    print(f"[{datetime.datetime.now()}] Uploading {args.transcoded_file}")
    for progress, upload_info in _upload_file(
            api=tator_api,
            project=media.project,
            path=args.transcoded_file,
            media_id=media.id,
            filename=os.path.basename(args.transcoded_file)):
        print(f"[{datetime.datetime.now()}] Uploading {args.transcoded_file} - {progress}")

    print(f"[{datetime.datetime.now()}] Uploading {segments_file}")
    for progress, segment_info in _upload_file(
            api=tator_api,
            project=media.project,
            path=segments_file,
            media_id=media.id,
            filename=os.path.basename(segments_file)):
        print(f"[{datetime.datetime.now()}] Uploading {segments_file} - {progress}")

    #
    # ADD VIDEO DEFINITION
    #
    print(f"[{datetime.datetime.now()}] Adding video definition to media file")
    media_def = {
        **make_video_definition(args.transcoded_file),
        "path": upload_info.key,
        "segment_info": segment_info.key,
        "description": args.description}
    response = tator_api.create_video_file(
        id=media.id,
        role="streaming",
        video_definition=media_def)
    print(response)

if __name__ == "__main__":
    script_main()
