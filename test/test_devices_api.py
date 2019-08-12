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
from liveagent_api.api.devices_api import DevicesApi  # noqa: E501
from liveagent_api.rest import ApiException


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self):
        self.api = liveagent_api.api.devices_api.DevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_device(self):
        """Test case for create_device

        Create new device  # noqa: E501
        """
        pass

    def test_create_device_department_plans(self):
        """Test case for create_device_department_plans

        Create device department plans  # noqa: E501
        """
        pass

    def test_delete_device(self):
        """Test case for delete_device

        Delete device  # noqa: E501
        """
        pass

    def test_delete_device_department(self):
        """Test case for delete_device_department

        Delete device department  # noqa: E501
        """
        pass

    def test_delete_device_department_plans(self):
        """Test case for delete_device_department_plans

        Delete device department plans  # noqa: E501
        """
        pass

    def test_delete_device_departments(self):
        """Test case for delete_device_departments

        Delete device departments  # noqa: E501
        """
        pass

    def test_get_device(self):
        """Test case for get_device

        Get device by id  # noqa: E501
        """
        pass

    def test_get_device_department(self):
        """Test case for get_device_department

        Get device department by id  # noqa: E501
        """
        pass

    def test_get_device_department_plan(self):
        """Test case for get_device_department_plan

        Get device department plan  # noqa: E501
        """
        pass

    def test_get_device_departments(self):
        """Test case for get_device_departments

        Get device departments  # noqa: E501
        """
        pass

    def test_get_device_departments_by_department_id(self):
        """Test case for get_device_departments_by_department_id

        Get device departments by department id  # noqa: E501
        """
        pass

    def test_get_devices_list(self):
        """Test case for get_devices_list

        Gets list of devices  # noqa: E501
        """
        pass

    def test_get_my_mobile_devices_list(self):
        """Test case for get_my_mobile_devices_list

        Gets list of current agent's mobile devices. Creates new one if there are no devices.  # noqa: E501
        """
        pass

    def test_update_device(self):
        """Test case for update_device

        Update device  # noqa: E501
        """
        pass

    def test_update_device_department(self):
        """Test case for update_device_department

        Update device department  # noqa: E501
        """
        pass

    def test_update_device_department_plan(self):
        """Test case for update_device_department_plan

        Update device department plan  # noqa: E501
        """
        pass

    def test_update_device_departments(self):
        """Test case for update_device_departments

        Update device departments  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
