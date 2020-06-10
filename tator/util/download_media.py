import os
import math

import requests
from urllib.parse import urljoin
from urllib.parse import urlsplit

def download_media(media, out_path, progress=False):
    """ Download a media file from Tator to an off-line location.

    :param media: `Media` object.
    :param path-like out_path: Path to where to download.
    :param progress: [Optional] If true, yield progress. Default is false.
    """
    if media.media_files is not None:
        archival = media.media_files.get('archival', [])
        streaming = media.media_files.get('streaming',[])
        split = urlsplit(self.url)
        if len(archival) > 0:
            url = urljoin("https://"+split.netloc, archival[0]['path'])
        elif len(streaming) > 0:
            url = urljoin("https://"+split.netloc, streaming[0]['path'])
    else:
        # Legacy way of using streaming prior to streaming
        url=os.path.join("media", media['file'])
        if media.original:
            url=os.path.join("data/raw", media.original)
        split = urlsplit(self.url)
        url = urljoin("https://"+split.netloc, url)

    # Supply token here for eventual media authorization
    with requests.get(url, stream=True, headers=self.headers) as r:
        r.raise_for_status()
        total_size = r.headers['Content-Length']
        total_chunks = math.ceil(int(total_size) / 8192)
        chunk_count = 0
        last_progress = 0
        if progress:
            yield last_progress
        with open(out_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    chunk_count += 1
                    f.write(chunk)
                    this_progress = round((chunk_count / total_chunks) *100,1)
                    if this_progress != last_progress:
                        if progress:
                            yield this_progress
                        last_progress = this_progress
        if progress:
            yield 100
