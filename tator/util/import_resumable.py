#!/usr/bin/python3

# Example:
# python3 import_resumable.py --token $(cat ~/token.txt)  16744335

import tator
import os
import tempfile
from tator.transcode.transcode import convert_archival, convert_streaming, convert_audio
from tator.transcode.make_thumbnails import make_thumbnails

from pprint import pprint
import argparse
import requests

import cv2


def import_resumable(api, media_id, work_dir=None, explicit_config=None, streaming_configs=[]):
    """Imports a resumable upload into Tator.
    :param api: `tator.TatorApi` object.
    :param media_id: Unique integer identifying a media.
    :param work_dir: [Optional] Temporary directory for joining components.
    :param explicit_config: [Optional] Explicit configuration for  archivals (see `tator.transcode.convert_archival` for details.)
    :param streaming_configs: [Optional] List of explicit configurations for streaming (see `tator.transcode.convert_streaming` for details.)
    """
    with tempfile.TemporaryDirectory() as td:
        host = api.api_client.configuration.host
        token = api.api_client.configuration.api_key["Authorization"]
        if work_dir is None:
            work_dir = td

        media = api.get_media(media_id, presigned=60 * 60 * 24)
        if streaming_configs == []:
            media_type = api.get_media_type(media.type)
            tator_streaming_config = media_type.to_dict()["streaming_config"]
            for config in tator_streaming_config:
                streaming_configs.append(
                    f"{config['resolution']}:{config['crf']}:{config['vcodec']}:{config.get('preset','fast')}:{config.get('pixel_format','yuv420p')}"
                )

        components = [x["path"] for x in media.media_files.to_dict().get("archival", [])]
        components.sort(key=lambda x: int(os.path.splitext(x)[0].split("_")[-2]))
        _, ext = os.path.splitext(components[0])
        ext = ext.split("?")[0]

        temp_path = os.path.join(work_dir, f"output{ext}")
        with open(temp_path, "wb") as output:
            for url in components:
                with requests.get(url, stream=True) as r:
                    r.raise_for_status()
                    for chunk in r.iter_content(chunk_size=8192):
                        output.write(chunk)

        thumb_path = os.path.join(work_dir, "thumb.jpg")
        thumb_gif_path = os.path.join(work_dir, "thumb.gif")

        make_thumbnails(
            host=args.host,
            token=args.token,
            video_path=temp_path,
            media_id=media_id,
            thumb_path=thumb_path,
            thumb_gif_path=thumb_gif_path,
        )
        print("Completed Thumbnail Processing.")

        #  Get video resolution
        cap = cv2.VideoCapture(temp_path)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cap.release()

        # convert video for archival,  streaming,  and audio
        outpath = os.path.join(work_dir, "archivals")
        convert_archival(
            host,
            token,
            media_id,
            temp_path,
            outpath,
            width,
            height,
            size=None,
            explicit_config=explicit_config,
        )

        convert_streaming(
            host,
            token,
            media_id,
            temp_path,
            work_dir,
            width,
            height,
            streaming_configs,
        )

        convert_audio(host, token, media_id, temp_path, work_dir)

        print("Completed Transcoding.")

    print("Now we can remove the fragments.")
    media = api.get_media(media_id)
    archival_files = media.media_files.to_dict().get("archival", [])
    fragments = [x for x in archival_files if x["codec"] == "fragment"]
    while fragments:
        # Find the frag location and iterate until all are gone.
        for frag_index, info in enumerate(archival_files):
            if info["codec"] == "fragment":
                break

        api.delete_video_file(media_id, "archival", frag_index)
        media = api.get_media(media_id)
        archival_files = media.media_files.to_dict().get("archival", [])
        fragments = [x for x in archival_files if x["codec"] == "fragment"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Join resumable upload components.")
    parser.add_argument("--host", type=str, default="https://cloud.tator.io")
    parser.add_argument("--token", type=str, required=True, help="Tator token.")
    parser.add_argument("--work-dir", type=str, help="Temporary directory for joining components.")
    parser.add_argument("media_id", type=int, help="Media ID to join.")
    args = parser.parse_args()

    api = tator.get_api(host=args.host, token=args.token)
    import_resumable(api, args.media_id, args.work_dir)
