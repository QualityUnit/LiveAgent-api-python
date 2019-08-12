# coding: utf-8

"""
    LiveAgent API

    This page contains complete API documentation for LiveAgent software. To display additional info and examples for specific API method, just click on the method name in the list below.<br/><br/>To be able to make API requests you need to generate an API key in your admin panel first. [See this article for detailed info.](https://support.ladesk.com/741982-API-key)<br/><br/>Additional info about more advanced agent, contact or ticket API filters can be found [in this article](https://support.ladesk.com/513528-APIv3-advanced-filter-examples).<br/><br/>If you have any question or doubts regarding this API, please do not hesitate to contact our support team.  # noqa: E501

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
