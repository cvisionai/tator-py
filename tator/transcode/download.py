"""Media downloads using curl with a requests fallback."""

import logging
import shutil
import subprocess

import requests

logger = logging.getLogger(__name__)


def download_file(url, output_path):
    """
    Download a file using curl if available, otherwise use requests.

    Args:
        url: URL to download from
        output_path: Local path where file should be saved
    """
    # Try curl if available
    if shutil.which('curl'):
        try:
            curl_cmd = [
                'curl',
                '--continue-at', '-',       # Resume partial downloads
                '--retry', '9',            # Up to ten attempts including the first
                '--retry-connrefused',      # Retry even if connection refused
                '--connect-timeout', '60',
                '--speed-limit', '1', '--speed-time', '600',
                '--fail', '--location', '--silent', '--show-error', '--globoff',
                '--proto', '=http,https,ftp', '--proto-redir', '=http,https,ftp',
                '--output', output_path,
                '--', url
            ]
            subprocess.run(curl_cmd, check=True, capture_output=True)
            logger.info(f"Successfully downloaded with curl: {output_path}")
            return
        except subprocess.CalledProcessError as e:
            logger.warning(f"curl download failed: {e}, falling back to requests")
            pass  # Fall back to requests

    # Fall back to requests
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(output_path, "wb") as fp:
        for chunk in response.iter_content(chunk_size=10485760):  # 10 MiB
            if chunk:
                fp.write(chunk)

