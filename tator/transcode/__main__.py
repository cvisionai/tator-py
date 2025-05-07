#!/usr/bin/env python

import argparse
import os
import shutil
import sys
from uuid import uuid1
import logging
import json
import glob
import re

from progressbar import progressbar
import requests
from tator.openapi.tator_openapi.models import MessageResponse

from ..util import md5sum
from ..util.get_api import get_api

from .create_media import create_media
from .determine_transcode import determine_transcode, update_media
from .transcode import convert_streaming
from .transcode import convert_archival
from .transcode import convert_audio
from .delete_media import delete_media
from .make_thumbnails import make_thumbnail_image, make_thumbnail_gif

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
                        help='Path to directory containing video files, or a video file, or text file with list of video files to be concatenated. '
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
    parser.add_argument('--force_fps', type=float, default=-1, help='Force a specific fps for the video.')
    parser.add_argument(
        "--inhibit-upload", action="store_true", help="Do not upload the transcoded files to Tator."
    )
    parser.add_argument('--filter_complex', type=str, help='Allows (optionally templated) override of filter_complex argument to ffmpeg for streaming files. Substitutes {fps}, {width}, {height}, {hw_upload}, and {ridx} if those patterns are present, where width and height correspond to the output resolutions.')
    parser.add_argument('--bucket_id', type=int, help='Bucket ID if not default.')
    return parser.parse_args()

def get_file_paths(path, base):
    paths = {
        'original': path,
        'transcoded': base + '_transcoded',
        'thumbnail': base + '_thumbnail.jpg',
        'thumbnail_gif': base + '_thumbnail_gif.gif',
    }
    return paths

def compare_workloads(workloads_list):
    """
    Compare the parameters of workloads across multiple lists to ensure consistency.
    
    :param workloads_list: List of workload lists to compare.
    :return: True if all workloads are consistent, False otherwise.
    """
    if not workloads_list:
        return True  # No workloads to compare, considered consistent

    # Extract the first workload list as the reference
    reference_workloads = workloads_list[0]

    # Define a helper function to extract relevant parameters from a workload
    def extract_params(workload):
        return (
            workload['category'],
            workload['raw_height'],
            workload['raw_width'],
            tuple(workload['configs'])
        )

    # Extract parameters from the reference workloads
    reference_params = [extract_params(workload) for workload in reference_workloads]

    # Compare parameters with other workload lists
    for workloads in workloads_list[1:]:
        current_params = [extract_params(workload) for workload in workloads]
        if current_params != reference_params:
            return False  # Inconsistent parameters found

    return True  # All parameters are consistent

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

    fnames = None
    if isinstance(path, list):
        if args.name is None:
            raise ValueError(f"Must provide --name when path is a list!")
        if args.work_dir:
            base = os.path.join(args.work_dir, args.name)
        else:
            base = args.name
        paths = get_file_paths(path[0], base)

    elif os.path.splitext(path)[-1] == '.json':
        # This transcode will concat multiple files
        with open(path,'r') as fp:
            fnames = json.load(fp)
        assert args.name is not None, "args.name must be provided"

        # Get file paths.
        if args.work_dir:
            base = os.path.join(args.work_dir, os.path.splitext(os.path.basename(args.name))[0])
        else:
            base, _ = os.path.splitext(args.name)

        # Use the first input file
        paths = get_file_paths(fnames[0], base)

    else:
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
        media_id = create_media(args.host, args.token, args.project, args.type, args.section, name, md5, gid, uid, args.attributes, args.url, **kwargs)
    else:
        media_id = args.media_id

    try:
        # Make thumbnails.
        make_thumbnail_image(
            args.host,
            args.token,
            media_id,
            paths["original"],
            paths["thumbnail"],
            inhibit_upload=args.inhibit_upload,
            bucket_id=args.bucket_id,
        )

        if fnames:
            workloads_list = []
            for fname in fnames:
                # Determine transcodes that need to be done.
                workloads = determine_transcode(
                    args.host, args.token, args.type, media_id, fname, group_to=args.group_to
                )
                workloads_list.append(workloads)
                if compare_workloads(workloads_list):
                    # Use the first workload, but update path
                    workloads = workloads_list[0]
                    for workload in workloads:
                        workload['path'] = fnames
        else:
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
                convert_streaming(
                    **workload,
                    host=args.host,
                    token=args.token,
                    media=media_id,
                    outpath=paths["transcoded"],
                    hwaccel=args.hwaccel,
                    force_fps=args.force_fps,
                    inhibit_upload=args.inhibit_upload,
                    filter_complex=getattr(args, "filter_complex", None),
                    bucket_id=args.bucket_id,
                )
            elif category == 'archival':
                del workload['configs']
                convert_archival(
                    **workload,
                    host=args.host,
                    token=args.token,
                    media=media_id,
                    outpath=paths["transcoded"],
                    hwaccel=args.hwaccel,
                    inhibit_upload=args.inhibit_upload,
                    bucket_id=args.bucket_id,
                )
            elif category == 'audio':
                del workload['configs']
                del workload['raw_width']
                del workload['raw_height']
                convert_audio(
                    **workload,
                    host=args.host,
                    token=args.token,
                    media=media_id,
                    outpath=paths["transcoded"],
                    inhibit_upload=args.inhibit_upload,
                    bucket_id=args.bucket_id,
                )

        # Get lowest resolution output for making the gif
        pattern = re.compile(r'^\d+\.mp4$')
        outputs = [os.path.basename(f) for f in glob.glob(os.path.join(paths['transcoded'], '*.mp4'))]
        outputs = list(filter(pattern.match, outputs))
        resolutions = [int(os.path.splitext(f)[0]) for f in outputs]
        if any([res > 256 for res in resolutions]):
            resolutions = [res for res in resolutions if res > 256]

        if len(resolutions) == 0:
            logger.info(f"No transcodes of streaming files was performed, skipping gif creation and media update.")
            return

        # Files are resolution height names, sort by lowest
        input_res = min(resolutions)

        # Make gif thumbnail
        make_thumbnail_gif(
            args.host,
            args.token,
            media_id,
            os.path.join(paths["transcoded"], f"{input_res}.mp4"),
            paths["thumbnail_gif"],
            inhibit_upload=args.inhibit_upload,
            bucket_id=args.bucket_id,
        )

        # Patch the media with the concatenated file
        max_res = max(resolutions)
        update_media(args.host, args.token, args.type, media_id, os.path.join(paths['transcoded'], f"{max_res}.mp4"))

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
    if args.path and not isinstance(args.path, list) and os.path.isdir(args.path):
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
