import os
import math

import requests
from urllib.parse import urljoin
from urllib.parse import urlsplit

def download_temporary_file(api, temporary_file, out_path):
    """ Download a temporary file from Tator to an off-line location.

    Example:

    .. code-block:: python

        api = tator.get_api(host, token)
        temporary_file = api.get_temporary_file(temporary_file_id)
        out_path = f'/tmp/{temporary_file.name}'
        for progress in tator.util.download_temporary_file(api, temporary_file,
                                                      out_path):
            print(f"Download progress: {progress}%")

    :param api: :class:`tator.TatorApi` object.
    :param temporary_file: :class:`tator.models.TemporaryFile` object.
    :param path-like out_path: Path to where to download.
    :returns: Generator that yields progress (0-100).
    """
    config = api.api_client.configuration
    host = config.host
    token = config.api_key['Authorization']
    prefix = config.api_key_prefix['Authorization']
    url = temporary_file.path

    # Supply token here for eventual media authorization
    headers = {
        'Authorization': f'{prefix} {token}',
        'Content-Type': f'application/json',
        'Accept-Encoding': 'gzip',
    }
    CHUNK_SIZE = 2 * 1024 * 1024
    with requests.get(url, stream=True, headers=headers) as r:
        r.raise_for_status()
        total_size = r.headers['Content-Length']
        total_chunks = math.ceil(int(total_size) / CHUNK_SIZE)
        chunk_count = 0
        last_progress = 0
        yield last_progress
        with open(out_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
                    this_progress = round((chunk_count / total_chunks) *100,1)
                    if this_progress != last_progress:
                        yield this_progress
                        last_progress = this_progress
        yield 100
