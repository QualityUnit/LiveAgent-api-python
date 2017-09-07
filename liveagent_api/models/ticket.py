# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Ticket(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Ticket - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
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
            'public_access_urlcode': 'str',
            'subject': 'str'
        }

        self.attribute_map = {
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
            'public_access_urlcode': 'public_access_urlcode',
            'subject': 'subject'
        }

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
        self._public_access_urlcode = None
        self._subject = None

    @property
    def id(self):
        """
        Gets the id of this Ticket.


        :return: The id of this Ticket.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Ticket.


        :param id: The id of this Ticket.
        :type: str
        """
        self._id = id

    @property
    def owner_contactid(self):
        """
        Gets the owner_contactid of this Ticket.


        :return: The owner_contactid of this Ticket.
        :rtype: str
        """
        return self._owner_contactid

    @owner_contactid.setter
    def owner_contactid(self, owner_contactid):
        """
        Sets the owner_contactid of this Ticket.


        :param owner_contactid: The owner_contactid of this Ticket.
        :type: str
        """
        self._owner_contactid = owner_contactid

    @property
    def owner_email(self):
        """
        Gets the owner_email of this Ticket.


        :return: The owner_email of this Ticket.
        :rtype: str
        """
        return self._owner_email

    @owner_email.setter
    def owner_email(self, owner_email):
        """
        Sets the owner_email of this Ticket.


        :param owner_email: The owner_email of this Ticket.
        :type: str
        """
        self._owner_email = owner_email

    @property
    def owner_name(self):
        """
        Gets the owner_name of this Ticket.


        :return: The owner_name of this Ticket.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """
        Sets the owner_name of this Ticket.


        :param owner_name: The owner_name of this Ticket.
        :type: str
        """
        self._owner_name = owner_name

    @property
    def departmentid(self):
        """
        Gets the departmentid of this Ticket.


        :return: The departmentid of this Ticket.
        :rtype: str
        """
        return self._departmentid

    @departmentid.setter
    def departmentid(self, departmentid):
        """
        Sets the departmentid of this Ticket.


        :param departmentid: The departmentid of this Ticket.
        :type: str
        """
        self._departmentid = departmentid

    @property
    def agentid(self):
        """
        Gets the agentid of this Ticket.


        :return: The agentid of this Ticket.
        :rtype: str
        """
        return self._agentid

    @agentid.setter
    def agentid(self, agentid):
        """
        Sets the agentid of this Ticket.


        :param agentid: The agentid of this Ticket.
        :type: str
        """
        self._agentid = agentid

    @property
    def status(self):
        """
        Gets the status of this Ticket.
        <br> I - init<br> N - new<br> T - chatting<br> P - calling<br> R - resolved<br> X - deleted<br> B - spam<br> A - answered<br> C - open<br> W - postponed

        :return: The status of this Ticket.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Ticket.
        <br> I - init<br> N - new<br> T - chatting<br> P - calling<br> R - resolved<br> X - deleted<br> B - spam<br> A - answered<br> C - open<br> W - postponed

        :param status: The status of this Ticket.
        :type: str
        """
        allowed_values = ["I", "N", "T", "P", "R", "X", "B", "A", "C", "W"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def tags(self):
        """
        Gets the tags of this Ticket.


        :return: The tags of this Ticket.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Ticket.


        :param tags: The tags of this Ticket.
        :type: list[str]
        """
        self._tags = tags

    @property
    def code(self):
        """
        Gets the code of this Ticket.


        :return: The code of this Ticket.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Ticket.


        :param code: The code of this Ticket.
        :type: str
        """
        self._code = code

    @property
    def channel_type(self):
        """
        Gets the channel_type of this Ticket.
        <br> E - email<br> B - contact button<br> M - contact form<br> I - invitation<br> C - call<br> W - call button<br> F - facebook<br> A - facebook message<br> T - twitter<br> H - weibo<br> J - weibo private<br> D - tencent<br> N - tencent private<br> Q - forum<br> S - suggestion

        :return: The channel_type of this Ticket.
        :rtype: str
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """
        Sets the channel_type of this Ticket.
        <br> E - email<br> B - contact button<br> M - contact form<br> I - invitation<br> C - call<br> W - call button<br> F - facebook<br> A - facebook message<br> T - twitter<br> H - weibo<br> J - weibo private<br> D - tencent<br> N - tencent private<br> Q - forum<br> S - suggestion

        :param channel_type: The channel_type of this Ticket.
        :type: str
        """
        self._channel_type = channel_type

    @property
    def date_created(self):
        """
        Gets the date_created of this Ticket.


        :return: The date_created of this Ticket.
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this Ticket.


        :param date_created: The date_created of this Ticket.
        :type: str
        """
        self._date_created = date_created

    @property
    def date_changed(self):
        """
        Gets the date_changed of this Ticket.


        :return: The date_changed of this Ticket.
        :rtype: str
        """
        return self._date_changed

    @date_changed.setter
    def date_changed(self, date_changed):
        """
        Sets the date_changed of this Ticket.


        :param date_changed: The date_changed of this Ticket.
        :type: str
        """
        self._date_changed = date_changed

    @property
    def date_resolved(self):
        """
        Gets the date_resolved of this Ticket.


        :return: The date_resolved of this Ticket.
        :rtype: str
        """
        return self._date_resolved

    @date_resolved.setter
    def date_resolved(self, date_resolved):
        """
        Sets the date_resolved of this Ticket.


        :param date_resolved: The date_resolved of this Ticket.
        :type: str
        """
        self._date_resolved = date_resolved

    @property
    def date_due(self):
        """
        Gets the date_due of this Ticket.


        :return: The date_due of this Ticket.
        :rtype: str
        """
        return self._date_due

    @date_due.setter
    def date_due(self, date_due):
        """
        Sets the date_due of this Ticket.


        :param date_due: The date_due of this Ticket.
        :type: str
        """
        self._date_due = date_due

    @property
    def date_deleted(self):
        """
        Gets the date_deleted of this Ticket.


        :return: The date_deleted of this Ticket.
        :rtype: str
        """
        return self._date_deleted

    @date_deleted.setter
    def date_deleted(self, date_deleted):
        """
        Sets the date_deleted of this Ticket.


        :param date_deleted: The date_deleted of this Ticket.
        :type: str
        """
        self._date_deleted = date_deleted

    @property
    def public_access_urlcode(self):
        """
        Gets the public_access_urlcode of this Ticket.


        :return: The public_access_urlcode of this Ticket.
        :rtype: str
        """
        return self._public_access_urlcode

    @public_access_urlcode.setter
    def public_access_urlcode(self, public_access_urlcode):
        """
        Sets the public_access_urlcode of this Ticket.


        :param public_access_urlcode: The public_access_urlcode of this Ticket.
        :type: str
        """
        self._public_access_urlcode = public_access_urlcode

    @property
    def subject(self):
        """
        Gets the subject of this Ticket.


        :return: The subject of this Ticket.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this Ticket.


        :param subject: The subject of this Ticket.
        :type: str
        """
        self._subject = subject

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

