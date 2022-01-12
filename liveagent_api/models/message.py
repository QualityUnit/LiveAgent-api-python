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


class Message(object):
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
        'type': 'str',
        'datecreated': 'datetime',
        'format': 'str',
        'message': 'str',
        'visibility': 'str'
    }

    attribute_map = {
        'id': 'id',
        'userid': 'userid',
        'type': 'type',
        'datecreated': 'datecreated',
        'format': 'format',
        'message': 'message',
        'visibility': 'visibility'
    }

    def __init__(self, id=None, userid=None, type=None, datecreated=None, format=None, message=None, visibility=None):  # noqa: E501
        """Message - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._userid = None
        self._type = None
        self._datecreated = None
        self._format = None
        self._message = None
        self._visibility = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if userid is not None:
            self.userid = userid
        if type is not None:
            self.type = type
        if datecreated is not None:
            self.datecreated = datecreated
        if format is not None:
            self.format = format
        if message is not None:
            self.message = message
        if visibility is not None:
            self.visibility = visibility

    @property
    def id(self):
        """Gets the id of this Message.  # noqa: E501


        :return: The id of this Message.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Message.


        :param id: The id of this Message.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def userid(self):
        """Gets the userid of this Message.  # noqa: E501


        :return: The userid of this Message.  # noqa: E501
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this Message.


        :param userid: The userid of this Message.  # noqa: E501
        :type: str
        """

        self._userid = userid

    @property
    def type(self):
        """Gets the type of this Message.  # noqa: E501

        M - MESSAGE Y - MESSAGE_LEGACY Q - QUOTED_TEXT I - INTERNAL F - FILE T - TITLE E - END D - DISCONNECT H - HEADER R - TRANSFER S - SYSTEM U - USERAGENT G - TAG V - VOICE 1 - VOICE_INTERNAL N - NOTE L - NOTE_FILE Z - FORMFIELD A - TEXT_HEADER O - TEXT_FOOTER J - STATUS B - SPLITTED W - RANKING_FEATURE_REWARD P - RANKING_FEATURE_PUNISHMENT C - RANKING_FEATURE_COMMENT K - SYSTEM_PUBLIC X - SYSTEM_VISITOR 0 - ERROR_FOOTER 2 - MERGED 3 - INVITATION_REROUTE  # noqa: E501

        :return: The type of this Message.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Message.

        M - MESSAGE Y - MESSAGE_LEGACY Q - QUOTED_TEXT I - INTERNAL F - FILE T - TITLE E - END D - DISCONNECT H - HEADER R - TRANSFER S - SYSTEM U - USERAGENT G - TAG V - VOICE 1 - VOICE_INTERNAL N - NOTE L - NOTE_FILE Z - FORMFIELD A - TEXT_HEADER O - TEXT_FOOTER J - STATUS B - SPLITTED W - RANKING_FEATURE_REWARD P - RANKING_FEATURE_PUNISHMENT C - RANKING_FEATURE_COMMENT K - SYSTEM_PUBLIC X - SYSTEM_VISITOR 0 - ERROR_FOOTER 2 - MERGED 3 - INVITATION_REROUTE  # noqa: E501

        :param type: The type of this Message.  # noqa: E501
        :type: str
        """
        allowed_values = ["M", "Y", "Q", "I", "F", "T", "E", "D", "H", "R", "S", "U", "G", "V", "1", "N", "L", "Z", "A", "O", "J", "B", "W", "P", "C", "K", "X", "0", "2", "3"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def datecreated(self):
        """Gets the datecreated of this Message.  # noqa: E501


        :return: The datecreated of this Message.  # noqa: E501
        :rtype: datetime
        """
        return self._datecreated

    @datecreated.setter
    def datecreated(self, datecreated):
        """Sets the datecreated of this Message.


        :param datecreated: The datecreated of this Message.  # noqa: E501
        :type: datetime
        """

        self._datecreated = datecreated

    @property
    def format(self):
        """Gets the format of this Message.  # noqa: E501

        T - TEXT H - HTML J - JSON X - TEXT_LEGACY // text with possibility of internal form links (e.g. note, ranking comment, quoted, header, footer, internal) Y - HTML_LEGACY // html with possibility of internal form links (e.g. tag) Z - JSON_LEGACY // json with possibility of internal form links (e.g. footer)  # noqa: E501

        :return: The format of this Message.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Message.

        T - TEXT H - HTML J - JSON X - TEXT_LEGACY // text with possibility of internal form links (e.g. note, ranking comment, quoted, header, footer, internal) Y - HTML_LEGACY // html with possibility of internal form links (e.g. tag) Z - JSON_LEGACY // json with possibility of internal form links (e.g. footer)  # noqa: E501

        :param format: The format of this Message.  # noqa: E501
        :type: str
        """
        allowed_values = ["T", "H", "J", "X", "Y", "Z"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def message(self):
        """Gets the message of this Message.  # noqa: E501


        :return: The message of this Message.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Message.


        :param message: The message of this Message.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def visibility(self):
        """Gets the visibility of this Message.  # noqa: E501


        :return: The visibility of this Message.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this Message.


        :param visibility: The visibility of this Message.  # noqa: E501
        :type: str
        """

        self._visibility = visibility

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
        if issubclass(Message, dict):
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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
