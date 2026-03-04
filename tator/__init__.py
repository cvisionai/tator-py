"""
Python Bindings and associated utilities for tator
online platform
"""

from .openapi.client import OpenAPIClient, get_api
from .openapi.api_object import APIObject
from .openapi.models import ModelFactory
from .version import __version__
from . import exceptions
import tator.util as util

# Shortcuts
from .util.get_parser import get_parser
from .util.download_media import download_media

# Backward compat: tator.api points to OpenAPIClient class
api = OpenAPIClient

# tator.models is set dynamically when get_api() is called
# (ModelFactory instance attached to module)
models = None
