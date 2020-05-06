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
from tator.models.inline_response200 import InlineResponse200  # noqa: E501
from tator.rest import ApiException

class TestInlineResponse200(unittest.TestCase):
    """InlineResponse200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse200
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.inline_response200.InlineResponse200()  # noqa: E501
        if include_optional :
            return InlineResponse200(
                columns = [
                    null
                    ], 
                type = tator.models.inline_response_200_type.inline_response_200_type(
                    color_map = { }, 
                    description = '0', 
                    dtype = 'box', 
                    id = 56, 
                    line_width = 1, 
                    name = '0', 
                    resourcetype = 'EntityTypeLocalizationBox', )
            )
        else :
            return InlineResponse200(
        )

    def testInlineResponse200(self):
        """Test InlineResponse200"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
