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

from liveagent_api.configuration import Configuration


class AgentActivity(object):
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
        'agent_status': 'str',
        'active_tickets': 'list[ActiveTicket]'
    }

    attribute_map = {
        'id': 'id',
        'agent_status': 'agent_status',
        'active_tickets': 'active_tickets'
    }

    def __init__(self, id=None, agent_status=None, active_tickets=None, _configuration=None):  # noqa: E501
        """AgentActivity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._agent_status = None
        self._active_tickets = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if agent_status is not None:
            self.agent_status = agent_status
        if active_tickets is not None:
            self.active_tickets = active_tickets

    @property
    def id(self):
        """Gets the id of this AgentActivity.  # noqa: E501


        :return: The id of this AgentActivity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AgentActivity.


        :param id: The id of this AgentActivity.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def agent_status(self):
        """Gets the agent_status of this AgentActivity.  # noqa: E501

        A - Available / B - Busy   # noqa: E501

        :return: The agent_status of this AgentActivity.  # noqa: E501
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this AgentActivity.

        A - Available / B - Busy   # noqa: E501

        :param agent_status: The agent_status of this AgentActivity.  # noqa: E501
        :type: str
        """

        self._agent_status = agent_status

    @property
    def active_tickets(self):
        """Gets the active_tickets of this AgentActivity.  # noqa: E501


        :return: The active_tickets of this AgentActivity.  # noqa: E501
        :rtype: list[ActiveTicket]
        """
        return self._active_tickets

    @active_tickets.setter
    def active_tickets(self, active_tickets):
        """Sets the active_tickets of this AgentActivity.


        :param active_tickets: The active_tickets of this AgentActivity.  # noqa: E501
        :type: list[ActiveTicket]
        """

        self._active_tickets = active_tickets

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
        if issubclass(AgentActivity, dict):
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
        if not isinstance(other, AgentActivity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgentActivity):
            return True

        return self.to_dict() != other.to_dict()
