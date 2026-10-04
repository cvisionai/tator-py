"""Offline download regression tests; servers and files are disposable."""

import base64
import importlib.util
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os
from pathlib import Path
import subprocess
import tempfile
import threading
import unittest
from unittest.mock import patch

# Load without importing the API client or starting a transcode job.
spec = importlib.util.spec_from_file_location(
    "transcode_download", Path(__file__).parents[1] / "tator/transcode/download.py"
)
download = importlib.util.module_from_spec(spec)
spec.loader.exec_module(download)


class DownloadTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.output = str(Path(self.temp.name) / "media.bin")
        self.seen = []
        seen = self.seen
        payload = b"media-content-for-download"
        self.payload = payload

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_GET(self):
                seen.append((self.path, self.headers.get("Authorization"), self.headers.get("Range")))
                if self.path == "/redirect":
                    self.send_response(302)
                    self.send_header("Location", f"http://127.0.0.1:{self.server.server_port}/media")
                    self.end_headers()
                    return
                if self.path == "/missing":
                    self.send_error(404)
                    return
                if self.path == "/retry" and sum(x[0] == "/retry" for x in seen) == 1:
                    self.send_response(503)
                    self.send_header("Content-Length", "0")
                    self.end_headers()
                    return
                offset = int(self.headers.get("Range", "bytes=0-").split("=")[1].split("-")[0])
                self.send_response(206 if offset else 200)
                if offset:
                    self.send_header("Content-Range", f"bytes {offset}-{len(payload)-1}/{len(payload)}")
                self.send_header("Content-Length", str(len(payload) - offset))
                self.end_headers()
                self.wfile.write(payload[offset:])

        self.server = ThreadingHTTPServer(("0.0.0.0", 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.stop_server)
        self.env = patch.dict(os.environ, {"NO_PROXY": "*", "no_proxy": "*"})
        self.env.start()
        self.addCleanup(self.env.stop)
        self.url = f"http://127.0.0.2:{self.server.server_port}"

    def stop_server(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    def test_cross_host_redirect_does_not_forward_credentials(self):
        url = self.url.replace("http://", "http://user:password@") + "/redirect"
        download.download_file(url, self.output)
        self.assertEqual(Path(self.output).read_bytes(), self.payload)
        self.assertEqual(self.seen[0][1], "Basic " + base64.b64encode(b"user:password").decode())
        self.assertIsNone(self.seen[-1][1])

    def test_transient_http_failure_is_retried(self):
        download.download_file(self.url + "/retry", self.output)
        self.assertEqual(Path(self.output).read_bytes(), self.payload)
        self.assertEqual([x[0] for x in self.seen], ["/retry", "/retry"])

    def test_literal_query_brackets_are_not_expanded(self):
        download.download_file(self.url + "/media?key=[1-2]", self.output)
        self.assertEqual(len(self.seen), 1)
        self.assertEqual(self.seen[0][0], "/media?key=[1-2]")
        self.assertEqual(Path(self.output).read_bytes(), self.payload)

    def test_partial_download_is_resumed(self):
        Path(self.output).write_bytes(self.payload[:5])
        download.download_file(self.url + "/media", self.output)
        self.assertEqual(Path(self.output).read_bytes(), self.payload)
        self.assertEqual(self.seen[0][2], "bytes=5-")

    def test_requests_fallback_downloads_when_curl_is_absent(self):
        with patch.object(download.shutil, "which", return_value=None):
            download.download_file(self.url + "/media", self.output)
        self.assertEqual(Path(self.output).read_bytes(), self.payload)

    def test_permanent_http_error_fails_both_downloaders(self):
        with self.assertRaises(download.requests.HTTPError):
            download.download_file(self.url + "/missing", self.output)
        self.assertEqual([x[0] for x in self.seen], ["/missing", "/missing"])


if __name__ == "__main__":
    unittest.main()
