from .client import OpenAPIClient, get_api
from .api_object import APIObject
from .models import ModelFactory


def __getattr__(name):
    """Lazy-load tator_openapi subpackage to avoid circular import."""
    if name == "tator_openapi":
        from . import tator_openapi as _mod
        return _mod
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
