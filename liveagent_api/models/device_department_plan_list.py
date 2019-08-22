# coding: utf-8

"""
    LiveAgent API

    This page contains complete API documentation for LiveAgent software. To display additional info and examples for specific API method, just click on the method name in the list below.<br/><br/>To be able to make API requests you need to generate an API key in your admin panel first. [See this article for detailed info.](https://support.ladesk.com/741982-API-key)<br/><br/>Additional info about more advanced agent, contact or ticket API filters can be found [in this article](https://support.ladesk.com/513528-APIv3-advanced-filter-examples).<br/><br/>If you have any question or doubts regarding this API, please do not hesitate to contact our support team.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from liveagent_api.models.device_department_plan import DeviceDepartmentPlan  # noqa: F401,E501


class DeviceDepartmentPlanList(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'device_departments': 'list[DeviceDepartmentPlan]'
    }

    attribute_map = {
        'device_departments': 'DeviceDepartments'
    }

    def __init__(self, device_departments=None):  # noqa: E501
        """DeviceDepartmentPlanList - a model defined in Swagger"""  # noqa: E501

        self._device_departments = None
        self.discriminator = None

        if device_departments is not None:
            self.device_departments = device_departments

    @property
    def device_departments(self):
        """Gets the device_departments of this DeviceDepartmentPlanList.  # noqa: E501


        :return: The device_departments of this DeviceDepartmentPlanList.  # noqa: E501
        :rtype: list[DeviceDepartmentPlan]
        """
        return self._device_departments

    @device_departments.setter
    def device_departments(self, device_departments):
        """Sets the device_departments of this DeviceDepartmentPlanList.


        :param device_departments: The device_departments of this DeviceDepartmentPlanList.  # noqa: E501
        :type: list[DeviceDepartmentPlan]
        """

        self._device_departments = device_departments

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DeviceDepartmentPlanList, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceDepartmentPlanList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
