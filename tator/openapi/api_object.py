class APIObject(dict):
    """Wraps a dict and allows attribute-style access with recursive wrapping."""

    # Subclasses created by ModelFactory will have these set:
    _schema_properties = None  # set of known property names
    _nested_refs = None        # dict of prop_name -> ref class name
    _schema_defaults = None    # dict of prop_name -> default value from schema
    _factory = None            # back-reference to ModelFactory

    def _wrap(self, item, value):
        """Wrap a value using schema info if available, otherwise generic wrap."""
        nested_refs = self.__class__._nested_refs
        factory = self.__class__._factory

        # If we know this property maps to a schema $ref, use the typed class
        if nested_refs and factory and item in nested_refs:
            ref_name = nested_refs[item]
            cls = factory._getObject(ref_name)
            if cls:
                if isinstance(value, dict):
                    return cls(value)
                if isinstance(value, list):
                    return [cls(v) if isinstance(v, dict) else v for v in value]

        # Fallback: generic wrapping
        if isinstance(value, dict):
            return APIObject(value)
        if isinstance(value, list):
            return [APIObject(v) if isinstance(v, dict) else v for v in value]
        return value

    def __getattr__(self, item):
        try:
            value = self[item]
        except KeyError:
            # Backward compat: the old generated models stored values with
            # underscore-prefixed private attrs (e.g. _audio) while the JSON
            # keys are unprefixed (audio).  Support both access patterns.
            if item.startswith('_') and not item.startswith('__'):
                stripped = item[1:]
                if stripped in self:
                    return self._wrap(stripped, self[stripped])
            # Return schema default if one exists for this property.
            defaults = self.__class__._schema_defaults
            if defaults and item in defaults:
                return defaults[item]
            # Return None for missing keys — matches generated model behavior
            # where unset fields default to None.
            return None
        return self._wrap(item, value)

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
