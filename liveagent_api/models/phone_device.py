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
        'reg_status': 'str',
        'connection_host': 'str',
        'connection_user': 'str',
        'connection_pass': 'str',
        'last_modified': 'str',
        'user_agent': 'str',
        'agent_id': 'str',
        'trunk_id': 'float',
        'params': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'number': 'number',
        'name': 'name',
        'reg_status': 'reg_status',
        'connection_host': 'connection_host',
        'connection_user': 'connection_user',
        'connection_pass': 'connection_pass',
        'last_modified': 'last_modified',
        'user_agent': 'user_agent',
        'agent_id': 'agent_id',
        'trunk_id': 'trunk_id',
        'params': 'params'
    }

    def __init__(self, id=None, type=None, number=None, name=None, reg_status=None, connection_host=None, connection_user=None, connection_pass=None, last_modified=None, user_agent=None, agent_id=None, trunk_id=None, params=None):  # noqa: E501
        """PhoneDevice - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._number = None
        self._name = None
        self._reg_status = None
        self._connection_host = None
        self._connection_user = None
        self._connection_pass = None
        self._last_modified = None
        self._user_agent = None
        self._agent_id = None
        self._trunk_id = None
        self._params = None
        self.discriminator = None

        self.id = id
        self.type = type
        if number is not None:
            self.number = number
        if name is not None:
            self.name = name
        if reg_status is not None:
            self.reg_status = reg_status
        if connection_host is not None:
            self.connection_host = connection_host
        if connection_user is not None:
            self.connection_user = connection_user
        if connection_pass is not None:
            self.connection_pass = connection_pass
        if last_modified is not None:
            self.last_modified = last_modified
        if user_agent is not None:
            self.user_agent = user_agent
        if agent_id is not None:
            self.agent_id = agent_id
        if trunk_id is not None:
            self.trunk_id = trunk_id
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
    def reg_status(self):
        """Gets the reg_status of this PhoneDevice.  # noqa: E501


        :return: The reg_status of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._reg_status

    @reg_status.setter
    def reg_status(self, reg_status):
        """Sets the reg_status of this PhoneDevice.


        :param reg_status: The reg_status of this PhoneDevice.  # noqa: E501
        :type: str
        """

        self._reg_status = reg_status

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
    def last_modified(self):
        """Gets the last_modified of this PhoneDevice.  # noqa: E501


        :return: The last_modified of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this PhoneDevice.


        :param last_modified: The last_modified of this PhoneDevice.  # noqa: E501
        :type: str
        """

        self._last_modified = last_modified

    @property
    def user_agent(self):
        """Gets the user_agent of this PhoneDevice.  # noqa: E501


        :return: The user_agent of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this PhoneDevice.


        :param user_agent: The user_agent of this PhoneDevice.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

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
    def trunk_id(self):
        """Gets the trunk_id of this PhoneDevice.  # noqa: E501


        :return: The trunk_id of this PhoneDevice.  # noqa: E501
        :rtype: float
        """
        return self._trunk_id

    @trunk_id.setter
    def trunk_id(self, trunk_id):
        """Sets the trunk_id of this PhoneDevice.


        :param trunk_id: The trunk_id of this PhoneDevice.  # noqa: E501
        :type: float
        """

        self._trunk_id = trunk_id

    @property
    def params(self):
        """Gets the params of this PhoneDevice.  # noqa: E501

        Additional params column with no specific meaning  # noqa: E501

        :return: The params of this PhoneDevice.  # noqa: E501
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this PhoneDevice.

        Additional params column with no specific meaning  # noqa: E501

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
