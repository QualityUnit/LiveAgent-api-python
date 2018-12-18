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
from liveagent_api.api.tickets_api import TicketsApi  # noqa: E501
from liveagent_api.rest import ApiException


class TestTicketsApi(unittest.TestCase):
    """TicketsApi unit test stubs"""

    def setUp(self):
        self.api = liveagent_api.api.tickets_api.TicketsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_ticket(self):
        """Test case for create_ticket

        Create ticket  # noqa: E501
        """
        pass

    def test_delete_ticket(self):
        """Test case for delete_ticket

        Deletes ticket  # noqa: E501
        """
        pass

    def test_get_ticket(self):
        """Test case for get_ticket

        Gets ticket  # noqa: E501
        """
        pass

    def test_get_ticket_attribute(self):
        """Test case for get_ticket_attribute

        Gets ticket attribute  # noqa: E501
        """
        pass

    def test_get_ticket_history(self):
        """Test case for get_ticket_history

        Gets ticket  # noqa: E501
        """
        pass

    def test_get_ticket_history_0(self):
        """Test case for get_ticket_history_0

        Gets ticket history  # noqa: E501
        """
        pass

    def test_get_ticket_message_groups(self):
        """Test case for get_ticket_message_groups

        Gets ticket message groups and messages  # noqa: E501
        """
        pass

    def test_get_ticket_sla(self):
        """Test case for get_ticket_sla

        Gets ticket Sla  # noqa: E501
        """
        pass

    def test_get_tickets_list(self):
        """Test case for get_tickets_list

        Gets list of tickets  # noqa: E501
        """
        pass

    def test_set_ticket_attribute(self):
        """Test case for set_ticket_attribute

        Sets ticket attribute  # noqa: E501
        """
        pass

    def test_set_ticket_postpone(self):
        """Test case for set_ticket_postpone

        Sets postpone status to ticket  # noqa: E501
        """
        pass

    def test_update_ticket(self):
        """Test case for update_ticket

        Updates ticket  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
