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
from tator.models.localization_list_update import LocalizationListUpdate  # noqa: E501
from tator.rest import ApiException

class TestLocalizationListUpdate(unittest.TestCase):
    """LocalizationListUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LocalizationListUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.localization_list_update.LocalizationListUpdate()  # noqa: E501
        if include_optional :
            return LocalizationListUpdate(
                attributes = { }
            )
        else :
            return LocalizationListUpdate(
                attributes = { },
        )

    def testLocalizationListUpdate(self):
        """Test LocalizationListUpdate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
