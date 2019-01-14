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


class CallTransferResult(object):
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
        'callee_status': 'str',
        'to_number': 'str',
        'via_number': 'str'
    }

    attribute_map = {
        'callee_status': 'callee_status',
        'to_number': 'to_number',
        'via_number': 'via_number'
    }

    def __init__(self, callee_status=None, to_number=None, via_number=None):  # noqa: E501
        """CallTransferResult - a model defined in Swagger"""  # noqa: E501

        self._callee_status = None
        self._to_number = None
        self._via_number = None
        self.discriminator = None

        self.callee_status = callee_status
        if to_number is not None:
            self.to_number = to_number
        if via_number is not None:
            self.via_number = via_number

    @property
    def callee_status(self):
        """Gets the callee_status of this CallTransferResult.  # noqa: E501

        O - online, F - offline  # noqa: E501

        :return: The callee_status of this CallTransferResult.  # noqa: E501
        :rtype: str
        """
        return self._callee_status

    @callee_status.setter
    def callee_status(self, callee_status):
        """Sets the callee_status of this CallTransferResult.

        O - online, F - offline  # noqa: E501

        :param callee_status: The callee_status of this CallTransferResult.  # noqa: E501
        :type: str
        """
        if callee_status is None:
            raise ValueError("Invalid value for `callee_status`, must not be `None`")  # noqa: E501
        allowed_values = ["O", "F"]  # noqa: E501
        if callee_status not in allowed_values:
            raise ValueError(
                "Invalid value for `callee_status` ({0}), must be one of {1}"  # noqa: E501
                .format(callee_status, allowed_values)
            )

        self._callee_status = callee_status

    @property
    def to_number(self):
        """Gets the to_number of this CallTransferResult.  # noqa: E501

        Callee number  # noqa: E501

        :return: The to_number of this CallTransferResult.  # noqa: E501
        :rtype: str
        """
        return self._to_number

    @to_number.setter
    def to_number(self, to_number):
        """Sets the to_number of this CallTransferResult.

        Callee number  # noqa: E501

        :param to_number: The to_number of this CallTransferResult.  # noqa: E501
        :type: str
        """

        self._to_number = to_number

    @property
    def via_number(self):
        """Gets the via_number of this CallTransferResult.  # noqa: E501

        trunk number via which call was made / received (if applicable)  # noqa: E501

        :return: The via_number of this CallTransferResult.  # noqa: E501
        :rtype: str
        """
        return self._via_number

    @via_number.setter
    def via_number(self, via_number):
        """Sets the via_number of this CallTransferResult.

        trunk number via which call was made / received (if applicable)  # noqa: E501

        :param via_number: The via_number of this CallTransferResult.  # noqa: E501
        :type: str
        """

        self._via_number = via_number

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
        if issubclass(CallTransferResult, dict):
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
        if not isinstance(other, CallTransferResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
