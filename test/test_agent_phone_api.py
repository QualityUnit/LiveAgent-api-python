# coding: utf-8

"""
    LiveAgent API

    This page contains complete API documentation for LiveAgent software. To display additional info and examples for specific API method, just click on the method name in the list below.<br/><br/>To be able to make API requests you need to generate an API key in your admin panel first. [See this article for detailed info.](https://support.liveagent.com/741982-API-key)<br/><br/>Additional info about more advanced agent, contact or ticket API filters can be found [in this article](https://support.liveagent.com/513528-APIv3-advanced-filter-examples).<br/><br/>If you have any question or doubts regarding this API, please do not hesitate to contact our support team.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import liveagent_api
from liveagent_api.api.agent_phone_api import AgentPhoneApi  # noqa: E501
from liveagent_api.rest import ApiException


class TestAgentPhoneApi(unittest.TestCase):
    """AgentPhoneApi unit test stubs"""

    def setUp(self):
        self.api = liveagent_api.api.agent_phone_api.AgentPhoneApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_agent_phone(self):
        """Test case for get_agent_phone

        Gets phone currently used by agent (use me as agentId for self)  # noqa: E501
        """
        pass

    def test_set_agent_phone(self):
        """Test case for set_agent_phone

        Sets phone currently used by agent (use me as agentId for self)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
