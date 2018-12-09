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


class PhoneNumbersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_number(self, type, number, status, **kwargs):  # noqa: E501
        """Add new number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_number(type, number, status, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: A - API controlled number, T - Twilio number, T-O - Twilio outgoing number, D - Digitale, S - Asterisk (required)
        :param str number: (required)
        :param str status: A - Active, I - Inactive (required)
        :param str dial_out_prefix: Prefix needed to originate call using this number
        :param bool record_call:
        :param str name:
        :param str departmentid:
        :param str host_settings: json encoded host settings
        :param str host:
        :param str port:
        :param str user:
        :param str password:
        :param str providerid:
        :param str ivr:
        :return: PhoneNumber
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_number_with_http_info(type, number, status, **kwargs)  # noqa: E501
        else:
            (data) = self.add_number_with_http_info(type, number, status, **kwargs)  # noqa: E501
            return data

    def add_number_with_http_info(self, type, number, status, **kwargs):  # noqa: E501
        """Add new number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_number_with_http_info(type, number, status, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: A - API controlled number, T - Twilio number, T-O - Twilio outgoing number, D - Digitale, S - Asterisk (required)
        :param str number: (required)
        :param str status: A - Active, I - Inactive (required)
        :param str dial_out_prefix: Prefix needed to originate call using this number
        :param bool record_call:
        :param str name:
        :param str departmentid:
        :param str host_settings: json encoded host settings
        :param str host:
        :param str port:
        :param str user:
        :param str password:
        :param str providerid:
        :param str ivr:
        :return: PhoneNumber
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'number', 'status', 'dial_out_prefix', 'record_call', 'name', 'departmentid', 'host_settings', 'host', 'port', 'user', 'password', 'providerid', 'ivr']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `add_number`")  # noqa: E501
        # verify the required parameter 'number' is set
        if ('number' not in params or
                params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `add_number`")  # noqa: E501
        # verify the required parameter 'status' is set
        if ('status' not in params or
                params['status'] is None):
            raise ValueError("Missing the required parameter `status` when calling `add_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'type' in params:
            form_params.append(('type', params['type']))  # noqa: E501
        if 'dial_out_prefix' in params:
            form_params.append(('dial_out_prefix', params['dial_out_prefix']))  # noqa: E501
        if 'record_call' in params:
            form_params.append(('record_call', params['record_call']))  # noqa: E501
        if 'number' in params:
            form_params.append(('number', params['number']))  # noqa: E501
        if 'status' in params:
            form_params.append(('status', params['status']))  # noqa: E501
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'departmentid' in params:
            form_params.append(('departmentid', params['departmentid']))  # noqa: E501
        if 'host_settings' in params:
            form_params.append(('host_settings', params['host_settings']))  # noqa: E501
        if 'host' in params:
            form_params.append(('host', params['host']))  # noqa: E501
        if 'port' in params:
            form_params.append(('port', params['port']))  # noqa: E501
        if 'user' in params:
            form_params.append(('user', params['user']))  # noqa: E501
        if 'password' in params:
            form_params.append(('password', params['password']))  # noqa: E501
        if 'providerid' in params:
            form_params.append(('providerid', params['providerid']))  # noqa: E501
        if 'ivr' in params:
            form_params.append(('ivr', params['ivr']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'privileges']  # noqa: E501

        return self.api_client.call_api(
            '/phone_numbers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PhoneNumber',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_phone_number(self, phone_number_id, **kwargs):  # noqa: E501
        """Gets phone number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_phone_number(phone_number_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_number_id: (required)
        :return: PhoneNumber
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_phone_number_with_http_info(phone_number_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_phone_number_with_http_info(phone_number_id, **kwargs)  # noqa: E501
            return data

    def get_phone_number_with_http_info(self, phone_number_id, **kwargs):  # noqa: E501
        """Gets phone number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_phone_number_with_http_info(phone_number_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_number_id: (required)
        :return: PhoneNumber
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_number_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_phone_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'phone_number_id' is set
        if ('phone_number_id' not in params or
                params['phone_number_id'] is None):
            raise ValueError("Missing the required parameter `phone_number_id` when calling `get_phone_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone_number_id' in params:
            path_params['phoneNumberId'] = params['phone_number_id']  # noqa: E501

        query_params = []

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
            '/phone_numbers/{phoneNumberId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PhoneNumber',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_phone_numbers_list(self, **kwargs):  # noqa: E501
        """Gets list of available phone numbers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_phone_numbers_list(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param str filters: Filters (json object {column:value, ...})
        :param list[str] additional_objects: Additional objects
        :return: list[PhoneNumber]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_phone_numbers_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_phone_numbers_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_phone_numbers_list_with_http_info(self, **kwargs):  # noqa: E501
        """Gets list of available phone numbers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_phone_numbers_list_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param str filters: Filters (json object {column:value, ...})
        :param list[str] additional_objects: Additional objects
        :return: list[PhoneNumber]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page', '_from', 'to', 'sort_dir', 'sort_field', 'filters', 'additional_objects']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_phone_numbers_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('_page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('_perPage', params['per_page']))  # noqa: E501
        if '_from' in params:
            query_params.append(('_from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('_to', params['to']))  # noqa: E501
        if 'sort_dir' in params:
            query_params.append(('_sortDir', params['sort_dir']))  # noqa: E501
        if 'sort_field' in params:
            query_params.append(('_sortField', params['sort_field']))  # noqa: E501
        if 'filters' in params:
            query_params.append(('_filters', params['filters']))  # noqa: E501
        if 'additional_objects' in params:
            query_params.append(('additionalObjects', params['additional_objects']))  # noqa: E501
            collection_formats['additionalObjects'] = 'csv'  # noqa: E501

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
            '/phone_numbers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PhoneNumber]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_phone_number(self, phone_number_id, **kwargs):  # noqa: E501
        """Remove phone number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_phone_number(phone_number_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_number_id: (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_phone_number_with_http_info(phone_number_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_phone_number_with_http_info(phone_number_id, **kwargs)  # noqa: E501
            return data

    def remove_phone_number_with_http_info(self, phone_number_id, **kwargs):  # noqa: E501
        """Remove phone number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_phone_number_with_http_info(phone_number_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_number_id: (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_number_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_phone_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'phone_number_id' is set
        if ('phone_number_id' not in params or
                params['phone_number_id'] is None):
            raise ValueError("Missing the required parameter `phone_number_id` when calling `remove_phone_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone_number_id' in params:
            path_params['phoneNumberId'] = params['phone_number_id']  # noqa: E501

        query_params = []

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
            '/phone_numbers/{phoneNumberId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OkResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_phone_number(self, phone_number_id, phone_number, **kwargs):  # noqa: E501
        """Update phone number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_phone_number(phone_number_id, phone_number, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_number_id: (required)
        :param PhoneNumber phone_number: (required)
        :return: PhoneNumber
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_phone_number_with_http_info(phone_number_id, phone_number, **kwargs)  # noqa: E501
        else:
            (data) = self.update_phone_number_with_http_info(phone_number_id, phone_number, **kwargs)  # noqa: E501
            return data

    def update_phone_number_with_http_info(self, phone_number_id, phone_number, **kwargs):  # noqa: E501
        """Update phone number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_phone_number_with_http_info(phone_number_id, phone_number, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_number_id: (required)
        :param PhoneNumber phone_number: (required)
        :return: PhoneNumber
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_number_id', 'phone_number']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_phone_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'phone_number_id' is set
        if ('phone_number_id' not in params or
                params['phone_number_id'] is None):
            raise ValueError("Missing the required parameter `phone_number_id` when calling `update_phone_number`")  # noqa: E501
        # verify the required parameter 'phone_number' is set
        if ('phone_number' not in params or
                params['phone_number'] is None):
            raise ValueError("Missing the required parameter `phone_number` when calling `update_phone_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone_number_id' in params:
            path_params['phoneNumberId'] = params['phone_number_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'phone_number' in params:
            body_params = params['phone_number']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'privileges']  # noqa: E501

        return self.api_client.call_api(
            '/phone_numbers/{phoneNumberId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PhoneNumber',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_phone_number_status(self, phone_number_id, status, **kwargs):  # noqa: E501
        """Update phone number status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_phone_number_status(phone_number_id, status, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_number_id: (required)
        :param str status: A - Active, I - Inactive (required)
        :return: PhoneNumber
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_phone_number_status_with_http_info(phone_number_id, status, **kwargs)  # noqa: E501
        else:
            (data) = self.update_phone_number_status_with_http_info(phone_number_id, status, **kwargs)  # noqa: E501
            return data

    def update_phone_number_status_with_http_info(self, phone_number_id, status, **kwargs):  # noqa: E501
        """Update phone number status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_phone_number_status_with_http_info(phone_number_id, status, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_number_id: (required)
        :param str status: A - Active, I - Inactive (required)
        :return: PhoneNumber
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_number_id', 'status']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_phone_number_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'phone_number_id' is set
        if ('phone_number_id' not in params or
                params['phone_number_id'] is None):
            raise ValueError("Missing the required parameter `phone_number_id` when calling `update_phone_number_status`")  # noqa: E501
        # verify the required parameter 'status' is set
        if ('status' not in params or
                params['status'] is None):
            raise ValueError("Missing the required parameter `status` when calling `update_phone_number_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone_number_id' in params:
            path_params['phoneNumberId'] = params['phone_number_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'status' in params:
            form_params.append(('status', params['status']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'privileges']  # noqa: E501

        return self.api_client.call_api(
            '/phone_numbers/{phoneNumberId}/status', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PhoneNumber',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)