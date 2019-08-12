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


class EventLogRow(object):
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
        'logid': 'str',
        'line': 'str',
        'filename': 'str',
        'created': 'str',
        'level': 'str',
        'type': 'str',
        'message': 'str',
        'ip': 'str',
        'groupid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'logid': 'logid',
        'line': 'line',
        'filename': 'filename',
        'created': 'created',
        'level': 'level',
        'type': 'type',
        'message': 'message',
        'ip': 'ip',
        'groupid': 'groupid'
    }

    def __init__(self, id=None, logid=None, line=None, filename=None, created=None, level=None, type=None, message=None, ip=None, groupid=None):  # noqa: E501
        """EventLogRow - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._logid = None
        self._line = None
        self._filename = None
        self._created = None
        self._level = None
        self._type = None
        self._message = None
        self._ip = None
        self._groupid = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if logid is not None:
            self.logid = logid
        if line is not None:
            self.line = line
        if filename is not None:
            self.filename = filename
        if created is not None:
            self.created = created
        if level is not None:
            self.level = level
        if type is not None:
            self.type = type
        if message is not None:
            self.message = message
        if ip is not None:
            self.ip = ip
        if groupid is not None:
            self.groupid = groupid

    @property
    def id(self):
        """Gets the id of this EventLogRow.  # noqa: E501


        :return: The id of this EventLogRow.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventLogRow.


        :param id: The id of this EventLogRow.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def logid(self):
        """Gets the logid of this EventLogRow.  # noqa: E501


        :return: The logid of this EventLogRow.  # noqa: E501
        :rtype: str
        """
        return self._logid

    @logid.setter
    def logid(self, logid):
        """Sets the logid of this EventLogRow.


        :param logid: The logid of this EventLogRow.  # noqa: E501
        :type: str
        """

        self._logid = logid

    @property
    def line(self):
        """Gets the line of this EventLogRow.  # noqa: E501


        :return: The line of this EventLogRow.  # noqa: E501
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this EventLogRow.


        :param line: The line of this EventLogRow.  # noqa: E501
        :type: str
        """

        self._line = line

    @property
    def filename(self):
        """Gets the filename of this EventLogRow.  # noqa: E501


        :return: The filename of this EventLogRow.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this EventLogRow.


        :param filename: The filename of this EventLogRow.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def created(self):
        """Gets the created of this EventLogRow.  # noqa: E501


        :return: The created of this EventLogRow.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EventLogRow.


        :param created: The created of this EventLogRow.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def level(self):
        """Gets the level of this EventLogRow.  # noqa: E501


        :return: The level of this EventLogRow.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this EventLogRow.


        :param level: The level of this EventLogRow.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def type(self):
        """Gets the type of this EventLogRow.  # noqa: E501


        :return: The type of this EventLogRow.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EventLogRow.


        :param type: The type of this EventLogRow.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def message(self):
        """Gets the message of this EventLogRow.  # noqa: E501


        :return: The message of this EventLogRow.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this EventLogRow.


        :param message: The message of this EventLogRow.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def ip(self):
        """Gets the ip of this EventLogRow.  # noqa: E501


        :return: The ip of this EventLogRow.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this EventLogRow.


        :param ip: The ip of this EventLogRow.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def groupid(self):
        """Gets the groupid of this EventLogRow.  # noqa: E501


        :return: The groupid of this EventLogRow.  # noqa: E501
        :rtype: str
        """
        return self._groupid

    @groupid.setter
    def groupid(self, groupid):
        """Sets the groupid of this EventLogRow.


        :param groupid: The groupid of this EventLogRow.  # noqa: E501
        :type: str
        """

        self._groupid = groupid

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
        if issubclass(EventLogRow, dict):
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
        if not isinstance(other, EventLogRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
