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


class SlasApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_sla(self, level_id, **kwargs):  # noqa: E501
        """Gets sla  # noqa: E501

        Gets sla  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sla(level_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str level_id: (required)
        :return: Sla
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sla_with_http_info(level_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sla_with_http_info(level_id, **kwargs)  # noqa: E501
            return data

    def get_sla_with_http_info(self, level_id, **kwargs):  # noqa: E501
        """Gets sla  # noqa: E501

        Gets sla  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sla_with_http_info(level_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str level_id: (required)
        :return: Sla
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['level_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sla" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'level_id' is set
        if ('level_id' not in params or
                params['level_id'] is None):
            raise ValueError("Missing the required parameter `level_id` when calling `get_sla`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'level_id' in params:
            path_params['levelId'] = params['level_id']  # noqa: E501

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
            '/slas/{levelId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Sla',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sla_ticket_history(self, ticket_id, **kwargs):  # noqa: E501
        """Gets ticket sla history  # noqa: E501

        Gets ticket sla history  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sla_ticket_history(ticket_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticket_id: (required)
        :return: SlaHistory
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sla_ticket_history_with_http_info(ticket_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sla_ticket_history_with_http_info(ticket_id, **kwargs)  # noqa: E501
            return data

    def get_sla_ticket_history_with_http_info(self, ticket_id, **kwargs):  # noqa: E501
        """Gets ticket sla history  # noqa: E501

        Gets ticket sla history  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sla_ticket_history_with_http_info(ticket_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticket_id: (required)
        :return: SlaHistory
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ticket_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sla_ticket_history" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ticket_id' is set
        if ('ticket_id' not in params or
                params['ticket_id'] is None):
            raise ValueError("Missing the required parameter `ticket_id` when calling `get_sla_ticket_history`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ticket_id' in params:
            path_params['ticketId'] = params['ticket_id']  # noqa: E501

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
            '/slas/{ticketId}/history', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SlaHistory',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_slas_list(self, **kwargs):  # noqa: E501
        """Gets list of slas  # noqa: E501

        Gets list of slas  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_slas_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Sla]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_slas_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_slas_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_slas_list_with_http_info(self, **kwargs):  # noqa: E501
        """Gets list of slas  # noqa: E501

        Gets list of slas  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_slas_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Sla]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_slas_list" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'privileges']  # noqa: E501

        return self.api_client.call_api(
            '/slas', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Sla]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
