import requests
import math
import os

def _upload_file(api, project, path, chunk_size=1024*1024*10):
    """ Uploads a file.
    """
    MAX_RETRIES = 10 # Maximum retries on a given chunk.

    # Get number of chunks.
    file_size = os.stat(path).st_size
    num_chunks = math.ceil(file_size / chunk_size)
    if num_chunks > 10000:
        chunk_size = math.ceil(file_size / 9000)
        logger.warning(f"Number of chunks {num_chunks} exceeds maximum of 10,000. Increasing "
                        "chunk size to {chunk_size}.")
        num_chunks = math.ceil(file_size / chunk_size)
    
    # Get upload info.
    upload_info = api.get_upload_info(project, num_parts=num_chunks)

    # Upload parts.
    parts = []
    last_progress = 0
    yield (last_progress, None)
    with open(path, 'rb') as f:
        for chunk, url in enumerate(upload_info.urls):
            file_part = f.read(chunk_size)
            for attempt in range(MAX_RETRIES):
                try:
                    response = requests.put(url, data=file_part)
                    etag = response.headers['ETag']
                    parts.append({'ETag': etag, 'PartNumber': chunk + 1})
                except:
                    logger.warning(f"Upload of {path} chunk {chunk} failed! Attempt "
                                   f"{attempt}/{MAX_RETRIES}")
                    if attempt == MAX_RETRIES - 1:
                        raise Exception(f"Upload of {path} failed!")
                this_progress = round((chunk_count / num_chunks) *100,1)
                if this_progress != last_progress:
                    yield (this_progress, None)
                    last_progress = this_progress

    # Complete the upload.
    response = api.complete_upload(project, upload_completion_spec={
        'key': upload_info.key,
        'upload_id': upload_info.upload_uid,
        'parts': parts,
    })
    if response.status_code != 201:
        raise Exception(f"Upload completion failed!")

    # Return the parts and upload info.
    yield (100, upload_info)

