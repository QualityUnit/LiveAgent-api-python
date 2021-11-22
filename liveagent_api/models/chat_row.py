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


class ChatRow(object):
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
        'conversationid': 'str',
        'datechanged': 'datetime',
        'status': 'str',
        'preview': 'str',
        'subject': 'str',
        'departmentname': 'str',
        'agentname': 'str',
        'tags': 'list[str]',
        'firstname': 'str',
        'lastname': 'str',
        'system_name': 'str',
        'emails': 'list[str]',
        'city': 'str',
        'countrycode': 'str',
        'avatar_url': 'str',
        'rstatus': 'str',
        'statusdatestarted': 'datetime',
        'chat_order': 'int'
    }

    attribute_map = {
        'conversationid': 'conversationid',
        'datechanged': 'datechanged',
        'status': 'status',
        'preview': 'preview',
        'subject': 'subject',
        'departmentname': 'departmentname',
        'agentname': 'agentname',
        'tags': 'tags',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'system_name': 'system_name',
        'emails': 'emails',
        'city': 'city',
        'countrycode': 'countrycode',
        'avatar_url': 'avatar_url',
        'rstatus': 'rstatus',
        'statusdatestarted': 'statusdatestarted',
        'chat_order': 'chat_order'
    }

    def __init__(self, conversationid=None, datechanged=None, status=None, preview=None, subject=None, departmentname=None, agentname=None, tags=None, firstname=None, lastname=None, system_name=None, emails=None, city=None, countrycode=None, avatar_url=None, rstatus=None, statusdatestarted=None, chat_order=None):  # noqa: E501
        """ChatRow - a model defined in Swagger"""  # noqa: E501

        self._conversationid = None
        self._datechanged = None
        self._status = None
        self._preview = None
        self._subject = None
        self._departmentname = None
        self._agentname = None
        self._tags = None
        self._firstname = None
        self._lastname = None
        self._system_name = None
        self._emails = None
        self._city = None
        self._countrycode = None
        self._avatar_url = None
        self._rstatus = None
        self._statusdatestarted = None
        self._chat_order = None
        self.discriminator = None

        if conversationid is not None:
            self.conversationid = conversationid
        if datechanged is not None:
            self.datechanged = datechanged
        if status is not None:
            self.status = status
        if preview is not None:
            self.preview = preview
        if subject is not None:
            self.subject = subject
        if departmentname is not None:
            self.departmentname = departmentname
        if agentname is not None:
            self.agentname = agentname
        if tags is not None:
            self.tags = tags
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if system_name is not None:
            self.system_name = system_name
        if emails is not None:
            self.emails = emails
        if city is not None:
            self.city = city
        if countrycode is not None:
            self.countrycode = countrycode
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if rstatus is not None:
            self.rstatus = rstatus
        if statusdatestarted is not None:
            self.statusdatestarted = statusdatestarted
        if chat_order is not None:
            self.chat_order = chat_order

    @property
    def conversationid(self):
        """Gets the conversationid of this ChatRow.  # noqa: E501


        :return: The conversationid of this ChatRow.  # noqa: E501
        :rtype: str
        """
        return self._conversationid

    @conversationid.setter
    def conversationid(self, conversationid):
        """Sets the conversationid of this ChatRow.


        :param conversationid: The conversationid of this ChatRow.  # noqa: E501
        :type: str
        """

        self._conversationid = conversationid

    @property
    def datechanged(self):
        """Gets the datechanged of this ChatRow.  # noqa: E501


        :return: The datechanged of this ChatRow.  # noqa: E501
        :rtype: datetime
        """
        return self._datechanged

    @datechanged.setter
    def datechanged(self, datechanged):
        """Sets the datechanged of this ChatRow.


        :param datechanged: The datechanged of this ChatRow.  # noqa: E501
        :type: datetime
        """

        self._datechanged = datechanged

    @property
    def status(self):
        """Gets the status of this ChatRow.  # noqa: E501


        :return: The status of this ChatRow.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ChatRow.


        :param status: The status of this ChatRow.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def preview(self):
        """Gets the preview of this ChatRow.  # noqa: E501


        :return: The preview of this ChatRow.  # noqa: E501
        :rtype: str
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """Sets the preview of this ChatRow.


        :param preview: The preview of this ChatRow.  # noqa: E501
        :type: str
        """

        self._preview = preview

    @property
    def subject(self):
        """Gets the subject of this ChatRow.  # noqa: E501


        :return: The subject of this ChatRow.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ChatRow.


        :param subject: The subject of this ChatRow.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def departmentname(self):
        """Gets the departmentname of this ChatRow.  # noqa: E501


        :return: The departmentname of this ChatRow.  # noqa: E501
        :rtype: str
        """
        return self._departmentname

    @departmentname.setter
    def departmentname(self, departmentname):
        """Sets the departmentname of this ChatRow.


        :param departmentname: The departmentname of this ChatRow.  # noqa: E501
        :type: str
        """

        self._departmentname = departmentname

    @property
    def agentname(self):
        """Gets the agentname of this ChatRow.  # noqa: E501


        :return: The agentname of this ChatRow.  # noqa: E501
        :rtype: str
        """
        return self._agentname

    @agentname.setter
    def agentname(self, agentname):
        """Sets the agentname of this ChatRow.


        :param agentname: The agentname of this ChatRow.  # noqa: E501
        :type: str
        """

        self._agentname = agentname

    @property
    def tags(self):
        """Gets the tags of this ChatRow.  # noqa: E501


        :return: The tags of this ChatRow.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ChatRow.


        :param tags: The tags of this ChatRow.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def firstname(self):
        """Gets the firstname of this ChatRow.  # noqa: E501


        :return: The firstname of this ChatRow.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this ChatRow.


        :param firstname: The firstname of this ChatRow.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this ChatRow.  # noqa: E501


        :return: The lastname of this ChatRow.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this ChatRow.


        :param lastname: The lastname of this ChatRow.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def system_name(self):
        """Gets the system_name of this ChatRow.  # noqa: E501


        :return: The system_name of this ChatRow.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this ChatRow.


        :param system_name: The system_name of this ChatRow.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

    @property
    def emails(self):
        """Gets the emails of this ChatRow.  # noqa: E501


        :return: The emails of this ChatRow.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this ChatRow.


        :param emails: The emails of this ChatRow.  # noqa: E501
        :type: list[str]
        """

        self._emails = emails

    @property
    def city(self):
        """Gets the city of this ChatRow.  # noqa: E501


        :return: The city of this ChatRow.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ChatRow.


        :param city: The city of this ChatRow.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def countrycode(self):
        """Gets the countrycode of this ChatRow.  # noqa: E501


        :return: The countrycode of this ChatRow.  # noqa: E501
        :rtype: str
        """
        return self._countrycode

    @countrycode.setter
    def countrycode(self, countrycode):
        """Sets the countrycode of this ChatRow.


        :param countrycode: The countrycode of this ChatRow.  # noqa: E501
        :type: str
        """

        self._countrycode = countrycode

    @property
    def avatar_url(self):
        """Gets the avatar_url of this ChatRow.  # noqa: E501


        :return: The avatar_url of this ChatRow.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this ChatRow.


        :param avatar_url: The avatar_url of this ChatRow.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def rstatus(self):
        """Gets the rstatus of this ChatRow.  # noqa: E501


        :return: The rstatus of this ChatRow.  # noqa: E501
        :rtype: str
        """
        return self._rstatus

    @rstatus.setter
    def rstatus(self, rstatus):
        """Sets the rstatus of this ChatRow.


        :param rstatus: The rstatus of this ChatRow.  # noqa: E501
        :type: str
        """

        self._rstatus = rstatus

    @property
    def statusdatestarted(self):
        """Gets the statusdatestarted of this ChatRow.  # noqa: E501


        :return: The statusdatestarted of this ChatRow.  # noqa: E501
        :rtype: datetime
        """
        return self._statusdatestarted

    @statusdatestarted.setter
    def statusdatestarted(self, statusdatestarted):
        """Sets the statusdatestarted of this ChatRow.


        :param statusdatestarted: The statusdatestarted of this ChatRow.  # noqa: E501
        :type: datetime
        """

        self._statusdatestarted = statusdatestarted

    @property
    def chat_order(self):
        """Gets the chat_order of this ChatRow.  # noqa: E501


        :return: The chat_order of this ChatRow.  # noqa: E501
        :rtype: int
        """
        return self._chat_order

    @chat_order.setter
    def chat_order(self, chat_order):
        """Sets the chat_order of this ChatRow.


        :param chat_order: The chat_order of this ChatRow.  # noqa: E501
        :type: int
        """

        self._chat_order = chat_order

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
        if issubclass(ChatRow, dict):
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
        if not isinstance(other, ChatRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
