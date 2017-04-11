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


class PhoneNumber(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PhoneNumber - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'dial_out_prefix': 'int',
            'number': 'str',
            'name': 'str',
            'departmentid': 'str',
            'status': 'str',
            'host': 'str',
            'port': 'str',
            'user': 'str',
            'password': 'str',
            'providerid': 'str',
            'ivr': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'dial_out_prefix': 'dial_out_prefix',
            'number': 'number',
            'name': 'name',
            'departmentid': 'departmentid',
            'status': 'status',
            'host': 'host',
            'port': 'port',
            'user': 'user',
            'password': 'password',
            'providerid': 'providerid',
            'ivr': 'ivr'
        }

        self._id = None
        self._type = None
        self._dial_out_prefix = None
        self._number = None
        self._name = None
        self._departmentid = None
        self._status = None
        self._host = None
        self._port = None
        self._user = None
        self._password = None
        self._providerid = None
        self._ivr = None

    @property
    def id(self):
        """
        Gets the id of this PhoneNumber.


        :return: The id of this PhoneNumber.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PhoneNumber.


        :param id: The id of this PhoneNumber.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """
        Gets the type of this PhoneNumber.
        A - API controlled number, T - Twilio number, T-O - Twilio outgoing number, D - Digitale, S - Asterisk

        :return: The type of this PhoneNumber.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PhoneNumber.
        A - API controlled number, T - Twilio number, T-O - Twilio outgoing number, D - Digitale, S - Asterisk

        :param type: The type of this PhoneNumber.
        :type: str
        """
        allowed_values = ["A", "C", "T", "T-O", "D", "S"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def dial_out_prefix(self):
        """
        Gets the dial_out_prefix of this PhoneNumber.
        Prefix needed to orifinate call using this number

        :return: The dial_out_prefix of this PhoneNumber.
        :rtype: int
        """
        return self._dial_out_prefix

    @dial_out_prefix.setter
    def dial_out_prefix(self, dial_out_prefix):
        """
        Sets the dial_out_prefix of this PhoneNumber.
        Prefix needed to orifinate call using this number

        :param dial_out_prefix: The dial_out_prefix of this PhoneNumber.
        :type: int
        """
        self._dial_out_prefix = dial_out_prefix

    @property
    def number(self):
        """
        Gets the number of this PhoneNumber.


        :return: The number of this PhoneNumber.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this PhoneNumber.


        :param number: The number of this PhoneNumber.
        :type: str
        """
        self._number = number

    @property
    def name(self):
        """
        Gets the name of this PhoneNumber.


        :return: The name of this PhoneNumber.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PhoneNumber.


        :param name: The name of this PhoneNumber.
        :type: str
        """
        self._name = name

    @property
    def departmentid(self):
        """
        Gets the departmentid of this PhoneNumber.


        :return: The departmentid of this PhoneNumber.
        :rtype: str
        """
        return self._departmentid

    @departmentid.setter
    def departmentid(self, departmentid):
        """
        Sets the departmentid of this PhoneNumber.


        :param departmentid: The departmentid of this PhoneNumber.
        :type: str
        """
        self._departmentid = departmentid

    @property
    def status(self):
        """
        Gets the status of this PhoneNumber.
        A - Active, I - Inactive

        :return: The status of this PhoneNumber.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PhoneNumber.
        A - Active, I - Inactive

        :param status: The status of this PhoneNumber.
        :type: str
        """
        allowed_values = ["A", "I"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def host(self):
        """
        Gets the host of this PhoneNumber.


        :return: The host of this PhoneNumber.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this PhoneNumber.


        :param host: The host of this PhoneNumber.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this PhoneNumber.


        :return: The port of this PhoneNumber.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this PhoneNumber.


        :param port: The port of this PhoneNumber.
        :type: str
        """
        self._port = port

    @property
    def user(self):
        """
        Gets the user of this PhoneNumber.


        :return: The user of this PhoneNumber.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this PhoneNumber.


        :param user: The user of this PhoneNumber.
        :type: str
        """
        self._user = user

    @property
    def password(self):
        """
        Gets the password of this PhoneNumber.


        :return: The password of this PhoneNumber.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this PhoneNumber.


        :param password: The password of this PhoneNumber.
        :type: str
        """
        self._password = password

    @property
    def providerid(self):
        """
        Gets the providerid of this PhoneNumber.


        :return: The providerid of this PhoneNumber.
        :rtype: str
        """
        return self._providerid

    @providerid.setter
    def providerid(self, providerid):
        """
        Sets the providerid of this PhoneNumber.


        :param providerid: The providerid of this PhoneNumber.
        :type: str
        """
        self._providerid = providerid

    @property
    def ivr(self):
        """
        Gets the ivr of this PhoneNumber.


        :return: The ivr of this PhoneNumber.
        :rtype: str
        """
        return self._ivr

    @ivr.setter
    def ivr(self, ivr):
        """
        Sets the ivr of this PhoneNumber.


        :param ivr: The ivr of this PhoneNumber.
        :type: str
        """
        self._ivr = ivr

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

