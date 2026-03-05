import inspect
import os
import re
import requests
import yaml
from textwrap import dedent
from types import FunctionType
from typing import Any, Optional
import tempfile
from .api_object import APIObject
from .models import ModelFactory
from ..exceptions import ApiException

import logging

logger = logging.getLogger(__name__)

def pythonify_operation_id(op_id: str) -> str:
    """Convert a CamelCase or PascalCase operationId to snake_case.

    Examples:
    - GetMediaList -> get_media_list
    - CreateFooBar -> create_foo_bar
    """
    words = re.findall(r"[A-Z][a-z0-9]*", op_id)
    return "_".join(w.lower() for w in words) if words else op_id.lower()

class _Configuration:
    """Backward-compatible shim for code that accesses api.api_client.configuration."""

    def __init__(self, client):
        self._client = client

    @property
    def host(self):
        return self._client.base_url

    @property
    def api_key(self):
        auth = self._client.session.headers.get("Authorization", "")
        # "Token <value>" -> extract <value>
        parts = auth.split(" ", 1)
        token = parts[1] if len(parts) == 2 else auth
        return {"Authorization": token}

    @property
    def api_key_prefix(self):
        auth = self._client.session.headers.get("Authorization", "")
        parts = auth.split(" ", 1)
        prefix = parts[0] if len(parts) == 2 else ""
        return {"Authorization": prefix}


class _ApiClientShim:
    """Backward-compatible shim for code that accesses api.api_client."""

    def __init__(self, client):
        self.configuration = _Configuration(client)


# Module-level cache: parsed schema + derived data keyed by schema URL.
# Avoids re-downloading and re-parsing the ~1 MB YAML on every get_api() call.
_schema_cache = {}


