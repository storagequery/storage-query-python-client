# coding: utf-8

"""
    StorageQuery API

    This document describes all operations that can be executed on the StorageQuery API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import storagequery
from storagequery.api.sql_api import SQLApi  # noqa: E501
from storagequery.rest import ApiException


class TestSQLApi(unittest.TestCase):
    """SQLApi unit test stubs"""

    def setUp(self):
        self.api = storagequery.api.sql_api.SQLApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_run_sql_query(self):
        """Test case for run_sql_query

        """
        pass


if __name__ == '__main__':
    unittest.main()