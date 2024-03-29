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


class Extension(object):
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
        'number': 'str',
        'status': 'str',
        'agent': 'Agent',
        'department': 'Department'
    }

    attribute_map = {
        'id': 'id',
        'number': 'number',
        'status': 'status',
        'agent': 'agent',
        'department': 'department'
    }

    def __init__(self, id=None, number=None, status=None, agent=None, department=None, _configuration=None):  # noqa: E501
        """Extension - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._number = None
        self._status = None
        self._agent = None
        self._department = None
        self.discriminator = None

        self.id = id
        if number is not None:
            self.number = number
        if status is not None:
            self.status = status
        if agent is not None:
            self.agent = agent
        if department is not None:
            self.department = department

    @property
    def id(self):
        """Gets the id of this Extension.  # noqa: E501


        :return: The id of this Extension.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Extension.


        :param id: The id of this Extension.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def number(self):
        """Gets the number of this Extension.  # noqa: E501


        :return: The number of this Extension.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Extension.


        :param number: The number of this Extension.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def status(self):
        """Gets the status of this Extension.  # noqa: E501

        A - Active (online)<br>E - Enabled (offline)<br> D - Disabled  # noqa: E501

        :return: The status of this Extension.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Extension.

        A - Active (online)<br>E - Enabled (offline)<br> D - Disabled  # noqa: E501

        :param status: The status of this Extension.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "E", "D"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def agent(self):
        """Gets the agent of this Extension.  # noqa: E501


        :return: The agent of this Extension.  # noqa: E501
        :rtype: Agent
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this Extension.


        :param agent: The agent of this Extension.  # noqa: E501
        :type: Agent
        """

        self._agent = agent

    @property
    def department(self):
        """Gets the department of this Extension.  # noqa: E501


        :return: The department of this Extension.  # noqa: E501
        :rtype: Department
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this Extension.


        :param department: The department of this Extension.  # noqa: E501
        :type: Department
        """

        self._department = department

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
        if issubclass(Extension, dict):
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
        if not isinstance(other, Extension):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Extension):
            return True

        return self.to_dict() != other.to_dict()
