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


class MessageGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MessageGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'parent_id': 'str',
            'userid': 'str',
            'user_full_name': 'str',
            'type': 'str',
            'status': 'str',
            'datecreated': 'datetime',
            'datefinished': 'datetime',
            'sort_order': 'int',
            'mail_msg_id': 'str',
            'pop3_msg_id': 'str',
            'messages': 'list[Message]'
        }

        self.attribute_map = {
            'id': 'id',
            'parent_id': 'parent_id',
            'userid': 'userid',
            'user_full_name': 'user_full_name',
            'type': 'type',
            'status': 'status',
            'datecreated': 'datecreated',
            'datefinished': 'datefinished',
            'sort_order': 'sort_order',
            'mail_msg_id': 'mail_msg_id',
            'pop3_msg_id': 'pop3_msg_id',
            'messages': 'messages'
        }

        self._id = None
        self._parent_id = None
        self._userid = None
        self._user_full_name = None
        self._type = None
        self._status = None
        self._datecreated = None
        self._datefinished = None
        self._sort_order = None
        self._mail_msg_id = None
        self._pop3_msg_id = None
        self._messages = None

    @property
    def id(self):
        """
        Gets the id of this MessageGroup.


        :return: The id of this MessageGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MessageGroup.


        :param id: The id of this MessageGroup.
        :type: str
        """
        self._id = id

    @property
    def parent_id(self):
        """
        Gets the parent_id of this MessageGroup.


        :return: The parent_id of this MessageGroup.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this MessageGroup.


        :param parent_id: The parent_id of this MessageGroup.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def userid(self):
        """
        Gets the userid of this MessageGroup.


        :return: The userid of this MessageGroup.
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """
        Sets the userid of this MessageGroup.


        :param userid: The userid of this MessageGroup.
        :type: str
        """
        self._userid = userid

    @property
    def user_full_name(self):
        """
        Gets the user_full_name of this MessageGroup.


        :return: The user_full_name of this MessageGroup.
        :rtype: str
        """
        return self._user_full_name

    @user_full_name.setter
    def user_full_name(self, user_full_name):
        """
        Sets the user_full_name of this MessageGroup.


        :param user_full_name: The user_full_name of this MessageGroup.
        :type: str
        """
        self._user_full_name = user_full_name

    @property
    def type(self):
        """
        Gets the type of this MessageGroup.
        M - OFFLINE C - CHAT P - CALL V - OUTGOING_CALL 1 - INTERNAL_CALL I - INTERNAL U - INTERNAL_OFFLINE Z - INTERNAL_COLLAPSED S - STARTINFO T - TRANSFER R - RESOLVE J - POSTPONE X - DELETE B - SPAM G - TAG F - FACEBOOK W - TWITTER H - WEIBO E - WEIBO_COMMENT D - TENCENT N - TENCENT_COMMENT Y - RETWEET A - KNOWLEDGEBASE_START K - KNOWLEDGEBASE O - FORWARD Q - FORWARD_REPLY L - SPLITTED 2 - MERGED

        :return: The type of this MessageGroup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MessageGroup.
        M - OFFLINE C - CHAT P - CALL V - OUTGOING_CALL 1 - INTERNAL_CALL I - INTERNAL U - INTERNAL_OFFLINE Z - INTERNAL_COLLAPSED S - STARTINFO T - TRANSFER R - RESOLVE J - POSTPONE X - DELETE B - SPAM G - TAG F - FACEBOOK W - TWITTER H - WEIBO E - WEIBO_COMMENT D - TENCENT N - TENCENT_COMMENT Y - RETWEET A - KNOWLEDGEBASE_START K - KNOWLEDGEBASE O - FORWARD Q - FORWARD_REPLY L - SPLITTED 2 - MERGED

        :param type: The type of this MessageGroup.
        :type: str
        """
        allowed_values = ["M", "C", "P", "V", "1", "I", "U", "Z", "S", "T", "R", "J", "X", "B", "G", "F", "W", "H", "E", "D", "N", "Y", "A", "K", "O", "Q", "L", "2"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def status(self):
        """
        Gets the status of this MessageGroup.
        D - DELETED P - PROMOTED V - VISIBLE S - SPLITTED M - MERGED I - INITIALIZING R - CONNECTING C - CALLING

        :return: The status of this MessageGroup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this MessageGroup.
        D - DELETED P - PROMOTED V - VISIBLE S - SPLITTED M - MERGED I - INITIALIZING R - CONNECTING C - CALLING

        :param status: The status of this MessageGroup.
        :type: str
        """
        allowed_values = ["D", "P", "V", "S", "M", "I", "R", "C"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def datecreated(self):
        """
        Gets the datecreated of this MessageGroup.


        :return: The datecreated of this MessageGroup.
        :rtype: datetime
        """
        return self._datecreated

    @datecreated.setter
    def datecreated(self, datecreated):
        """
        Sets the datecreated of this MessageGroup.


        :param datecreated: The datecreated of this MessageGroup.
        :type: datetime
        """
        self._datecreated = datecreated

    @property
    def datefinished(self):
        """
        Gets the datefinished of this MessageGroup.


        :return: The datefinished of this MessageGroup.
        :rtype: datetime
        """
        return self._datefinished

    @datefinished.setter
    def datefinished(self, datefinished):
        """
        Sets the datefinished of this MessageGroup.


        :param datefinished: The datefinished of this MessageGroup.
        :type: datetime
        """
        self._datefinished = datefinished

    @property
    def sort_order(self):
        """
        Gets the sort_order of this MessageGroup.


        :return: The sort_order of this MessageGroup.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this MessageGroup.


        :param sort_order: The sort_order of this MessageGroup.
        :type: int
        """
        self._sort_order = sort_order

    @property
    def mail_msg_id(self):
        """
        Gets the mail_msg_id of this MessageGroup.


        :return: The mail_msg_id of this MessageGroup.
        :rtype: str
        """
        return self._mail_msg_id

    @mail_msg_id.setter
    def mail_msg_id(self, mail_msg_id):
        """
        Sets the mail_msg_id of this MessageGroup.


        :param mail_msg_id: The mail_msg_id of this MessageGroup.
        :type: str
        """
        self._mail_msg_id = mail_msg_id

    @property
    def pop3_msg_id(self):
        """
        Gets the pop3_msg_id of this MessageGroup.


        :return: The pop3_msg_id of this MessageGroup.
        :rtype: str
        """
        return self._pop3_msg_id

    @pop3_msg_id.setter
    def pop3_msg_id(self, pop3_msg_id):
        """
        Sets the pop3_msg_id of this MessageGroup.


        :param pop3_msg_id: The pop3_msg_id of this MessageGroup.
        :type: str
        """
        self._pop3_msg_id = pop3_msg_id

    @property
    def messages(self):
        """
        Gets the messages of this MessageGroup.


        :return: The messages of this MessageGroup.
        :rtype: list[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this MessageGroup.


        :param messages: The messages of this MessageGroup.
        :type: list[Message]
        """
        self._messages = messages

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

