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
from liveagent_api.api.slas_api import SlasApi  # noqa: E501
from liveagent_api.rest import ApiException


class TestSlasApi(unittest.TestCase):
    """SlasApi unit test stubs"""

    def setUp(self):
        self.api = liveagent_api.api.slas_api.SlasApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_sla(self):
        """Test case for get_sla

        Gets sla  # noqa: E501
        """
        pass

    def test_get_sla_ticket_history(self):
        """Test case for get_sla_ticket_history

        Gets ticket sla history  # noqa: E501
        """
        pass

    def test_get_slas_list(self):
        """Test case for get_slas_list

        Gets list of slas  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
