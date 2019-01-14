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

from liveagent_api.models.ban import Ban  # noqa: F401,E501


class BanListItem(object):
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
        'id': 'int',
        'date_created': 'datetime',
        'agent_id': 'str',
        'start_ip': 'float',
        'end_ip': 'float',
        'date_valid': 'datetime',
        'contact_id': 'str',
        'conversation_id': 'str',
        'reason': 'str',
        'agent_name': 'str',
        'contact_name': 'str',
        'conversation_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'date_created': 'date_created',
        'agent_id': 'agent_id',
        'start_ip': 'start_ip',
        'end_ip': 'end_ip',
        'date_valid': 'date_valid',
        'contact_id': 'contact_id',
        'conversation_id': 'conversation_id',
        'reason': 'reason',
        'agent_name': 'agent_name',
        'contact_name': 'contact_name',
        'conversation_code': 'conversation_code'
    }

    def __init__(self, id=None, date_created=None, agent_id=None, start_ip=None, end_ip=None, date_valid=None, contact_id=None, conversation_id=None, reason=None, agent_name=None, contact_name=None, conversation_code=None):  # noqa: E501
        """BanListItem - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._date_created = None
        self._agent_id = None
        self._start_ip = None
        self._end_ip = None
        self._date_valid = None
        self._contact_id = None
        self._conversation_id = None
        self._reason = None
        self._agent_name = None
        self._contact_name = None
        self._conversation_code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if date_created is not None:
            self.date_created = date_created
        if agent_id is not None:
            self.agent_id = agent_id
        if start_ip is not None:
            self.start_ip = start_ip
        if end_ip is not None:
            self.end_ip = end_ip
        if date_valid is not None:
            self.date_valid = date_valid
        if contact_id is not None:
            self.contact_id = contact_id
        if conversation_id is not None:
            self.conversation_id = conversation_id
        if reason is not None:
            self.reason = reason
        if agent_name is not None:
            self.agent_name = agent_name
        if contact_name is not None:
            self.contact_name = contact_name
        if conversation_code is not None:
            self.conversation_code = conversation_code

    @property
    def id(self):
        """Gets the id of this BanListItem.  # noqa: E501


        :return: The id of this BanListItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BanListItem.


        :param id: The id of this BanListItem.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this BanListItem.  # noqa: E501


        :return: The date_created of this BanListItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this BanListItem.


        :param date_created: The date_created of this BanListItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def agent_id(self):
        """Gets the agent_id of this BanListItem.  # noqa: E501


        :return: The agent_id of this BanListItem.  # noqa: E501
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this BanListItem.


        :param agent_id: The agent_id of this BanListItem.  # noqa: E501
        :type: str
        """

        self._agent_id = agent_id

    @property
    def start_ip(self):
        """Gets the start_ip of this BanListItem.  # noqa: E501


        :return: The start_ip of this BanListItem.  # noqa: E501
        :rtype: float
        """
        return self._start_ip

    @start_ip.setter
    def start_ip(self, start_ip):
        """Sets the start_ip of this BanListItem.


        :param start_ip: The start_ip of this BanListItem.  # noqa: E501
        :type: float
        """

        self._start_ip = start_ip

    @property
    def end_ip(self):
        """Gets the end_ip of this BanListItem.  # noqa: E501


        :return: The end_ip of this BanListItem.  # noqa: E501
        :rtype: float
        """
        return self._end_ip

    @end_ip.setter
    def end_ip(self, end_ip):
        """Sets the end_ip of this BanListItem.


        :param end_ip: The end_ip of this BanListItem.  # noqa: E501
        :type: float
        """

        self._end_ip = end_ip

    @property
    def date_valid(self):
        """Gets the date_valid of this BanListItem.  # noqa: E501


        :return: The date_valid of this BanListItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_valid

    @date_valid.setter
    def date_valid(self, date_valid):
        """Sets the date_valid of this BanListItem.


        :param date_valid: The date_valid of this BanListItem.  # noqa: E501
        :type: datetime
        """

        self._date_valid = date_valid

    @property
    def contact_id(self):
        """Gets the contact_id of this BanListItem.  # noqa: E501


        :return: The contact_id of this BanListItem.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this BanListItem.


        :param contact_id: The contact_id of this BanListItem.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def conversation_id(self):
        """Gets the conversation_id of this BanListItem.  # noqa: E501


        :return: The conversation_id of this BanListItem.  # noqa: E501
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """Sets the conversation_id of this BanListItem.


        :param conversation_id: The conversation_id of this BanListItem.  # noqa: E501
        :type: str
        """

        self._conversation_id = conversation_id

    @property
    def reason(self):
        """Gets the reason of this BanListItem.  # noqa: E501


        :return: The reason of this BanListItem.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this BanListItem.


        :param reason: The reason of this BanListItem.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def agent_name(self):
        """Gets the agent_name of this BanListItem.  # noqa: E501


        :return: The agent_name of this BanListItem.  # noqa: E501
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """Sets the agent_name of this BanListItem.


        :param agent_name: The agent_name of this BanListItem.  # noqa: E501
        :type: str
        """

        self._agent_name = agent_name

    @property
    def contact_name(self):
        """Gets the contact_name of this BanListItem.  # noqa: E501


        :return: The contact_name of this BanListItem.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this BanListItem.


        :param contact_name: The contact_name of this BanListItem.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def conversation_code(self):
        """Gets the conversation_code of this BanListItem.  # noqa: E501


        :return: The conversation_code of this BanListItem.  # noqa: E501
        :rtype: str
        """
        return self._conversation_code

    @conversation_code.setter
    def conversation_code(self, conversation_code):
        """Sets the conversation_code of this BanListItem.


        :param conversation_code: The conversation_code of this BanListItem.  # noqa: E501
        :type: str
        """

        self._conversation_code = conversation_code

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
        if issubclass(BanListItem, dict):
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
        if not isinstance(other, BanListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
