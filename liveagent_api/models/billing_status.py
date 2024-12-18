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


class BillingStatus(object):
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
        'valid_to': 'int',
        'has_errors': 'bool'
    }

    attribute_map = {
        'valid_to': 'valid_to',
        'has_errors': 'has_errors'
    }

    def __init__(self, valid_to=None, has_errors=None, _configuration=None):  # noqa: E501
        """BillingStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._valid_to = None
        self._has_errors = None
        self.discriminator = None

        if valid_to is not None:
            self.valid_to = valid_to
        self.has_errors = has_errors

    @property
    def valid_to(self):
        """Gets the valid_to of this BillingStatus.  # noqa: E501

        Timestamp until which the account is valid  # noqa: E501

        :return: The valid_to of this BillingStatus.  # noqa: E501
        :rtype: int
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this BillingStatus.

        Timestamp until which the account is valid  # noqa: E501

        :param valid_to: The valid_to of this BillingStatus.  # noqa: E501
        :type: int
        """

        self._valid_to = valid_to

    @property
    def has_errors(self):
        """Gets the has_errors of this BillingStatus.  # noqa: E501

        True if account has charge errors since last successful billing or account unsuspend. False otherwise  # noqa: E501

        :return: The has_errors of this BillingStatus.  # noqa: E501
        :rtype: bool
        """
        return self._has_errors

    @has_errors.setter
    def has_errors(self, has_errors):
        """Sets the has_errors of this BillingStatus.

        True if account has charge errors since last successful billing or account unsuspend. False otherwise  # noqa: E501

        :param has_errors: The has_errors of this BillingStatus.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and has_errors is None:
            raise ValueError("Invalid value for `has_errors`, must not be `None`")  # noqa: E501

        self._has_errors = has_errors

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
        if issubclass(BillingStatus, dict):
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
        if not isinstance(other, BillingStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillingStatus):
            return True

        return self.to_dict() != other.to_dict()
