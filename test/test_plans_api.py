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
from liveagent_api.api.plans_api import PlansApi  # noqa: E501
from liveagent_api.rest import ApiException


class TestPlansApi(unittest.TestCase):
    """PlansApi unit test stubs"""

    def setUp(self):
        self.api = liveagent_api.api.plans_api.PlansApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_device_department_plan(self):
        """Test case for get_device_department_plan

        Get device department plan  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()