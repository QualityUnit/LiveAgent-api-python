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


class PredefinedAnswer(object):
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
        'userid': 'str',
        'departmentid': 'str',
        'name': 'str',
        'subject': 'str',
        'body': 'str',
        'format': 'str'
    }

    attribute_map = {
        'id': 'id',
        'userid': 'userid',
        'departmentid': 'departmentid',
        'name': 'name',
        'subject': 'subject',
        'body': 'body',
        'format': 'format'
    }

    def __init__(self, id=None, userid=None, departmentid=None, name=None, subject=None, body=None, format='T'):  # noqa: E501
        """PredefinedAnswer - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._userid = None
        self._departmentid = None
        self._name = None
        self._subject = None
        self._body = None
        self._format = None
        self.discriminator = None

        self.id = id
        if userid is not None:
            self.userid = userid
        if departmentid is not None:
            self.departmentid = departmentid
        if name is not None:
            self.name = name
        if subject is not None:
            self.subject = subject
        if body is not None:
            self.body = body
        if format is not None:
            self.format = format

    @property
    def id(self):
        """Gets the id of this PredefinedAnswer.  # noqa: E501


        :return: The id of this PredefinedAnswer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PredefinedAnswer.


        :param id: The id of this PredefinedAnswer.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def userid(self):
        """Gets the userid of this PredefinedAnswer.  # noqa: E501


        :return: The userid of this PredefinedAnswer.  # noqa: E501
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this PredefinedAnswer.


        :param userid: The userid of this PredefinedAnswer.  # noqa: E501
        :type: str
        """

        self._userid = userid

    @property
    def departmentid(self):
        """Gets the departmentid of this PredefinedAnswer.  # noqa: E501


        :return: The departmentid of this PredefinedAnswer.  # noqa: E501
        :rtype: str
        """
        return self._departmentid

    @departmentid.setter
    def departmentid(self, departmentid):
        """Sets the departmentid of this PredefinedAnswer.


        :param departmentid: The departmentid of this PredefinedAnswer.  # noqa: E501
        :type: str
        """

        self._departmentid = departmentid

    @property
    def name(self):
        """Gets the name of this PredefinedAnswer.  # noqa: E501


        :return: The name of this PredefinedAnswer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PredefinedAnswer.


        :param name: The name of this PredefinedAnswer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def subject(self):
        """Gets the subject of this PredefinedAnswer.  # noqa: E501


        :return: The subject of this PredefinedAnswer.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this PredefinedAnswer.


        :param subject: The subject of this PredefinedAnswer.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def body(self):
        """Gets the body of this PredefinedAnswer.  # noqa: E501


        :return: The body of this PredefinedAnswer.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this PredefinedAnswer.


        :param body: The body of this PredefinedAnswer.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def format(self):
        """Gets the format of this PredefinedAnswer.  # noqa: E501

        Format of body field: T - text, H - html  # noqa: E501

        :return: The format of this PredefinedAnswer.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this PredefinedAnswer.

        Format of body field: T - text, H - html  # noqa: E501

        :param format: The format of this PredefinedAnswer.  # noqa: E501
        :type: str
        """
        allowed_values = ["T", "H"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

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
        if issubclass(PredefinedAnswer, dict):
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
        if not isinstance(other, PredefinedAnswer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
