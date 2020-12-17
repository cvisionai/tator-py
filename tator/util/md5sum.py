import hashlib
import os

def md5sum(fname, size=None):
    """ Computes md5 sum of a file contents.

    :param fname: Path to file.
    :param size: Size of file. Will be computed if not given.
    :returns: md5 sum of the file.
    """
    CHUNK_SIZE = 100*1024*1024 # 100MB
    md5 = hashlib.md5()
    with open(fname, 'rb') as f:
        for chunk in iter(lambda: f.read(CHUNK_SIZE), b''):
            md5.update(chunk)
            break # Exit after one chunk
    # Compute file size if not given.
    if size is None:
        size = os.stat(fname).st_size
    # Salt in file size.
    out = hashlib.md5()
    out.update(md5.hexdigest().encode('utf-8') + str(size).encode('utf-8'))
    return out.hexdigest()
