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


class _LazyModels:
    """Proxy for tator.models that works before and after get_api().

    Before get_api(): returns placeholder classes from the shared registry
    so that type annotations (e.g. ``-> tator.models.Foo``) and
    ``from tator.openapi.tator_openapi import Foo`` resolve without error.

    After get_api(): delegates to the real ModelFactory, which populates
    the same shared class objects with schema metadata.
    """

    def __init__(self):
        object.__setattr__(self, '_factory', None)

    def _set_factory(self, factory):
        object.__setattr__(self, '_factory', factory)

    def __getattr__(self, name):
        factory = object.__getattribute__(self, '_factory')
        if factory is not None:
            return getattr(factory, name)
        # Before get_api(): return a bare class from the shared registry
        # so type annotations and isinstance pre-checks don't crash.
        from .openapi.models import get_or_create_model_class
        return get_or_create_model_class(name)

    def __repr__(self):
        factory = object.__getattribute__(self, '_factory')
        if factory is not None:
            return repr(factory)
        return "<tator.models (not yet initialized — call tator.get_api() first)>"


models = _LazyModels()
