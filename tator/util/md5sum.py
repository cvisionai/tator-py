import hashlib
import os
import requests

def md5sum(fname, size=None):
    """ Computes md5sum-based fingerprint of a file contents. The return
        is the md5sum of the file contents (up to 100Mb) hashed along with
        the file size.

    :param fname: Path to file.
    :param size: Size of file. Will be computed if not given.
    :returns: md5 sum of the file.
    """
    CHUNK_SIZE = 100*1024*1024 # 100MB
    md5 = hashlib.md5()
    if fname.startswith("https://") or fname.startswith("http://"):
        HTTP_CHUNK = 10*1024*1024
        with requests.get(fname, stream=True) as r:
            r.raise_for_status()
            for count,chunk in enumerate(r.iter_content(chunk_size=HTTP_CHUNK)):
                md5.update(chunk)
                if (count + 1) * HTTP_CHUNK >= CHUNK_SIZE:
                    break # bail out after intended chunk size

        # Try to get the file size via HTTP, fall-back to provided size
        # if it doesn't work
        try:
            r = requests.head(fname)
            proposed_size = int(r.headers.get('content-length',0))
            if proposed_size:
                size = proposed_size
        except:
            if size is None or size <= 0:
                raise Exception("Must supply size if HTTP server doesn't support HEAD requests for size.")
    else:
        with open(fname, 'rb') as f:
            for chunk in iter(lambda: f.read(CHUNK_SIZE), b''):
                md5.update(chunk)
                break # Exit after one chunk

    # Compute file size if not given. (Already set for HTTP files)
    if (size is None or size <= 0) and os.path.exists(fname):
        size = os.stat(fname).st_size

    # If size still not computed, raise an exception.
    if size is None or size <= 0:
        raise Exception(f"Could not determine size of file {fname}!")

    # Salt in file size.
    out = hashlib.md5()
    out.update(md5.hexdigest().encode('utf-8') + str(size).encode('utf-8'))
    return out.hexdigest()
