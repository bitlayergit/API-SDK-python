# coding: utf-8

"""
    Phone.com API

    This is a Phone.com api Swagger definition

    OpenAPI spec version: 1.0.0
    Contact: apisupport@phone.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.applications_api import ApplicationsApi


class TestApplicationsApi(unittest.TestCase):
    """ ApplicationsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.applications_api.ApplicationsApi()

    def tearDown(self):
        pass

    def test_get_account_application(self):
        """
        Test case for get_account_application

        Show details of an individual Application on a given account.
        """
        pass

    def test_list_account_applications(self):
        """
        Test case for list_account_applications

        This service lists the Applications on a given account
        """
        pass


if __name__ == '__main__':
    unittest.main()
