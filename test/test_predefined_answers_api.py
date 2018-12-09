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
from liveagent_api.api.predefined_answers_api import PredefinedAnswersApi  # noqa: E501
from liveagent_api.rest import ApiException


class TestPredefinedAnswersApi(unittest.TestCase):
    """PredefinedAnswersApi unit test stubs"""

    def setUp(self):
        self.api = liveagent_api.api.predefined_answers_api.PredefinedAnswersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_predefined_answer(self):
        """Test case for create_predefined_answer

        Create predefined answer  # noqa: E501
        """
        pass

    def test_delete_predefined_answer(self):
        """Test case for delete_predefined_answer

        Predefined answer  # noqa: E501
        """
        pass

    def test_get_predefined_answer(self):
        """Test case for get_predefined_answer

        Gets canned message  # noqa: E501
        """
        pass

    def test_get_predefined_answers_list(self):
        """Test case for get_predefined_answers_list

        Gets list of predefined answers  # noqa: E501
        """
        pass

    def test_update_predefined_answer(self):
        """Test case for update_predefined_answer

        Update predefined answer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()