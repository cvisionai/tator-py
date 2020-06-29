import logging
import math

from tusclient.client import TusClient
from progressbar import progressbar

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def upload_file(path, host):
    tus_url = host + '/files/'
    logger.info(f"Uploading file {path}...")
    tus = TusClient(tus_url)
    chunk_size = 1*1024*1024 # 1 Mb
    uploader = tus.uploader(path, chunk_size=chunk_size)
    num_chunks = math.ceil(uploader.get_file_size()/chunk_size)

    for _ in progressbar(range(num_chunks)):
        uploader.upload_chunk()
    return uploader.url

