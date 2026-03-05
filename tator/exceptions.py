class OpenApiException(Exception):
    """Base exception for Tator API errors"""

class ApiException(OpenApiException):
    def __init__(self, status=None, reason=None, http_resp=None):
        self.status = status
        self.reason = reason
        self.body = http_resp.text if http_resp is not None else None
        self.headers = dict(http_resp.headers) if http_resp is not None else None
        msg = f"({status}) Reason: {reason}"
        if self.body:
            msg += f"\nBody: {self.body}"
        super().__init__(msg)

class ApiTypeError(OpenApiException, TypeError): ...
class ApiValueError(OpenApiException, ValueError): ...
class ApiKeyError(OpenApiException, KeyError): ...
