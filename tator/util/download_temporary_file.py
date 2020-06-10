import os
import math

import requests
from urllib.parse import urljoin
from urllib.parse import urlsplit

def download_temporary_file(api, temporary_file, out_path):
    """ Download a temporary file from Tator to an off-line location.

    :param api: :class:`tator.TatorApi` object.
    :param temporary_file: :class:`tator.TemporaryFile` object.
    :param path-like out_path: Path to where to download.
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
    with requests.get(url, stream=True, headers=headers) as r:
        r.raise_for_status()
        with open(out_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
