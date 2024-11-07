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


class Ticket(object):
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
        'owner_contactid': 'str',
        'owner_email': 'str',
        'owner_name': 'str',
        'departmentid': 'str',
        'agentid': 'str',
        'status': 'str',
        'tags': 'list[str]',
        'code': 'str',
        'channel_type': 'str',
        'date_created': 'str',
        'date_changed': 'str',
        'date_resolved': 'str',
        'date_due': 'str',
        'date_deleted': 'str',
        'last_activity': 'datetime',
        'last_activity_public': 'str',
        'public_access_urlcode': 'str',
        'subject': 'str',
        'custom_fields': 'list[CustomFields]'
    }

    attribute_map = {
        'id': 'id',
        'owner_contactid': 'owner_contactid',
        'owner_email': 'owner_email',
        'owner_name': 'owner_name',
        'departmentid': 'departmentid',
        'agentid': 'agentid',
        'status': 'status',
        'tags': 'tags',
        'code': 'code',
        'channel_type': 'channel_type',
        'date_created': 'date_created',
        'date_changed': 'date_changed',
        'date_resolved': 'date_resolved',
        'date_due': 'date_due',
        'date_deleted': 'date_deleted',
        'last_activity': 'last_activity',
        'last_activity_public': 'last_activity_public',
        'public_access_urlcode': 'public_access_urlcode',
        'subject': 'subject',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, id=None, owner_contactid=None, owner_email=None, owner_name=None, departmentid=None, agentid=None, status=None, tags=None, code=None, channel_type=None, date_created=None, date_changed=None, date_resolved=None, date_due=None, date_deleted=None, last_activity=None, last_activity_public=None, public_access_urlcode=None, subject=None, custom_fields=None, _configuration=None):  # noqa: E501
        """Ticket - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._owner_contactid = None
        self._owner_email = None
        self._owner_name = None
        self._departmentid = None
        self._agentid = None
        self._status = None
        self._tags = None
        self._code = None
        self._channel_type = None
        self._date_created = None
        self._date_changed = None
        self._date_resolved = None
        self._date_due = None
        self._date_deleted = None
        self._last_activity = None
        self._last_activity_public = None
        self._public_access_urlcode = None
        self._subject = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if owner_contactid is not None:
            self.owner_contactid = owner_contactid
        if owner_email is not None:
            self.owner_email = owner_email
        if owner_name is not None:
            self.owner_name = owner_name
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
        if date_changed is not None:
            self.date_changed = date_changed
        if date_resolved is not None:
            self.date_resolved = date_resolved
        if date_due is not None:
            self.date_due = date_due
        if date_deleted is not None:
            self.date_deleted = date_deleted
        if last_activity is not None:
            self.last_activity = last_activity
        if last_activity_public is not None:
            self.last_activity_public = last_activity_public
        if public_access_urlcode is not None:
            self.public_access_urlcode = public_access_urlcode
        if subject is not None:
            self.subject = subject
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this Ticket.  # noqa: E501


        :return: The id of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Ticket.


        :param id: The id of this Ticket.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def owner_contactid(self):
        """Gets the owner_contactid of this Ticket.  # noqa: E501


        :return: The owner_contactid of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._owner_contactid

    @owner_contactid.setter
    def owner_contactid(self, owner_contactid):
        """Sets the owner_contactid of this Ticket.


        :param owner_contactid: The owner_contactid of this Ticket.  # noqa: E501
        :type: str
        """

        self._owner_contactid = owner_contactid

    @property
    def owner_email(self):
        """Gets the owner_email of this Ticket.  # noqa: E501


        :return: The owner_email of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._owner_email

    @owner_email.setter
    def owner_email(self, owner_email):
        """Sets the owner_email of this Ticket.


        :param owner_email: The owner_email of this Ticket.  # noqa: E501
        :type: str
        """

        self._owner_email = owner_email

    @property
    def owner_name(self):
        """Gets the owner_name of this Ticket.  # noqa: E501


        :return: The owner_name of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this Ticket.


        :param owner_name: The owner_name of this Ticket.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def departmentid(self):
        """Gets the departmentid of this Ticket.  # noqa: E501


        :return: The departmentid of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._departmentid

    @departmentid.setter
    def departmentid(self, departmentid):
        """Sets the departmentid of this Ticket.


        :param departmentid: The departmentid of this Ticket.  # noqa: E501
        :type: str
        """

        self._departmentid = departmentid

    @property
    def agentid(self):
        """Gets the agentid of this Ticket.  # noqa: E501


        :return: The agentid of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._agentid

    @agentid.setter
    def agentid(self, agentid):
        """Sets the agentid of this Ticket.


        :param agentid: The agentid of this Ticket.  # noqa: E501
        :type: str
        """

        self._agentid = agentid

    @property
    def status(self):
        """Gets the status of this Ticket.  # noqa: E501

        <br> I - init<br> N - new<br> T - chatting<br> P - calling<br> R - resolved<br> X - deleted<br> B - spam<br> A - answered<br> C - open<br> W - postponed<br> L - closed  # noqa: E501

        :return: The status of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Ticket.

        <br> I - init<br> N - new<br> T - chatting<br> P - calling<br> R - resolved<br> X - deleted<br> B - spam<br> A - answered<br> C - open<br> W - postponed<br> L - closed  # noqa: E501

        :param status: The status of this Ticket.  # noqa: E501
        :type: str
        """
        allowed_values = ["I", "N", "T", "P", "R", "X", "B", "A", "C", "W", "L"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this Ticket.  # noqa: E501


        :return: The tags of this Ticket.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Ticket.


        :param tags: The tags of this Ticket.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def code(self):
        """Gets the code of this Ticket.  # noqa: E501


        :return: The code of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Ticket.


        :param code: The code of this Ticket.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def channel_type(self):
        """Gets the channel_type of this Ticket.  # noqa: E501

        <br> E - email<br> B - contact button<br> M - contact form<br> I - invitation<br> C - call<br> W - call button<br> F - facebook<br> A - facebook message<br> T - twitter<br> Q - forum<br> S - suggestion  # noqa: E501

        :return: The channel_type of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """Sets the channel_type of this Ticket.

        <br> E - email<br> B - contact button<br> M - contact form<br> I - invitation<br> C - call<br> W - call button<br> F - facebook<br> A - facebook message<br> T - twitter<br> Q - forum<br> S - suggestion  # noqa: E501

        :param channel_type: The channel_type of this Ticket.  # noqa: E501
        :type: str
        """

        self._channel_type = channel_type

    @property
    def date_created(self):
        """Gets the date_created of this Ticket.  # noqa: E501


        :return: The date_created of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Ticket.


        :param date_created: The date_created of this Ticket.  # noqa: E501
        :type: str
        """

        self._date_created = date_created

    @property
    def date_changed(self):
        """Gets the date_changed of this Ticket.  # noqa: E501


        :return: The date_changed of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._date_changed

    @date_changed.setter
    def date_changed(self, date_changed):
        """Sets the date_changed of this Ticket.


        :param date_changed: The date_changed of this Ticket.  # noqa: E501
        :type: str
        """

        self._date_changed = date_changed

    @property
    def date_resolved(self):
        """Gets the date_resolved of this Ticket.  # noqa: E501


        :return: The date_resolved of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._date_resolved

    @date_resolved.setter
    def date_resolved(self, date_resolved):
        """Sets the date_resolved of this Ticket.


        :param date_resolved: The date_resolved of this Ticket.  # noqa: E501
        :type: str
        """

        self._date_resolved = date_resolved

    @property
    def date_due(self):
        """Gets the date_due of this Ticket.  # noqa: E501


        :return: The date_due of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._date_due

    @date_due.setter
    def date_due(self, date_due):
        """Sets the date_due of this Ticket.


        :param date_due: The date_due of this Ticket.  # noqa: E501
        :type: str
        """

        self._date_due = date_due

    @property
    def date_deleted(self):
        """Gets the date_deleted of this Ticket.  # noqa: E501


        :return: The date_deleted of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._date_deleted

    @date_deleted.setter
    def date_deleted(self, date_deleted):
        """Sets the date_deleted of this Ticket.


        :param date_deleted: The date_deleted of this Ticket.  # noqa: E501
        :type: str
        """

        self._date_deleted = date_deleted

    @property
    def last_activity(self):
        """Gets the last_activity of this Ticket.  # noqa: E501


        :return: The last_activity of this Ticket.  # noqa: E501
        :rtype: datetime
        """
        return self._last_activity

    @last_activity.setter
    def last_activity(self, last_activity):
        """Sets the last_activity of this Ticket.


        :param last_activity: The last_activity of this Ticket.  # noqa: E501
        :type: datetime
        """

        self._last_activity = last_activity

    @property
    def last_activity_public(self):
        """Gets the last_activity_public of this Ticket.  # noqa: E501


        :return: The last_activity_public of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._last_activity_public

    @last_activity_public.setter
    def last_activity_public(self, last_activity_public):
        """Sets the last_activity_public of this Ticket.


        :param last_activity_public: The last_activity_public of this Ticket.  # noqa: E501
        :type: str
        """

        self._last_activity_public = last_activity_public

    @property
    def public_access_urlcode(self):
        """Gets the public_access_urlcode of this Ticket.  # noqa: E501


        :return: The public_access_urlcode of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._public_access_urlcode

    @public_access_urlcode.setter
    def public_access_urlcode(self, public_access_urlcode):
        """Sets the public_access_urlcode of this Ticket.


        :param public_access_urlcode: The public_access_urlcode of this Ticket.  # noqa: E501
        :type: str
        """

        self._public_access_urlcode = public_access_urlcode

    @property
    def subject(self):
        """Gets the subject of this Ticket.  # noqa: E501


        :return: The subject of this Ticket.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Ticket.


        :param subject: The subject of this Ticket.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Ticket.  # noqa: E501


        :return: The custom_fields of this Ticket.  # noqa: E501
        :rtype: list[CustomFields]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Ticket.


        :param custom_fields: The custom_fields of this Ticket.  # noqa: E501
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
        if issubclass(Ticket, dict):
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
        if not isinstance(other, Ticket):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Ticket):
            return True

        return self.to_dict() != other.to_dict()
