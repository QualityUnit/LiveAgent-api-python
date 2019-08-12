# coding: utf-8

"""
    LiveAgent API

    This page contains complete API documentation for LiveAgent software. To display additional info and examples for specific API method, just click on the method name in the list below.<br/><br/>To be able to make API requests you need to generate an API key in your admin panel first. [See this article for detailed info.](https://support.ladesk.com/741982-API-key)<br/><br/>Additional info about more advanced agent, contact or ticket API filters can be found [in this article](https://support.ladesk.com/513528-APIv3-advanced-filter-examples).<br/><br/>If you have any question or doubts regarding this API, please do not hesitate to contact our support team.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from liveagent_api.api_client import ApiClient


class CannedMessagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_canned_message(self, **kwargs):  # noqa: E501
        """Create canned message  # noqa: E501

        Create new canned message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_canned_message(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CannedMessage canned_message:
        :return: CannedMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_canned_message_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_canned_message_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_canned_message_with_http_info(self, **kwargs):  # noqa: E501
        """Create canned message  # noqa: E501

        Create new canned message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_canned_message_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CannedMessage canned_message:
        :return: CannedMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['canned_message']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_canned_message" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'canned_message' in params:
            body_params = params['canned_message']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'privileges']  # noqa: E501

        return self.api_client.call_api(
            '/canned_messages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CannedMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_canned_message(self, canned_message_id, **kwargs):  # noqa: E501
        """Canned message  # noqa: E501

        Deletes a canned message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_canned_message(canned_message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str canned_message_id: (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_canned_message_with_http_info(canned_message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_canned_message_with_http_info(canned_message_id, **kwargs)  # noqa: E501
            return data

    def delete_canned_message_with_http_info(self, canned_message_id, **kwargs):  # noqa: E501
        """Canned message  # noqa: E501

        Deletes a canned message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_canned_message_with_http_info(canned_message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str canned_message_id: (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['canned_message_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_canned_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'canned_message_id' is set
        if ('canned_message_id' not in params or
                params['canned_message_id'] is None):
            raise ValueError("Missing the required parameter `canned_message_id` when calling `delete_canned_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'canned_message_id' in params:
            path_params['cannedMessageId'] = params['canned_message_id']  # noqa: E501

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
            '/canned_messages/{cannedMessageId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OkResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_canned_message(self, canned_message_id, **kwargs):  # noqa: E501
        """Gets canned message  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_canned_message(canned_message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str canned_message_id: (required)
        :return: CannedMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_canned_message_with_http_info(canned_message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_canned_message_with_http_info(canned_message_id, **kwargs)  # noqa: E501
            return data

    def get_canned_message_with_http_info(self, canned_message_id, **kwargs):  # noqa: E501
        """Gets canned message  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_canned_message_with_http_info(canned_message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str canned_message_id: (required)
        :return: CannedMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['canned_message_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_canned_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'canned_message_id' is set
        if ('canned_message_id' not in params or
                params['canned_message_id'] is None):
            raise ValueError("Missing the required parameter `canned_message_id` when calling `get_canned_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'canned_message_id' in params:
            path_params['cannedMessageId'] = params['canned_message_id']  # noqa: E501

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
            '/canned_messages/{cannedMessageId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CannedMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_canned_messages_list(self, **kwargs):  # noqa: E501
        """Gets list of canned messages  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_canned_messages_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param str filters: Filters (json object {column:value, ...} or json array [[column,operator,value], ...])
        :return: list[CannedMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_canned_messages_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_canned_messages_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_canned_messages_list_with_http_info(self, **kwargs):  # noqa: E501
        """Gets list of canned messages  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_canned_messages_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param str filters: Filters (json object {column:value, ...} or json array [[column,operator,value], ...])
        :return: list[CannedMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page', '_from', 'to', 'sort_dir', 'sort_field', 'filters']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_canned_messages_list" % key
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
            '/canned_messages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CannedMessage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_canned_message(self, canned_message_id, **kwargs):  # noqa: E501
        """Update canned message  # noqa: E501

        Update a canned message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_canned_message(canned_message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str canned_message_id: (required)
        :param CannedMessage canned_message:
        :return: CannedMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_canned_message_with_http_info(canned_message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_canned_message_with_http_info(canned_message_id, **kwargs)  # noqa: E501
            return data

    def update_canned_message_with_http_info(self, canned_message_id, **kwargs):  # noqa: E501
        """Update canned message  # noqa: E501

        Update a canned message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_canned_message_with_http_info(canned_message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str canned_message_id: (required)
        :param CannedMessage canned_message:
        :return: CannedMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['canned_message_id', 'canned_message']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_canned_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'canned_message_id' is set
        if ('canned_message_id' not in params or
                params['canned_message_id'] is None):
            raise ValueError("Missing the required parameter `canned_message_id` when calling `update_canned_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'canned_message_id' in params:
            path_params['cannedMessageId'] = params['canned_message_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'canned_message' in params:
            body_params = params['canned_message']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'privileges']  # noqa: E501

        return self.api_client.call_api(
            '/canned_messages/{cannedMessageId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CannedMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
