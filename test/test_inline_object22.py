# coding: utf-8

"""
    Tator REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import tator
from tator.models.inline_object22 import InlineObject22  # noqa: E501
from tator.rest import ApiException

class TestInlineObject22(unittest.TestCase):
    """InlineObject22 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject22
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.inline_object22.InlineObject22()  # noqa: E501
        if include_optional :
            return InlineObject22(
                description = '0', 
                name = '0'
            )
        else :
            return InlineObject22(
                name = '0',
        )

    def testInlineObject22(self):
        """Test InlineObject22"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
