#!/usr/bin/env python

import argparse
import os
import shutil
import sys
from uuid import uuid1
import logging
import json

from progressbar import progressbar
import requests
from tator.openapi.tator_openapi.models import MessageResponse

from ..util import md5sum
from ..util.get_api import get_api

from .create_media import create_media
from .determine_transcode import determine_transcode
from .transcode import convert_streaming
from .transcode import convert_archival
from .transcode import convert_audio
from .delete_media import delete_media
from .make_thumbnails import make_thumbnails

if os.getenv("DD_LOGS_INJECTION"):
    import ddtrace.auto
    FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
              '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
              '- %(message)s')
else:
    FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
              '- %(message)s')
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def parse_args():
    parser = argparse.ArgumentParser(description='Full transcode pipeline on a directory of files.')
    parser.add_argument('path', nargs='?', type=str,
                        help='Path to directory containing video files, or a video file. '
                             'Ignored if --url is given.')
    parser.add_argument('--extension', type=str, default='mp4', help='File extension to upload. '
                                                                     'Ignored if path is a file.')
    parser.add_argument('--work_dir', type=str, help='Path to working directory. If not given, '
                                                     'the path containing videos will be used.')
    parser.add_argument('--url', type=str, help='URL where original file is hosted.')
    parser.add_argument('--host', type=str, default='https://cloud.tator.io', help='Host URL.')
    parser.add_argument('--token', type=str, help='REST API token.')
    parser.add_argument('--project', type=int, help='Unique integer specifying project ID.')
    parser.add_argument('--type', type=int, help='Unique integer specifying a media type.')
    parser.add_argument('--name', type=str, help='Name of the media.')
    parser.add_argument('--section', type=str, help='Media section name.')
    parser.add_argument('--section_id', type=int, help='Media section ID. If given `--section` is ignored.')
    parser.add_argument('--attributes', type=str, help="Attributes for media as a JSON string.")
    parser.add_argument('--media_id', type=int, help="Existing media ID, if applicable",
                        default=-1)
    parser.add_argument('--gid', type=str, help="Upload group ID.")
    parser.add_argument('--uid', type=str, help="Upload unique ID.")
    parser.add_argument('--group_to', type=int, default=1080,
                         help='Vertical resolutions below this will be transcoded with '
                              'multi-headed ffmpeg.')
    parser.add_argument('--email_spec', type=str, help="Optional email spec as a JSON string. The email will be sent upon completion of the transcode (see Email rest endpoint docs).")
    parser.add_argument('--cleanup', action='store_true',
                        help="Deletes working files after each file is transcoded and "
                             "uploaded.")
    parser.add_argument('--hwaccel', action='store_true', help="Use hardware acceleration.")
    return parser.parse_args()

def get_file_paths(path, base):
    paths = {
        'original': path,
        'transcoded': base + '_transcoded',
        'thumbnail': base + '_thumbnail.jpg',
        'thumbnail_gif': base + '_thumbnail_gif.gif',
    }
    return paths

def transcode_single(path, args, gid):
    """Transcodes a single file.
    """
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    # If a URL is given and path doesn't exist, download the file to path.
    if args.url:
        path = os.path.join(args.work_dir, args.name)
        response = requests.get(args.url, stream=True)
        response.raise_for_status()
        with open(path, "wb") as fp:
            for chunk in response.iter_content(chunk_size=10485760):  # 10 MiB
                if chunk:
                    fp.write(chunk)
    elif path is None:
        raise ValueError(f"Must provide one of --url or path!")

    # Get file paths.
    if args.work_dir:
        base = os.path.join(args.work_dir, os.path.splitext(os.path.basename(path))[0])
    else:
        base, _ = os.path.splitext(path)
    paths = get_file_paths(path, base)

    # Get md5 for the file.
    md5 = md5sum(paths['original'])

    # Get base filename.
    if args.name:
        name = args.name
    else:
        name = os.path.basename(paths['original'])

    # Create a uid if not set.
    if args.uid is None:
        uid = str(uuid1())
    else:
        uid = args.uid

    # Create the media object.
    if args.media_id == -1:
        kwargs = {}
        if args.section_id:
            kwargs['section_id'] = args.section_id
            args.section = None
        media_id = create_media(args.host, args.token, args.project, args.type, args.section,
                                name, md5, gid, uid, args.attributes, args.url, **kwargs)
    else:
        media_id = args.media_id

    try:
        # Make thumbnails.
        make_thumbnails(args.host, args.token, media_id, paths['original'], paths['thumbnail'],
                        paths['thumbnail_gif'])

        # Determine transcodes that need to be done.
        workloads = determine_transcode(
            args.host, args.token, args.type, media_id, path, group_to=args.group_to
        )

        # Transcode the video file.
        for workload in workloads:
            category = workload['category']
            del workload['category']
            del workload['id']
            if category == 'streaming':
                convert_streaming(**workload, host=args.host, token=args.token, media=media_id,
                                  outpath=paths['transcoded'], hwaccel=args.hwaccel)
            elif category == 'archival':
                del workload['configs']
                convert_archival(**workload, host=args.host, token=args.token, media=media_id,
                                 outpath=paths['transcoded'], hwaccel=args.hwaccel)
            elif category == 'audio':
                del workload['configs']
                del workload['raw_width']
                del workload['raw_height']
                convert_audio(**workload, host=args.host, token=args.token, media=media_id,
                              outpath=paths['transcoded'])
    except Exception as exc:
        logging.error("Encountered exception!", exc_info=True)
        if args.media_id == -1:
            delete_media(args.host, args.token, media_id)
        raise RuntimeError(f"Transcode of file {path} failed!") from exc

    # Clean up after the transcode is finished (if enabled).
    if args.cleanup:
        for key in ['transcoded', 'thumbnail', 'thumbnail_gif']:
            path = paths[key]
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)

    # Send an email.
    if isinstance(args.email_spec, str):
        try:
            email_spec = json.loads(args.email_spec)
        except json.JSONDecodeError:
            logger.warning(
                "Could not decode email_spec string '%s'", args.email_spec, exc_info=True
            )
            email_spec = None
    else:
        email_spec = args.email_spec

    if email_spec:
        api = get_api(args.host, args.token)
        response = api.send_email(args.project, email_spec=email_spec)
        if isinstance(response, MessageResponse):
            logger.info(response.message)

def transcode_main(args):
    if args.gid is None:
        gid = str(uuid1())
    else:
        gid = args.gid
    if args.path and os.path.isdir(args.path):
        file_list = []
        for root, _, files in os.walk(args.path):
            for fname in files:
                if fname.endswith(args.extension):
                    path = os.path.join(root, fname)
                    file_list.append(path)
        for path in progressbar(file_list):
            transcode_single(path, args, gid)
    else:
        transcode_single(args.path, args, gid)
    
if __name__ == '__main__':
    args = parse_args()
    transcode_main(args)
