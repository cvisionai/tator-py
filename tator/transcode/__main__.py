#!/usr/bin/env python

import argparse
import os
from uuid import uuid1

from progressbar import progressbar

from ..util import md5sum

from .transcode import transcode
from .make_thumbnails import make_thumbnails
from .upload_transcoded_video import upload_transcoded_video

def parse_args():
    parser = argparse.ArgumentParser(description='Full transcode pipeline on a directory of files.')
    parser.add_argument('path', type=str, help='Path to directory containing video files, or a video file.')
    parser.add_argument('--extension', type=str, default='mp4', help='File extension to upload. '
                                                                     'Ignored if path is a file.')
    parser.add_argument('--tus_url', type=str, default='https://www.tatorapp.com/files/', help='TUS URL.')
    parser.add_argument('--url', type=str, default='https://www.tatorapp.com/rest', help='REST API URL.')
    parser.add_argument('--token', type=str, help='REST API token.')
    parser.add_argument('--project', type=int, help='Unique integer specifying project ID.')
    parser.add_argument('--type', type=int, help='Unique integer specifying a media type.')
    parser.add_argument('--section', type=str, help='Media section name.')
    return parser.parse_args()

def get_file_paths(path):
    base, _ = os.path.splitext(path)
    paths = {
        'original': path,
        'transcoded': base + '_transcoded',
        'thumbnail': base + '_thumbnail.jpg',
        'thumbnail_gif': base + '_thumbnail_gif.gif',
        'segments': base + '_segments.json',
    }
    return paths

def transcode_single(path, args, gid):
    """Transcodes a single file.
    """
    paths = get_file_paths(path)

    # Get md5 for the file.
    md5 = md5sum(paths['original'])

    # Get base filename.
    name = os.path.basename(paths['original'])

    # Transcode the video file.
    transcode(paths['original'], paths['transcoded'])
    
    # Make thumbnails.
    make_thumbnails(paths['original'], paths['thumbnail'], paths['thumbnail_gif'])
    
    # Upload the results.
    uid = str(uuid1())
    upload_transcoded_video(paths['original'], paths['transcoded'],
                            paths['thumbnail'], paths['thumbnail_gif'], args.tus_url, args.url,
                            args.token, args.project, args.type, gid, uid, args.section, 
                            name, md5)

if __name__ == '__main__':
    args = parse_args()
    if os.path.isdir(args.path):
        file_list = []
        for root, dirs, files in os.walk(args.path):
            for fname in files:
                if fname.endswith(args.extension):
                    path = os.path.join(root, fname)
                    file_list.append(path)
        gid = str(uuid1())
        for path in progressbar(file_list):
            transcode_single(path, args, gid)
    else:
        gid = str(uuid1())
        transcode_single(args.path, args, gid)
