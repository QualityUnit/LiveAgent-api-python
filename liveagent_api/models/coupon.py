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


class Coupon(object):
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
        'code': 'str',
        'subscription_id': 'str',
        'discount_type': 'str',
        'discount_value_type': 'str',
        'discount': 'int',
        'discount_name': 'str',
        'reusable': 'bool',
        'date_valid': 'str',
        'note': 'str',
        'created_by': 'str',
        'date_created': 'str',
        'ended_by': 'str',
        'date_expired': 'str'
    }

    attribute_map = {
        'code': 'code',
        'subscription_id': 'subscription_id',
        'discount_type': 'discount_type',
        'discount_value_type': 'discount_value_type',
        'discount': 'discount',
        'discount_name': 'discount_name',
        'reusable': 'reusable',
        'date_valid': 'date_valid',
        'note': 'note',
        'created_by': 'created_by',
        'date_created': 'date_created',
        'ended_by': 'ended_by',
        'date_expired': 'date_expired'
    }

    def __init__(self, code=None, subscription_id=None, discount_type=None, discount_value_type=None, discount=None, discount_name=None, reusable=None, date_valid=None, note=None, created_by=None, date_created=None, ended_by=None, date_expired=None):  # noqa: E501
        """Coupon - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._subscription_id = None
        self._discount_type = None
        self._discount_value_type = None
        self._discount = None
        self._discount_name = None
        self._reusable = None
        self._date_valid = None
        self._note = None
        self._created_by = None
        self._date_created = None
        self._ended_by = None
        self._date_expired = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if subscription_id is not None:
            self.subscription_id = subscription_id
        self.discount_type = discount_type
        self.discount_value_type = discount_value_type
        self.discount = discount
        if discount_name is not None:
            self.discount_name = discount_name
        if reusable is not None:
            self.reusable = reusable
        if date_valid is not None:
            self.date_valid = date_valid
        if note is not None:
            self.note = note
        if created_by is not None:
            self.created_by = created_by
        if date_created is not None:
            self.date_created = date_created
        if ended_by is not None:
            self.ended_by = ended_by
        if date_expired is not None:
            self.date_expired = date_expired

    @property
    def code(self):
        """Gets the code of this Coupon.  # noqa: E501


        :return: The code of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Coupon.


        :param code: The code of this Coupon.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def subscription_id(self):
        """Gets the subscription_id of this Coupon.  # noqa: E501


        :return: The subscription_id of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this Coupon.


        :param subscription_id: The subscription_id of this Coupon.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def discount_type(self):
        """Gets the discount_type of this Coupon.  # noqa: E501


        :return: The discount_type of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """Sets the discount_type of this Coupon.


        :param discount_type: The discount_type of this Coupon.  # noqa: E501
        :type: str
        """
        if discount_type is None:
            raise ValueError("Invalid value for `discount_type`, must not be `None`")  # noqa: E501
        allowed_values = ["one_time", "current_plan", "permanent"]  # noqa: E501
        if discount_type not in allowed_values:
            raise ValueError(
                "Invalid value for `discount_type` ({0}), must be one of {1}"  # noqa: E501
                .format(discount_type, allowed_values)
            )

        self._discount_type = discount_type

    @property
    def discount_value_type(self):
        """Gets the discount_value_type of this Coupon.  # noqa: E501


        :return: The discount_value_type of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._discount_value_type

    @discount_value_type.setter
    def discount_value_type(self, discount_value_type):
        """Sets the discount_value_type of this Coupon.


        :param discount_value_type: The discount_value_type of this Coupon.  # noqa: E501
        :type: str
        """
        if discount_value_type is None:
            raise ValueError("Invalid value for `discount_value_type`, must not be `None`")  # noqa: E501
        allowed_values = ["constant", "per_cent"]  # noqa: E501
        if discount_value_type not in allowed_values:
            raise ValueError(
                "Invalid value for `discount_value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(discount_value_type, allowed_values)
            )

        self._discount_value_type = discount_value_type

    @property
    def discount(self):
        """Gets the discount of this Coupon.  # noqa: E501


        :return: The discount of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this Coupon.


        :param discount: The discount of this Coupon.  # noqa: E501
        :type: int
        """
        if discount is None:
            raise ValueError("Invalid value for `discount`, must not be `None`")  # noqa: E501

        self._discount = discount

    @property
    def discount_name(self):
        """Gets the discount_name of this Coupon.  # noqa: E501


        :return: The discount_name of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._discount_name

    @discount_name.setter
    def discount_name(self, discount_name):
        """Sets the discount_name of this Coupon.


        :param discount_name: The discount_name of this Coupon.  # noqa: E501
        :type: str
        """

        self._discount_name = discount_name

    @property
    def reusable(self):
        """Gets the reusable of this Coupon.  # noqa: E501


        :return: The reusable of this Coupon.  # noqa: E501
        :rtype: bool
        """
        return self._reusable

    @reusable.setter
    def reusable(self, reusable):
        """Sets the reusable of this Coupon.


        :param reusable: The reusable of this Coupon.  # noqa: E501
        :type: bool
        """

        self._reusable = reusable

    @property
    def date_valid(self):
        """Gets the date_valid of this Coupon.  # noqa: E501


        :return: The date_valid of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._date_valid

    @date_valid.setter
    def date_valid(self, date_valid):
        """Sets the date_valid of this Coupon.


        :param date_valid: The date_valid of this Coupon.  # noqa: E501
        :type: str
        """

        self._date_valid = date_valid

    @property
    def note(self):
        """Gets the note of this Coupon.  # noqa: E501


        :return: The note of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Coupon.


        :param note: The note of this Coupon.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def created_by(self):
        """Gets the created_by of this Coupon.  # noqa: E501


        :return: The created_by of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Coupon.


        :param created_by: The created_by of this Coupon.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def date_created(self):
        """Gets the date_created of this Coupon.  # noqa: E501


        :return: The date_created of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Coupon.


        :param date_created: The date_created of this Coupon.  # noqa: E501
        :type: str
        """

        self._date_created = date_created

    @property
    def ended_by(self):
        """Gets the ended_by of this Coupon.  # noqa: E501


        :return: The ended_by of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._ended_by

    @ended_by.setter
    def ended_by(self, ended_by):
        """Sets the ended_by of this Coupon.


        :param ended_by: The ended_by of this Coupon.  # noqa: E501
        :type: str
        """

        self._ended_by = ended_by

    @property
    def date_expired(self):
        """Gets the date_expired of this Coupon.  # noqa: E501


        :return: The date_expired of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._date_expired

    @date_expired.setter
    def date_expired(self, date_expired):
        """Sets the date_expired of this Coupon.


        :param date_expired: The date_expired of this Coupon.  # noqa: E501
        :type: str
        """

        self._date_expired = date_expired

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
        if issubclass(Coupon, dict):
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
        if not isinstance(other, Coupon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
