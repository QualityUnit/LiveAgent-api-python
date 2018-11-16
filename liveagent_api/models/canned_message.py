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


class CannedMessage(object):
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
        'id': 'str',
        'userid': 'str',
        'departmentid': 'str',
        'messagetext': 'str',
        'keywords': 'str'
    }

    attribute_map = {
        'id': 'id',
        'userid': 'userid',
        'departmentid': 'departmentid',
        'messagetext': 'messagetext',
        'keywords': 'keywords'
    }

    def __init__(self, id=None, userid=None, departmentid=None, messagetext=None, keywords=None):  # noqa: E501
        """CannedMessage - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._userid = None
        self._departmentid = None
        self._messagetext = None
        self._keywords = None
        self.discriminator = None

        self.id = id
        if userid is not None:
            self.userid = userid
        if departmentid is not None:
            self.departmentid = departmentid
        if messagetext is not None:
            self.messagetext = messagetext
        if keywords is not None:
            self.keywords = keywords

    @property
    def id(self):
        """Gets the id of this CannedMessage.  # noqa: E501


        :return: The id of this CannedMessage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CannedMessage.


        :param id: The id of this CannedMessage.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def userid(self):
        """Gets the userid of this CannedMessage.  # noqa: E501


        :return: The userid of this CannedMessage.  # noqa: E501
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this CannedMessage.


        :param userid: The userid of this CannedMessage.  # noqa: E501
        :type: str
        """

        self._userid = userid

    @property
    def departmentid(self):
        """Gets the departmentid of this CannedMessage.  # noqa: E501


        :return: The departmentid of this CannedMessage.  # noqa: E501
        :rtype: str
        """
        return self._departmentid

    @departmentid.setter
    def departmentid(self, departmentid):
        """Sets the departmentid of this CannedMessage.


        :param departmentid: The departmentid of this CannedMessage.  # noqa: E501
        :type: str
        """

        self._departmentid = departmentid

    @property
    def messagetext(self):
        """Gets the messagetext of this CannedMessage.  # noqa: E501


        :return: The messagetext of this CannedMessage.  # noqa: E501
        :rtype: str
        """
        return self._messagetext

    @messagetext.setter
    def messagetext(self, messagetext):
        """Sets the messagetext of this CannedMessage.


        :param messagetext: The messagetext of this CannedMessage.  # noqa: E501
        :type: str
        """

        self._messagetext = messagetext

    @property
    def keywords(self):
        """Gets the keywords of this CannedMessage.  # noqa: E501


        :return: The keywords of this CannedMessage.  # noqa: E501
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this CannedMessage.


        :param keywords: The keywords of this CannedMessage.  # noqa: E501
        :type: str
        """

        self._keywords = keywords

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
        if not isinstance(other, CannedMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
