from .api_object import APIObject


def _resolve_ref(ref, schemas):
    """Resolve a $ref string like '#/components/schemas/Foo' to its schema dict."""
    if ref and ref.startswith("#/components/schemas/"):
        return ref.split("/")[-1]
    return None


# Global registry of model classes. Shared across all ModelFactory instances
# and import-time lookups so that isinstance() checks always use the same
# class objects.
_model_registry = {}


def get_or_create_model_class(name):
    """Return the model class for *name*, creating a bare one if needed.

    This guarantees that ``from tator.openapi.tator_openapi import Foo``
    at import time returns the exact same class object that ModelFactory
    later populates with schema metadata.
    """
    if name not in _model_registry:
        _model_registry[name] = type(name, (APIObject,), {
            "_schema_properties": None,
            "_nested_refs": None,
            "_factory": None,
        })
    return _model_registry[name]


class ModelFactory:
    def __init__(self, schema: dict):
        self.schema = schema
        self._schemas = schema.get("components", {}).get("schemas", {})
        self._models = {}
        # Create / update all model classes up front
        for name in self._schemas:
            self._models[name] = self._make_model_class(name)

    def _make_model_class(self, name):
        """Create (or update) a model class with schema properties and nested refs."""
        schema_def = self._schemas.get(name, {})
        props = schema_def.get("properties", {})

        # Build a map of property_name -> ref class name for nested objects
        # and collect schema defaults
        nested_refs = {}
        defaults = {}
        for prop_name, prop_def in props.items():
            ref = prop_def.get("$ref")
            if ref:
                nested_refs[prop_name] = _resolve_ref(ref, self._schemas)
            # Also handle array items with $ref
            items = prop_def.get("items", {})
            if isinstance(items, dict) and "$ref" in items:
                nested_refs[prop_name] = _resolve_ref(items["$ref"], self._schemas)
            # Collect schema defaults
            if "default" in prop_def:
                defaults[prop_name] = prop_def["default"]

        # Get-or-create from the global registry, then update in-place
        cls = get_or_create_model_class(name)
        cls._schema_properties = set(props.keys())
        cls._nested_refs = nested_refs
        cls._schema_defaults = defaults
        cls._factory = self
        return cls

    def __getattr__(self, name: str):
        if name in self._models:
            return self._models[name]
        raise AttributeError(f"Model '{name}' not found in schema.")

    def _getObject(self, name: str):
        return self._models.get(name)
