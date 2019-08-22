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


class PageVisit(object):
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
        'browser': 'str',
        'date_visit': 'datetime',
        'title': 'str',
        'url': 'str',
        'referrerurl': 'str'
    }

    attribute_map = {
        'browser': 'browser',
        'date_visit': 'date_visit',
        'title': 'title',
        'url': 'url',
        'referrerurl': 'referrerurl'
    }

    def __init__(self, browser=None, date_visit=None, title=None, url=None, referrerurl=None):  # noqa: E501
        """PageVisit - a model defined in Swagger"""  # noqa: E501

        self._browser = None
        self._date_visit = None
        self._title = None
        self._url = None
        self._referrerurl = None
        self.discriminator = None

        if browser is not None:
            self.browser = browser
        if date_visit is not None:
            self.date_visit = date_visit
        if title is not None:
            self.title = title
        if url is not None:
            self.url = url
        if referrerurl is not None:
            self.referrerurl = referrerurl

    @property
    def browser(self):
        """Gets the browser of this PageVisit.  # noqa: E501


        :return: The browser of this PageVisit.  # noqa: E501
        :rtype: str
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        """Sets the browser of this PageVisit.


        :param browser: The browser of this PageVisit.  # noqa: E501
        :type: str
        """

        self._browser = browser

    @property
    def date_visit(self):
        """Gets the date_visit of this PageVisit.  # noqa: E501


        :return: The date_visit of this PageVisit.  # noqa: E501
        :rtype: datetime
        """
        return self._date_visit

    @date_visit.setter
    def date_visit(self, date_visit):
        """Sets the date_visit of this PageVisit.


        :param date_visit: The date_visit of this PageVisit.  # noqa: E501
        :type: datetime
        """

        self._date_visit = date_visit

    @property
    def title(self):
        """Gets the title of this PageVisit.  # noqa: E501


        :return: The title of this PageVisit.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PageVisit.


        :param title: The title of this PageVisit.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def url(self):
        """Gets the url of this PageVisit.  # noqa: E501


        :return: The url of this PageVisit.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PageVisit.


        :param url: The url of this PageVisit.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def referrerurl(self):
        """Gets the referrerurl of this PageVisit.  # noqa: E501


        :return: The referrerurl of this PageVisit.  # noqa: E501
        :rtype: str
        """
        return self._referrerurl

    @referrerurl.setter
    def referrerurl(self, referrerurl):
        """Sets the referrerurl of this PageVisit.


        :param referrerurl: The referrerurl of this PageVisit.  # noqa: E501
        :type: str
        """

        self._referrerurl = referrerurl

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
        if issubclass(PageVisit, dict):
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
        if not isinstance(other, PageVisit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
