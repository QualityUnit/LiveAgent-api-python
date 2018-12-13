# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Device(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Device - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'float',
            'agent_id': 'str',
            'phone_id': 'str',
            'api_phone_id': 'str',
            'type': 'str',
            'service_type': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'agent_id': 'agent_id',
            'phone_id': 'phone_id',
            'api_phone_id': 'api_phone_id',
            'type': 'type',
            'service_type': 'service_type',
            'status': 'status'
        }

        self._id = None
        self._agent_id = None
        self._phone_id = None
        self._api_phone_id = None
        self._type = None
        self._service_type = None
        self._status = None

    @property
    def id(self):
        """
        Gets the id of this Device.


        :return: The id of this Device.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Device.


        :param id: The id of this Device.
        :type: float
        """
        self._id = id

    @property
    def agent_id(self):
        """
        Gets the agent_id of this Device.


        :return: The agent_id of this Device.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this Device.


        :param agent_id: The agent_id of this Device.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def phone_id(self):
        """
        Gets the phone_id of this Device.


        :return: The phone_id of this Device.
        :rtype: str
        """
        return self._phone_id

    @phone_id.setter
    def phone_id(self, phone_id):
        """
        Sets the phone_id of this Device.


        :param phone_id: The phone_id of this Device.
        :type: str
        """
        self._phone_id = phone_id

    @property
    def api_phone_id(self):
        """
        Gets the api_phone_id of this Device.


        :return: The api_phone_id of this Device.
        :rtype: str
        """
        return self._api_phone_id

    @api_phone_id.setter
    def api_phone_id(self, api_phone_id):
        """
        Sets the api_phone_id of this Device.


        :param api_phone_id: The api_phone_id of this Device.
        :type: str
        """
        self._api_phone_id = api_phone_id

    @property
    def type(self):
        """
        Gets the type of this Device.


        :return: The type of this Device.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Device.


        :param type: The type of this Device.
        :type: str
        """
        self._type = type

    @property
    def service_type(self):
        """
        Gets the service_type of this Device.


        :return: The service_type of this Device.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """
        Sets the service_type of this Device.


        :param service_type: The service_type of this Device.
        :type: str
        """
        self._service_type = service_type

    @property
    def status(self):
        """
        Gets the status of this Device.


        :return: The status of this Device.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Device.


        :param status: The status of this Device.
        :type: str
        """
        self._status = status

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

