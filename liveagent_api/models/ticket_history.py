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


class TicketHistory(object):
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
        'conversation_id': 'str',
        'conversation_code': 'str',
        'department_id': 'str',
        'agent_id': 'str',
        'status': 'str',
        'date_from': 'str',
        'date_to': 'str',
        'elapsed_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'conversation_id': 'conversation_id',
        'conversation_code': 'conversation_code',
        'department_id': 'department_id',
        'agent_id': 'agent_id',
        'status': 'status',
        'date_from': 'date_from',
        'date_to': 'date_to',
        'elapsed_time': 'elapsed_time'
    }

    def __init__(self, id=None, conversation_id=None, conversation_code=None, department_id=None, agent_id=None, status=None, date_from=None, date_to=None, elapsed_time=None):  # noqa: E501
        """TicketHistory - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._conversation_id = None
        self._conversation_code = None
        self._department_id = None
        self._agent_id = None
        self._status = None
        self._date_from = None
        self._date_to = None
        self._elapsed_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if conversation_id is not None:
            self.conversation_id = conversation_id
        if conversation_code is not None:
            self.conversation_code = conversation_code
        if department_id is not None:
            self.department_id = department_id
        if agent_id is not None:
            self.agent_id = agent_id
        if status is not None:
            self.status = status
        if date_from is not None:
            self.date_from = date_from
        if date_to is not None:
            self.date_to = date_to
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time

    @property
    def id(self):
        """Gets the id of this TicketHistory.  # noqa: E501


        :return: The id of this TicketHistory.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TicketHistory.


        :param id: The id of this TicketHistory.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def conversation_id(self):
        """Gets the conversation_id of this TicketHistory.  # noqa: E501


        :return: The conversation_id of this TicketHistory.  # noqa: E501
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """Sets the conversation_id of this TicketHistory.


        :param conversation_id: The conversation_id of this TicketHistory.  # noqa: E501
        :type: str
        """

        self._conversation_id = conversation_id

    @property
    def conversation_code(self):
        """Gets the conversation_code of this TicketHistory.  # noqa: E501


        :return: The conversation_code of this TicketHistory.  # noqa: E501
        :rtype: str
        """
        return self._conversation_code

    @conversation_code.setter
    def conversation_code(self, conversation_code):
        """Sets the conversation_code of this TicketHistory.


        :param conversation_code: The conversation_code of this TicketHistory.  # noqa: E501
        :type: str
        """

        self._conversation_code = conversation_code

    @property
    def department_id(self):
        """Gets the department_id of this TicketHistory.  # noqa: E501


        :return: The department_id of this TicketHistory.  # noqa: E501
        :rtype: str
        """
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        """Sets the department_id of this TicketHistory.


        :param department_id: The department_id of this TicketHistory.  # noqa: E501
        :type: str
        """

        self._department_id = department_id

    @property
    def agent_id(self):
        """Gets the agent_id of this TicketHistory.  # noqa: E501


        :return: The agent_id of this TicketHistory.  # noqa: E501
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this TicketHistory.


        :param agent_id: The agent_id of this TicketHistory.  # noqa: E501
        :type: str
        """

        self._agent_id = agent_id

    @property
    def status(self):
        """Gets the status of this TicketHistory.  # noqa: E501


        :return: The status of this TicketHistory.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TicketHistory.


        :param status: The status of this TicketHistory.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def date_from(self):
        """Gets the date_from of this TicketHistory.  # noqa: E501


        :return: The date_from of this TicketHistory.  # noqa: E501
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this TicketHistory.


        :param date_from: The date_from of this TicketHistory.  # noqa: E501
        :type: str
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this TicketHistory.  # noqa: E501


        :return: The date_to of this TicketHistory.  # noqa: E501
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this TicketHistory.


        :param date_to: The date_to of this TicketHistory.  # noqa: E501
        :type: str
        """

        self._date_to = date_to

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this TicketHistory.  # noqa: E501


        :return: The elapsed_time of this TicketHistory.  # noqa: E501
        :rtype: str
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this TicketHistory.


        :param elapsed_time: The elapsed_time of this TicketHistory.  # noqa: E501
        :type: str
        """

        self._elapsed_time = elapsed_time

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
        if not isinstance(other, TicketHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other