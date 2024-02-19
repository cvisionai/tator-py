#!/usr/bin/python3

# This implements a  resumable upload for large files to Tator.
# This is useful for uploading large files to Tator, as it allows for the upload to be resumed if it is interrupted.
# The protocol stores the files in parts referenced in the `archival` section of the media object.

#  To rejoin the parts, use the `tator.util.import_resumable` module

#  Example:
#  python3 resumable_upload.py --token $(cat ~/token.txt) --part-size $((512*1024)) --section "Resumable Uploads" --project 2 --type 14 ~/Videos/Dragons.mp4

import tator
from tator.util._upload_file import _upload_file
from tator.util.md5sum import md5sum

import os
import math
import tempfile
import base64
import tqdm


def continue_resumable_upload(
    api,
    media_id,
    file_path,
    part_size=100 * 1024 * 1024,
    chunk_size=10 * 1024 * 1024,
    max_workers=10,
):
    """Upload a file to a media object in a project using resumable uploads.
    This function can be used to upload large files to Tator in  resumable parts.
    :param api: Tator API object.
    :param media_id: Media ID.
    :param file_path: Path to file to upload.
    :param part_size: This is the resumable part size
    :param chunk_size: This is the chunk size for transmission

    """
    media = api.get_media(media_id)
    media_type = api.get_media_type(media.type)
    if media_type.dtype != "video":
        raise ValueError("Resumable upload is only supported for video media.")

    file_size = os.stat(file_path).st_size
    num_parts = math.ceil(file_size / part_size)

    existing_parts = []
    if media.media_files:
        for archival in media.media_files.to_dict().get("archival", []):
            raw_name, ext = os.path.splitext(archival["path"])
            # Tator adds a slug to the end of the  file comps,  remove it so  we  can  keep track of which parts are left.
            last_under = raw_name.rfind("_")
            part_name = raw_name[:last_under] + ext
            existing_parts.append(os.path.basename(part_name))

    print(f"Uploading {file_path} to media {media_id} in {num_parts} resumable parts.")

    base_name, ext = os.path.splitext(os.path.basename(file_path))
    part_size_str = base64.b64encode(str(part_size).encode()).decode()
    for part in tqdm.tqdm(range(num_parts), desc="Parts"):
        part_name = part_size_str + "_" + base_name + "_" + str(part) + ext
        if part_name in existing_parts:
            print(f"Part {part} already exists. Skipping.")
            continue
        with tempfile.TemporaryDirectory() as td:
            part_path = os.path.join(td, part_name)
            with open(file_path, "rb") as f:
                f.seek(part * part_size)
                with open(part_path, "wb") as part_file:
                    part_file.write(f.read(part_size))
            for _, upload_info in _upload_file(
                api=api,
                project=media.project,
                path=part_path,
                media_id=media_id,
                filename=part_name,
                chunk_size=chunk_size,
                max_workers=max_workers,
            ):
                pass

            media_def = {"path": upload_info.key, "codec": "fragment", "resolution": [1, 1]}
            api.create_video_file(media_id, "archival", media_def)


if __name__ == "__main__":
    """CLI frontend to resumable upload"""
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description="Upload a file to a media object in a project using resumable uploads."
    )
    parser.add_argument("--host", type=str, help="Tator host", default="https://cloud.tator.io")
    parser.add_argument("--token", type=str, help="Tator token", required=True)
    parser.add_argument("--project", type=int, help="Project ID", required=False)
    parser.add_argument("--section", type=str, help="Section Name", required=False)
    parser.add_argument("--type", type=int, help="Media Type ID", required=False)
    parser.add_argument("--media-id", type=int, help="Media ID", required=False)

    ## Optional arguments  for tuning upload
    parser.add_argument(
        "--part-size", type=int, help="Resumable part size", default=100 * 1024 * 1024
    )
    parser.add_argument(
        "--chunk-size", type=int, help="Chunk size for transmission", default=10 * 1024 * 1024
    )
    parser.add_argument(
        "--max-workers", type=int, help="Max workers for concurrent requests", default=10
    )

    parser.add_argument("file_path", type=str)
    args = parser.parse_args()
    if not any([args.media_id, bool(args.project and args.section and args.type)]):
        print("Must supply project + section + type or an existing media id")
        sys.exit(-1)

    api = tator.get_api(host=args.host, token=args.token)

    # Either use the media ID  or make a  new media
    # Of note, this will be  thumbnail less to avoid excessive thumbnail generation times
    # if the input file is roughly encoded for fast decode operations
    if args.media_id:
        media_id = args.media_id
    else:
        md5 = md5sum(args.file_path)
        response = api.create_media_list(
            args.project,
            {
                "type": args.type,
                "section": args.section,
                "md5": md5,
                "name": os.path.basename(args.file_path),
            },
        )
        media_id = response.id

    print(f"Using media ID {media_id} for upload.")
    print(f"To relaunch this upload, use the following command:")
    print(
        f"python3 {sys.argv[0]} --host {args.host} --token YOUR_TOKEN_HERE --media-id {media_id} --part-size {args.part_size} {args.file_path}"
    )
    continue_resumable_upload(
        api=api,
        media_id=media_id,
        file_path=args.file_path,
        part_size=args.part_size,
        chunk_size=args.chunk_size,
        max_workers=args.max_workers,
    )
