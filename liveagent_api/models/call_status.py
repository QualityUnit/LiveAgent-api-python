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


class CallStatus(object):
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
        'status': 'str',
        'manually_picked_up': 'bool',
        'agent': 'CallAgent',
        'queue_position': 'float'
    }

    attribute_map = {
        'status': 'status',
        'manually_picked_up': 'manually_picked_up',
        'agent': 'agent',
        'queue_position': 'queue_position'
    }

    def __init__(self, status=None, manually_picked_up=False, agent=None, queue_position=None, _configuration=None):  # noqa: E501
        """CallStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._manually_picked_up = None
        self._agent = None
        self._queue_position = None
        self.discriminator = None

        self.status = status
        if manually_picked_up is not None:
            self.manually_picked_up = manually_picked_up
        if agent is not None:
            self.agent = agent
        if queue_position is not None:
            self.queue_position = queue_position

    @property
    def status(self):
        """Gets the status of this CallStatus.  # noqa: E501

        O (callee offline), Q (waiting in queue), R (ringing to an agent), C (calling with an agent), F (finished)  # noqa: E501

        :return: The status of this CallStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CallStatus.

        O (callee offline), Q (waiting in queue), R (ringing to an agent), C (calling with an agent), F (finished)  # noqa: E501

        :param status: The status of this CallStatus.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["O", "Q", "R", "C", "F"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def manually_picked_up(self):
        """Gets the manually_picked_up of this CallStatus.  # noqa: E501

        If the call was picked up from the call queue manually by agent.  # noqa: E501

        :return: The manually_picked_up of this CallStatus.  # noqa: E501
        :rtype: bool
        """
        return self._manually_picked_up

    @manually_picked_up.setter
    def manually_picked_up(self, manually_picked_up):
        """Sets the manually_picked_up of this CallStatus.

        If the call was picked up from the call queue manually by agent.  # noqa: E501

        :param manually_picked_up: The manually_picked_up of this CallStatus.  # noqa: E501
        :type: bool
        """

        self._manually_picked_up = manually_picked_up

    @property
    def agent(self):
        """Gets the agent of this CallStatus.  # noqa: E501


        :return: The agent of this CallStatus.  # noqa: E501
        :rtype: CallAgent
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this CallStatus.


        :param agent: The agent of this CallStatus.  # noqa: E501
        :type: CallAgent
        """

        self._agent = agent

    @property
    def queue_position(self):
        """Gets the queue_position of this CallStatus.  # noqa: E501


        :return: The queue_position of this CallStatus.  # noqa: E501
        :rtype: float
        """
        return self._queue_position

    @queue_position.setter
    def queue_position(self, queue_position):
        """Sets the queue_position of this CallStatus.


        :param queue_position: The queue_position of this CallStatus.  # noqa: E501
        :type: float
        """

        self._queue_position = queue_position

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
        if issubclass(CallStatus, dict):
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
        if not isinstance(other, CallStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CallStatus):
            return True

        return self.to_dict() != other.to_dict()
