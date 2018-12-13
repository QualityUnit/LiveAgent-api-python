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

from liveagent_api.models.custom_fields import CustomFields  # noqa: F401,E501


class TicketUpdatable(object):
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
        'owner_contactid': 'str',
        'departmentid': 'str',
        'agentid': 'str',
        'status': 'str',
        'tags': 'list[str]',
        'custom_fields': 'list[CustomFields]'
    }

    attribute_map = {
        'owner_contactid': 'owner_contactid',
        'departmentid': 'departmentid',
        'agentid': 'agentid',
        'status': 'status',
        'tags': 'tags',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, owner_contactid=None, departmentid=None, agentid=None, status=None, tags=None, custom_fields=None):  # noqa: E501
        """TicketUpdatable - a model defined in Swagger"""  # noqa: E501

        self._owner_contactid = None
        self._departmentid = None
        self._agentid = None
        self._status = None
        self._tags = None
        self._custom_fields = None
        self.discriminator = None

        if owner_contactid is not None:
            self.owner_contactid = owner_contactid
        if departmentid is not None:
            self.departmentid = departmentid
        if agentid is not None:
            self.agentid = agentid
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def owner_contactid(self):
        """Gets the owner_contactid of this TicketUpdatable.  # noqa: E501


        :return: The owner_contactid of this TicketUpdatable.  # noqa: E501
        :rtype: str
        """
        return self._owner_contactid

    @owner_contactid.setter
    def owner_contactid(self, owner_contactid):
        """Sets the owner_contactid of this TicketUpdatable.


        :param owner_contactid: The owner_contactid of this TicketUpdatable.  # noqa: E501
        :type: str
        """

        self._owner_contactid = owner_contactid

    @property
    def departmentid(self):
        """Gets the departmentid of this TicketUpdatable.  # noqa: E501


        :return: The departmentid of this TicketUpdatable.  # noqa: E501
        :rtype: str
        """
        return self._departmentid

    @departmentid.setter
    def departmentid(self, departmentid):
        """Sets the departmentid of this TicketUpdatable.


        :param departmentid: The departmentid of this TicketUpdatable.  # noqa: E501
        :type: str
        """

        self._departmentid = departmentid

    @property
    def agentid(self):
        """Gets the agentid of this TicketUpdatable.  # noqa: E501


        :return: The agentid of this TicketUpdatable.  # noqa: E501
        :rtype: str
        """
        return self._agentid

    @agentid.setter
    def agentid(self, agentid):
        """Sets the agentid of this TicketUpdatable.


        :param agentid: The agentid of this TicketUpdatable.  # noqa: E501
        :type: str
        """

        self._agentid = agentid

    @property
    def status(self):
        """Gets the status of this TicketUpdatable.  # noqa: E501

        <br> I - init<br> N - new<br> T - chatting<br> P - calling<br> R - resolved<br> X - deleted<br> B - spam<br> A - answered<br> C - open<br> W - postponed  # noqa: E501

        :return: The status of this TicketUpdatable.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TicketUpdatable.

        <br> I - init<br> N - new<br> T - chatting<br> P - calling<br> R - resolved<br> X - deleted<br> B - spam<br> A - answered<br> C - open<br> W - postponed  # noqa: E501

        :param status: The status of this TicketUpdatable.  # noqa: E501
        :type: str
        """
        allowed_values = ["I", "N", "T", "P", "R", "X", "B", "A", "C", "W"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this TicketUpdatable.  # noqa: E501


        :return: The tags of this TicketUpdatable.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TicketUpdatable.


        :param tags: The tags of this TicketUpdatable.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def custom_fields(self):
        """Gets the custom_fields of this TicketUpdatable.  # noqa: E501


        :return: The custom_fields of this TicketUpdatable.  # noqa: E501
        :rtype: list[CustomFields]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this TicketUpdatable.


        :param custom_fields: The custom_fields of this TicketUpdatable.  # noqa: E501
        :type: list[CustomFields]
        """

        self._custom_fields = custom_fields

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
        if not isinstance(other, TicketUpdatable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
