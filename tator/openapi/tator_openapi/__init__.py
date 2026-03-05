# Backward-compatibility shim — the generated package is gone;
# re-export the pieces that external code may still reference.
from . import exceptions


def __getattr__(name):
    """Allow ``from tator.openapi.tator_openapi import SomeModel`` to work.

    Delegates to the shared model registry so the returned class is the
    same object used by the API client at runtime.
    """
    import tator
    return getattr(tator.models, name)
