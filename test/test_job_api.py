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
from api.job_api import JobApi  # noqa: E501
from tator.rest import ApiException


class TestJobApi(unittest.TestCase):
    """JobApi unit test stubs"""

    def setUp(self):
        self.api = api.job_api.JobApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_job(self):
        """Test case for delete_job

        """
        pass

    def test_delete_job_group(self):
        """Test case for delete_job_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
