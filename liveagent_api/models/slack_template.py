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


class SlackTemplate(object):
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
        'body': 'str',
        'class_name': 'str',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'body': 'body',
        'class_name': 'class_name',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, body=None, class_name=None, name=None, id=None):  # noqa: E501
        """SlackTemplate - a model defined in Swagger"""  # noqa: E501

        self._body = None
        self._class_name = None
        self._name = None
        self._id = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if class_name is not None:
            self.class_name = class_name
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def body(self):
        """Gets the body of this SlackTemplate.  # noqa: E501


        :return: The body of this SlackTemplate.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SlackTemplate.


        :param body: The body of this SlackTemplate.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def class_name(self):
        """Gets the class_name of this SlackTemplate.  # noqa: E501


        :return: The class_name of this SlackTemplate.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this SlackTemplate.


        :param class_name: The class_name of this SlackTemplate.  # noqa: E501
        :type: str
        """

        self._class_name = class_name

    @property
    def name(self):
        """Gets the name of this SlackTemplate.  # noqa: E501


        :return: The name of this SlackTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SlackTemplate.


        :param name: The name of this SlackTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this SlackTemplate.  # noqa: E501


        :return: The id of this SlackTemplate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlackTemplate.


        :param id: The id of this SlackTemplate.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(SlackTemplate, dict):
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
        if not isinstance(other, SlackTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
