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
from api.notify_api import NotifyApi  # noqa: E501
from tator.rest import ApiException


class TestNotifyApi(unittest.TestCase):
    """NotifyApi unit test stubs"""

    def setUp(self):
        self.api = api.notify_api.NotifyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_notify(self):
        """Test case for notify

        """
        pass


if __name__ == '__main__':
    unittest.main()