class OpenAPIClient:
    def __init__(self, schema_url: str, base_url: str):
        if schema_url in _schema_cache:
            cached = _schema_cache[schema_url]
            self.schema = cached["schema"]
            self._endpoints = cached["endpoints"]
            self._factory = cached["factory"]
        else:
            resp = requests.get(schema_url)
            resp.raise_for_status()
            self.schema = yaml.safe_load(resp.text) or {}
            self._endpoints = self._parse_schema()
            self._factory = ModelFactory(self.schema)
            _schema_cache[schema_url] = {
                "schema": self.schema,
                "endpoints": self._endpoints,
                "factory": self._factory,
            }
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self._cache = {}
        self._debug = False
        self.api_client = _ApiClientShim(self)

    def _parse_schema(self):
        endpoints = {}
        for path, path_item in (self.schema.get("paths") or {}).items():
            for method, operation in path_item.items():
                op_id = operation.get("operationId")
                if not op_id:
                    continue
                func_name = pythonify_operation_id(op_id)
                path_params = re.findall(r"{([^}]+)}", path)

                query_params = []
                for param in operation.get("parameters", []):
                    if param.get("in") == "query":
                        query_params.append(param)

                body_param = None
                rb = operation.get("requestBody")
                if rb:
                    content = rb.get("content", {})
                    if content:
                        media_type, media_spec = next(iter(content.items()))
                        schema_ref = (media_spec.get("schema") or {}).get("$ref")
                        if schema_ref:
                            body_param = pythonify_operation_id(schema_ref.split("/")[-1])
                        else:
                            body_param = "body"
                    else:
                        body_param = "body"

                endpoints[func_name] = {
                    "method": method.upper(),
                    "path": path,
                    "path_params": path_params,
                    "query_params": query_params,
                    "body_param": body_param,
                    "description": operation.get("description", ""),
                    "responses": operation.get("responses", {}),
                }
        return endpoints

    def _resolve_oneof(self, oneof_list, obj):
        """Pick the best matching class from a oneOf list based on response keys."""
        schemas = self.schema.get("components", {}).get("schemas", {})
        if isinstance(obj, dict):
            obj_keys = set(obj.keys())
            for option in oneof_list:
                ref = option.get("$ref", "")
                if not ref:
                    continue
                class_name = ref.split("/")[-1]
                schema_def = schemas.get(class_name, {})
                required = set(schema_def.get("required", []))
                # Match if all required fields are present in the response
                if required and required.issubset(obj_keys):
                    cls = self._factory._getObject(class_name)
                    if cls:
                        return cls
            # Fallback: return the first ref class
            for option in oneof_list:
                ref = option.get("$ref", "")
                if ref:
                    cls = self._factory._getObject(ref.split("/")[-1])
                    if cls:
                        return cls
        return APIObject

    def __getattr__(self, name):
        if name not in self._endpoints:
            raise AttributeError(f"No such API operation: {name}")
        if name in self._cache:
            return self._cache[name]

        endpoint = self._endpoints[name]

        parameters = [
            inspect.Parameter(p, inspect.Parameter.POSITIONAL_OR_KEYWORD)
            for p in endpoint["path_params"]
        ]

        if endpoint["body_param"]:
            parameters.append(
                inspect.Parameter(
                    endpoint["body_param"], inspect.Parameter.POSITIONAL_OR_KEYWORD
                )
            )

        for qp in endpoint["query_params"]:
            annotated_type = f"Optional[{(qp.get('schema') or {}).get('type', 'Any')}]"
            parameters.append(
                inspect.Parameter(
                    qp["name"],
                    inspect.Parameter.POSITIONAL_OR_KEYWORD,
                    annotation=annotated_type,
                )
            )

        sig = inspect.Signature(parameters)

        def _impl(*args, **kwargs):
            path = endpoint["path"]
            n_path = len(endpoint["path_params"])
            # Consume positional args: first N are path params, next is body
            for arg_name, arg_value in zip(endpoint["path_params"], args):
                path = path.replace(f"{{{arg_name}}}", str(arg_value))
            remaining_args = args[n_path:]
            # Also handle path params passed as kwargs
            for param_name in endpoint["path_params"]:
                if param_name in kwargs:
                    path = path.replace(f"{{{param_name}}}", str(kwargs.pop(param_name)))

            query = {
                qp["name"]: kwargs.pop(qp["name"], None)
                for qp in endpoint["query_params"]
                if qp["name"] in kwargs
            }

            # Support a "format" kwarg
            if kwargs.get("format", None):
                query["format"] = kwargs.pop("format")

            # Strip legacy kwargs from the old generated client
            kwargs.pop("_request_timeout", None)

            # Verify all kwargs are part of the schema for this endpoint
            for key, value in kwargs.items():
                if key not in query and key != endpoint["body_param"] and key not in endpoint["path_params"]:
                    raise TypeError(f"Got an unexpected keyword argument '{key}' {value} {endpoint['body_param']}")

            for key, value in list(query.items()):
                if value is None:
                    del query[key]
                elif type(value) is list:
                    query[key] = ",".join(str(v) for v in value)

            body = None
            if endpoint["body_param"]:
                # Body can come from remaining positional args or kwargs
                if remaining_args:
                    body = remaining_args[0]
                else:
                    body = kwargs.pop(endpoint["body_param"], None)

            is_streaming = query.get("format", "json") == "jsonl"

            url = f"{self.base_url}{path}"

            try:
                if is_streaming:
                    resp = self.session.get(url, params=query, json=body, stream=True)
                else:
                    resp = self.session.request(
                        endpoint["method"], url, params=query, json=body
                    )
                if self._debug:
                    logger.debug("Request URL: %s", url)
                    logger.debug("Request body: %s", body)
                    logger.debug("Query params: %s", query)
                    logger.debug("Response headers: %s", resp.headers)
                    logger.debug("Response status code: %s", resp.status_code)

                resp.raise_for_status()
            except requests.exceptions.HTTPError as exc:
                raise ApiException(
                    status=exc.response.status_code,
                    reason=str(exc),
                    http_resp=exc.response,
                ) from exc

            if is_streaming:
                # Return a generator that parses each line of the JSONL response
                def generator():
                    for line in resp.iter_lines():
                        if line:
                            yield APIObject(yaml.safe_load(line))
                return generator()

            if resp.headers.get("content-type", "").startswith("application/json"):
                obj = resp.json()
            elif resp.headers.get("content-type", "").startswith("video/") or \
               resp.headers.get("content-type", "").startswith("image/"):
                # make a temporary file and return its path
                suffix = ""
                if "content-type" in resp.headers:
                    suffix = "." + resp.headers["content-type"].split("/")[-1].split(";")[0]
                tf = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
                tf.write(resp.content)
                return tf.name
            else:
                return resp.content

            response_code = str(resp.status_code)
            if response_code not in endpoint["responses"]:
                logger.warning(f"Response code {response_code} not documented in schema for {name}")

            # Lookup the response class from the schema
            response_class = endpoint["responses"].get(response_code, {}).get("content", {}).get("application/json", {}).get("schema", {})
            if "$ref" in response_class:
                class_name = response_class["$ref"].split("/")[-1]
                class_constructor = self._factory._getObject(class_name) or APIObject
            elif response_class.get("type") == "array" and "$ref" in response_class.get("items", {}):
                class_name = response_class["items"]["$ref"].split("/")[-1]
                class_constructor = self._factory._getObject(class_name) or APIObject
            elif "oneOf" in response_class:
                class_constructor = self._resolve_oneof(response_class["oneOf"], obj)
            else:
                class_constructor = APIObject

            if isinstance(obj, list):
                return [class_constructor(item) if isinstance(item, dict) else item for item in obj]
            elif isinstance(obj, dict):
                return class_constructor(obj)
            else:
                return obj

        func = FunctionType(_impl.__code__, globals(), name, (), _impl.__closure__)

        func.__doc__ = dedent(
            f"""{endpoint.get('description', '')}

            Method: {endpoint['method']}
            Path: {endpoint['path']}
            Path parameters: {', '.join(endpoint['path_params']) or 'None'}
            Query parameters: {', '.join(qp['name'] for qp in endpoint['query_params']) or 'None'}
            Body parameter: {endpoint['body_param'] or 'None'}
            """
        )
        func.__signature__ = sig
        self._cache[name] = func
        return func

    def __dir__(self):
        return sorted(set(super().__dir__()) | set(self._endpoints.keys()))

def get_api(host: str, token: Optional[str] = None) -> OpenAPIClient:
    """Helper to create an authenticated API client for a given host.

    The host should be the base URL to the API (e.g. https://cloud.tator.io).
    This function expects the OpenAPI schema to be available at {host}/schema.
    """
    if token is None:
        token = os.getenv('TATOR_TOKEN')
    client = OpenAPIClient(f"{host}/schema", host)
    if token:
        client.session.headers.update({"Authorization": f"Token {token}"})
    # Set module-level models
    import tator
    tator.models._set_factory(client._factory)
    return client
