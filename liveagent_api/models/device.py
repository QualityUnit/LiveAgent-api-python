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


class Device(object):
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
        'id': 'float',
        'agent_id': 'str',
        'phone_id': 'str',
        'phone': 'PhoneDevice',
        'type': 'str',
        'service_type': 'str',
        'online_status': 'str',
        'preset_status': 'str',
        'route_if_offline': 'str'
    }

    attribute_map = {
        'id': 'id',
        'agent_id': 'agent_id',
        'phone_id': 'phone_id',
        'phone': 'phone',
        'type': 'type',
        'service_type': 'service_type',
        'online_status': 'online_status',
        'preset_status': 'preset_status',
        'route_if_offline': 'route_if_offline'
    }

    def __init__(self, id=None, agent_id=None, phone_id=None, phone=None, type=None, service_type=None, online_status='N', preset_status=None, route_if_offline='Y', _configuration=None):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._agent_id = None
        self._phone_id = None
        self._phone = None
        self._type = None
        self._service_type = None
        self._online_status = None
        self._preset_status = None
        self._route_if_offline = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.agent_id = agent_id
        if phone_id is not None:
            self.phone_id = phone_id
        if phone is not None:
            self.phone = phone
        self.type = type
        self.service_type = service_type
        if online_status is not None:
            self.online_status = online_status
        self.preset_status = preset_status
        if route_if_offline is not None:
            self.route_if_offline = route_if_offline

    @property
    def id(self):
        """Gets the id of this Device.  # noqa: E501


        :return: The id of this Device.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.


        :param id: The id of this Device.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def agent_id(self):
        """Gets the agent_id of this Device.  # noqa: E501


        :return: The agent_id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this Device.


        :param agent_id: The agent_id of this Device.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and agent_id is None:
            raise ValueError("Invalid value for `agent_id`, must not be `None`")  # noqa: E501

        self._agent_id = agent_id

    @property
    def phone_id(self):
        """Gets the phone_id of this Device.  # noqa: E501


        :return: The phone_id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._phone_id

    @phone_id.setter
    def phone_id(self, phone_id):
        """Sets the phone_id of this Device.


        :param phone_id: The phone_id of this Device.  # noqa: E501
        :type: str
        """

        self._phone_id = phone_id

    @property
    def phone(self):
        """Gets the phone of this Device.  # noqa: E501


        :return: The phone of this Device.  # noqa: E501
        :rtype: PhoneDevice
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Device.


        :param phone: The phone of this Device.  # noqa: E501
        :type: PhoneDevice
        """

        self._phone = phone

    @property
    def type(self):
        """Gets the type of this Device.  # noqa: E501

        W - WEB A - MOBILE APP E - EXTERNAL (Corresponds to the phone types: SIP, API, PSTN, SIP Provider Extension)  # noqa: E501

        :return: The type of this Device.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Device.

        W - WEB A - MOBILE APP E - EXTERNAL (Corresponds to the phone types: SIP, API, PSTN, SIP Provider Extension)  # noqa: E501

        :param type: The type of this Device.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["W", "A", "E"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def service_type(self):
        """Gets the service_type of this Device.  # noqa: E501

        M - MESSAGE T - CHAT P - PHONE  # noqa: E501

        :return: The service_type of this Device.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this Device.

        M - MESSAGE T - CHAT P - PHONE  # noqa: E501

        :param service_type: The service_type of this Device.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and service_type is None:
            raise ValueError("Invalid value for `service_type`, must not be `None`")  # noqa: E501
        allowed_values = ["M", "T", "P"]  # noqa: E501
        if (self._configuration.client_side_validation and
                service_type not in allowed_values):
            raise ValueError(
                "Invalid value for `service_type` ({0}), must be one of {1}"  # noqa: E501
                .format(service_type, allowed_values)
            )

        self._service_type = service_type

    @property
    def online_status(self):
        """Gets the online_status of this Device.  # noqa: E501

        N - ONLINE F - OFFLINE  # noqa: E501

        :return: The online_status of this Device.  # noqa: E501
        :rtype: str
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status):
        """Sets the online_status of this Device.

        N - ONLINE F - OFFLINE  # noqa: E501

        :param online_status: The online_status of this Device.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "F"]  # noqa: E501
        if (self._configuration.client_side_validation and
                online_status not in allowed_values):
            raise ValueError(
                "Invalid value for `online_status` ({0}), must be one of {1}"  # noqa: E501
                .format(online_status, allowed_values)
            )

        self._online_status = online_status

    @property
    def preset_status(self):
        """Gets the preset_status of this Device.  # noqa: E501

        N - ONLINE F - OFFLINE  # noqa: E501

        :return: The preset_status of this Device.  # noqa: E501
        :rtype: str
        """
        return self._preset_status

    @preset_status.setter
    def preset_status(self, preset_status):
        """Sets the preset_status of this Device.

        N - ONLINE F - OFFLINE  # noqa: E501

        :param preset_status: The preset_status of this Device.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and preset_status is None:
            raise ValueError("Invalid value for `preset_status`, must not be `None`")  # noqa: E501
        allowed_values = ["N", "F"]  # noqa: E501
        if (self._configuration.client_side_validation and
                preset_status not in allowed_values):
            raise ValueError(
                "Invalid value for `preset_status` ({0}), must be one of {1}"  # noqa: E501
                .format(preset_status, allowed_values)
            )

        self._preset_status = preset_status

    @property
    def route_if_offline(self):
        """Gets the route_if_offline of this Device.  # noqa: E501

        Y - Yes N - No  # noqa: E501

        :return: The route_if_offline of this Device.  # noqa: E501
        :rtype: str
        """
        return self._route_if_offline

    @route_if_offline.setter
    def route_if_offline(self, route_if_offline):
        """Sets the route_if_offline of this Device.

        Y - Yes N - No  # noqa: E501

        :param route_if_offline: The route_if_offline of this Device.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N"]  # noqa: E501
        if (self._configuration.client_side_validation and
                route_if_offline not in allowed_values):
            raise ValueError(
                "Invalid value for `route_if_offline` ({0}), must be one of {1}"  # noqa: E501
                .format(route_if_offline, allowed_values)
            )

        self._route_if_offline = route_if_offline

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
        if issubclass(Device, dict):
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
        if not isinstance(other, Device):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Device):
            return True

        return self.to_dict() != other.to_dict()
