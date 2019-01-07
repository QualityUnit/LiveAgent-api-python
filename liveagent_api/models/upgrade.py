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


class Upgrade(object):
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
        'variation_id': 'str',
        'addons': 'list[str]',
        'billing_period': 'str',
        'coupon': 'str'
    }

    attribute_map = {
        'variation_id': 'variation_id',
        'addons': 'addons',
        'billing_period': 'billing_period',
        'coupon': 'coupon'
    }

    def __init__(self, variation_id=None, addons=None, billing_period='1m', coupon=None):  # noqa: E501
        """Upgrade - a model defined in Swagger"""  # noqa: E501

        self._variation_id = None
        self._addons = None
        self._billing_period = None
        self._coupon = None
        self.discriminator = None

        self.variation_id = variation_id
        if addons is not None:
            self.addons = addons
        if billing_period is not None:
            self.billing_period = billing_period
        if coupon is not None:
            self.coupon = coupon

    @property
    def variation_id(self):
        """Gets the variation_id of this Upgrade.  # noqa: E501


        :return: The variation_id of this Upgrade.  # noqa: E501
        :rtype: str
        """
        return self._variation_id

    @variation_id.setter
    def variation_id(self, variation_id):
        """Sets the variation_id of this Upgrade.


        :param variation_id: The variation_id of this Upgrade.  # noqa: E501
        :type: str
        """
        if variation_id is None:
            raise ValueError("Invalid value for `variation_id`, must not be `None`")  # noqa: E501

        self._variation_id = variation_id

    @property
    def addons(self):
        """Gets the addons of this Upgrade.  # noqa: E501


        :return: The addons of this Upgrade.  # noqa: E501
        :rtype: list[str]
        """
        return self._addons

    @addons.setter
    def addons(self, addons):
        """Sets the addons of this Upgrade.


        :param addons: The addons of this Upgrade.  # noqa: E501
        :type: list[str]
        """

        self._addons = addons

    @property
    def billing_period(self):
        """Gets the billing_period of this Upgrade.  # noqa: E501


        :return: The billing_period of this Upgrade.  # noqa: E501
        :rtype: str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this Upgrade.


        :param billing_period: The billing_period of this Upgrade.  # noqa: E501
        :type: str
        """
        allowed_values = ["1m"]  # noqa: E501
        if billing_period not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_period` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_period, allowed_values)
            )

        self._billing_period = billing_period

    @property
    def coupon(self):
        """Gets the coupon of this Upgrade.  # noqa: E501


        :return: The coupon of this Upgrade.  # noqa: E501
        :rtype: str
        """
        return self._coupon

    @coupon.setter
    def coupon(self, coupon):
        """Sets the coupon of this Upgrade.


        :param coupon: The coupon of this Upgrade.  # noqa: E501
        :type: str
        """

        self._coupon = coupon

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
        if issubclass(Upgrade, dict):
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
        if not isinstance(other, Upgrade):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
