from .api_object import APIObject

class ModelFactory:
    def __init__(self, schema: dict):
        self.schema = schema
        self._models = {}
        for component in schema.get("components", {}).get("schemas", {}).keys():
            self._models[component] = type(component, (APIObject,), {})

    def __getattr__(self, name: str):
        if name in self._models:
            return self._models[name]
        raise AttributeError(f"Model '{name}' not found in schema.")

    def _getObject(self, name: str):
        return self._models.get(name)
