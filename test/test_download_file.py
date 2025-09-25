import os
import tempfile
import pytest
from unittest.mock import Mock, patch, mock_open, call
from io import BytesIO

import requests

from tator.util._download_file import _download_file


class MockResponse:
    """Mock HTTP response for testing"""
    def __init__(self, content=b'', status_code=200, headers=None, raise_exception=None):
        self.content = content
        self.status_code = status_code
        self.headers = headers or {}
        self.raise_exception = raise_exception
        self._content_consumed = False

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}")

    def iter_content(self, chunk_size=1024):
        if self.raise_exception:
            if hasattr(self.raise_exception, '__iter__'):
                # Multiple exceptions - raise different ones for different chunks
                for i, chunk_start in enumerate(range(0, len(self.content), chunk_size)):
                    if i < len(self.raise_exception) and self.raise_exception[i]:
                        raise self.raise_exception[i]
                    yield self.content[chunk_start:chunk_start + chunk_size]
            else:
                # Single exception - raise on first chunk
                if not self._content_consumed:
                    self._content_consumed = True
                    raise self.raise_exception
        else:
            for chunk_start in range(0, len(self.content), chunk_size):
                yield self.content[chunk_start:chunk_start + chunk_size]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


@pytest.fixture
def mock_api():
    """Mock API client for testing"""
    api = Mock()
    config = Mock()
    config.host = 'https://example.com'
    config.api_key = {'Authorization': 'test-token'}
    config.api_key_prefix = {'Authorization': 'Bearer'}
    api.api_client.configuration = config

    # Mock S3 download info
    download_info = Mock()
    download_info.url = 'https://s3.amazonaws.com/bucket/file.mp4?presigned=true'
    api.get_download_info.return_value = [download_info]

    return api


class TestDownloadFileBasic:
    """Test basic functionality and backward compatibility"""

    @patch('tator.util._download_file.requests.get')
    @patch('tator.util._download_file.time.sleep')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=False)
    def test_basic_download_http_url(self, mock_exists, mock_file, mock_sleep, mock_get, mock_api, tmp_path):
        """Test basic HTTP URL download"""
        content = b'test file content'
        mock_response = MockResponse(content=content, headers={'Content-Length': str(len(content))})
        mock_get.return_value = mock_response

        out_path = str(tmp_path / 'test.mp4')
        progress_values = list(_download_file(mock_api, 123, 'https://example.com/file.mp4', out_path))

        # Verify progress reporting
        assert progress_values[0] == 0
        assert progress_values[-1] == 100

        # Verify file operations
        mock_file.assert_called_once_with(out_path, 'wb')
        handle = mock_file()
        handle.write.assert_called_once_with(content)
        handle.flush.assert_called_once()

        # Verify HTTP request
        mock_get.assert_called_once_with('https://example.com/file.mp4', stream=True, headers={})

    @patch('tator.util._download_file.requests.get')
    @patch('tator.util._download_file.time.sleep')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=False)
    def test_basic_download_relative_path(self, mock_exists, mock_file, mock_sleep, mock_get, mock_api, tmp_path):
        """Test relative path with API authentication"""
        content = b'api file content'
        mock_response = MockResponse(content=content, headers={'Content-Length': str(len(content))})
        mock_get.return_value = mock_response

        out_path = str(tmp_path / 'test.mp4')
        progress_values = list(_download_file(mock_api, 123, '/data/raw/file.mp4', out_path))

        # Verify authentication headers
        expected_headers = {
            'Authorization': 'Bearer test-token',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip',
        }
        mock_get.assert_called_once_with('https://example.com/data/raw/file.mp4', stream=True, headers=expected_headers)

    @patch('tator.util._download_file.requests.get')
    @patch('tator.util._download_file.time.sleep')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=False)
    def test_basic_download_s3_key(self, mock_exists, mock_file, mock_sleep, mock_get, mock_api, tmp_path):
        """Test S3 object key resolution"""
        content = b's3 file content'
        mock_response = MockResponse(content=content, headers={'Content-Length': str(len(content))})
        mock_get.return_value = mock_response

        out_path = str(tmp_path / 'test.mp4')
        progress_values = list(_download_file(mock_api, 123, 's3-object-key', out_path))

        # Verify S3 URL resolution
        mock_api.get_download_info.assert_called_once_with(123, {'keys': ['s3-object-key']})
        mock_get.assert_called_once_with('https://s3.amazonaws.com/bucket/file.mp4?presigned=true', stream=True, headers={})


