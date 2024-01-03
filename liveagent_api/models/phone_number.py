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


class PhoneNumber(object):
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
        'dial_out_prefix': 'int',
        'dial_out_prefix_formatted': 'str',
        'record_in_call': 'bool',
        'record_out_call': 'bool',
        'number': 'str',
        'name': 'str',
        'departmentid': 'str',
        'department': 'Department',
        'status': 'str',
        'status_message': 'str',
        'host_settings': 'str',
        'host': 'str',
        'port': 'str',
        'user': 'str',
        'auth_user': 'str',
        'password': 'str',
        'proxy_host': 'str',
        'proxy_port': 'str',
        'proxy_user': 'str',
        'providerid': 'str',
        'ivr': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'dial_out_prefix': 'dial_out_prefix',
        'dial_out_prefix_formatted': 'dial_out_prefix_formatted',
        'record_in_call': 'record_in_call',
        'record_out_call': 'record_out_call',
        'number': 'number',
        'name': 'name',
        'departmentid': 'departmentid',
        'department': 'department',
        'status': 'status',
        'status_message': 'status_message',
        'host_settings': 'host_settings',
        'host': 'host',
        'port': 'port',
        'user': 'user',
        'auth_user': 'auth_user',
        'password': 'password',
        'proxy_host': 'proxy_host',
        'proxy_port': 'proxy_port',
        'proxy_user': 'proxy_user',
        'providerid': 'providerid',
        'ivr': 'ivr'
    }

    def __init__(self, id=None, type=None, dial_out_prefix=None, dial_out_prefix_formatted=None, record_in_call=None, record_out_call=None, number=None, name=None, departmentid=None, department=None, status=None, status_message=None, host_settings=None, host=None, port=None, user=None, auth_user=None, password=None, proxy_host=None, proxy_port=None, proxy_user=None, providerid=None, ivr=None, _configuration=None):  # noqa: E501
        """PhoneNumber - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._type = None
        self._dial_out_prefix = None
        self._dial_out_prefix_formatted = None
        self._record_in_call = None
        self._record_out_call = None
        self._number = None
        self._name = None
        self._departmentid = None
        self._department = None
        self._status = None
        self._status_message = None
        self._host_settings = None
        self._host = None
        self._port = None
        self._user = None
        self._auth_user = None
        self._password = None
        self._proxy_host = None
        self._proxy_port = None
        self._proxy_user = None
        self._providerid = None
        self._ivr = None
        self.discriminator = None

        self.id = id
        if type is not None:
            self.type = type
        if dial_out_prefix is not None:
            self.dial_out_prefix = dial_out_prefix
        if dial_out_prefix_formatted is not None:
            self.dial_out_prefix_formatted = dial_out_prefix_formatted
        if record_in_call is not None:
            self.record_in_call = record_in_call
        if record_out_call is not None:
            self.record_out_call = record_out_call
        self.number = number
        if name is not None:
            self.name = name
        if departmentid is not None:
            self.departmentid = departmentid
        if department is not None:
            self.department = department
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if host_settings is not None:
            self.host_settings = host_settings
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if user is not None:
            self.user = user
        if auth_user is not None:
            self.auth_user = auth_user
        if password is not None:
            self.password = password
        if proxy_host is not None:
            self.proxy_host = proxy_host
        if proxy_port is not None:
            self.proxy_port = proxy_port
        if proxy_user is not None:
            self.proxy_user = proxy_user
        if providerid is not None:
            self.providerid = providerid
        if ivr is not None:
            self.ivr = ivr

    @property
    def id(self):
        """Gets the id of this PhoneNumber.  # noqa: E501


        :return: The id of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PhoneNumber.


        :param id: The id of this PhoneNumber.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this PhoneNumber.  # noqa: E501

        A - API controlled number, T - Twilio number, T-O - Twilio outgoing number, D - Digitale, S - Asterisk  # noqa: E501

        :return: The type of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PhoneNumber.

        A - API controlled number, T - Twilio number, T-O - Twilio outgoing number, D - Digitale, S - Asterisk  # noqa: E501

        :param type: The type of this PhoneNumber.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "C", "T", "T-O", "D", "S"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def dial_out_prefix(self):
        """Gets the dial_out_prefix of this PhoneNumber.  # noqa: E501

        Prefix needed to originate call using this number  # noqa: E501

        :return: The dial_out_prefix of this PhoneNumber.  # noqa: E501
        :rtype: int
        """
        return self._dial_out_prefix

    @dial_out_prefix.setter
    def dial_out_prefix(self, dial_out_prefix):
        """Sets the dial_out_prefix of this PhoneNumber.

        Prefix needed to originate call using this number  # noqa: E501

        :param dial_out_prefix: The dial_out_prefix of this PhoneNumber.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                dial_out_prefix is not None and dial_out_prefix > 999):  # noqa: E501
            raise ValueError("Invalid value for `dial_out_prefix`, must be a value less than or equal to `999`")  # noqa: E501
        if (self._configuration.client_side_validation and
                dial_out_prefix is not None and dial_out_prefix < 1):  # noqa: E501
            raise ValueError("Invalid value for `dial_out_prefix`, must be a value greater than or equal to `1`")  # noqa: E501

        self._dial_out_prefix = dial_out_prefix

    @property
    def dial_out_prefix_formatted(self):
        """Gets the dial_out_prefix_formatted of this PhoneNumber.  # noqa: E501

        Dial out prefix in 2 or 3 digits string format according to application settings  # noqa: E501

        :return: The dial_out_prefix_formatted of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._dial_out_prefix_formatted

    @dial_out_prefix_formatted.setter
    def dial_out_prefix_formatted(self, dial_out_prefix_formatted):
        """Sets the dial_out_prefix_formatted of this PhoneNumber.

        Dial out prefix in 2 or 3 digits string format according to application settings  # noqa: E501

        :param dial_out_prefix_formatted: The dial_out_prefix_formatted of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._dial_out_prefix_formatted = dial_out_prefix_formatted

    @property
    def record_in_call(self):
        """Gets the record_in_call of this PhoneNumber.  # noqa: E501


        :return: The record_in_call of this PhoneNumber.  # noqa: E501
        :rtype: bool
        """
        return self._record_in_call

    @record_in_call.setter
    def record_in_call(self, record_in_call):
        """Sets the record_in_call of this PhoneNumber.


        :param record_in_call: The record_in_call of this PhoneNumber.  # noqa: E501
        :type: bool
        """

        self._record_in_call = record_in_call

    @property
    def record_out_call(self):
        """Gets the record_out_call of this PhoneNumber.  # noqa: E501


        :return: The record_out_call of this PhoneNumber.  # noqa: E501
        :rtype: bool
        """
        return self._record_out_call

    @record_out_call.setter
    def record_out_call(self, record_out_call):
        """Sets the record_out_call of this PhoneNumber.


        :param record_out_call: The record_out_call of this PhoneNumber.  # noqa: E501
        :type: bool
        """

        self._record_out_call = record_out_call

    @property
    def number(self):
        """Gets the number of this PhoneNumber.  # noqa: E501


        :return: The number of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PhoneNumber.


        :param number: The number of this PhoneNumber.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def name(self):
        """Gets the name of this PhoneNumber.  # noqa: E501


        :return: The name of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhoneNumber.


        :param name: The name of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def departmentid(self):
        """Gets the departmentid of this PhoneNumber.  # noqa: E501


        :return: The departmentid of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._departmentid

    @departmentid.setter
    def departmentid(self, departmentid):
        """Sets the departmentid of this PhoneNumber.


        :param departmentid: The departmentid of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._departmentid = departmentid

    @property
    def department(self):
        """Gets the department of this PhoneNumber.  # noqa: E501


        :return: The department of this PhoneNumber.  # noqa: E501
        :rtype: Department
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this PhoneNumber.


        :param department: The department of this PhoneNumber.  # noqa: E501
        :type: Department
        """

        self._department = department

    @property
    def status(self):
        """Gets the status of this PhoneNumber.  # noqa: E501

        A - Active, I - Inactive  # noqa: E501

        :return: The status of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PhoneNumber.

        A - Active, I - Inactive  # noqa: E501

        :param status: The status of this PhoneNumber.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "I"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this PhoneNumber.  # noqa: E501


        :return: The status_message of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this PhoneNumber.


        :param status_message: The status_message of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def host_settings(self):
        """Gets the host_settings of this PhoneNumber.  # noqa: E501

        json encoded host settings  # noqa: E501

        :return: The host_settings of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._host_settings

    @host_settings.setter
    def host_settings(self, host_settings):
        """Sets the host_settings of this PhoneNumber.

        json encoded host settings  # noqa: E501

        :param host_settings: The host_settings of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._host_settings = host_settings

    @property
    def host(self):
        """Gets the host of this PhoneNumber.  # noqa: E501


        :return: The host of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this PhoneNumber.


        :param host: The host of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this PhoneNumber.  # noqa: E501


        :return: The port of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this PhoneNumber.


        :param port: The port of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def user(self):
        """Gets the user of this PhoneNumber.  # noqa: E501


        :return: The user of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PhoneNumber.


        :param user: The user of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def auth_user(self):
        """Gets the auth_user of this PhoneNumber.  # noqa: E501


        :return: The auth_user of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._auth_user

    @auth_user.setter
    def auth_user(self, auth_user):
        """Sets the auth_user of this PhoneNumber.


        :param auth_user: The auth_user of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._auth_user = auth_user

    @property
    def password(self):
        """Gets the password of this PhoneNumber.  # noqa: E501


        :return: The password of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PhoneNumber.


        :param password: The password of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def proxy_host(self):
        """Gets the proxy_host of this PhoneNumber.  # noqa: E501


        :return: The proxy_host of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._proxy_host

    @proxy_host.setter
    def proxy_host(self, proxy_host):
        """Sets the proxy_host of this PhoneNumber.


        :param proxy_host: The proxy_host of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._proxy_host = proxy_host

    @property
    def proxy_port(self):
        """Gets the proxy_port of this PhoneNumber.  # noqa: E501


        :return: The proxy_port of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._proxy_port

    @proxy_port.setter
    def proxy_port(self, proxy_port):
        """Sets the proxy_port of this PhoneNumber.


        :param proxy_port: The proxy_port of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._proxy_port = proxy_port

    @property
    def proxy_user(self):
        """Gets the proxy_user of this PhoneNumber.  # noqa: E501


        :return: The proxy_user of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._proxy_user

    @proxy_user.setter
    def proxy_user(self, proxy_user):
        """Sets the proxy_user of this PhoneNumber.


        :param proxy_user: The proxy_user of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._proxy_user = proxy_user

    @property
    def providerid(self):
        """Gets the providerid of this PhoneNumber.  # noqa: E501


        :return: The providerid of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._providerid

    @providerid.setter
    def providerid(self, providerid):
        """Sets the providerid of this PhoneNumber.


        :param providerid: The providerid of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._providerid = providerid

    @property
    def ivr(self):
        """Gets the ivr of this PhoneNumber.  # noqa: E501


        :return: The ivr of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._ivr

    @ivr.setter
    def ivr(self, ivr):
        """Sets the ivr of this PhoneNumber.


        :param ivr: The ivr of this PhoneNumber.  # noqa: E501
        :type: str
        """

        self._ivr = ivr

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
        if issubclass(PhoneNumber, dict):
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
        if not isinstance(other, PhoneNumber):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhoneNumber):
            return True

        return self.to_dict() != other.to_dict()
