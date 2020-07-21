"""
Python Bindings and associated utilities for tator
online platform
"""

# import submodule to top-level first
import tator.openapi as openapi

# Shortcuts
from .util.get_api import get_api
from .util.get_parser import get_parser
from .util.download_media import download_media

from .version import __version__ as __version__

# Generated code imports to top-level
import tator.openapi.tator_openapi.models as models
import tator.openapi.tator_openapi.exceptions as exceptions
from tator.openapi.tator_openapi import TatorApi as api


# Finally import utility functions
import tator.util as util
