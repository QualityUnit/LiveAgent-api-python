# coding: utf-8

"""
    LiveAgent API

    LiveAgent API  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import liveagent_api
from liveagent_api.api.api_api import ApiApi  # noqa: E501
from liveagent_api.rest import ApiException


class TestApiApi(unittest.TestCase):
    """ApiApi unit test stubs"""

    def setUp(self):
        self.api = liveagent_api.api.api_api.ApiApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_api_keys(self):
        """Test case for create_api_keys

        Creates api key  # noqa: E501
        """
        pass

    def test_delete_api_key(self):
        """Test case for delete_api_key

        Deletes api key  # noqa: E501
        """
        pass

    def test_generate_api_key(self):
        """Test case for generate_api_key

        Gets new api keys  # noqa: E501
        """
        pass

    def test_get_api_info(self):
        """Test case for get_api_info

        Gets api info  # noqa: E501
        """
        pass

    def test_get_api_key(self):
        """Test case for get_api_key

        Gets api keys  # noqa: E501
        """
        pass

    def test_get_api_keys(self):
        """Test case for get_api_keys

        Gets api keys  # noqa: E501
        """
        pass

    def test_get_api_privileges(self):
        """Test case for get_api_privileges

        Gets api privileges  # noqa: E501
        """
        pass

    def test_login(self):
        """Test case for login

        Creates or returns API key from login.  # noqa: E501
        """
        pass

    def test_update_api_key(self):
        """Test case for update_api_key

        Updates api key  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