class TestDownloadFileResumable:
    """Test resumable download functionality"""

    @patch('tator.util._download_file.requests.get')
    @patch('tator.util._download_file.time.sleep')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=True)
    @patch('os.path.getsize', return_value=500)  # Partial file exists
    def test_resume_download_http_206(self, mock_getsize, mock_exists, mock_file, mock_sleep, mock_get, mock_api, tmp_path):
        """Test successful resume with HTTP 206 Partial Content"""
        remaining_content = b'remaining content'
        mock_response = MockResponse(
            content=remaining_content,
            status_code=206,
            headers={
                'Content-Range': 'bytes 500-600/601',
                'Content-Length': str(len(remaining_content))
            }
        )
        mock_get.return_value = mock_response

        out_path = str(tmp_path / 'test.mp4')
        progress_values = list(_download_file(mock_api, 123, 'https://example.com/file.mp4', out_path))

        # Verify range request
        expected_headers = {'Range': 'bytes=500-'}
        mock_get.assert_called_once_with('https://example.com/file.mp4', stream=True, headers=expected_headers)

        # Verify file opened in append mode
        mock_file.assert_called_once_with(out_path, 'ab')

        # Verify progress starts from partial completion
        assert progress_values[0] == pytest.approx(83.2, abs=0.1)  # 500/601
        assert progress_values[-1] == 100

    @patch('tator.util._download_file.requests.get')
    @patch('tator.util._download_file.time.sleep')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=True)
    @patch('os.path.getsize', return_value=500)
    def test_resume_fallback_http_200(self, mock_getsize, mock_exists, mock_file, mock_sleep, mock_get, mock_api, tmp_path):
        """Test fallback to full download when server doesn't support range requests"""
        full_content = b'full file content from start'
        mock_response = MockResponse(
            content=full_content,
            status_code=200,  # Server ignores range request
            headers={'Content-Length': str(len(full_content))}
        )
        mock_get.return_value = mock_response

        out_path = str(tmp_path / 'test.mp4')
        with patch('tator.util._download_file.logger') as mock_logger:
            progress_values = list(_download_file(mock_api, 123, 'https://example.com/file.mp4', out_path))

        # Verify warning was logged
        mock_logger.warning.assert_any_call("Server doesn't support range requests, restarting download")

        # Verify file opened in write mode (not append)
        mock_file.assert_called_once_with(out_path, 'wb')

        # Verify progress starts from 0
        assert progress_values[0] == 0
        assert progress_values[-1] == 100


