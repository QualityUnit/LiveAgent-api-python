# coding: utf-8

"""
    LiveAgent API

    This page contains complete API documentation for LiveAgent software. To display additional info and examples for specific API method, just click on the method name in the list below.<br/><br/>To be able to make API requests you need to generate an API key in your admin panel first. [See this article for detailed info.](https://support.ladesk.com/741982-API-key)<br/><br/>Additional info about more advanced agent, contact or ticket API filters can be found [in this article](https://support.ladesk.com/513528-APIv3-advanced-filter-examples).<br/><br/>If you have any question or doubts regarding this API, please do not hesitate to contact our support team.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ActiveTicket(object):
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
        'ticket_id': 'str',
        'ticket_code': 'str',
        'date_joined': 'datetime',
        'department_id': 'str',
        'status': 'str',
        'ticket_status': 'str'
    }

    attribute_map = {
        'ticket_id': 'ticket_id',
        'ticket_code': 'ticket_code',
        'date_joined': 'date_joined',
        'department_id': 'department_id',
        'status': 'status',
        'ticket_status': 'ticket_status'
    }

    def __init__(self, ticket_id=None, ticket_code=None, date_joined=None, department_id=None, status=None, ticket_status=None):  # noqa: E501
        """ActiveTicket - a model defined in Swagger"""  # noqa: E501

        self._ticket_id = None
        self._ticket_code = None
        self._date_joined = None
        self._department_id = None
        self._status = None
        self._ticket_status = None
        self.discriminator = None

        if ticket_id is not None:
            self.ticket_id = ticket_id
        if ticket_code is not None:
            self.ticket_code = ticket_code
        if date_joined is not None:
            self.date_joined = date_joined
        if department_id is not None:
            self.department_id = department_id
        if status is not None:
            self.status = status
        if ticket_status is not None:
            self.ticket_status = ticket_status

    @property
    def ticket_id(self):
        """Gets the ticket_id of this ActiveTicket.  # noqa: E501


        :return: The ticket_id of this ActiveTicket.  # noqa: E501
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        """Sets the ticket_id of this ActiveTicket.


        :param ticket_id: The ticket_id of this ActiveTicket.  # noqa: E501
        :type: str
        """

        self._ticket_id = ticket_id

    @property
    def ticket_code(self):
        """Gets the ticket_code of this ActiveTicket.  # noqa: E501


        :return: The ticket_code of this ActiveTicket.  # noqa: E501
        :rtype: str
        """
        return self._ticket_code

    @ticket_code.setter
    def ticket_code(self, ticket_code):
        """Sets the ticket_code of this ActiveTicket.


        :param ticket_code: The ticket_code of this ActiveTicket.  # noqa: E501
        :type: str
        """

        self._ticket_code = ticket_code

    @property
    def date_joined(self):
        """Gets the date_joined of this ActiveTicket.  # noqa: E501


        :return: The date_joined of this ActiveTicket.  # noqa: E501
        :rtype: datetime
        """
        return self._date_joined

    @date_joined.setter
    def date_joined(self, date_joined):
        """Sets the date_joined of this ActiveTicket.


        :param date_joined: The date_joined of this ActiveTicket.  # noqa: E501
        :type: datetime
        """

        self._date_joined = date_joined

    @property
    def department_id(self):
        """Gets the department_id of this ActiveTicket.  # noqa: E501


        :return: The department_id of this ActiveTicket.  # noqa: E501
        :rtype: str
        """
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        """Sets the department_id of this ActiveTicket.


        :param department_id: The department_id of this ActiveTicket.  # noqa: E501
        :type: str
        """

        self._department_id = department_id

    @property
    def status(self):
        """Gets the status of this ActiveTicket.  # noqa: E501

        V - Viewing / J - Replying, Chatting / R - Ringing / C - Calling   # noqa: E501

        :return: The status of this ActiveTicket.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ActiveTicket.

        V - Viewing / J - Replying, Chatting / R - Ringing / C - Calling   # noqa: E501

        :param status: The status of this ActiveTicket.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def ticket_status(self):
        """Gets the ticket_status of this ActiveTicket.  # noqa: E501

        C - Opened / R - Resolved / A - Answered / X - Deleted / T - Chat / P - Call   # noqa: E501

        :return: The ticket_status of this ActiveTicket.  # noqa: E501
        :rtype: str
        """
        return self._ticket_status

    @ticket_status.setter
    def ticket_status(self, ticket_status):
        """Sets the ticket_status of this ActiveTicket.

        C - Opened / R - Resolved / A - Answered / X - Deleted / T - Chat / P - Call   # noqa: E501

        :param ticket_status: The ticket_status of this ActiveTicket.  # noqa: E501
        :type: str
        """

        self._ticket_status = ticket_status

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
        if issubclass(ActiveTicket, dict):
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
        if not isinstance(other, ActiveTicket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
