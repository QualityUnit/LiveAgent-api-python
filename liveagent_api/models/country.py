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


class Country(object):
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
        'eu': 'bool',
        'code': 'str',
        'name': 'str'
    }

    attribute_map = {
        'eu': 'eu',
        'code': 'code',
        'name': 'name'
    }

    def __init__(self, eu=None, code=None, name=None):  # noqa: E501
        """Country - a model defined in Swagger"""  # noqa: E501

        self._eu = None
        self._code = None
        self._name = None
        self.discriminator = None

        if eu is not None:
            self.eu = eu
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name

    @property
    def eu(self):
        """Gets the eu of this Country.  # noqa: E501


        :return: The eu of this Country.  # noqa: E501
        :rtype: bool
        """
        return self._eu

    @eu.setter
    def eu(self, eu):
        """Sets the eu of this Country.


        :param eu: The eu of this Country.  # noqa: E501
        :type: bool
        """

        self._eu = eu

    @property
    def code(self):
        """Gets the code of this Country.  # noqa: E501


        :return: The code of this Country.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Country.


        :param code: The code of this Country.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this Country.  # noqa: E501


        :return: The name of this Country.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Country.


        :param name: The name of this Country.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Country):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
