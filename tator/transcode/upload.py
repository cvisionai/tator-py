import logging
import math
from uuid import uuid1

from tusclient.client import TusClient
from urllib.parse import urljoin
from progressbar import progressbar

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def upload_file(path, api):
    host = api.api_client.configuration.host
    token = api.api_client.configuration.api_key['Authorization']
    prefix = api.api_client.configuration.api_key_prefix['Authorization']
    upload_uid = str(uuid1())
    tusURL = urljoin(host, "files/")
    tus = TusClient(tusURL, headers={'Authorization': f'{prefix} {token}',
                                     'Upload-Uid': f'{upload_uid}'})
    logger.info(f"Uploading file {path}...")
    chunk_size = 10*1024*1024 # 10 Mb
    uploader = tus.uploader(path, chunk_size=chunk_size,
                            retries=10, retry_delay=15)
    num_chunks = math.ceil(uploader.get_file_size()/chunk_size)

    for _ in progressbar(range(num_chunks)):
        uploader.upload_chunk()
    return uploader.url

