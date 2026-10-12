"""Offline tests for the schema-generated Python API. No automatic retries."""
import inspect
import unittest
from unittest.mock import Mock
import requests

from tator.openapi.client import OpenAPIClient
from tator.openapi.models import ModelFactory


class HeaderParametersTest(unittest.TestCase):
    def client(self):
        client = OpenAPIClient.__new__(OpenAPIClient)
        client.schema = {"paths": {
            "/rest/States/{project}": {"post": {
                "operationId": "CreateStateList",
                "parameters": [{"name": "Idempotency-Key", "in": "header", "required": False, "schema": {"type": "string"}}],
                "requestBody": {"content": {"application/json": {"schema": {"type": "array"}}}},
                "responses": {"201": {}},
            }},
            "/rest/Jobs/{project}": {"post": {"operationId": "CreateJobList",
                "parameters": [{"name": "Idempotency-Key", "in": "header", "required": False, "schema": {"type": "string"}}],
                "requestBody": {"content": {"application/json": {"schema": {"type": "object"}}}},
                "responses": {"201": {}}}},
            "/rest/Email/{project}": {"post": {"operationId": "CreateEmail", "responses": {"201": {}}}},
        }}
        client._endpoints = client._parse_schema()
        client._factory = ModelFactory(client.schema)
        client._cache = {}
        client._debug = False
        client.base_url = "https://tator.test"
        response = requests.Response()
        response.status_code = 201
        response.headers['Content-Type'] = 'application/json'
        response._content = b'{"id":[1]}'
        client.session = Mock()
        client.session.request.return_value = response
        return client

    def test_optional_key_is_keyword_only_and_sent_in_header(self):
        client = self.client()
        parameter = inspect.signature(client.create_state_list).parameters['idempotency_key']
        self.assertEqual(parameter.kind, inspect.Parameter.KEYWORD_ONLY)
        self.assertIsNone(parameter.default)
        self.assertEqual(client.create_state_list(1, [], idempotency_key='operation')['id'], [1])
        self.assertEqual(client.session.request.call_args.kwargs['headers'], {'Idempotency-Key': 'operation'})
        self.assertNotIn('idempotency_key', client.session.request.call_args.kwargs['params'])
        client.create_state_list(1, [])
        self.assertEqual(client.session.request.call_args.kwargs['headers'], {})

    def test_jobs_key_is_optional_and_no_automatic_retry_is_added(self):
        client = self.client()
        client.create_job_list(1, {'algorithm_name':'algorithm', 'media_ids':[1]}, idempotency_key='job')
        self.assertEqual(client.session.request.call_args.kwargs['headers'], {'Idempotency-Key':'job'})
        client.create_job_list(1, {})
        self.assertEqual(client.session.request.call_args.kwargs['headers'], {})

    def test_unsupported_operation_rejects_key(self):
        with self.assertRaises(TypeError):
            self.client().create_email(1, idempotency_key='operation')

    def test_transport_failure_is_not_automatically_retried(self):
        client = self.client()
        client.session.request.side_effect = requests.ConnectionError('lost response')
        with self.assertRaises(requests.ConnectionError):
            client.create_state_list(1, [], idempotency_key='operation')
        self.assertEqual(client.session.request.call_count, 1)


if __name__ == '__main__':
    unittest.main()
