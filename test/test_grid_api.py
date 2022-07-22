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
from liveagent_api.api.grid_api import GridApi  # noqa: E501
from liveagent_api.rest import ApiException


class TestGridApi(unittest.TestCase):
    """GridApi unit test stubs"""

    def setUp(self):
        self.api = liveagent_api.api.grid_api.GridApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_agents_grid_list(self):
        """Test case for get_agents_grid_list

        Gets list of agents for grid  # noqa: E501
        """
        pass

    def test_get_agents_grid_list_count(self):
        """Test case for get_agents_grid_list_count

        Gets count of agents for agents grid  # noqa: E501
        """
        pass

    def test_get_calls_sla_log_grid_list(self):
        """Test case for get_calls_sla_log_grid_list

        Gets list of call slas for grid  # noqa: E501
        """
        pass

    def test_get_calls_sla_log_grid_list_count(self):
        """Test case for get_calls_sla_log_grid_list_count

        Gets count of calls for tickets sla grid  # noqa: E501
        """
        pass

    def test_get_chats_grid_list(self):
        """Test case for get_chats_grid_list

        Gets list of chats for chats grid  # noqa: E501
        """
        pass

    def test_get_chats_grid_list_count(self):
        """Test case for get_chats_grid_list_count

        Gets count of chats for chats grid  # noqa: E501
        """
        pass

    def test_get_chats_sla_log_grid_list(self):
        """Test case for get_chats_sla_log_grid_list

        Gets list of chat slas for grid  # noqa: E501
        """
        pass

    def test_get_chats_sla_log_grid_list_count(self):
        """Test case for get_chats_sla_log_grid_list_count

        Gets count of chats for chats sla grid  # noqa: E501
        """
        pass

    def test_get_customer_groups_grid_list(self):
        """Test case for get_customer_groups_grid_list

        Gets list of customer groups for grid  # noqa: E501
        """
        pass

    def test_get_departmens_grid_list_count(self):
        """Test case for get_departmens_grid_list_count

        Gets count of departments for department grid  # noqa: E501
        """
        pass

    def test_get_departments_grid_list(self):
        """Test case for get_departments_grid_list

        Gets list of departments for grid  # noqa: E501
        """
        pass

    def test_get_event_logs_grid_list(self):
        """Test case for get_event_logs_grid_list

        Gets list of event logs for grid  # noqa: E501
        """
        pass

    def test_get_event_logs_grid_list_count(self):
        """Test case for get_event_logs_grid_list_count

        Gets count of logs for event logs grid  # noqa: E501
        """
        pass

    def test_get_invite_agents_grid_list(self):
        """Test case for get_invite_agents_grid_list

        Gets list of invite agents for grid  # noqa: E501
        """
        pass

    def test_get_languages_grid_list(self):
        """Test case for get_languages_grid_list

        Gets list of languages for grid  # noqa: E501
        """
        pass

    def test_get_languages_grid_list_count(self):
        """Test case for get_languages_grid_list_count

        Gets count of languages for languages grid  # noqa: E501
        """
        pass

    def test_get_plugind_grid_list(self):
        """Test case for get_plugind_grid_list

        Gets plugins  for grid  # noqa: E501
        """
        pass

    def test_get_tags_grid_list(self):
        """Test case for get_tags_grid_list

        Gets list of tags for grid  # noqa: E501
        """
        pass

    def test_get_tickets_grid_list(self):
        """Test case for get_tickets_grid_list

        Gets list of tickets for tickets grid  # noqa: E501
        """
        pass

    def test_get_tickets_grid_list_count(self):
        """Test case for get_tickets_grid_list_count

        Gets count of tickets for tickets grid  # noqa: E501
        """
        pass

    def test_get_tickets_sla_log_grid_list(self):
        """Test case for get_tickets_sla_log_grid_list

        Gets list of ticket slas for grid  # noqa: E501
        """
        pass

    def test_get_tickets_sla_log_grid_list_count(self):
        """Test case for get_tickets_sla_log_grid_list_count

        Gets count of tickets for tickets sla grid  # noqa: E501
        """
        pass

    def test_get_time_reports_grid_list(self):
        """Test case for get_time_reports_grid_list

        Gets list of reports for time reports grid  # noqa: E501
        """
        pass

    def test_get_time_reports_grid_list_count(self):
        """Test case for get_time_reports_grid_list_count

        Gets count of time reporst grid  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
