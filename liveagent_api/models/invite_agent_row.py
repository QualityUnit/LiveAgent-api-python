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


class InviteAgentRow(object):
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
        'agentid': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'system_name': 'str',
        'avatar_url': 'str',
        'chats': 'float'
    }

    attribute_map = {
        'agentid': 'agentid',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'system_name': 'system_name',
        'avatar_url': 'avatar_url',
        'chats': 'chats'
    }

    def __init__(self, agentid=None, firstname=None, lastname=None, system_name=None, avatar_url=None, chats=None):  # noqa: E501
        """InviteAgentRow - a model defined in Swagger"""  # noqa: E501

        self._agentid = None
        self._firstname = None
        self._lastname = None
        self._system_name = None
        self._avatar_url = None
        self._chats = None
        self.discriminator = None

        if agentid is not None:
            self.agentid = agentid
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if system_name is not None:
            self.system_name = system_name
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if chats is not None:
            self.chats = chats

    @property
    def agentid(self):
        """Gets the agentid of this InviteAgentRow.  # noqa: E501


        :return: The agentid of this InviteAgentRow.  # noqa: E501
        :rtype: str
        """
        return self._agentid

    @agentid.setter
    def agentid(self, agentid):
        """Sets the agentid of this InviteAgentRow.


        :param agentid: The agentid of this InviteAgentRow.  # noqa: E501
        :type: str
        """

        self._agentid = agentid

    @property
    def firstname(self):
        """Gets the firstname of this InviteAgentRow.  # noqa: E501


        :return: The firstname of this InviteAgentRow.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this InviteAgentRow.


        :param firstname: The firstname of this InviteAgentRow.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this InviteAgentRow.  # noqa: E501


        :return: The lastname of this InviteAgentRow.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this InviteAgentRow.


        :param lastname: The lastname of this InviteAgentRow.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def system_name(self):
        """Gets the system_name of this InviteAgentRow.  # noqa: E501


        :return: The system_name of this InviteAgentRow.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this InviteAgentRow.


        :param system_name: The system_name of this InviteAgentRow.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this InviteAgentRow.  # noqa: E501


        :return: The avatar_url of this InviteAgentRow.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this InviteAgentRow.


        :param avatar_url: The avatar_url of this InviteAgentRow.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def chats(self):
        """Gets the chats of this InviteAgentRow.  # noqa: E501


        :return: The chats of this InviteAgentRow.  # noqa: E501
        :rtype: float
        """
        return self._chats

    @chats.setter
    def chats(self, chats):
        """Sets the chats of this InviteAgentRow.


        :param chats: The chats of this InviteAgentRow.  # noqa: E501
        :type: float
        """

        self._chats = chats

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
        if issubclass(InviteAgentRow, dict):
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
        if not isinstance(other, InviteAgentRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other