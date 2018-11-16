# coding: utf-8

"""
    LiveAgent API

    LiveAgent API  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from liveagent_api.models.custom_fields import CustomFields  # noqa: F401,E501


class TicketListItem(object):
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
        'useridentifier': 'str',
        'subject': 'str',
        'departmentid': 'str',
        'recipient': 'str',
        'message': 'str',
        'date_created': 'str',
        'recipient_name': 'str',
        'carbon_copy': 'str',
        'blind_carbon_copy': 'str',
        'status': 'str',
        'mail_message_id': 'str',
        'do_not_send_mail': 'str',
        'use_template': 'str',
        'is_html_message': 'str',
        'custom_fields': 'list[CustomFields]',
        'tags': 'list[str]',
        'attachments': 'str'
    }

    attribute_map = {
        'useridentifier': 'useridentifier',
        'subject': 'subject',
        'departmentid': 'departmentid',
        'recipient': 'recipient',
        'message': 'message',
        'date_created': 'date_created',
        'recipient_name': 'recipient_name',
        'carbon_copy': 'carbon_copy',
        'blind_carbon_copy': 'blind_carbon_copy',
        'status': 'status',
        'mail_message_id': 'mail_message_id',
        'do_not_send_mail': 'do_not_send_mail',
        'use_template': 'use_template',
        'is_html_message': 'is_html_message',
        'custom_fields': 'custom_fields',
        'tags': 'tags',
        'attachments': 'attachments'
    }

    def __init__(self, useridentifier=None, subject=None, departmentid=None, recipient=None, message=None, date_created=None, recipient_name=None, carbon_copy=None, blind_carbon_copy=None, status='N', mail_message_id=None, do_not_send_mail='N', use_template='Y', is_html_message='N', custom_fields=None, tags=None, attachments=None):  # noqa: E501
        """TicketListItem - a model defined in Swagger"""  # noqa: E501

        self._useridentifier = None
        self._subject = None
        self._departmentid = None
        self._recipient = None
        self._message = None
        self._date_created = None
        self._recipient_name = None
        self._carbon_copy = None
        self._blind_carbon_copy = None
        self._status = None
        self._mail_message_id = None
        self._do_not_send_mail = None
        self._use_template = None
        self._is_html_message = None
        self._custom_fields = None
        self._tags = None
        self._attachments = None
        self.discriminator = None

        self.useridentifier = useridentifier
        self.subject = subject
        self.departmentid = departmentid
        self.recipient = recipient
        self.message = message
        if date_created is not None:
            self.date_created = date_created
        if recipient_name is not None:
            self.recipient_name = recipient_name
        if carbon_copy is not None:
            self.carbon_copy = carbon_copy
        if blind_carbon_copy is not None:
            self.blind_carbon_copy = blind_carbon_copy
        if status is not None:
            self.status = status
        if mail_message_id is not None:
            self.mail_message_id = mail_message_id
        if do_not_send_mail is not None:
            self.do_not_send_mail = do_not_send_mail
        if use_template is not None:
            self.use_template = use_template
        if is_html_message is not None:
            self.is_html_message = is_html_message
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if tags is not None:
            self.tags = tags
        if attachments is not None:
            self.attachments = attachments

    @property
    def useridentifier(self):
        """Gets the useridentifier of this TicketListItem.  # noqa: E501


        :return: The useridentifier of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._useridentifier

    @useridentifier.setter
    def useridentifier(self, useridentifier):
        """Sets the useridentifier of this TicketListItem.


        :param useridentifier: The useridentifier of this TicketListItem.  # noqa: E501
        :type: str
        """
        if useridentifier is None:
            raise ValueError("Invalid value for `useridentifier`, must not be `None`")  # noqa: E501

        self._useridentifier = useridentifier

    @property
    def subject(self):
        """Gets the subject of this TicketListItem.  # noqa: E501


        :return: The subject of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this TicketListItem.


        :param subject: The subject of this TicketListItem.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def departmentid(self):
        """Gets the departmentid of this TicketListItem.  # noqa: E501


        :return: The departmentid of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._departmentid

    @departmentid.setter
    def departmentid(self, departmentid):
        """Sets the departmentid of this TicketListItem.


        :param departmentid: The departmentid of this TicketListItem.  # noqa: E501
        :type: str
        """
        if departmentid is None:
            raise ValueError("Invalid value for `departmentid`, must not be `None`")  # noqa: E501

        self._departmentid = departmentid

    @property
    def recipient(self):
        """Gets the recipient of this TicketListItem.  # noqa: E501


        :return: The recipient of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this TicketListItem.


        :param recipient: The recipient of this TicketListItem.  # noqa: E501
        :type: str
        """
        if recipient is None:
            raise ValueError("Invalid value for `recipient`, must not be `None`")  # noqa: E501

        self._recipient = recipient

    @property
    def message(self):
        """Gets the message of this TicketListItem.  # noqa: E501


        :return: The message of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TicketListItem.


        :param message: The message of this TicketListItem.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def date_created(self):
        """Gets the date_created of this TicketListItem.  # noqa: E501

         date and time with valid format: YYYY-MM-DD HH:MM:SS  # noqa: E501

        :return: The date_created of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this TicketListItem.

         date and time with valid format: YYYY-MM-DD HH:MM:SS  # noqa: E501

        :param date_created: The date_created of this TicketListItem.  # noqa: E501
        :type: str
        """

        self._date_created = date_created

    @property
    def recipient_name(self):
        """Gets the recipient_name of this TicketListItem.  # noqa: E501


        :return: The recipient_name of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._recipient_name

    @recipient_name.setter
    def recipient_name(self, recipient_name):
        """Sets the recipient_name of this TicketListItem.


        :param recipient_name: The recipient_name of this TicketListItem.  # noqa: E501
        :type: str
        """

        self._recipient_name = recipient_name

    @property
    def carbon_copy(self):
        """Gets the carbon_copy of this TicketListItem.  # noqa: E501


        :return: The carbon_copy of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._carbon_copy

    @carbon_copy.setter
    def carbon_copy(self, carbon_copy):
        """Sets the carbon_copy of this TicketListItem.


        :param carbon_copy: The carbon_copy of this TicketListItem.  # noqa: E501
        :type: str
        """

        self._carbon_copy = carbon_copy

    @property
    def blind_carbon_copy(self):
        """Gets the blind_carbon_copy of this TicketListItem.  # noqa: E501


        :return: The blind_carbon_copy of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._blind_carbon_copy

    @blind_carbon_copy.setter
    def blind_carbon_copy(self, blind_carbon_copy):
        """Sets the blind_carbon_copy of this TicketListItem.


        :param blind_carbon_copy: The blind_carbon_copy of this TicketListItem.  # noqa: E501
        :type: str
        """

        self._blind_carbon_copy = blind_carbon_copy

    @property
    def status(self):
        """Gets the status of this TicketListItem.  # noqa: E501

        <br> I - init<br> N - new<br> T - chatting<br> P - calling<br> R - resolved<br> X - deleted<br> B - spam<br> A - answered<br> C - open<br> W - postponed  # noqa: E501

        :return: The status of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TicketListItem.

        <br> I - init<br> N - new<br> T - chatting<br> P - calling<br> R - resolved<br> X - deleted<br> B - spam<br> A - answered<br> C - open<br> W - postponed  # noqa: E501

        :param status: The status of this TicketListItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["I", "N", "T", "P", "R", "X", "B", "A", "C", "W"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def mail_message_id(self):
        """Gets the mail_message_id of this TicketListItem.  # noqa: E501


        :return: The mail_message_id of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._mail_message_id

    @mail_message_id.setter
    def mail_message_id(self, mail_message_id):
        """Sets the mail_message_id of this TicketListItem.


        :param mail_message_id: The mail_message_id of this TicketListItem.  # noqa: E501
        :type: str
        """

        self._mail_message_id = mail_message_id

    @property
    def do_not_send_mail(self):
        """Gets the do_not_send_mail of this TicketListItem.  # noqa: E501

        Y - yes, N - no  # noqa: E501

        :return: The do_not_send_mail of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._do_not_send_mail

    @do_not_send_mail.setter
    def do_not_send_mail(self, do_not_send_mail):
        """Sets the do_not_send_mail of this TicketListItem.

        Y - yes, N - no  # noqa: E501

        :param do_not_send_mail: The do_not_send_mail of this TicketListItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N"]  # noqa: E501
        if do_not_send_mail not in allowed_values:
            raise ValueError(
                "Invalid value for `do_not_send_mail` ({0}), must be one of {1}"  # noqa: E501
                .format(do_not_send_mail, allowed_values)
            )

        self._do_not_send_mail = do_not_send_mail

    @property
    def use_template(self):
        """Gets the use_template of this TicketListItem.  # noqa: E501

        Y - yes, N - no  # noqa: E501

        :return: The use_template of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._use_template

    @use_template.setter
    def use_template(self, use_template):
        """Sets the use_template of this TicketListItem.

        Y - yes, N - no  # noqa: E501

        :param use_template: The use_template of this TicketListItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N"]  # noqa: E501
        if use_template not in allowed_values:
            raise ValueError(
                "Invalid value for `use_template` ({0}), must be one of {1}"  # noqa: E501
                .format(use_template, allowed_values)
            )

        self._use_template = use_template

    @property
    def is_html_message(self):
        """Gets the is_html_message of this TicketListItem.  # noqa: E501

        Y - yes, N - no  # noqa: E501

        :return: The is_html_message of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._is_html_message

    @is_html_message.setter
    def is_html_message(self, is_html_message):
        """Sets the is_html_message of this TicketListItem.

        Y - yes, N - no  # noqa: E501

        :param is_html_message: The is_html_message of this TicketListItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N"]  # noqa: E501
        if is_html_message not in allowed_values:
            raise ValueError(
                "Invalid value for `is_html_message` ({0}), must be one of {1}"  # noqa: E501
                .format(is_html_message, allowed_values)
            )

        self._is_html_message = is_html_message

    @property
    def custom_fields(self):
        """Gets the custom_fields of this TicketListItem.  # noqa: E501


        :return: The custom_fields of this TicketListItem.  # noqa: E501
        :rtype: list[CustomFields]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this TicketListItem.


        :param custom_fields: The custom_fields of this TicketListItem.  # noqa: E501
        :type: list[CustomFields]
        """

        self._custom_fields = custom_fields

    @property
    def tags(self):
        """Gets the tags of this TicketListItem.  # noqa: E501

        array of tags id  # noqa: E501

        :return: The tags of this TicketListItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TicketListItem.

        array of tags id  # noqa: E501

        :param tags: The tags of this TicketListItem.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def attachments(self):
        """Gets the attachments of this TicketListItem.  # noqa: E501


        :return: The attachments of this TicketListItem.  # noqa: E501
        :rtype: str
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this TicketListItem.


        :param attachments: The attachments of this TicketListItem.  # noqa: E501
        :type: str
        """

        self._attachments = attachments

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TicketListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
