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


class ViberAccount(object):
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
        'viber_account_id': 'str',
        'department_id': 'str',
        'name': 'str',
        'icon_url': 'str',
        'viber_uri': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'viber_account_id': 'viber_account_id',
        'department_id': 'department_id',
        'name': 'name',
        'icon_url': 'icon_url',
        'viber_uri': 'viber_uri',
        'status': 'status'
    }

    def __init__(self, id=None, viber_account_id=None, department_id=None, name=None, icon_url=None, viber_uri=None, status=None):  # noqa: E501
        """ViberAccount - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._viber_account_id = None
        self._department_id = None
        self._name = None
        self._icon_url = None
        self._viber_uri = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if viber_account_id is not None:
            self.viber_account_id = viber_account_id
        if department_id is not None:
            self.department_id = department_id
        if name is not None:
            self.name = name
        if icon_url is not None:
            self.icon_url = icon_url
        if viber_uri is not None:
            self.viber_uri = viber_uri
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this ViberAccount.  # noqa: E501


        :return: The id of this ViberAccount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ViberAccount.


        :param id: The id of this ViberAccount.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def viber_account_id(self):
        """Gets the viber_account_id of this ViberAccount.  # noqa: E501


        :return: The viber_account_id of this ViberAccount.  # noqa: E501
        :rtype: str
        """
        return self._viber_account_id

    @viber_account_id.setter
    def viber_account_id(self, viber_account_id):
        """Sets the viber_account_id of this ViberAccount.


        :param viber_account_id: The viber_account_id of this ViberAccount.  # noqa: E501
        :type: str
        """

        self._viber_account_id = viber_account_id

    @property
    def department_id(self):
        """Gets the department_id of this ViberAccount.  # noqa: E501


        :return: The department_id of this ViberAccount.  # noqa: E501
        :rtype: str
        """
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        """Sets the department_id of this ViberAccount.


        :param department_id: The department_id of this ViberAccount.  # noqa: E501
        :type: str
        """

        self._department_id = department_id

    @property
    def name(self):
        """Gets the name of this ViberAccount.  # noqa: E501


        :return: The name of this ViberAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ViberAccount.


        :param name: The name of this ViberAccount.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def icon_url(self):
        """Gets the icon_url of this ViberAccount.  # noqa: E501


        :return: The icon_url of this ViberAccount.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this ViberAccount.


        :param icon_url: The icon_url of this ViberAccount.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def viber_uri(self):
        """Gets the viber_uri of this ViberAccount.  # noqa: E501


        :return: The viber_uri of this ViberAccount.  # noqa: E501
        :rtype: str
        """
        return self._viber_uri

    @viber_uri.setter
    def viber_uri(self, viber_uri):
        """Sets the viber_uri of this ViberAccount.


        :param viber_uri: The viber_uri of this ViberAccount.  # noqa: E501
        :type: str
        """

        self._viber_uri = viber_uri

    @property
    def status(self):
        """Gets the status of this ViberAccount.  # noqa: E501

        A - Active (subscribed to events)<br>I - Inactive (unsubscribed from events)  # noqa: E501

        :return: The status of this ViberAccount.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ViberAccount.

        A - Active (subscribed to events)<br>I - Inactive (unsubscribed from events)  # noqa: E501

        :param status: The status of this ViberAccount.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "I"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(ViberAccount, dict):
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
        if not isinstance(other, ViberAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
