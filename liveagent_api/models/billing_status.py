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
        'status': 'str',
        'valid_to_date': 'datetime',
        'next_billing_date': 'datetime',
        'errors': 'int',
        'last_error_date': 'datetime',
        'payment_compatible': 'bool'
    }

    attribute_map = {
        'status': 'status',
        'valid_to_date': 'valid_to_date',
        'next_billing_date': 'next_billing_date',
        'errors': 'errors',
        'last_error_date': 'last_error_date',
        'payment_compatible': 'payment_compatible'
    }

    def __init__(self, status=None, valid_to_date=None, next_billing_date=None, errors=None, last_error_date=None, payment_compatible=None):  # noqa: E501
        """BillingStatus - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._valid_to_date = None
        self._next_billing_date = None
        self._errors = None
        self._last_error_date = None
        self._payment_compatible = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if valid_to_date is not None:
            self.valid_to_date = valid_to_date
        if next_billing_date is not None:
            self.next_billing_date = next_billing_date
        if errors is not None:
            self.errors = errors
        if last_error_date is not None:
            self.last_error_date = last_error_date
        if payment_compatible is not None:
            self.payment_compatible = payment_compatible

    @property
    def status(self):
        """Gets the status of this BillingStatus.  # noqa: E501

        N - No billing A - Billing active S = Billing stopped   # noqa: E501

        :return: The status of this BillingStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BillingStatus.

        N - No billing A - Billing active S = Billing stopped   # noqa: E501

        :param status: The status of this BillingStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "A", "S"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def valid_to_date(self):
        """Gets the valid_to_date of this BillingStatus.  # noqa: E501


        :return: The valid_to_date of this BillingStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_to_date

    @valid_to_date.setter
    def valid_to_date(self, valid_to_date):
        """Sets the valid_to_date of this BillingStatus.


        :param valid_to_date: The valid_to_date of this BillingStatus.  # noqa: E501
        :type: datetime
        """

        self._valid_to_date = valid_to_date

    @property
    def next_billing_date(self):
        """Gets the next_billing_date of this BillingStatus.  # noqa: E501


        :return: The next_billing_date of this BillingStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._next_billing_date

    @next_billing_date.setter
    def next_billing_date(self, next_billing_date):
        """Sets the next_billing_date of this BillingStatus.


        :param next_billing_date: The next_billing_date of this BillingStatus.  # noqa: E501
        :type: datetime
        """

        self._next_billing_date = next_billing_date

    @property
    def errors(self):
        """Gets the errors of this BillingStatus.  # noqa: E501

        Number of charge errors since last successful billing or account unsuspend.  # noqa: E501

        :return: The errors of this BillingStatus.  # noqa: E501
        :rtype: int
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this BillingStatus.

        Number of charge errors since last successful billing or account unsuspend.  # noqa: E501

        :param errors: The errors of this BillingStatus.  # noqa: E501
        :type: int
        """

        self._errors = errors

    @property
    def last_error_date(self):
        """Gets the last_error_date of this BillingStatus.  # noqa: E501

        Time an date of the last failed charge attempt. Only present if number or errors is greater than 0.  # noqa: E501

        :return: The last_error_date of this BillingStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_error_date

    @last_error_date.setter
    def last_error_date(self, last_error_date):
        """Sets the last_error_date of this BillingStatus.

        Time an date of the last failed charge attempt. Only present if number or errors is greater than 0.  # noqa: E501

        :param last_error_date: The last_error_date of this BillingStatus.  # noqa: E501
        :type: datetime
        """

        self._last_error_date = last_error_date

    @property
    def payment_compatible(self):
        """Gets the payment_compatible of this BillingStatus.  # noqa: E501

        True if used payment method is fully compatible with selected country, false otherwise. False when either payment method or country is not set.  # noqa: E501

        :return: The payment_compatible of this BillingStatus.  # noqa: E501
        :rtype: bool
        """
        return self._payment_compatible

    @payment_compatible.setter
    def payment_compatible(self, payment_compatible):
        """Sets the payment_compatible of this BillingStatus.

        True if used payment method is fully compatible with selected country, false otherwise. False when either payment method or country is not set.  # noqa: E501

        :param payment_compatible: The payment_compatible of this BillingStatus.  # noqa: E501
        :type: bool
        """

        self._payment_compatible = payment_compatible

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

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
