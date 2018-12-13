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


class TicketInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TicketInformation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
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

        self.attribute_map = {
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

    @property
    def id(self):
        """
        Gets the id of this TicketInformation.


        :return: The id of this TicketInformation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TicketInformation.


        :param id: The id of this TicketInformation.
        :type: str
        """
        self._id = id

    @property
    def ownerid(self):
        """
        Gets the ownerid of this TicketInformation.


        :return: The ownerid of this TicketInformation.
        :rtype: str
        """
        return self._ownerid

    @ownerid.setter
    def ownerid(self, ownerid):
        """
        Sets the ownerid of this TicketInformation.


        :param ownerid: The ownerid of this TicketInformation.
        :type: str
        """
        self._ownerid = ownerid

    @property
    def owner_contactid(self):
        """
        Gets the owner_contactid of this TicketInformation.


        :return: The owner_contactid of this TicketInformation.
        :rtype: str
        """
        return self._owner_contactid

    @owner_contactid.setter
    def owner_contactid(self, owner_contactid):
        """
        Sets the owner_contactid of this TicketInformation.


        :param owner_contactid: The owner_contactid of this TicketInformation.
        :type: str
        """
        self._owner_contactid = owner_contactid

    @property
    def departmentid(self):
        """
        Gets the departmentid of this TicketInformation.


        :return: The departmentid of this TicketInformation.
        :rtype: str
        """
        return self._departmentid

    @departmentid.setter
    def departmentid(self, departmentid):
        """
        Sets the departmentid of this TicketInformation.


        :param departmentid: The departmentid of this TicketInformation.
        :type: str
        """
        self._departmentid = departmentid

    @property
    def agentid(self):
        """
        Gets the agentid of this TicketInformation.


        :return: The agentid of this TicketInformation.
        :rtype: str
        """
        return self._agentid

    @agentid.setter
    def agentid(self, agentid):
        """
        Sets the agentid of this TicketInformation.


        :param agentid: The agentid of this TicketInformation.
        :type: str
        """
        self._agentid = agentid

    @property
    def status(self):
        """
        Gets the status of this TicketInformation.


        :return: The status of this TicketInformation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TicketInformation.


        :param status: The status of this TicketInformation.
        :type: str
        """
        self._status = status

    @property
    def tags(self):
        """
        Gets the tags of this TicketInformation.


        :return: The tags of this TicketInformation.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this TicketInformation.


        :param tags: The tags of this TicketInformation.
        :type: str
        """
        self._tags = tags

    @property
    def code(self):
        """
        Gets the code of this TicketInformation.


        :return: The code of this TicketInformation.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this TicketInformation.


        :param code: The code of this TicketInformation.
        :type: str
        """
        self._code = code

    @property
    def channel_type(self):
        """
        Gets the channel_type of this TicketInformation.


        :return: The channel_type of this TicketInformation.
        :rtype: str
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """
        Sets the channel_type of this TicketInformation.


        :param channel_type: The channel_type of this TicketInformation.
        :type: str
        """
        self._channel_type = channel_type

    @property
    def date_created(self):
        """
        Gets the date_created of this TicketInformation.


        :return: The date_created of this TicketInformation.
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this TicketInformation.


        :param date_created: The date_created of this TicketInformation.
        :type: str
        """
        self._date_created = date_created

    @property
    def public_access_urlcode(self):
        """
        Gets the public_access_urlcode of this TicketInformation.


        :return: The public_access_urlcode of this TicketInformation.
        :rtype: str
        """
        return self._public_access_urlcode

    @public_access_urlcode.setter
    def public_access_urlcode(self, public_access_urlcode):
        """
        Sets the public_access_urlcode of this TicketInformation.


        :param public_access_urlcode: The public_access_urlcode of this TicketInformation.
        :type: str
        """
        self._public_access_urlcode = public_access_urlcode

    @property
    def subject(self):
        """
        Gets the subject of this TicketInformation.


        :return: The subject of this TicketInformation.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this TicketInformation.


        :param subject: The subject of this TicketInformation.
        :type: str
        """
        self._subject = subject

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this TicketInformation.


        :return: The custom_fields of this TicketInformation.
        :rtype: list[CustomFields]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this TicketInformation.


        :param custom_fields: The custom_fields of this TicketInformation.
        :type: list[CustomFields]
        """
        self._custom_fields = custom_fields

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

