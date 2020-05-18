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


class AgentRow(object):
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
        'agentid': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'system_name': 'str',
        'username': 'str',
        'countrycode': 'str',
        'avatar_url': 'str',
        'roleid': 'str',
        'rolename': 'str',
        'departmentid': 'str',
        'twofa': 'str'
    }

    attribute_map = {
        'agentid': 'agentid',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'system_name': 'system_name',
        'username': 'username',
        'countrycode': 'countrycode',
        'avatar_url': 'avatar_url',
        'roleid': 'roleid',
        'rolename': 'rolename',
        'departmentid': 'departmentid',
        'twofa': 'twofa'
    }

    def __init__(self, agentid=None, firstname=None, lastname=None, system_name=None, username=None, countrycode=None, avatar_url=None, roleid=None, rolename=None, departmentid=None, twofa=None):  # noqa: E501
        """AgentRow - a model defined in Swagger"""  # noqa: E501

        self._agentid = None
        self._firstname = None
        self._lastname = None
        self._system_name = None
        self._username = None
        self._countrycode = None
        self._avatar_url = None
        self._roleid = None
        self._rolename = None
        self._departmentid = None
        self._twofa = None
        self.discriminator = None

        if agentid is not None:
            self.agentid = agentid
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if system_name is not None:
            self.system_name = system_name
        if username is not None:
            self.username = username
        if countrycode is not None:
            self.countrycode = countrycode
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if roleid is not None:
            self.roleid = roleid
        if rolename is not None:
            self.rolename = rolename
        if departmentid is not None:
            self.departmentid = departmentid
        if twofa is not None:
            self.twofa = twofa

    @property
    def agentid(self):
        """Gets the agentid of this AgentRow.  # noqa: E501


        :return: The agentid of this AgentRow.  # noqa: E501
        :rtype: str
        """
        return self._agentid

    @agentid.setter
    def agentid(self, agentid):
        """Sets the agentid of this AgentRow.


        :param agentid: The agentid of this AgentRow.  # noqa: E501
        :type: str
        """

        self._agentid = agentid

    @property
    def firstname(self):
        """Gets the firstname of this AgentRow.  # noqa: E501


        :return: The firstname of this AgentRow.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this AgentRow.


        :param firstname: The firstname of this AgentRow.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this AgentRow.  # noqa: E501


        :return: The lastname of this AgentRow.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this AgentRow.


        :param lastname: The lastname of this AgentRow.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def system_name(self):
        """Gets the system_name of this AgentRow.  # noqa: E501


        :return: The system_name of this AgentRow.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this AgentRow.


        :param system_name: The system_name of this AgentRow.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

    @property
    def username(self):
        """Gets the username of this AgentRow.  # noqa: E501


        :return: The username of this AgentRow.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AgentRow.


        :param username: The username of this AgentRow.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def countrycode(self):
        """Gets the countrycode of this AgentRow.  # noqa: E501


        :return: The countrycode of this AgentRow.  # noqa: E501
        :rtype: str
        """
        return self._countrycode

    @countrycode.setter
    def countrycode(self, countrycode):
        """Sets the countrycode of this AgentRow.


        :param countrycode: The countrycode of this AgentRow.  # noqa: E501
        :type: str
        """

        self._countrycode = countrycode

    @property
    def avatar_url(self):
        """Gets the avatar_url of this AgentRow.  # noqa: E501


        :return: The avatar_url of this AgentRow.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this AgentRow.


        :param avatar_url: The avatar_url of this AgentRow.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def roleid(self):
        """Gets the roleid of this AgentRow.  # noqa: E501


        :return: The roleid of this AgentRow.  # noqa: E501
        :rtype: str
        """
        return self._roleid

    @roleid.setter
    def roleid(self, roleid):
        """Sets the roleid of this AgentRow.


        :param roleid: The roleid of this AgentRow.  # noqa: E501
        :type: str
        """

        self._roleid = roleid

    @property
    def rolename(self):
        """Gets the rolename of this AgentRow.  # noqa: E501


        :return: The rolename of this AgentRow.  # noqa: E501
        :rtype: str
        """
        return self._rolename

    @rolename.setter
    def rolename(self, rolename):
        """Sets the rolename of this AgentRow.


        :param rolename: The rolename of this AgentRow.  # noqa: E501
        :type: str
        """

        self._rolename = rolename

    @property
    def departmentid(self):
        """Gets the departmentid of this AgentRow.  # noqa: E501


        :return: The departmentid of this AgentRow.  # noqa: E501
        :rtype: str
        """
        return self._departmentid

    @departmentid.setter
    def departmentid(self, departmentid):
        """Sets the departmentid of this AgentRow.


        :param departmentid: The departmentid of this AgentRow.  # noqa: E501
        :type: str
        """

        self._departmentid = departmentid

    @property
    def twofa(self):
        """Gets the twofa of this AgentRow.  # noqa: E501


        :return: The twofa of this AgentRow.  # noqa: E501
        :rtype: str
        """
        return self._twofa

    @twofa.setter
    def twofa(self, twofa):
        """Sets the twofa of this AgentRow.


        :param twofa: The twofa of this AgentRow.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N", ""]  # noqa: E501
        if twofa not in allowed_values:
            raise ValueError(
                "Invalid value for `twofa` ({0}), must be one of {1}"  # noqa: E501
                .format(twofa, allowed_values)
            )

        self._twofa = twofa

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
        if issubclass(AgentRow, dict):
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
        if not isinstance(other, AgentRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other