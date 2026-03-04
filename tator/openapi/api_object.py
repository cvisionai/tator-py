class APIObject(dict):
    """Wraps a dict and allows attribute-style access with recursive wrapping."""

    def __getattr__(self, item):
        try:
            value = self[item]
            if isinstance(value, dict):
                return APIObject(value)
            if isinstance(value, list):
                return [APIObject(v) if isinstance(v, dict) else v for v in value]
            return value
        except KeyError as exc:
            raise AttributeError(f"{item} not found") from exc

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def to_dict(self):
        """Recursively convert APIObject (and any nested APIObjects) to a plain dict."""
        def convert(obj):
            if isinstance(obj, APIObject):
                return {k: convert(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert(v) for v in obj]
            else:
                return obj
        return convert(self)
