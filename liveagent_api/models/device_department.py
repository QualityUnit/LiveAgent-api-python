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


class DeviceDepartment(object):
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
        'user_id': 'str',
        'department_name': 'str',
        'online_status': 'str',
        'preset_status': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'department_id': 'department_id',
        'user_id': 'user_id',
        'department_name': 'department_name',
        'online_status': 'online_status',
        'preset_status': 'preset_status'
    }

    def __init__(self, device_id=None, department_id=None, user_id=None, department_name=None, online_status=None, preset_status=None):  # noqa: E501
        """DeviceDepartment - a model defined in Swagger"""  # noqa: E501

        self._device_id = None
        self._department_id = None
        self._user_id = None
        self._department_name = None
        self._online_status = None
        self._preset_status = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if department_id is not None:
            self.department_id = department_id
        if user_id is not None:
            self.user_id = user_id
        if department_name is not None:
            self.department_name = department_name
        if online_status is not None:
            self.online_status = online_status
        if preset_status is not None:
            self.preset_status = preset_status

    @property
    def device_id(self):
        """Gets the device_id of this DeviceDepartment.  # noqa: E501


        :return: The device_id of this DeviceDepartment.  # noqa: E501
        :rtype: float
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceDepartment.


        :param device_id: The device_id of this DeviceDepartment.  # noqa: E501
        :type: float
        """

        self._device_id = device_id

    @property
    def department_id(self):
        """Gets the department_id of this DeviceDepartment.  # noqa: E501


        :return: The department_id of this DeviceDepartment.  # noqa: E501
        :rtype: str
        """
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        """Sets the department_id of this DeviceDepartment.


        :param department_id: The department_id of this DeviceDepartment.  # noqa: E501
        :type: str
        """

        self._department_id = department_id

    @property
    def user_id(self):
        """Gets the user_id of this DeviceDepartment.  # noqa: E501


        :return: The user_id of this DeviceDepartment.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DeviceDepartment.


        :param user_id: The user_id of this DeviceDepartment.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def department_name(self):
        """Gets the department_name of this DeviceDepartment.  # noqa: E501


        :return: The department_name of this DeviceDepartment.  # noqa: E501
        :rtype: str
        """
        return self._department_name

    @department_name.setter
    def department_name(self, department_name):
        """Sets the department_name of this DeviceDepartment.


        :param department_name: The department_name of this DeviceDepartment.  # noqa: E501
        :type: str
        """

        self._department_name = department_name

    @property
    def online_status(self):
        """Gets the online_status of this DeviceDepartment.  # noqa: E501


        :return: The online_status of this DeviceDepartment.  # noqa: E501
        :rtype: str
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status):
        """Sets the online_status of this DeviceDepartment.


        :param online_status: The online_status of this DeviceDepartment.  # noqa: E501
        :type: str
        """

        self._online_status = online_status

    @property
    def preset_status(self):
        """Gets the preset_status of this DeviceDepartment.  # noqa: E501


        :return: The preset_status of this DeviceDepartment.  # noqa: E501
        :rtype: str
        """
        return self._preset_status

    @preset_status.setter
    def preset_status(self, preset_status):
        """Sets the preset_status of this DeviceDepartment.


        :param preset_status: The preset_status of this DeviceDepartment.  # noqa: E501
        :type: str
        """

        self._preset_status = preset_status

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
        if issubclass(DeviceDepartment, dict):
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
        if not isinstance(other, DeviceDepartment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
