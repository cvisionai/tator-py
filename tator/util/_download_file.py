import math
import logging
import os
import time
from urllib.parse import urljoin

import requests

logger = logging.getLogger(__name__)

def _download_file(api, project, url, out_path):
    CHUNK_SIZE = 10 * 1024 * 1024
    MAX_RETRIES = 10
    CHUNK_RETRY_LIMIT = 3
    RETRY_BACKOFF_BASE = 1.0  # Base delay in seconds

    # URL and headers resolution - same as before
    original_url = url
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
        supports_range = True  # Tator API should support range requests
    elif url.startswith('http'):
        headers = {}
        supports_range = True  # Most HTTP servers support range requests
    # If this is a S3 object key, get a download url.
    else:
        url = api.get_download_info(project, {'keys': [url]})[0].url
        headers = {}
        supports_range = True  # S3 presigned URLs support range requests

    # Determine if we can resume from partial file
    resume_byte_pos = 0
    original_resume_attempt = False  # Track if we originally tried to resume
    try:
        if os.path.exists(out_path) and supports_range:
            resume_byte_pos = os.path.getsize(out_path)
            original_resume_attempt = True
            logger.info(f"Resuming download from byte {resume_byte_pos}")
    except (OSError, IOError) as fs_ex:
        logger.warning(f"Could not check existing file for resume: {fs_ex}")
        resume_byte_pos = 0  # Start fresh if we can't check the file

    total_retries = 0
    stream_retry_count = 0
    chunk_retry_count = 0
    download_completed = False

    for attempt in range(MAX_RETRIES):
        try:
            # Add range header for resumption if needed
            request_headers = headers.copy()
            if resume_byte_pos > 0:
                request_headers['Range'] = f'bytes={resume_byte_pos}-'

            with requests.get(url, stream=True, headers=request_headers) as r:
                r.raise_for_status()

                # Handle range request responses
                if resume_byte_pos > 0 and r.status_code == 206:
                    # Partial content - continuing download
                    content_range = r.headers.get('Content-Range', '')
                    if content_range:
                        # Parse Content-Range: bytes 1000-2000/3000
                        total_size = int(content_range.split('/')[-1])
                    else:
                        # Fallback if no Content-Range header
                        total_size = resume_byte_pos + int(r.headers.get('Content-Length', 0))
                elif resume_byte_pos > 0 and r.status_code == 200:
                    # Server doesn't support range requests - start over
                    logger.warning("Server doesn't support range requests, restarting download")
                    resume_byte_pos = 0
                    total_size = int(r.headers.get('Content-Length', 0))
                else:
                    # Fresh download
                    total_size = int(r.headers.get('Content-Length', 0))

                if total_size == 0:
                    logger.warning("Could not determine file size, progress reporting will be limited")
                    total_chunks = 1
                else:
                    total_chunks = math.ceil(total_size / CHUNK_SIZE)

                bytes_written = resume_byte_pos
                last_progress = round((bytes_written / total_size) * 100, 1) if total_size > 0 else 0
                yield last_progress

                # Open file in append mode if resuming, write mode if starting fresh
                file_mode = 'ab' if resume_byte_pos > 0 else 'wb'

                with open(out_path, file_mode) as f:
                    chunk_failures = 0

                    for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                        if chunk:
                            # Retry logic for individual chunk writes
                            chunk_success = False
                            for chunk_attempt in range(CHUNK_RETRY_LIMIT):
                                try:
                                    f.write(chunk)
                                    f.flush()  # Ensure chunk is written to disk
                                    bytes_written += len(chunk)
                                    chunk_success = True
                                    break
                                except (OSError, IOError) as chunk_ex:
                                    chunk_failures += 1
                                    total_retries += 1
                                    chunk_retry_count += 1
                                    logger.warning(
                                        f"Chunk write failed (attempt {chunk_attempt + 1}/{CHUNK_RETRY_LIMIT}): {chunk_ex}"
                                    )
                                    if chunk_attempt < CHUNK_RETRY_LIMIT - 1:
                                        time.sleep(RETRY_BACKOFF_BASE * (2 ** chunk_attempt))

                                    if chunk_retry_count >= MAX_RETRIES:
                                        raise RuntimeError(f"Too many chunk failures ({chunk_retry_count})")

                            if not chunk_success:
                                raise RuntimeError("Failed to write chunk after all retries")

                            # Update progress
                            if total_size > 0:
                                this_progress = round((bytes_written / total_size) * 100, 1)
                                if this_progress != last_progress:
                                    yield this_progress
                                    last_progress = this_progress

                # Validate final file size if we have expected size
                if total_size > 0:
                    try:
                        actual_size = os.path.getsize(out_path)
                        # Use original_resume_attempt to determine validation logic, not current resume_byte_pos
                        # because resume_byte_pos can be reset to 0 if server doesn't support range requests
                        if original_resume_attempt:
                            # Originally was a resume attempt - size validation is more complex
                            # Could be total_size (successful resume) or bytes_written (restart from 0)
                            if actual_size != total_size and actual_size != bytes_written:
                                logger.warning(f"Resume download size ({actual_size}) differs from both "
                                             f"total size ({total_size}) and bytes written ({bytes_written})")
                        else:
                            # Fresh download - check if actual file size matches bytes written
                            if actual_size != bytes_written:
                                raise ValueError(f"Download validation failed: file size mismatch. "
                                               f"Expected {bytes_written} bytes, got {actual_size} bytes")
                    except (OSError, IOError) as size_ex:
                        logger.warning(f"Could not validate downloaded file size: {size_ex}")
                        # Continue anyway - file might still be valid

                download_completed = True
                yield 100
                break  # Success - exit retry loop

        except (requests.exceptions.ConnectionError,
                requests.exceptions.ChunkedEncodingError,
                requests.exceptions.Timeout) as stream_ex:
            # Stream interruption - try to resume
            try:
                if os.path.exists(out_path) and supports_range:
                    current_size = os.path.getsize(out_path)
                    if current_size > resume_byte_pos:
                        logger.info(f"Stream interrupted, will resume from byte {current_size}")
                        resume_byte_pos = current_size
            except (OSError, IOError) as fs_ex:
                logger.warning(f"Could not check file for resume after stream interruption: {fs_ex}")
                # Continue with existing resume_byte_pos

            # Regenerate S3 URL if needed (presigned URLs may have expired)
            if not original_url.startswith(('/', 'http')):
                try:
                    new_download_info = api.get_download_info(project, {'keys': [original_url]})
                    if not new_download_info:
                        logger.error("Failed to regenerate S3 URL: No download info returned")
                        # Continue with existing URL - may still work or fail gracefully
                    else:
                        new_url = new_download_info[0].url
                        if new_url:
                            url = new_url
                            logger.info(f"Regenerated S3 URL for retry")
                        else:
                            logger.error("Failed to regenerate S3 URL: Empty URL returned")
                except Exception as regen_ex:
                    logger.error(f"Failed to regenerate S3 URL: {regen_ex}")
                    # Continue with existing URL - may still work or fail gracefully

            total_retries += 1
            stream_retry_count += 1
            backoff_delay = RETRY_BACKOFF_BASE * (2 ** min(attempt, 5))  # Cap exponential growth
            logger.error(
                f"Download stream failed on attempt {attempt + 1}/{MAX_RETRIES}: {stream_ex}. "
                f"Retrying in {backoff_delay:.1f}s..."
            )
            if attempt < MAX_RETRIES - 1:
                time.sleep(backoff_delay)
            else:
                # Final attempt failed - re-raise the stream exception
                logger.error(f"Download stream failed on final attempt {attempt + 1}/{MAX_RETRIES}")
                raise stream_ex

        except Exception as ex:
            total_retries += 1
            logger.error(f"Download failed on attempt {attempt + 1}/{MAX_RETRIES}: {ex}")
            if attempt == MAX_RETRIES - 1:
                # Final attempt failed - clean up partial file
                if os.path.exists(out_path):
                    try:
                        os.remove(out_path)
                        logger.info("Removed partial download file")
                    except OSError:
                        pass
                raise

            # Exponential backoff for general failures
            backoff_delay = RETRY_BACKOFF_BASE * (2 ** min(attempt, 5))
            time.sleep(backoff_delay)

    # Check if download completed successfully
    if not download_completed:
        raise RuntimeError(f"Download failed to complete after {MAX_RETRIES} attempts without specific exception")

