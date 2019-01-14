# coding: utf-8

"""
    LiveAgent API

    LiveAgent API  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from liveagent_api.api_client import ApiClient


class PageVisitsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_page_visit_by_contact_id(self, contact_id, **kwargs):  # noqa: E501
        """Gets a page visits  # noqa: E501

        Gets a page visits for user contact id. If elastic search is enabled and it throws exception, error is logged and empty array is returned.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page_visit_by_contact_id(contact_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str contact_id: (required)
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :return: list[PageVisit]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_page_visit_by_contact_id_with_http_info(contact_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_page_visit_by_contact_id_with_http_info(contact_id, **kwargs)  # noqa: E501
            return data

    def get_page_visit_by_contact_id_with_http_info(self, contact_id, **kwargs):  # noqa: E501
        """Gets a page visits  # noqa: E501

        Gets a page visits for user contact id. If elastic search is enabled and it throws exception, error is logged and empty array is returned.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page_visit_by_contact_id_with_http_info(contact_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str contact_id: (required)
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :return: list[PageVisit]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contact_id', 'sort_dir', 'sort_field', 'page', 'per_page', '_from', 'to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_page_visit_by_contact_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params or
                params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `get_page_visit_by_contact_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'contact_id' in params:
            path_params['contactId'] = params['contact_id']  # noqa: E501

        query_params = []
        if 'sort_dir' in params:
            query_params.append(('_sortDir', params['sort_dir']))  # noqa: E501
        if 'sort_field' in params:
            query_params.append(('_sortField', params['sort_field']))  # noqa: E501
        if 'page' in params:
            query_params.append(('_page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('_perPage', params['per_page']))  # noqa: E501
        if '_from' in params:
            query_params.append(('_from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('_to', params['to']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'privileges']  # noqa: E501

        return self.api_client.call_api(
            '/page_visits/{contactId}/contact', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PageVisit]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
