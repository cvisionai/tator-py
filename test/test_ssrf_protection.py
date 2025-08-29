"""Test SSRF protection for server-side requests."""

import os
import pytest
import tator


# Helper to determine if SSRF protection should be tested
# Since we're setting SERVER_SIDE_REQUEST_ORIGINS in our test configurations,
# we expect these tests to pass unless explicitly disabled
def should_test_ssrf():
    """Check if SSRF protection tests should run."""
    # You could add logic here to skip tests in certain environments
    # For now, we always test since our test configs include the setting
    return True


def test_ssrf_protection_transcode(host, token, project):
    """Test that transcode endpoint blocks unauthorized origins."""
    api = tator.get_api(host, token)
    
    # Try to transcode from an unauthorized domain
    unauthorized_url = "https://evil-site.com/malicious-video.mp4"
    
    # Attempt to create a transcode with an unauthorized URL
    with pytest.raises(tator.exceptions.ApiException) as exc_info:
        api.transcode(
            project=project,
            transcode_spec={
                "type": -1,  # Auto-detect type
                "gid": "test_ssrf_gid",
                "uid": "test_ssrf_uid",
                "url": unauthorized_url,
                "name": "test_ssrf_video.mp4",
                "section": "SSRF Test",
            }
        )
    
    # Verify we get a 403 Forbidden response
    assert exc_info.value.status == 403
    assert "not from an allowed origin" in str(exc_info.value.body).lower() or \
           "not from an allowed origin" in str(exc_info.value.reason).lower()


def test_ssrf_protection_import_media(host, token, project, image_type):
    """Test that import media endpoint blocks unauthorized origins."""
    api = tator.get_api(host, token)
    
    # Try to import from an unauthorized domain
    unauthorized_url = "https://malicious-cdn.com/evil-image.jpg"
    
    # Attempt to import media with an unauthorized URL using the utility function
    with pytest.raises(tator.exceptions.ApiException) as exc_info:
        tator.util.import_media(api, image_type, unauthorized_url)
    
    # Verify we get a 403 Forbidden response
    assert exc_info.value.status == 403
    assert "not from an allowed origin" in str(exc_info.value.body).lower() or \
           "not from an allowed origin" in str(exc_info.value.reason).lower()


def test_ssrf_protection_temporary_file(host, token, project):
    """Test that temporary file endpoint blocks unauthorized origins."""
    api = tator.get_api(host, token)
    
    # Try to create a temporary file from an unauthorized domain
    unauthorized_url = "https://attacker-server.com/payload.txt"
    
    # Attempt to create a temporary file with an unauthorized URL
    with pytest.raises(tator.exceptions.ApiException) as exc_info:
        api.create_temporary_file(
            project=project,
            temporary_file_spec={
                "url": unauthorized_url,
                "name": "test_ssrf_file.txt",
                "lookup": "ssrf_test_lookup",
                "hours": 1,
            }
        )
    
    # Verify we get a 403 Forbidden response
    assert exc_info.value.status == 403
    assert "not from an allowed origin" in str(exc_info.value.body).lower() or \
           "not from an allowed origin" in str(exc_info.value.reason).lower()


def test_ssrf_protection_hosted_template(host, token, organization):
    """Test that hosted template endpoint blocks unauthorized origins."""
    api = tator.get_api(host, token)
    
    # Try to create a hosted template from an unauthorized domain
    unauthorized_url = "https://evil-templates.com/malicious.yaml"
    
    # Attempt to create a hosted template with an unauthorized URL
    with pytest.raises(tator.exceptions.ApiException) as exc_info:
        api.create_hosted_template(
            organization=organization,
            hosted_template_spec={
                "name": "SSRF Test Template",
                "url": unauthorized_url,
            }
        )
    
    # Verify we get a 403 Forbidden response
    assert exc_info.value.status == 403
    assert "not from an allowed origin" in str(exc_info.value.body).lower() or \
           "not from an allowed origin" in str(exc_info.value.reason).lower()


def test_ssrf_protection_allowed_origin(host, token, project, image_type):
    """Test that allowed origins still work."""
    api = tator.get_api(host, token)
    
    # Use an allowed test URL from our CI bucket
    allowed_url = "https://tator-ci.s3.us-east-1.amazonaws.com/trip-summary.png"
    
    # This should succeed without raising an exception
    response = api.import_media(
        project=project,
        import_media_spec={
            "type": image_type,
            "url": allowed_url,
            "name": "test_allowed_image.png",
            "section": "SSRF Test Allowed",
        }
    )
    
    # Verify the import was accepted (might still be processing)
    assert response.message is not None
    assert "import" in response.message.lower() or "started" in response.message.lower()