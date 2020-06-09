import os
import math

import requests
from urllib.parse import urljoin
from urllib.parse import urlsplit

def download_temporary_file(temporary_file, out_path):
    """ Download a temporary file from Tator to an off-line location.

    :param temporary_file: `TemporaryFile` object.
    :param path-like out_path: Path to where to download.
    """
    url = temporary_file.path

    # Supply token here for eventual media authorization
    with requests.get(url, stream=True, headers=self.headers) as r:
        r.raise_for_status()
        with open(out_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
