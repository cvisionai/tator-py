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
from tator.models.localization_spec_one_of1 import LocalizationSpecOneOf1  # noqa: E501
from tator.rest import ApiException

class TestLocalizationSpecOneOf1(unittest.TestCase):
    """LocalizationSpecOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LocalizationSpecOneOf1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.localization_spec_one_of1.LocalizationSpecOneOf1()  # noqa: E501
        if include_optional :
            return LocalizationSpecOneOf1(
                media_id = 56, 
                modified = True, 
                type = 56, 
                version = 56, 
                x0 = 0.0, 
                x1 = 0.0, 
                y0 = 0.0, 
                y1 = 0.0
            )
        else :
            return LocalizationSpecOneOf1(
                media_id = 56,
                type = 56,
                x0 = 0.0,
                x1 = 0.0,
                y0 = 0.0,
                y1 = 0.0,
        )

    def testLocalizationSpecOneOf1(self):
        """Test LocalizationSpecOneOf1"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
