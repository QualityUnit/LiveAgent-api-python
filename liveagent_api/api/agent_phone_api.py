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


class AgentPhoneApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_agent_phone(self, agent_id, **kwargs):  # noqa: E501
        """Gets phone currently used by agent (use me as agentId for self)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_agent_phone(agent_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str agent_id: (required)
        :param str type: API (I - default), SIP (S)
        :return: PhoneDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_agent_phone_with_http_info(agent_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_agent_phone_with_http_info(agent_id, **kwargs)  # noqa: E501
            return data

    def get_agent_phone_with_http_info(self, agent_id, **kwargs):  # noqa: E501
        """Gets phone currently used by agent (use me as agentId for self)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_agent_phone_with_http_info(agent_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str agent_id: (required)
        :param str type: API (I - default), SIP (S)
        :return: PhoneDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_id', 'type']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_agent_phone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_id' is set
        if ('agent_id' not in params or
                params['agent_id'] is None):
            raise ValueError("Missing the required parameter `agent_id` when calling `get_agent_phone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_id' in params:
            path_params['agentId'] = params['agent_id']  # noqa: E501

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

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
            '/agent_phone/{agentId}', 'GET',
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

    def set_agent_phone(self, agent_id, phone_id, **kwargs):  # noqa: E501
        """Sets phone currently used by agent (use me as agentId for self)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_agent_phone(agent_id, phone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str agent_id: (required)
        :param str phone_id: New phone ID (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_agent_phone_with_http_info(agent_id, phone_id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_agent_phone_with_http_info(agent_id, phone_id, **kwargs)  # noqa: E501
            return data

    def set_agent_phone_with_http_info(self, agent_id, phone_id, **kwargs):  # noqa: E501
        """Sets phone currently used by agent (use me as agentId for self)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_agent_phone_with_http_info(agent_id, phone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str agent_id: (required)
        :param str phone_id: New phone ID (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_id', 'phone_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_agent_phone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_id' is set
        if ('agent_id' not in params or
                params['agent_id'] is None):
            raise ValueError("Missing the required parameter `agent_id` when calling `set_agent_phone`")  # noqa: E501
        # verify the required parameter 'phone_id' is set
        if ('phone_id' not in params or
                params['phone_id'] is None):
            raise ValueError("Missing the required parameter `phone_id` when calling `set_agent_phone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_id' in params:
            path_params['agentId'] = params['agent_id']  # noqa: E501

        query_params = []
        if 'phone_id' in params:
            query_params.append(('phoneId', params['phone_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
            '/agent_phone/{agentId}', 'PUT',
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