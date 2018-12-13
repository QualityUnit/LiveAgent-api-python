# coding: utf-8

"""
    LiveAgent API

    LiveAgent API  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from liveagent_api.models.phone_device import PhoneDevice  # noqa: F401,E501


class CallAgent(object):
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
        'id': 'str',
        'device': 'PhoneDevice',
        'alternative_devices': 'list[PhoneDevice]'
    }

    attribute_map = {
        'id': 'id',
        'device': 'device',
        'alternative_devices': 'alternative_devices'
    }

    def __init__(self, id=None, device=None, alternative_devices=None):  # noqa: E501
        """CallAgent - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._device = None
        self._alternative_devices = None
        self.discriminator = None

        self.id = id
        if device is not None:
            self.device = device
        if alternative_devices is not None:
            self.alternative_devices = alternative_devices

    @property
    def id(self):
        """Gets the id of this CallAgent.  # noqa: E501


        :return: The id of this CallAgent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CallAgent.


        :param id: The id of this CallAgent.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def device(self):
        """Gets the device of this CallAgent.  # noqa: E501


        :return: The device of this CallAgent.  # noqa: E501
        :rtype: PhoneDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this CallAgent.


        :param device: The device of this CallAgent.  # noqa: E501
        :type: PhoneDevice
        """

        self._device = device

    @property
    def alternative_devices(self):
        """Gets the alternative_devices of this CallAgent.  # noqa: E501

        Alternative devices for an agent  # noqa: E501

        :return: The alternative_devices of this CallAgent.  # noqa: E501
        :rtype: list[PhoneDevice]
        """
        return self._alternative_devices

    @alternative_devices.setter
    def alternative_devices(self, alternative_devices):
        """Sets the alternative_devices of this CallAgent.

        Alternative devices for an agent  # noqa: E501

        :param alternative_devices: The alternative_devices of this CallAgent.  # noqa: E501
        :type: list[PhoneDevice]
        """

        self._alternative_devices = alternative_devices

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CallAgent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
