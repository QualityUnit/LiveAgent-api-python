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


class Customer(object):
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
        'name': 'str',
        'email': 'str',
        'company': 'str',
        'phone': 'str',
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'state': 'str',
        'country': 'str',
        'zip': 'str',
        'vat_id': 'str',
        'ico_sk': 'str',
        'dic_sk': 'str'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'company': 'company',
        'phone': 'phone',
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'state': 'state',
        'country': 'country',
        'zip': 'zip',
        'vat_id': 'vat_id',
        'ico_sk': 'ico_sk',
        'dic_sk': 'dic_sk'
    }

    def __init__(self, name=None, email=None, company=None, phone=None, address1=None, address2=None, city=None, state=None, country=None, zip=None, vat_id=None, ico_sk=None, dic_sk=None):  # noqa: E501
        """Customer - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._email = None
        self._company = None
        self._phone = None
        self._address1 = None
        self._address2 = None
        self._city = None
        self._state = None
        self._country = None
        self._zip = None
        self._vat_id = None
        self._ico_sk = None
        self._dic_sk = None
        self.discriminator = None

        self.name = name
        self.email = email
        if company is not None:
            self.company = company
        if phone is not None:
            self.phone = phone
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if country is not None:
            self.country = country
        if zip is not None:
            self.zip = zip
        if vat_id is not None:
            self.vat_id = vat_id
        if ico_sk is not None:
            self.ico_sk = ico_sk
        if dic_sk is not None:
            self.dic_sk = dic_sk

    @property
    def name(self):
        """Gets the name of this Customer.  # noqa: E501


        :return: The name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Customer.


        :param name: The name of this Customer.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this Customer.  # noqa: E501


        :return: The email of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Customer.


        :param email: The email of this Customer.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def company(self):
        """Gets the company of this Customer.  # noqa: E501


        :return: The company of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Customer.


        :param company: The company of this Customer.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def phone(self):
        """Gets the phone of this Customer.  # noqa: E501


        :return: The phone of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Customer.


        :param phone: The phone of this Customer.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def address1(self):
        """Gets the address1 of this Customer.  # noqa: E501


        :return: The address1 of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this Customer.


        :param address1: The address1 of this Customer.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this Customer.  # noqa: E501


        :return: The address2 of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Customer.


        :param address2: The address2 of this Customer.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this Customer.  # noqa: E501


        :return: The city of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Customer.


        :param city: The city of this Customer.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this Customer.  # noqa: E501


        :return: The state of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Customer.


        :param state: The state of this Customer.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """Gets the country of this Customer.  # noqa: E501


        :return: The country of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Customer.


        :param country: The country of this Customer.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def zip(self):
        """Gets the zip of this Customer.  # noqa: E501


        :return: The zip of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this Customer.


        :param zip: The zip of this Customer.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def vat_id(self):
        """Gets the vat_id of this Customer.  # noqa: E501


        :return: The vat_id of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._vat_id

    @vat_id.setter
    def vat_id(self, vat_id):
        """Sets the vat_id of this Customer.


        :param vat_id: The vat_id of this Customer.  # noqa: E501
        :type: str
        """

        self._vat_id = vat_id

    @property
    def ico_sk(self):
        """Gets the ico_sk of this Customer.  # noqa: E501


        :return: The ico_sk of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._ico_sk

    @ico_sk.setter
    def ico_sk(self, ico_sk):
        """Sets the ico_sk of this Customer.


        :param ico_sk: The ico_sk of this Customer.  # noqa: E501
        :type: str
        """

        self._ico_sk = ico_sk

    @property
    def dic_sk(self):
        """Gets the dic_sk of this Customer.  # noqa: E501


        :return: The dic_sk of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._dic_sk

    @dic_sk.setter
    def dic_sk(self, dic_sk):
        """Sets the dic_sk of this Customer.


        :param dic_sk: The dic_sk of this Customer.  # noqa: E501
        :type: str
        """

        self._dic_sk = dic_sk

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
        if issubclass(Customer, dict):
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
        if not isinstance(other, Customer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
