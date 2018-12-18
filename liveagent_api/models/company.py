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

from liveagent_api.models.company_list_item import CompanyListItem  # noqa: F401,E501
from liveagent_api.models.custom_fields import CustomFields  # noqa: F401,E501


class Company(object):
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
        'name': 'str',
        'system_name': 'str',
        'description': 'str',
        'avatar_url': 'str',
        'type': 'str',
        'date_created': 'datetime',
        'language': 'str',
        'city': 'str',
        'countrycode': 'str',
        'ip': 'str',
        'emails': 'list[str]',
        'phones': 'list[str]',
        'groups': 'list[str]',
        'note': 'str',
        'useragent': 'str',
        'screen': 'str',
        'time_offset': 'float',
        'latitude': 'float',
        'longitude': 'float',
        'custom_fields': 'list[CustomFields]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'system_name': 'system_name',
        'description': 'description',
        'avatar_url': 'avatar_url',
        'type': 'type',
        'date_created': 'date_created',
        'language': 'language',
        'city': 'city',
        'countrycode': 'countrycode',
        'ip': 'ip',
        'emails': 'emails',
        'phones': 'phones',
        'groups': 'groups',
        'note': 'note',
        'useragent': 'useragent',
        'screen': 'screen',
        'time_offset': 'time_offset',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, id=None, name=None, system_name=None, description=None, avatar_url=None, type='V', date_created=None, language=None, city=None, countrycode=None, ip=None, emails=None, phones=None, groups=None, note=None, useragent=None, screen=None, time_offset=None, latitude=None, longitude=None, custom_fields=None):  # noqa: E501
        """Company - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._system_name = None
        self._description = None
        self._avatar_url = None
        self._type = None
        self._date_created = None
        self._language = None
        self._city = None
        self._countrycode = None
        self._ip = None
        self._emails = None
        self._phones = None
        self._groups = None
        self._note = None
        self._useragent = None
        self._screen = None
        self._time_offset = None
        self._latitude = None
        self._longitude = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if system_name is not None:
            self.system_name = system_name
        if description is not None:
            self.description = description
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if type is not None:
            self.type = type
        if date_created is not None:
            self.date_created = date_created
        if language is not None:
            self.language = language
        if city is not None:
            self.city = city
        if countrycode is not None:
            self.countrycode = countrycode
        if ip is not None:
            self.ip = ip
        if emails is not None:
            self.emails = emails
        if phones is not None:
            self.phones = phones
        if groups is not None:
            self.groups = groups
        if note is not None:
            self.note = note
        if useragent is not None:
            self.useragent = useragent
        if screen is not None:
            self.screen = screen
        if time_offset is not None:
            self.time_offset = time_offset
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this Company.  # noqa: E501


        :return: The id of this Company.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Company.


        :param id: The id of this Company.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Company.  # noqa: E501


        :return: The name of this Company.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Company.


        :param name: The name of this Company.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def system_name(self):
        """Gets the system_name of this Company.  # noqa: E501


        :return: The system_name of this Company.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this Company.


        :param system_name: The system_name of this Company.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

    @property
    def description(self):
        """Gets the description of this Company.  # noqa: E501


        :return: The description of this Company.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Company.


        :param description: The description of this Company.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def avatar_url(self):
        """Gets the avatar_url of this Company.  # noqa: E501


        :return: The avatar_url of this Company.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this Company.


        :param avatar_url: The avatar_url of this Company.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def type(self):
        """Gets the type of this Company.  # noqa: E501

        V - visitor, R - registered visitor  # noqa: E501

        :return: The type of this Company.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Company.

        V - visitor, R - registered visitor  # noqa: E501

        :param type: The type of this Company.  # noqa: E501
        :type: str
        """
        allowed_values = ["V", "R"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def date_created(self):
        """Gets the date_created of this Company.  # noqa: E501


        :return: The date_created of this Company.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Company.


        :param date_created: The date_created of this Company.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def language(self):
        """Gets the language of this Company.  # noqa: E501


        :return: The language of this Company.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Company.


        :param language: The language of this Company.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def city(self):
        """Gets the city of this Company.  # noqa: E501


        :return: The city of this Company.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Company.


        :param city: The city of this Company.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def countrycode(self):
        """Gets the countrycode of this Company.  # noqa: E501


        :return: The countrycode of this Company.  # noqa: E501
        :rtype: str
        """
        return self._countrycode

    @countrycode.setter
    def countrycode(self, countrycode):
        """Sets the countrycode of this Company.


        :param countrycode: The countrycode of this Company.  # noqa: E501
        :type: str
        """

        self._countrycode = countrycode

    @property
    def ip(self):
        """Gets the ip of this Company.  # noqa: E501


        :return: The ip of this Company.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Company.


        :param ip: The ip of this Company.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def emails(self):
        """Gets the emails of this Company.  # noqa: E501


        :return: The emails of this Company.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this Company.


        :param emails: The emails of this Company.  # noqa: E501
        :type: list[str]
        """

        self._emails = emails

    @property
    def phones(self):
        """Gets the phones of this Company.  # noqa: E501


        :return: The phones of this Company.  # noqa: E501
        :rtype: list[str]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this Company.


        :param phones: The phones of this Company.  # noqa: E501
        :type: list[str]
        """

        self._phones = phones

    @property
    def groups(self):
        """Gets the groups of this Company.  # noqa: E501


        :return: The groups of this Company.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Company.


        :param groups: The groups of this Company.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def note(self):
        """Gets the note of this Company.  # noqa: E501


        :return: The note of this Company.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Company.


        :param note: The note of this Company.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def useragent(self):
        """Gets the useragent of this Company.  # noqa: E501


        :return: The useragent of this Company.  # noqa: E501
        :rtype: str
        """
        return self._useragent

    @useragent.setter
    def useragent(self, useragent):
        """Sets the useragent of this Company.


        :param useragent: The useragent of this Company.  # noqa: E501
        :type: str
        """

        self._useragent = useragent

    @property
    def screen(self):
        """Gets the screen of this Company.  # noqa: E501


        :return: The screen of this Company.  # noqa: E501
        :rtype: str
        """
        return self._screen

    @screen.setter
    def screen(self, screen):
        """Sets the screen of this Company.


        :param screen: The screen of this Company.  # noqa: E501
        :type: str
        """

        self._screen = screen

    @property
    def time_offset(self):
        """Gets the time_offset of this Company.  # noqa: E501


        :return: The time_offset of this Company.  # noqa: E501
        :rtype: float
        """
        return self._time_offset

    @time_offset.setter
    def time_offset(self, time_offset):
        """Sets the time_offset of this Company.


        :param time_offset: The time_offset of this Company.  # noqa: E501
        :type: float
        """

        self._time_offset = time_offset

    @property
    def latitude(self):
        """Gets the latitude of this Company.  # noqa: E501


        :return: The latitude of this Company.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Company.


        :param latitude: The latitude of this Company.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this Company.  # noqa: E501


        :return: The longitude of this Company.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Company.


        :param longitude: The longitude of this Company.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Company.  # noqa: E501


        :return: The custom_fields of this Company.  # noqa: E501
        :rtype: list[CustomFields]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Company.


        :param custom_fields: The custom_fields of this Company.  # noqa: E501
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Company):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
