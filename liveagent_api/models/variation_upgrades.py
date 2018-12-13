# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class VariationUpgrades(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VariationUpgrades - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'current': 'VariationUpgrade',
            'upgrades': 'list[VariationUpgrade]',
            'currency': 'str',
            'tax_per_cent': 'float',
            'tax_included': 'bool'
        }

        self.attribute_map = {
            'current': 'current',
            'upgrades': 'upgrades',
            'currency': 'currency',
            'tax_per_cent': 'tax_per_cent',
            'tax_included': 'tax_included'
        }

        self._current = None
        self._upgrades = None
        self._currency = None
        self._tax_per_cent = None
        self._tax_included = None

    @property
    def current(self):
        """
        Gets the current of this VariationUpgrades.


        :return: The current of this VariationUpgrades.
        :rtype: VariationUpgrade
        """
        return self._current

    @current.setter
    def current(self, current):
        """
        Sets the current of this VariationUpgrades.


        :param current: The current of this VariationUpgrades.
        :type: VariationUpgrade
        """
        self._current = current

    @property
    def upgrades(self):
        """
        Gets the upgrades of this VariationUpgrades.


        :return: The upgrades of this VariationUpgrades.
        :rtype: list[VariationUpgrade]
        """
        return self._upgrades

    @upgrades.setter
    def upgrades(self, upgrades):
        """
        Sets the upgrades of this VariationUpgrades.


        :param upgrades: The upgrades of this VariationUpgrades.
        :type: list[VariationUpgrade]
        """
        self._upgrades = upgrades

    @property
    def currency(self):
        """
        Gets the currency of this VariationUpgrades.


        :return: The currency of this VariationUpgrades.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this VariationUpgrades.


        :param currency: The currency of this VariationUpgrades.
        :type: str
        """
        allowed_values = ["USD", "EUR"]
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency`, must be one of {0}"
                .format(allowed_values)
            )
        self._currency = currency

    @property
    def tax_per_cent(self):
        """
        Gets the tax_per_cent of this VariationUpgrades.


        :return: The tax_per_cent of this VariationUpgrades.
        :rtype: float
        """
        return self._tax_per_cent

    @tax_per_cent.setter
    def tax_per_cent(self, tax_per_cent):
        """
        Sets the tax_per_cent of this VariationUpgrades.


        :param tax_per_cent: The tax_per_cent of this VariationUpgrades.
        :type: float
        """
        self._tax_per_cent = tax_per_cent

    @property
    def tax_included(self):
        """
        Gets the tax_included of this VariationUpgrades.


        :return: The tax_included of this VariationUpgrades.
        :rtype: bool
        """
        return self._tax_included

    @tax_included.setter
    def tax_included(self, tax_included):
        """
        Sets the tax_included of this VariationUpgrades.


        :param tax_included: The tax_included of this VariationUpgrades.
        :type: bool
        """
        self._tax_included = tax_included

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

