import requests
import math
import os
import logging
import requests
import time
import concurrent.futures

import tator

logger = logging.getLogger(__name__)

MAX_RETRIES = 10 # Maximum retries on a given chunk.
GCP_CHUNK_MOD = 256 * 1024 # Chunk size must be a multiple of 256KB for Google Cloud Storage

def _upload_chunk(file_part, chunk_count, chunk_size, file_size, url, path, gcp_upload, default_etag_val, timeout):
    for attempt in range(MAX_RETRIES):
        try:
            kwargs = {"data": file_part, "timeout": timeout}
            if gcp_upload:
                first_byte = chunk_count * chunk_size
                last_byte = min(first_byte + chunk_size, file_size) - 1
                kwargs["headers"] = {
                    "Content-Length": str(last_byte - first_byte),
                    "Content-Range": f"bytes {first_byte}-{last_byte}/{file_size}",
                }
            response = requests.put(url, **kwargs)
            etag_str = response.headers.get("ETag", default_etag_val)
            if etag_str == None:
                raise RuntimeError("No ETag in response!")
            return {
                "ETag": etag_str,
                "PartNumber": chunk_count + 1,
            }
        except Exception as e:
            logger.warning(f"Upload of {path} chunk {chunk_count} failed ({e})! Attempt "
                           f"{attempt + 1}/{MAX_RETRIES}")
            if attempt == MAX_RETRIES - 1:
                raise RuntimeError(f"Upload of {path} failed!")
            else:
                time.sleep(10 * attempt)
                logger.warning(f"Backing off for {10 * attempt} seconds...")

def _upload_file(api, project, path, media_id=None, filename=None, chunk_size=1024*1024*10, file_size=None, file_id=None, timeout=30, max_workers=10):
    """ Uploads a file.

    :param api: `tator.TatorApi` object.
    :param project: Unique integer identifying a project.
    :param path: Path to file on disk.
    :param media_id: [Optional] Media ID if this is an upload for existing media.
    :param filename: [Optional] Filename (only used if media ID is given).
    :param file_id: [Optional] File ID if this is an upload for existing File.
    :param chunk_size: [Optional] Upload chunk size in bytes.
    :param timeout: [Optional] Request timeout for uploads in seconds. Default is 30.
    :param max_workers: [Optional] Max workers for concurrent requests.
    """

    # Get number of chunks.
    if file_size is None or file_size <= 0:
        file_size = os.stat(path).st_size

    if math.ceil(file_size / chunk_size) > 10000:
        chunk_size = math.ceil(file_size / 9000)
        logger.warning(
            f"Number of chunks exceeds maximum of 10,000. Increasing chunk size to {chunk_size}."
        )

    if chunk_size % GCP_CHUNK_MOD:
        logger.warning(
            f"Chunk size must be a multiple of 256KB for Google Cloud Storage compatibility"
        )
        chunk_size = math.ceil(chunk_size / GCP_CHUNK_MOD) * GCP_CHUNK_MOD

    if path.startswith('https://') or path.startswith('http://') and filename:
        filename = filename.split('?')[0]
    # Get upload info.
    num_chunks = math.ceil(file_size / chunk_size)
    upload_kwargs = {'num_parts': num_chunks}
    if media_id is not None:
        upload_kwargs['media_id'] = media_id
    if file_id is not None:
        upload_kwargs['file_id'] = file_id
    if filename is not None:
        upload_kwargs['filename'] = filename
    upload_info = api.get_upload_info(project, **upload_kwargs)

    # Functor to wrap around file versus URL
    def get_data(path):
        if path.startswith('https://') or path.startswith('http://'):
            return requests.get(path, stream=True).raw
        else:
            return open(path, 'rb')
    if num_chunks > 1:
        # Upload parts.
        parts = []
        yield (0, None)
        gcp_upload = upload_info.upload_id == upload_info.urls[0]
        with get_data(path) as f:
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                def complete_chunk(fs):
                    parts.append(fs.result())
                    progress = round((len(parts) / num_chunks) *100,1)
                    return (progress, None)
                futures = set()
                for chunk_count, url in enumerate(upload_info.urls):
                    file_part = f.read(chunk_size)
                    default_etag_val = str(chunk_count) if gcp_upload else None
                    future = executor.submit(_upload_chunk, file_part, chunk_count, chunk_size, file_size, url, path, gcp_upload, default_etag_val, timeout)
                    futures.add(future)
                    if len(futures) > max_workers:
                        done, futures = concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)
                        for future in done:
                            yield complete_chunk(future)
                for future in concurrent.futures.as_completed(futures):
                    yield complete_chunk(future)

                # Complete the upload.
                completed = False
                count = 0
                while completed is False and count < MAX_RETRIES:
                    try:
                        count += 1
                        response = api.complete_upload(project, upload_completion_spec={
                            'key': upload_info.key,
                            'upload_id': upload_info.upload_id,
                            'parts': sorted(parts, key=lambda x: x['PartNumber']),
                        })
                        if not isinstance(response, tator.models.MessageResponse):
                            raise RuntimeError(f"Upload completion failed!")
                        print(response.message)
                        completed=True
                    except Exception as e:
                        logger.warning(e)
                        if count == MAX_RETRIES - 1:
                            raise RuntimeError(f"Upload of {path} failed!")
                        else:
                            time.sleep(10 * count)
                            logger.warning(f"Backing off for {10 * count} seconds...")
                        completed = False
    else:
        # Upload in single request.
        with get_data(path) as f:
            data = f.read()
            for attempt in range(MAX_RETRIES):
                response = requests.put(upload_info.urls[0], data=data, timeout=timeout)
                if response.status_code == 200:
                    break
                else:
                    logger.warning(f"Upload of {path} failed ({response.text}) size={len(data)}! Attempt "
                                   f"{attempt + 1}/{MAX_RETRIES}")
                    if attempt == MAX_RETRIES - 1:
                        raise RuntimeError(f"Upload of {path} failed!")
                    else:
                        time.sleep(10 * attempt)
                        logger.warning(f"Backing off for {10 * attempt} seconds...")

    # Return the parts and upload info.
    yield (100, upload_info)
