# coding: utf-8

"""
    Tator REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import tator
from api.token_api import TokenApi  # noqa: E501
from tator.rest import ApiException


class TestTokenApi(unittest.TestCase):
    """TokenApi unit test stubs"""

    def setUp(self):
        self.api = api.token_api.TokenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_obtain_auth_token(self):
        """Test case for create_obtain_auth_token

        """
        pass


if __name__ == '__main__':
    unittest.main()
