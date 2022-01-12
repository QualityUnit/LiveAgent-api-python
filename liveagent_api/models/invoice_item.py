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


class InvoiceItem(object):
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
        'type': 'str',
        'price': 'float',
        'description': 'str',
        'from_date': 'datetime',
        'to_date': 'datetime'
    }

    attribute_map = {
        'type': 'type',
        'price': 'price',
        'description': 'description',
        'from_date': 'from_date',
        'to_date': 'to_date'
    }

    def __init__(self, type=None, price=None, description=None, from_date=None, to_date=None):  # noqa: E501
        """InvoiceItem - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._price = None
        self._description = None
        self._from_date = None
        self._to_date = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if price is not None:
            self.price = price
        if description is not None:
            self.description = description
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date

    @property
    def type(self):
        """Gets the type of this InvoiceItem.  # noqa: E501


        :return: The type of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InvoiceItem.


        :param type: The type of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def price(self):
        """Gets the price of this InvoiceItem.  # noqa: E501


        :return: The price of this InvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InvoiceItem.


        :param price: The price of this InvoiceItem.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def description(self):
        """Gets the description of this InvoiceItem.  # noqa: E501


        :return: The description of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InvoiceItem.


        :param description: The description of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def from_date(self):
        """Gets the from_date of this InvoiceItem.  # noqa: E501


        :return: The from_date of this InvoiceItem.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this InvoiceItem.


        :param from_date: The from_date of this InvoiceItem.  # noqa: E501
        :type: datetime
        """

        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this InvoiceItem.  # noqa: E501


        :return: The to_date of this InvoiceItem.  # noqa: E501
        :rtype: datetime
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this InvoiceItem.


        :param to_date: The to_date of this InvoiceItem.  # noqa: E501
        :type: datetime
        """

        self._to_date = to_date

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
        if issubclass(InvoiceItem, dict):
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
        if not isinstance(other, InvoiceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
