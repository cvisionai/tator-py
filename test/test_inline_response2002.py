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
from tator.models.inline_response2002 import InlineResponse2002  # noqa: E501
from tator.rest import ApiException

class TestInlineResponse2002(unittest.TestCase):
    """InlineResponse2002 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2002
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.inline_response2002.InlineResponse2002()  # noqa: E501
        if include_optional :
            return InlineResponse2002(
                next = 0
            )
        else :
            return InlineResponse2002(
        )

    def testInlineResponse2002(self):
        """Test InlineResponse2002"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
