class OpenApiException(Exception):
    """Base exception for Tator API errors"""

class ApiException(OpenApiException):
    def __init__(self, status=None, reason=None, http_resp=None):
        self.status = status
        self.reason = reason
        self.body = http_resp.text if http_resp else None
        self.headers = dict(http_resp.headers) if http_resp else None
        super().__init__(f"({status}) Reason: {reason}")

class ApiTypeError(OpenApiException, TypeError): ...
class ApiValueError(OpenApiException, ValueError): ...
class ApiKeyError(OpenApiException, KeyError): ...
