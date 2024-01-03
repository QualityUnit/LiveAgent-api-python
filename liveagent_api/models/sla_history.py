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


class SlaHistory(object):
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
        'sla_level_id': 'str',
        'sla_type': 'str',
        'date_created': 'str',
        'date_due': 'str',
        'date_closed': 'str',
        'total_time': 'int',
        'elapsed_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'sla_level_id': 'sla_level_id',
        'sla_type': 'sla_type',
        'date_created': 'date_created',
        'date_due': 'date_due',
        'date_closed': 'date_closed',
        'total_time': 'total_time',
        'elapsed_time': 'elapsed_time'
    }

    def __init__(self, id=None, sla_level_id=None, sla_type=None, date_created=None, date_due=None, date_closed=None, total_time=None, elapsed_time=None, _configuration=None):  # noqa: E501
        """SlaHistory - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._sla_level_id = None
        self._sla_type = None
        self._date_created = None
        self._date_due = None
        self._date_closed = None
        self._total_time = None
        self._elapsed_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sla_level_id is not None:
            self.sla_level_id = sla_level_id
        if sla_type is not None:
            self.sla_type = sla_type
        if date_created is not None:
            self.date_created = date_created
        if date_due is not None:
            self.date_due = date_due
        if date_closed is not None:
            self.date_closed = date_closed
        if total_time is not None:
            self.total_time = total_time
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time

    @property
    def id(self):
        """Gets the id of this SlaHistory.  # noqa: E501


        :return: The id of this SlaHistory.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlaHistory.


        :param id: The id of this SlaHistory.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sla_level_id(self):
        """Gets the sla_level_id of this SlaHistory.  # noqa: E501


        :return: The sla_level_id of this SlaHistory.  # noqa: E501
        :rtype: str
        """
        return self._sla_level_id

    @sla_level_id.setter
    def sla_level_id(self, sla_level_id):
        """Sets the sla_level_id of this SlaHistory.


        :param sla_level_id: The sla_level_id of this SlaHistory.  # noqa: E501
        :type: str
        """

        self._sla_level_id = sla_level_id

    @property
    def sla_type(self):
        """Gets the sla_type of this SlaHistory.  # noqa: E501


        :return: The sla_type of this SlaHistory.  # noqa: E501
        :rtype: str
        """
        return self._sla_type

    @sla_type.setter
    def sla_type(self, sla_type):
        """Sets the sla_type of this SlaHistory.


        :param sla_type: The sla_type of this SlaHistory.  # noqa: E501
        :type: str
        """

        self._sla_type = sla_type

    @property
    def date_created(self):
        """Gets the date_created of this SlaHistory.  # noqa: E501


        :return: The date_created of this SlaHistory.  # noqa: E501
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SlaHistory.


        :param date_created: The date_created of this SlaHistory.  # noqa: E501
        :type: str
        """

        self._date_created = date_created

    @property
    def date_due(self):
        """Gets the date_due of this SlaHistory.  # noqa: E501


        :return: The date_due of this SlaHistory.  # noqa: E501
        :rtype: str
        """
        return self._date_due

    @date_due.setter
    def date_due(self, date_due):
        """Sets the date_due of this SlaHistory.


        :param date_due: The date_due of this SlaHistory.  # noqa: E501
        :type: str
        """

        self._date_due = date_due

    @property
    def date_closed(self):
        """Gets the date_closed of this SlaHistory.  # noqa: E501


        :return: The date_closed of this SlaHistory.  # noqa: E501
        :rtype: str
        """
        return self._date_closed

    @date_closed.setter
    def date_closed(self, date_closed):
        """Sets the date_closed of this SlaHistory.


        :param date_closed: The date_closed of this SlaHistory.  # noqa: E501
        :type: str
        """

        self._date_closed = date_closed

    @property
    def total_time(self):
        """Gets the total_time of this SlaHistory.  # noqa: E501


        :return: The total_time of this SlaHistory.  # noqa: E501
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this SlaHistory.


        :param total_time: The total_time of this SlaHistory.  # noqa: E501
        :type: int
        """

        self._total_time = total_time

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this SlaHistory.  # noqa: E501


        :return: The elapsed_time of this SlaHistory.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this SlaHistory.


        :param elapsed_time: The elapsed_time of this SlaHistory.  # noqa: E501
        :type: int
        """

        self._elapsed_time = elapsed_time

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
        if issubclass(SlaHistory, dict):
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
        if not isinstance(other, SlaHistory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SlaHistory):
            return True

        return self.to_dict() != other.to_dict()
