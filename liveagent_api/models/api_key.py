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


class ApiKey(object):
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
        'id': 'float',
        'key': 'str',
        'valid_to_date': 'str',
        'role': 'str',
        'name': 'str',
        'type': 'str',
        'installid': 'str',
        'userid': 'str',
        'whitelist': 'str'
    }

    attribute_map = {
        'id': 'id',
        'key': 'key',
        'valid_to_date': 'valid_to_date',
        'role': 'role',
        'name': 'name',
        'type': 'type',
        'installid': 'installid',
        'userid': 'userid',
        'whitelist': 'whitelist'
    }

    def __init__(self, id=None, key=None, valid_to_date=None, role=None, name=None, type=None, installid=None, userid=None, whitelist=None):  # noqa: E501
        """ApiKey - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._key = None
        self._valid_to_date = None
        self._role = None
        self._name = None
        self._type = None
        self._installid = None
        self._userid = None
        self._whitelist = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if valid_to_date is not None:
            self.valid_to_date = valid_to_date
        if role is not None:
            self.role = role
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if installid is not None:
            self.installid = installid
        if userid is not None:
            self.userid = userid
        if whitelist is not None:
            self.whitelist = whitelist

    @property
    def id(self):
        """Gets the id of this ApiKey.  # noqa: E501


        :return: The id of this ApiKey.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiKey.


        :param id: The id of this ApiKey.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this ApiKey.  # noqa: E501


        :return: The key of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ApiKey.


        :param key: The key of this ApiKey.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def valid_to_date(self):
        """Gets the valid_to_date of this ApiKey.  # noqa: E501


        :return: The valid_to_date of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._valid_to_date

    @valid_to_date.setter
    def valid_to_date(self, valid_to_date):
        """Sets the valid_to_date of this ApiKey.


        :param valid_to_date: The valid_to_date of this ApiKey.  # noqa: E501
        :type: str
        """

        self._valid_to_date = valid_to_date

    @property
    def role(self):
        """Gets the role of this ApiKey.  # noqa: E501


        :return: The role of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ApiKey.


        :param role: The role of this ApiKey.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def name(self):
        """Gets the name of this ApiKey.  # noqa: E501


        :return: The name of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiKey.


        :param name: The name of this ApiKey.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ApiKey.  # noqa: E501

        - A - API - C - Chat - P - Phone - T - Ticket - W - Web (Agent Panel)  # noqa: E501

        :return: The type of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApiKey.

        - A - API - C - Chat - P - Phone - T - Ticket - W - Web (Agent Panel)  # noqa: E501

        :param type: The type of this ApiKey.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "C", "P", "T", "W"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def installid(self):
        """Gets the installid of this ApiKey.  # noqa: E501


        :return: The installid of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._installid

    @installid.setter
    def installid(self, installid):
        """Sets the installid of this ApiKey.


        :param installid: The installid of this ApiKey.  # noqa: E501
        :type: str
        """

        self._installid = installid

    @property
    def userid(self):
        """Gets the userid of this ApiKey.  # noqa: E501


        :return: The userid of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this ApiKey.


        :param userid: The userid of this ApiKey.  # noqa: E501
        :type: str
        """

        self._userid = userid

    @property
    def whitelist(self):
        """Gets the whitelist of this ApiKey.  # noqa: E501


        :return: The whitelist of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this ApiKey.


        :param whitelist: The whitelist of this ApiKey.  # noqa: E501
        :type: str
        """

        self._whitelist = whitelist

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
        if issubclass(ApiKey, dict):
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
        if not isinstance(other, ApiKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
