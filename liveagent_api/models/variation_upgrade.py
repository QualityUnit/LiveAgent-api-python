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

from liveagent_api.models.addon import Addon  # noqa: F401,E501
from liveagent_api.models.billing_metric import BillingMetric  # noqa: F401,E501
from liveagent_api.models.discount_value import DiscountValue  # noqa: F401,E501
from liveagent_api.models.variation import Variation  # noqa: F401,E501


class VariationUpgrade(object):
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
        'variation': 'Variation',
        'addons': 'list[Addon]',
        'metrics': 'list[BillingMetric]',
        'base_price': 'int',
        'discounts': 'list[DiscountValue]'
    }

    attribute_map = {
        'variation': 'variation',
        'addons': 'addons',
        'metrics': 'metrics',
        'base_price': 'base_price',
        'discounts': 'discounts'
    }

    def __init__(self, variation=None, addons=None, metrics=None, base_price=None, discounts=None):  # noqa: E501
        """VariationUpgrade - a model defined in Swagger"""  # noqa: E501

        self._variation = None
        self._addons = None
        self._metrics = None
        self._base_price = None
        self._discounts = None
        self.discriminator = None

        if variation is not None:
            self.variation = variation
        if addons is not None:
            self.addons = addons
        if metrics is not None:
            self.metrics = metrics
        if base_price is not None:
            self.base_price = base_price
        if discounts is not None:
            self.discounts = discounts

    @property
    def variation(self):
        """Gets the variation of this VariationUpgrade.  # noqa: E501


        :return: The variation of this VariationUpgrade.  # noqa: E501
        :rtype: Variation
        """
        return self._variation

    @variation.setter
    def variation(self, variation):
        """Sets the variation of this VariationUpgrade.


        :param variation: The variation of this VariationUpgrade.  # noqa: E501
        :type: Variation
        """

        self._variation = variation

    @property
    def addons(self):
        """Gets the addons of this VariationUpgrade.  # noqa: E501


        :return: The addons of this VariationUpgrade.  # noqa: E501
        :rtype: list[Addon]
        """
        return self._addons

    @addons.setter
    def addons(self, addons):
        """Sets the addons of this VariationUpgrade.


        :param addons: The addons of this VariationUpgrade.  # noqa: E501
        :type: list[Addon]
        """

        self._addons = addons

    @property
    def metrics(self):
        """Gets the metrics of this VariationUpgrade.  # noqa: E501


        :return: The metrics of this VariationUpgrade.  # noqa: E501
        :rtype: list[BillingMetric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this VariationUpgrade.


        :param metrics: The metrics of this VariationUpgrade.  # noqa: E501
        :type: list[BillingMetric]
        """

        self._metrics = metrics

    @property
    def base_price(self):
        """Gets the base_price of this VariationUpgrade.  # noqa: E501


        :return: The base_price of this VariationUpgrade.  # noqa: E501
        :rtype: int
        """
        return self._base_price

    @base_price.setter
    def base_price(self, base_price):
        """Sets the base_price of this VariationUpgrade.


        :param base_price: The base_price of this VariationUpgrade.  # noqa: E501
        :type: int
        """

        self._base_price = base_price

    @property
    def discounts(self):
        """Gets the discounts of this VariationUpgrade.  # noqa: E501


        :return: The discounts of this VariationUpgrade.  # noqa: E501
        :rtype: list[DiscountValue]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """Sets the discounts of this VariationUpgrade.


        :param discounts: The discounts of this VariationUpgrade.  # noqa: E501
        :type: list[DiscountValue]
        """

        self._discounts = discounts

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
        if not isinstance(other, VariationUpgrade):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
