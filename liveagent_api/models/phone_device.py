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


class PhoneDevice(object):
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
        'type': 'str',
        'number': 'str',
        'name': 'str',
        'status_message': 'str',
        'connection_host': 'str',
        'connection_user': 'str',
        'connection_pass': 'str',
        'agent_id': 'str',
        'params': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'number': 'number',
        'name': 'name',
        'status_message': 'status_message',
        'connection_host': 'connection_host',
        'connection_user': 'connection_user',
        'connection_pass': 'connection_pass',
        'agent_id': 'agent_id',
        'params': 'params'
    }

    def __init__(self, id=None, type=None, number=None, name=None, status_message=None, connection_host=None, connection_user=None, connection_pass=None, agent_id=None, params=None):  # noqa: E501
        """PhoneDevice - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._number = None
        self._name = None
        self._status_message = None
        self._connection_host = None
        self._connection_user = None
        self._connection_pass = None
        self._agent_id = None
        self._params = None
        self.discriminator = None

        self.id = id
        self.type = type
        if number is not None:
            self.number = number
        if name is not None:
            self.name = name
        if status_message is not None:
            self.status_message = status_message
        if connection_host is not None:
            self.connection_host = connection_host
        if connection_user is not None:
            self.connection_user = connection_user
        if connection_pass is not None:
            self.connection_pass = connection_pass
        if agent_id is not None:
            self.agent_id = agent_id
        if params is not None:
            self.params = params

    @property
    def id(self):
        """Gets the id of this PhoneDevice.  # noqa: E501


        :return: The id of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PhoneDevice.


        :param id: The id of this PhoneDevice.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this PhoneDevice.  # noqa: E501

        A - LiveAgent phone app, S - SIP phone, E - PSTN phone, W - In panel web phone, I - Api phone  # noqa: E501

        :return: The type of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PhoneDevice.

        A - LiveAgent phone app, S - SIP phone, E - PSTN phone, W - In panel web phone, I - Api phone  # noqa: E501

        :param type: The type of this PhoneDevice.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["A", "S", "E", "W", "I"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def number(self):
        """Gets the number of this PhoneDevice.  # noqa: E501


        :return: The number of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PhoneDevice.


        :param number: The number of this PhoneDevice.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def name(self):
        """Gets the name of this PhoneDevice.  # noqa: E501


        :return: The name of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhoneDevice.


        :param name: The name of this PhoneDevice.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status_message(self):
        """Gets the status_message of this PhoneDevice.  # noqa: E501


        :return: The status_message of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this PhoneDevice.


        :param status_message: The status_message of this PhoneDevice.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def connection_host(self):
        """Gets the connection_host of this PhoneDevice.  # noqa: E501


        :return: The connection_host of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._connection_host

    @connection_host.setter
    def connection_host(self, connection_host):
        """Sets the connection_host of this PhoneDevice.


        :param connection_host: The connection_host of this PhoneDevice.  # noqa: E501
        :type: str
        """

        self._connection_host = connection_host

    @property
    def connection_user(self):
        """Gets the connection_user of this PhoneDevice.  # noqa: E501


        :return: The connection_user of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._connection_user

    @connection_user.setter
    def connection_user(self, connection_user):
        """Sets the connection_user of this PhoneDevice.


        :param connection_user: The connection_user of this PhoneDevice.  # noqa: E501
        :type: str
        """

        self._connection_user = connection_user

    @property
    def connection_pass(self):
        """Gets the connection_pass of this PhoneDevice.  # noqa: E501


        :return: The connection_pass of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._connection_pass

    @connection_pass.setter
    def connection_pass(self, connection_pass):
        """Sets the connection_pass of this PhoneDevice.


        :param connection_pass: The connection_pass of this PhoneDevice.  # noqa: E501
        :type: str
        """

        self._connection_pass = connection_pass

    @property
    def agent_id(self):
        """Gets the agent_id of this PhoneDevice.  # noqa: E501


        :return: The agent_id of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this PhoneDevice.


        :param agent_id: The agent_id of this PhoneDevice.  # noqa: E501
        :type: str
        """

        self._agent_id = agent_id

    @property
    def params(self):
        """Gets the params of this PhoneDevice.  # noqa: E501

        Addtional params column with no specific meaning  # noqa: E501

        :return: The params of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this PhoneDevice.

        Addtional params column with no specific meaning  # noqa: E501

        :param params: The params of this PhoneDevice.  # noqa: E501
        :type: str
        """

        self._params = params

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
        if issubclass(PhoneDevice, dict):
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
        if not isinstance(other, PhoneDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
