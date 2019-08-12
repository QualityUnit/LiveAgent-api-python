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

from liveagent_api.models.custom_fields import CustomFields  # noqa: F401,E501


class ContactRequest(object):
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
        'company_id': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'system_name': 'str',
        'description': 'str',
        'avatar_url': 'str',
        'type': 'str',
        'gender': 'str',
        'language': 'str',
        'city': 'str',
        'countrycode': 'str',
        'ip': 'str',
        'registration_email': 'str',
        'emails': 'list[str]',
        'phones': 'list[str]',
        'groups': 'list[str]',
        'job_position': 'str',
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
        'company_id': 'company_id',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'system_name': 'system_name',
        'description': 'description',
        'avatar_url': 'avatar_url',
        'type': 'type',
        'gender': 'gender',
        'language': 'language',
        'city': 'city',
        'countrycode': 'countrycode',
        'ip': 'ip',
        'registration_email': 'registration_email',
        'emails': 'emails',
        'phones': 'phones',
        'groups': 'groups',
        'job_position': 'job_position',
        'note': 'note',
        'useragent': 'useragent',
        'screen': 'screen',
        'time_offset': 'time_offset',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, id=None, company_id=None, firstname=None, lastname=None, system_name=None, description=None, avatar_url=None, type='V', gender=None, language=None, city=None, countrycode=None, ip=None, registration_email=None, emails=None, phones=None, groups=None, job_position=None, note=None, useragent=None, screen=None, time_offset=None, latitude=None, longitude=None, custom_fields=None):  # noqa: E501
        """ContactRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._company_id = None
        self._firstname = None
        self._lastname = None
        self._system_name = None
        self._description = None
        self._avatar_url = None
        self._type = None
        self._gender = None
        self._language = None
        self._city = None
        self._countrycode = None
        self._ip = None
        self._registration_email = None
        self._emails = None
        self._phones = None
        self._groups = None
        self._job_position = None
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
        if company_id is not None:
            self.company_id = company_id
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if system_name is not None:
            self.system_name = system_name
        if description is not None:
            self.description = description
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if type is not None:
            self.type = type
        if gender is not None:
            self.gender = gender
        if language is not None:
            self.language = language
        if city is not None:
            self.city = city
        if countrycode is not None:
            self.countrycode = countrycode
        if ip is not None:
            self.ip = ip
        if registration_email is not None:
            self.registration_email = registration_email
        if emails is not None:
            self.emails = emails
        if phones is not None:
            self.phones = phones
        if groups is not None:
            self.groups = groups
        if job_position is not None:
            self.job_position = job_position
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
        """Gets the id of this ContactRequest.  # noqa: E501


        :return: The id of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContactRequest.


        :param id: The id of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def company_id(self):
        """Gets the company_id of this ContactRequest.  # noqa: E501


        :return: The company_id of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this ContactRequest.


        :param company_id: The company_id of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def firstname(self):
        """Gets the firstname of this ContactRequest.  # noqa: E501


        :return: The firstname of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this ContactRequest.


        :param firstname: The firstname of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this ContactRequest.  # noqa: E501


        :return: The lastname of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this ContactRequest.


        :param lastname: The lastname of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def system_name(self):
        """Gets the system_name of this ContactRequest.  # noqa: E501


        :return: The system_name of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this ContactRequest.


        :param system_name: The system_name of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

    @property
    def description(self):
        """Gets the description of this ContactRequest.  # noqa: E501


        :return: The description of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ContactRequest.


        :param description: The description of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def avatar_url(self):
        """Gets the avatar_url of this ContactRequest.  # noqa: E501


        :return: The avatar_url of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this ContactRequest.


        :param avatar_url: The avatar_url of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def type(self):
        """Gets the type of this ContactRequest.  # noqa: E501

        V - visitor, R - registered visitor  # noqa: E501

        :return: The type of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ContactRequest.

        V - visitor, R - registered visitor  # noqa: E501

        :param type: The type of this ContactRequest.  # noqa: E501
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
    def gender(self):
        """Gets the gender of this ContactRequest.  # noqa: E501

        M - Male, F - Female, X - Unspecified  # noqa: E501

        :return: The gender of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this ContactRequest.

        M - Male, F - Female, X - Unspecified  # noqa: E501

        :param gender: The gender of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def language(self):
        """Gets the language of this ContactRequest.  # noqa: E501


        :return: The language of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ContactRequest.


        :param language: The language of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def city(self):
        """Gets the city of this ContactRequest.  # noqa: E501


        :return: The city of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ContactRequest.


        :param city: The city of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def countrycode(self):
        """Gets the countrycode of this ContactRequest.  # noqa: E501


        :return: The countrycode of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._countrycode

    @countrycode.setter
    def countrycode(self, countrycode):
        """Sets the countrycode of this ContactRequest.


        :param countrycode: The countrycode of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._countrycode = countrycode

    @property
    def ip(self):
        """Gets the ip of this ContactRequest.  # noqa: E501


        :return: The ip of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ContactRequest.


        :param ip: The ip of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def registration_email(self):
        """Gets the registration_email of this ContactRequest.  # noqa: E501


        :return: The registration_email of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._registration_email

    @registration_email.setter
    def registration_email(self, registration_email):
        """Sets the registration_email of this ContactRequest.


        :param registration_email: The registration_email of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._registration_email = registration_email

    @property
    def emails(self):
        """Gets the emails of this ContactRequest.  # noqa: E501


        :return: The emails of this ContactRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this ContactRequest.


        :param emails: The emails of this ContactRequest.  # noqa: E501
        :type: list[str]
        """

        self._emails = emails

    @property
    def phones(self):
        """Gets the phones of this ContactRequest.  # noqa: E501


        :return: The phones of this ContactRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this ContactRequest.


        :param phones: The phones of this ContactRequest.  # noqa: E501
        :type: list[str]
        """

        self._phones = phones

    @property
    def groups(self):
        """Gets the groups of this ContactRequest.  # noqa: E501


        :return: The groups of this ContactRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ContactRequest.


        :param groups: The groups of this ContactRequest.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def job_position(self):
        """Gets the job_position of this ContactRequest.  # noqa: E501


        :return: The job_position of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._job_position

    @job_position.setter
    def job_position(self, job_position):
        """Sets the job_position of this ContactRequest.


        :param job_position: The job_position of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._job_position = job_position

    @property
    def note(self):
        """Gets the note of this ContactRequest.  # noqa: E501


        :return: The note of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ContactRequest.


        :param note: The note of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def useragent(self):
        """Gets the useragent of this ContactRequest.  # noqa: E501


        :return: The useragent of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._useragent

    @useragent.setter
    def useragent(self, useragent):
        """Sets the useragent of this ContactRequest.


        :param useragent: The useragent of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._useragent = useragent

    @property
    def screen(self):
        """Gets the screen of this ContactRequest.  # noqa: E501


        :return: The screen of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._screen

    @screen.setter
    def screen(self, screen):
        """Sets the screen of this ContactRequest.


        :param screen: The screen of this ContactRequest.  # noqa: E501
        :type: str
        """

        self._screen = screen

    @property
    def time_offset(self):
        """Gets the time_offset of this ContactRequest.  # noqa: E501


        :return: The time_offset of this ContactRequest.  # noqa: E501
        :rtype: float
        """
        return self._time_offset

    @time_offset.setter
    def time_offset(self, time_offset):
        """Sets the time_offset of this ContactRequest.


        :param time_offset: The time_offset of this ContactRequest.  # noqa: E501
        :type: float
        """

        self._time_offset = time_offset

    @property
    def latitude(self):
        """Gets the latitude of this ContactRequest.  # noqa: E501


        :return: The latitude of this ContactRequest.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this ContactRequest.


        :param latitude: The latitude of this ContactRequest.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this ContactRequest.  # noqa: E501


        :return: The longitude of this ContactRequest.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this ContactRequest.


        :param longitude: The longitude of this ContactRequest.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ContactRequest.  # noqa: E501


        :return: The custom_fields of this ContactRequest.  # noqa: E501
        :rtype: list[CustomFields]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ContactRequest.


        :param custom_fields: The custom_fields of this ContactRequest.  # noqa: E501
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
        if issubclass(ContactRequest, dict):
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
        if not isinstance(other, ContactRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
