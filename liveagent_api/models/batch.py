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


class Batch(object):
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
        'is_committed': 'bool',
        'item_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'is_committed': 'is_committed',
        'item_count': 'item_count'
    }

    def __init__(self, id=None, is_committed=None, item_count=None, _configuration=None):  # noqa: E501
        """Batch - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._is_committed = None
        self._item_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if is_committed is not None:
            self.is_committed = is_committed
        if item_count is not None:
            self.item_count = item_count

    @property
    def id(self):
        """Gets the id of this Batch.  # noqa: E501


        :return: The id of this Batch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Batch.


        :param id: The id of this Batch.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_committed(self):
        """Gets the is_committed of this Batch.  # noqa: E501


        :return: The is_committed of this Batch.  # noqa: E501
        :rtype: bool
        """
        return self._is_committed

    @is_committed.setter
    def is_committed(self, is_committed):
        """Sets the is_committed of this Batch.


        :param is_committed: The is_committed of this Batch.  # noqa: E501
        :type: bool
        """

        self._is_committed = is_committed

    @property
    def item_count(self):
        """Gets the item_count of this Batch.  # noqa: E501


        :return: The item_count of this Batch.  # noqa: E501
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """Sets the item_count of this Batch.


        :param item_count: The item_count of this Batch.  # noqa: E501
        :type: int
        """

        self._item_count = item_count

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
        if issubclass(Batch, dict):
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
        if not isinstance(other, Batch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Batch):
            return True

        return self.to_dict() != other.to_dict()
