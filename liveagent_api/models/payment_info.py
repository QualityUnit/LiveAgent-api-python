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


class PaymentInfo(object):
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
        'payment_type': 'str',
        'detail': 'str',
        'card_expire': 'str'
    }

    attribute_map = {
        'payment_type': 'payment_type',
        'detail': 'detail',
        'card_expire': 'card_expire'
    }

    def __init__(self, payment_type=None, detail=None, card_expire=None):  # noqa: E501
        """PaymentInfo - a model defined in Swagger"""  # noqa: E501

        self._payment_type = None
        self._detail = None
        self._card_expire = None
        self.discriminator = None

        self.payment_type = payment_type
        if detail is not None:
            self.detail = detail
        if card_expire is not None:
            self.card_expire = card_expire

    @property
    def payment_type(self):
        """Gets the payment_type of this PaymentInfo.  # noqa: E501


        :return: The payment_type of this PaymentInfo.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this PaymentInfo.


        :param payment_type: The payment_type of this PaymentInfo.  # noqa: E501
        :type: str
        """
        if payment_type is None:
            raise ValueError("Invalid value for `payment_type`, must not be `None`")  # noqa: E501

        self._payment_type = payment_type

    @property
    def detail(self):
        """Gets the detail of this PaymentInfo.  # noqa: E501


        :return: The detail of this PaymentInfo.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this PaymentInfo.


        :param detail: The detail of this PaymentInfo.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def card_expire(self):
        """Gets the card_expire of this PaymentInfo.  # noqa: E501


        :return: The card_expire of this PaymentInfo.  # noqa: E501
        :rtype: str
        """
        return self._card_expire

    @card_expire.setter
    def card_expire(self, card_expire):
        """Sets the card_expire of this PaymentInfo.


        :param card_expire: The card_expire of this PaymentInfo.  # noqa: E501
        :type: str
        """

        self._card_expire = card_expire

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
        if issubclass(PaymentInfo, dict):
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
        if not isinstance(other, PaymentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