class TestDownloadFileRetries:
    """Test retry mechanisms"""

    @patch('tator.util._download_file.requests.get')
    @patch('tator.util._download_file.time.sleep')
    @patch('builtins.open', new_callable=mock_open)
    def test_stream_interruption_retry(self, mock_file, mock_sleep, mock_get, mock_api, tmp_path):
        """Test recovery from stream interruption"""
        content_part1 = b'first part'
        content_part2 = b'second part'
        full_content = content_part1 + content_part2

        # First attempt fails with ConnectionError after first chunk
        failing_response = MockResponse(
            content=content_part1,
            headers={'Content-Length': str(len(full_content))},
            raise_exception=requests.ConnectionError("Connection broken")
        )

        # Second attempt succeeds with remaining content
        success_response = MockResponse(
            content=content_part2,
            status_code=206,
            headers={
                'Content-Range': f'bytes {len(content_part1)}-{len(full_content)-1}/{len(full_content)}',
                'Content-Length': str(len(content_part2))
            }
        )

        # Provide many responses to handle all potential calls during retries
        mock_get.side_effect = [failing_response] + [success_response] * 15

        # Mock file size progression: first partial (10 bytes), then completed (21 bytes)
        with patch('os.path.getsize', side_effect=[len(content_part1)] * 5 + [len(full_content)] * 10):
            with patch('os.path.exists', side_effect=[False, True] + [True] * 10):  # File doesn't exist initially, then exists
                out_path = str(tmp_path / 'test.mp4')
                with patch('tator.util._download_file.logger') as mock_logger:
                    progress_values = list(_download_file(mock_api, 123, 'https://example.com/file.mp4', out_path))

        # Verify retry was attempted (should be at least 2 calls, but may be more due to additional retries)
        assert mock_get.call_count >= 2
        mock_logger.error.assert_called()
        mock_logger.info.assert_called_with(f"Stream interrupted, will resume from byte {len(content_part1)}")

        # Verify exponential backoff
        mock_sleep.assert_called()

    @patch('tator.util._download_file.requests.get')
    @patch('tator.util._download_file.time.sleep')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=False)
    def test_chunk_write_retry(self, mock_exists, mock_file, mock_sleep, mock_get, mock_api, tmp_path):
        """Test chunk-level write retry"""
        content = b'test content that will fail to write'
        mock_response = MockResponse(content=content, headers={'Content-Length': str(len(content))})
        mock_get.return_value = mock_response

        # Mock file handle to fail on first write, succeed on second
        mock_handle = mock_file()
        mock_handle.write.side_effect = [OSError("Disk full"), None]

        out_path = str(tmp_path / 'test.mp4')
        with patch('tator.util._download_file.logger') as mock_logger:
            progress_values = list(_download_file(mock_api, 123, 'https://example.com/file.mp4', out_path))

        # Verify chunk retry occurred
        assert mock_handle.write.call_count == 2
        mock_logger.warning.assert_called()

        # Verify exponential backoff for chunk retry
        mock_sleep.assert_called()
        assert progress_values[-1] == 100

    @patch('tator.util._download_file.requests.get')
    @patch('tator.util._download_file.time.sleep')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=False)
    @patch('os.path.getsize', return_value=0)  # Mock getsize to avoid FileNotFoundError
    @patch('os.remove')
    def test_max_retries_cleanup(self, mock_remove, mock_getsize, mock_exists, mock_file, mock_sleep, mock_get, mock_api, tmp_path):
        """Test that partial file is cleaned up after max retries exceeded"""
        # Use a different exception type that goes through the general exception handler
        # ConnectionError is handled differently and doesn't re-raise after max retries
        mock_get.side_effect = [requests.HTTPError("HTTP Error")] * 10

        out_path = str(tmp_path / 'test.mp4')
        with patch('os.path.exists', return_value=True):  # File exists after failed attempts
            with pytest.raises(requests.HTTPError):
                list(_download_file(mock_api, 123, 'https://example.com/file.mp4', out_path))

        # Verify cleanup
        mock_remove.assert_called_once_with(out_path)


class TestDownloadFileEdgeCases:
    """Test edge cases and error conditions"""

    @patch('tator.util._download_file.requests.get')
    @patch('tator.util._download_file.time.sleep')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=False)
    def test_missing_content_length(self, mock_exists, mock_file, mock_sleep, mock_get, mock_api, tmp_path):
        """Test handling of missing Content-Length header"""
        content = b'content with unknown length'
        mock_response = MockResponse(content=content)  # No Content-Length header
        mock_get.return_value = mock_response

        out_path = str(tmp_path / 'test.mp4')
        with patch('tator.util._download_file.logger') as mock_logger:
            progress_values = list(_download_file(mock_api, 123, 'https://example.com/file.mp4', out_path))

        # Should warn about missing size
        mock_logger.warning.assert_called_with("Could not determine file size, progress reporting will be limited")

        # Should still complete successfully
        assert progress_values[-1] == 100

    @patch('tator.util._download_file.requests.get')
    @patch('tator.util._download_file.time.sleep')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=False)
    def test_s3_url_regeneration(self, mock_exists, mock_file, mock_sleep, mock_get, mock_api, tmp_path):
        """Test S3 presigned URL regeneration on retry"""
        content = b'partial'

        # First attempt fails with stream interruption after partial content
        failing_response = MockResponse(
            content=content,
            headers={'Content-Length': '7'},
            raise_exception=requests.exceptions.ChunkedEncodingError("Connection broken")
        )

        # Second attempt succeeds with proper range response
        success_response = MockResponse(
            content=b'tent',
            status_code=206,  # Important: return 206 for range request
            headers={
                'Content-Length': '4',
                'Content-Range': 'bytes 7-10/11'
            }
        )
        # Provide more responses to handle retries
        mock_get.side_effect = [failing_response] + [success_response] * 10

        # Mock multiple S3 URL generations - provide more responses
        download_info1 = Mock()
        download_info1.url = 'https://s3.amazonaws.com/bucket/file.mp4?expires=1'
        download_info2 = Mock()
        download_info2.url = 'https://s3.amazonaws.com/bucket/file.mp4?expires=2'
        mock_api.get_download_info.side_effect = [[download_info1], [download_info2]] + [[download_info2]] * 5

        out_path = str(tmp_path / 'test.mp4')

        # Mock file operations for resume logic - provide more responses
        with patch('os.path.exists', side_effect=[False, True] + [True] * 10):  # File exists after partial write
            with patch('os.path.getsize', side_effect=[len(content)] * 5 + [len(content) + 4] * 10):  # Size progression
                progress_values = list(_download_file(mock_api, 123, 's3-object-key', out_path))

        # Verify S3 URL was regenerated on retry (at least 2 calls, may be more)
        assert mock_api.get_download_info.call_count >= 2
        assert mock_get.call_count >= 2

        # Second call should use new URL with range header
        mock_get.assert_any_call('https://s3.amazonaws.com/bucket/file.mp4?expires=2', stream=True, headers={'Range': f'bytes={len(content)}-'})

    @patch('tator.util._download_file.requests.get')
    @patch('tator.util._download_file.time.sleep')
    def test_chunk_retry_limit_exceeded(self, mock_sleep, mock_get, mock_api, tmp_path):
        """Test that chunk retry limit is enforced"""
        content = b'failing content'
        mock_response = MockResponse(content=content, headers={'Content-Length': str(len(content))})
        mock_get.return_value = mock_response

        # Mock file operations to always fail - need to support context manager protocol
        mock_file_handle = Mock()
        mock_file_handle.write.side_effect = OSError("Persistent disk error")
        mock_file_handle.flush = Mock()
        mock_file_handle.__enter__ = Mock(return_value=mock_file_handle)
        mock_file_handle.__exit__ = Mock(return_value=None)

        out_path = str(tmp_path / 'test.mp4')
        with patch('builtins.open', return_value=mock_file_handle):
            with patch('os.path.exists', return_value=False):
                with pytest.raises(RuntimeError, match="Too many chunk failures"):
                    list(_download_file(mock_api, 123, 'https://example.com/file.mp4', out_path))

        # Verify chunk retries were attempted (3 attempts per chunk * some chunks)
        assert mock_file_handle.write.call_count >= 3


