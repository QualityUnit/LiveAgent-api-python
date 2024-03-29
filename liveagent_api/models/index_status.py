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


class IndexStatus(object):
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
        'index_count': 'str',
        'datechanged': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'index_count': 'index_count',
        'datechanged': 'datechanged'
    }

    def __init__(self, id=None, index_count=None, datechanged=None, _configuration=None):  # noqa: E501
        """IndexStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._index_count = None
        self._datechanged = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if index_count is not None:
            self.index_count = index_count
        if datechanged is not None:
            self.datechanged = datechanged

    @property
    def id(self):
        """Gets the id of this IndexStatus.  # noqa: E501


        :return: The id of this IndexStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IndexStatus.


        :param id: The id of this IndexStatus.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def index_count(self):
        """Gets the index_count of this IndexStatus.  # noqa: E501


        :return: The index_count of this IndexStatus.  # noqa: E501
        :rtype: str
        """
        return self._index_count

    @index_count.setter
    def index_count(self, index_count):
        """Sets the index_count of this IndexStatus.


        :param index_count: The index_count of this IndexStatus.  # noqa: E501
        :type: str
        """

        self._index_count = index_count

    @property
    def datechanged(self):
        """Gets the datechanged of this IndexStatus.  # noqa: E501


        :return: The datechanged of this IndexStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._datechanged

    @datechanged.setter
    def datechanged(self, datechanged):
        """Sets the datechanged of this IndexStatus.


        :param datechanged: The datechanged of this IndexStatus.  # noqa: E501
        :type: datetime
        """

        self._datechanged = datechanged

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
        if issubclass(IndexStatus, dict):
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
        if not isinstance(other, IndexStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IndexStatus):
            return True

        return self.to_dict() != other.to_dict()
