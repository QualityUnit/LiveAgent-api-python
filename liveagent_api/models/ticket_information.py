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


class TicketInformation(object):
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
        'ownerid': 'str',
        'owner_contactid': 'str',
        'departmentid': 'str',
        'agentid': 'str',
        'status': 'str',
        'tags': 'str',
        'code': 'str',
        'channel_type': 'str',
        'date_created': 'str',
        'public_access_urlcode': 'str',
        'subject': 'str',
        'custom_fields': 'list[CustomFields]'
    }

    attribute_map = {
        'id': 'id',
        'ownerid': 'ownerid',
        'owner_contactid': 'owner_contactid',
        'departmentid': 'departmentid',
        'agentid': 'agentid',
        'status': 'status',
        'tags': 'tags',
        'code': 'code',
        'channel_type': 'channel_type',
        'date_created': 'date_created',
        'public_access_urlcode': 'public_access_urlcode',
        'subject': 'subject',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, id=None, ownerid=None, owner_contactid=None, departmentid=None, agentid=None, status=None, tags=None, code=None, channel_type=None, date_created=None, public_access_urlcode=None, subject=None, custom_fields=None, _configuration=None):  # noqa: E501
        """TicketInformation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._ownerid = None
        self._owner_contactid = None
        self._departmentid = None
        self._agentid = None
        self._status = None
        self._tags = None
        self._code = None
        self._channel_type = None
        self._date_created = None
        self._public_access_urlcode = None
        self._subject = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ownerid is not None:
            self.ownerid = ownerid
        if owner_contactid is not None:
            self.owner_contactid = owner_contactid
        if departmentid is not None:
            self.departmentid = departmentid
        if agentid is not None:
            self.agentid = agentid
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if code is not None:
            self.code = code
        if channel_type is not None:
            self.channel_type = channel_type
        if date_created is not None:
            self.date_created = date_created
        if public_access_urlcode is not None:
            self.public_access_urlcode = public_access_urlcode
        if subject is not None:
            self.subject = subject
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this TicketInformation.  # noqa: E501


        :return: The id of this TicketInformation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TicketInformation.


        :param id: The id of this TicketInformation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ownerid(self):
        """Gets the ownerid of this TicketInformation.  # noqa: E501


        :return: The ownerid of this TicketInformation.  # noqa: E501
        :rtype: str
        """
        return self._ownerid

    @ownerid.setter
    def ownerid(self, ownerid):
        """Sets the ownerid of this TicketInformation.


        :param ownerid: The ownerid of this TicketInformation.  # noqa: E501
        :type: str
        """

        self._ownerid = ownerid

    @property
    def owner_contactid(self):
        """Gets the owner_contactid of this TicketInformation.  # noqa: E501


        :return: The owner_contactid of this TicketInformation.  # noqa: E501
        :rtype: str
        """
        return self._owner_contactid

    @owner_contactid.setter
    def owner_contactid(self, owner_contactid):
        """Sets the owner_contactid of this TicketInformation.


        :param owner_contactid: The owner_contactid of this TicketInformation.  # noqa: E501
        :type: str
        """

        self._owner_contactid = owner_contactid

    @property
    def departmentid(self):
        """Gets the departmentid of this TicketInformation.  # noqa: E501


        :return: The departmentid of this TicketInformation.  # noqa: E501
        :rtype: str
        """
        return self._departmentid

    @departmentid.setter
    def departmentid(self, departmentid):
        """Sets the departmentid of this TicketInformation.


        :param departmentid: The departmentid of this TicketInformation.  # noqa: E501
        :type: str
        """

        self._departmentid = departmentid

    @property
    def agentid(self):
        """Gets the agentid of this TicketInformation.  # noqa: E501


        :return: The agentid of this TicketInformation.  # noqa: E501
        :rtype: str
        """
        return self._agentid

    @agentid.setter
    def agentid(self, agentid):
        """Sets the agentid of this TicketInformation.


        :param agentid: The agentid of this TicketInformation.  # noqa: E501
        :type: str
        """

        self._agentid = agentid

    @property
    def status(self):
        """Gets the status of this TicketInformation.  # noqa: E501


        :return: The status of this TicketInformation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TicketInformation.


        :param status: The status of this TicketInformation.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this TicketInformation.  # noqa: E501


        :return: The tags of this TicketInformation.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TicketInformation.


        :param tags: The tags of this TicketInformation.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def code(self):
        """Gets the code of this TicketInformation.  # noqa: E501


        :return: The code of this TicketInformation.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TicketInformation.


        :param code: The code of this TicketInformation.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def channel_type(self):
        """Gets the channel_type of this TicketInformation.  # noqa: E501


        :return: The channel_type of this TicketInformation.  # noqa: E501
        :rtype: str
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """Sets the channel_type of this TicketInformation.


        :param channel_type: The channel_type of this TicketInformation.  # noqa: E501
        :type: str
        """

        self._channel_type = channel_type

    @property
    def date_created(self):
        """Gets the date_created of this TicketInformation.  # noqa: E501


        :return: The date_created of this TicketInformation.  # noqa: E501
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this TicketInformation.


        :param date_created: The date_created of this TicketInformation.  # noqa: E501
        :type: str
        """

        self._date_created = date_created

    @property
    def public_access_urlcode(self):
        """Gets the public_access_urlcode of this TicketInformation.  # noqa: E501


        :return: The public_access_urlcode of this TicketInformation.  # noqa: E501
        :rtype: str
        """
        return self._public_access_urlcode

    @public_access_urlcode.setter
    def public_access_urlcode(self, public_access_urlcode):
        """Sets the public_access_urlcode of this TicketInformation.


        :param public_access_urlcode: The public_access_urlcode of this TicketInformation.  # noqa: E501
        :type: str
        """

        self._public_access_urlcode = public_access_urlcode

    @property
    def subject(self):
        """Gets the subject of this TicketInformation.  # noqa: E501


        :return: The subject of this TicketInformation.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this TicketInformation.


        :param subject: The subject of this TicketInformation.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def custom_fields(self):
        """Gets the custom_fields of this TicketInformation.  # noqa: E501


        :return: The custom_fields of this TicketInformation.  # noqa: E501
        :rtype: list[CustomFields]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this TicketInformation.


        :param custom_fields: The custom_fields of this TicketInformation.  # noqa: E501
        :type: list[CustomFields]
        """

        self._custom_fields = custom_fields

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
        if issubclass(TicketInformation, dict):
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
        if not isinstance(other, TicketInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TicketInformation):
            return True

        return self.to_dict() != other.to_dict()
