import math
import logging

import requests

logger = logging.getLogger(__name__)

def _download_file(url, headers, out_path):
    CHUNK_SIZE = 2 * 1024 * 1024
    MAX_RETRIES = 10
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
            logger.info(f"Failed to download {url} on attempt {attempt}...")
            pass

