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


class PhonesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_phone(self, number, **kwargs):  # noqa: E501
        """Creates external phone  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_phone(number, async=True)
        >>> result = thread.get()

        :param async bool
        :param str number: (required)
        :param str type: S - SIP phone, E - PSTN phone
        :param str name:
        :return: PhoneDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_phone_with_http_info(number, **kwargs)  # noqa: E501
        else:
            (data) = self.create_phone_with_http_info(number, **kwargs)  # noqa: E501
            return data

    def create_phone_with_http_info(self, number, **kwargs):  # noqa: E501
        """Creates external phone  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_phone_with_http_info(number, async=True)
        >>> result = thread.get()

        :param async bool
        :param str number: (required)
        :param str type: S - SIP phone, E - PSTN phone
        :param str name:
        :return: PhoneDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['number', 'type', 'name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_phone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'number' is set
        if ('number' not in params or
                params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `create_phone`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'number' in params:
            query_params.append(('number', params['number']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501

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
        auth_settings = ['privileges']  # noqa: E501

        return self.api_client.call_api(
            '/phones', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PhoneDevice',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_phone(self, phone_id, **kwargs):  # noqa: E501
        """Gets phone device (use _app_ for LiveAgent Phone app device and _web_ for web device)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_phone(phone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_id: (required)
        :return: PhoneDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_phone_with_http_info(phone_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_phone_with_http_info(phone_id, **kwargs)  # noqa: E501
            return data

    def get_phone_with_http_info(self, phone_id, **kwargs):  # noqa: E501
        """Gets phone device (use _app_ for LiveAgent Phone app device and _web_ for web device)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_phone_with_http_info(phone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_id: (required)
        :return: PhoneDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_phone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'phone_id' is set
        if ('phone_id' not in params or
                params['phone_id'] is None):
            raise ValueError("Missing the required parameter `phone_id` when calling `get_phone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone_id' in params:
            path_params['phoneId'] = params['phone_id']  # noqa: E501

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
            '/phones/{phoneId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PhoneDevice',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_phones_list(self, **kwargs):  # noqa: E501
        """Gets list of available phone devices. Special filters (userId - filter phones available for specified user only)   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_phones_list(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param str filters: Filters (json object {column:value, ...})
        :return: list[PhoneDevice]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_phones_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_phones_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_phones_list_with_http_info(self, **kwargs):  # noqa: E501
        """Gets list of available phone devices. Special filters (userId - filter phones available for specified user only)   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_phones_list_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param str filters: Filters (json object {column:value, ...})
        :return: list[PhoneDevice]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page', '_from', 'to', 'sort_dir', 'sort_field', 'filters']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_phones_list" % key
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
            '/phones', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PhoneDevice]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_phone(self, phone_id, **kwargs):  # noqa: E501
        """Remove phone  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_phone(phone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_id: (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_phone_with_http_info(phone_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_phone_with_http_info(phone_id, **kwargs)  # noqa: E501
            return data

    def remove_phone_with_http_info(self, phone_id, **kwargs):  # noqa: E501
        """Remove phone  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_phone_with_http_info(phone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_id: (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_phone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'phone_id' is set
        if ('phone_id' not in params or
                params['phone_id'] is None):
            raise ValueError("Missing the required parameter `phone_id` when calling `remove_phone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone_id' in params:
            path_params['phoneId'] = params['phone_id']  # noqa: E501

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
            '/phones/{phoneId}', 'DELETE',
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

    def update_phone_params(self, phone_id, params, **kwargs):  # noqa: E501
        """Update phone paramas  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_phone_params(phone_id, params, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_id: (required)
        :param str params: New params (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_phone_params_with_http_info(phone_id, params, **kwargs)  # noqa: E501
        else:
            (data) = self.update_phone_params_with_http_info(phone_id, params, **kwargs)  # noqa: E501
            return data

    def update_phone_params_with_http_info(self, phone_id, params, **kwargs):  # noqa: E501
        """Update phone paramas  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_phone_params_with_http_info(phone_id, params, async=True)
        >>> result = thread.get()

        :param async bool
        :param str phone_id: (required)
        :param str params: New params (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_id', 'params']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_phone_params" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'phone_id' is set
        if ('phone_id' not in params or
                params['phone_id'] is None):
            raise ValueError("Missing the required parameter `phone_id` when calling `update_phone_params`")  # noqa: E501
        # verify the required parameter 'params' is set
        if ('params' not in params or
                params['params'] is None):
            raise ValueError("Missing the required parameter `params` when calling `update_phone_params`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone_id' in params:
            path_params['phoneId'] = params['phone_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'params' in params:
            form_params.append(('params', params['params']))  # noqa: E501

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
            '/phones/{phoneId}/_updateParams', 'PUT',
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