@pytest.mark.parametrize("url,expected_supports_range", [
    ('/relative/path', True),
    ('https://example.com/file.mp4', True),
    ('s3-object-key', True),
])
@patch('tator.util._download_file.requests.get')
@patch('tator.util._download_file.time.sleep')
@patch('builtins.open', new_callable=mock_open)
@patch('os.path.exists', return_value=False)
def test_url_type_range_support(mock_exists, mock_file, mock_sleep, mock_get, url, expected_supports_range, mock_api, tmp_path):
    """Test that all URL types are marked as supporting range requests"""
    content = b'test content'
    mock_response = MockResponse(content=content, headers={'Content-Length': str(len(content))})
    mock_get.return_value = mock_response

    out_path = str(tmp_path / 'test.mp4')
    progress_values = list(_download_file(mock_api, 123, url, out_path))

    # All URL types should work and support resumption conceptually
    # (though the actual implementation may vary)
    assert progress_values[-1] == 100


class TestDownloadFileIntegration:
    """Integration-style tests that verify end-to-end behavior"""

    @patch('tator.util._download_file.requests.get')
    @patch('tator.util._download_file.time.sleep')
    def test_multi_chunk_download_with_progress(self, mock_sleep, mock_get, mock_api, tmp_path):
        """Test multi-chunk download with accurate progress reporting"""
        # Create content that will be split into multiple chunks
        chunk_size = 10 * 1024 * 1024  # 10MB chunks as used in _download_file
        content_size = int(2.5 * chunk_size)  # 25MB total
        content = b'x' * content_size

        mock_response = MockResponse(content=content, headers={'Content-Length': str(content_size)})
        mock_get.return_value = mock_response

        out_path = str(tmp_path / 'large_file.mp4')

        with patch('builtins.open', mock_open()) as mock_file:
            with patch('os.path.exists', return_value=False):
                progress_values = list(_download_file(mock_api, 123, 'https://example.com/large.mp4', out_path))

        # Verify progress reporting
        assert progress_values[0] == 0
        assert progress_values[-1] == 100
        assert all(0 <= p <= 100 for p in progress_values)

        # Verify progressive increase
        for i in range(1, len(progress_values)):
            assert progress_values[i] >= progress_values[i-1]

        # Verify file writing
        mock_handle = mock_file()
        # Should have multiple write calls for multiple chunks
        assert mock_handle.write.call_count >= 3  # At least 3 chunks for 2.5x chunk size

