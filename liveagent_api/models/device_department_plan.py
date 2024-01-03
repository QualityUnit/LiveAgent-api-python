# coding: utf-8

"""
    LiveAgent API

    This page contains complete API documentation for LiveAgent software. To display additional info and examples for specific API method, just click on the method name in the list below.<br/><br/>To be able to make API requests you need to generate an API key in your admin panel first. [See this article for detailed info.](https://support.liveagent.com/741982-API-key)<br/><br/>Additional info about more advanced agent, contact or ticket API filters can be found [in this article](https://support.liveagent.com/513528-APIv3-advanced-filter-examples).<br/><br/>If you have any question or doubts regarding this API, please do not hesitate to contact our support team.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from liveagent_api.configuration import Configuration


class DeviceDepartmentPlan(object):
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
        'device_id': 'float',
        'department_id': 'str',
        'plan_id_start': 'str',
        'plan_id_end': 'str',
        'day': 'float',
        'start': 'str',
        'end': 'str',
        'title': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'department_id': 'department_id',
        'plan_id_start': 'plan_id_start',
        'plan_id_end': 'plan_id_end',
        'day': 'day',
        'start': 'start',
        'end': 'end',
        'title': 'title'
    }

    def __init__(self, device_id=None, department_id=None, plan_id_start=None, plan_id_end=None, day=None, start=None, end=None, title=None, _configuration=None):  # noqa: E501
        """DeviceDepartmentPlan - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_id = None
        self._department_id = None
        self._plan_id_start = None
        self._plan_id_end = None
        self._day = None
        self._start = None
        self._end = None
        self._title = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if department_id is not None:
            self.department_id = department_id
        if plan_id_start is not None:
            self.plan_id_start = plan_id_start
        if plan_id_end is not None:
            self.plan_id_end = plan_id_end
        if day is not None:
            self.day = day
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if title is not None:
            self.title = title

    @property
    def device_id(self):
        """Gets the device_id of this DeviceDepartmentPlan.  # noqa: E501


        :return: The device_id of this DeviceDepartmentPlan.  # noqa: E501
        :rtype: float
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceDepartmentPlan.


        :param device_id: The device_id of this DeviceDepartmentPlan.  # noqa: E501
        :type: float
        """

        self._device_id = device_id

    @property
    def department_id(self):
        """Gets the department_id of this DeviceDepartmentPlan.  # noqa: E501


        :return: The department_id of this DeviceDepartmentPlan.  # noqa: E501
        :rtype: str
        """
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        """Sets the department_id of this DeviceDepartmentPlan.


        :param department_id: The department_id of this DeviceDepartmentPlan.  # noqa: E501
        :type: str
        """

        self._department_id = department_id

    @property
    def plan_id_start(self):
        """Gets the plan_id_start of this DeviceDepartmentPlan.  # noqa: E501


        :return: The plan_id_start of this DeviceDepartmentPlan.  # noqa: E501
        :rtype: str
        """
        return self._plan_id_start

    @plan_id_start.setter
    def plan_id_start(self, plan_id_start):
        """Sets the plan_id_start of this DeviceDepartmentPlan.


        :param plan_id_start: The plan_id_start of this DeviceDepartmentPlan.  # noqa: E501
        :type: str
        """

        self._plan_id_start = plan_id_start

    @property
    def plan_id_end(self):
        """Gets the plan_id_end of this DeviceDepartmentPlan.  # noqa: E501


        :return: The plan_id_end of this DeviceDepartmentPlan.  # noqa: E501
        :rtype: str
        """
        return self._plan_id_end

    @plan_id_end.setter
    def plan_id_end(self, plan_id_end):
        """Sets the plan_id_end of this DeviceDepartmentPlan.


        :param plan_id_end: The plan_id_end of this DeviceDepartmentPlan.  # noqa: E501
        :type: str
        """

        self._plan_id_end = plan_id_end

    @property
    def day(self):
        """Gets the day of this DeviceDepartmentPlan.  # noqa: E501


        :return: The day of this DeviceDepartmentPlan.  # noqa: E501
        :rtype: float
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this DeviceDepartmentPlan.


        :param day: The day of this DeviceDepartmentPlan.  # noqa: E501
        :type: float
        """

        self._day = day

    @property
    def start(self):
        """Gets the start of this DeviceDepartmentPlan.  # noqa: E501


        :return: The start of this DeviceDepartmentPlan.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this DeviceDepartmentPlan.


        :param start: The start of this DeviceDepartmentPlan.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this DeviceDepartmentPlan.  # noqa: E501


        :return: The end of this DeviceDepartmentPlan.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this DeviceDepartmentPlan.


        :param end: The end of this DeviceDepartmentPlan.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def title(self):
        """Gets the title of this DeviceDepartmentPlan.  # noqa: E501


        :return: The title of this DeviceDepartmentPlan.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DeviceDepartmentPlan.


        :param title: The title of this DeviceDepartmentPlan.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(DeviceDepartmentPlan, dict):
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
        if not isinstance(other, DeviceDepartmentPlan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceDepartmentPlan):
            return True

        return self.to_dict() != other.to_dict()
