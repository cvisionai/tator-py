import math
import logging
from urllib.parse import urljoin

import requests

logger = logging.getLogger(__name__)

def _download_file(api, project, url, out_path):
    CHUNK_SIZE = 10 * 1024 * 1024
    MAX_RETRIES = 10
    # If this is a normal url, get headers.
    if url.startswith('/'):
        config = api.api_client.configuration
        host = config.host
        token = config.api_key['Authorization']
        prefix = config.api_key_prefix['Authorization']
        url = urljoin(host, url)
        # Supply token here for eventual media authorization
        headers = {
            'Authorization': f'{prefix} {token}',
            'Content-Type': f'application/json',
            'Accept-Encoding': 'gzip',
        }
    elif url.startswith('http'):
        headers = {}
    # If this is a S3 object key, get a download url.
    else:
        url = api.get_download_info(project, {'keys': [url]})[0].url
        headers = {}
    for attempt in range(MAX_RETRIES):
        try:
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
                            chunk_count += 1
                            f.write(chunk)
                            this_progress = round((chunk_count / total_chunks) *100,1)
                            if this_progress != last_progress:
                                yield this_progress
                                last_progress = this_progress
                yield 100
            break
        except Exception as ex:
            logger.error(f"Failed to download {url} on attempt {attempt} {ex}...")
            pass

