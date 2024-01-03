# coding: utf-8

"""
    LiveAgent API

    This page contains complete API documentation for LiveAgent software. To display additional info and examples for specific API method, just click on the method name in the list below.<br/><br/>To be able to make API requests you need to generate an API key in your admin panel first. [See this article for detailed info.](https://support.liveagent.com/741982-API-key)<br/><br/>Additional info about more advanced agent, contact or ticket API filters can be found [in this article](https://support.liveagent.com/513528-APIv3-advanced-filter-examples).<br/><br/>If you have any question or doubts regarding this API, please do not hesitate to contact our support team.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from liveagent_api.api_client import ApiClient


class CustomButtonsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_custom_button(self, **kwargs):  # noqa: E501
        """Create new custom button  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_custom_button(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomButton custom_button:
        :return: CustomButton
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_custom_button_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_custom_button_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_custom_button_with_http_info(self, **kwargs):  # noqa: E501
        """Create new custom button  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_custom_button_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomButton custom_button:
        :return: CustomButton
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['custom_button']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_custom_button" % key
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
        if 'custom_button' in params:
            body_params = params['custom_button']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'privileges']  # noqa: E501

        return self.api_client.call_api(
            '/custom_buttons', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomButton',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_custom_button(self, custom_button_id, **kwargs):  # noqa: E501
        """Delete custom button  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_custom_button(custom_button_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_button_id: (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_custom_button_with_http_info(custom_button_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_custom_button_with_http_info(custom_button_id, **kwargs)  # noqa: E501
            return data

    def delete_custom_button_with_http_info(self, custom_button_id, **kwargs):  # noqa: E501
        """Delete custom button  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_custom_button_with_http_info(custom_button_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_button_id: (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['custom_button_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_custom_button" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'custom_button_id' is set
        if self.api_client.client_side_validation and ('custom_button_id' not in params or
                                                       params['custom_button_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `custom_button_id` when calling `delete_custom_button`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'custom_button_id' in params:
            path_params['customButtonId'] = params['custom_button_id']  # noqa: E501

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
            '/custom_buttons/{customButtonId}', 'DELETE',
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

    def get_custom_button(self, custom_button_id, **kwargs):  # noqa: E501
        """Get custom button by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_button(custom_button_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_button_id: (required)
        :return: CustomButton
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_custom_button_with_http_info(custom_button_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_custom_button_with_http_info(custom_button_id, **kwargs)  # noqa: E501
            return data

    def get_custom_button_with_http_info(self, custom_button_id, **kwargs):  # noqa: E501
        """Get custom button by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_button_with_http_info(custom_button_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_button_id: (required)
        :return: CustomButton
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['custom_button_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_custom_button" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'custom_button_id' is set
        if self.api_client.client_side_validation and ('custom_button_id' not in params or
                                                       params['custom_button_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `custom_button_id` when calling `get_custom_button`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'custom_button_id' in params:
            path_params['customButtonId'] = params['custom_button_id']  # noqa: E501

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
            '/custom_buttons/{customButtonId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomButton',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_custom_buttons_list(self, **kwargs):  # noqa: E501
        """Gets list of custom buttons  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_buttons_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param str filters: Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...]
        :return: list[CustomButton]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_custom_buttons_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_custom_buttons_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_custom_buttons_list_with_http_info(self, **kwargs):  # noqa: E501
        """Gets list of custom buttons  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_buttons_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param str filters: Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...]
        :return: list[CustomButton]
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
                    " to method get_custom_buttons_list" % key
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
            '/custom_buttons', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CustomButton]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_custom_button(self, custom_button_id, **kwargs):  # noqa: E501
        """Update custom button  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_custom_button(custom_button_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_button_id: (required)
        :param CustomButton custom_button:
        :return: CustomButton
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_custom_button_with_http_info(custom_button_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_custom_button_with_http_info(custom_button_id, **kwargs)  # noqa: E501
            return data

    def update_custom_button_with_http_info(self, custom_button_id, **kwargs):  # noqa: E501
        """Update custom button  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_custom_button_with_http_info(custom_button_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_button_id: (required)
        :param CustomButton custom_button:
        :return: CustomButton
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['custom_button_id', 'custom_button']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_custom_button" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'custom_button_id' is set
        if self.api_client.client_side_validation and ('custom_button_id' not in params or
                                                       params['custom_button_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `custom_button_id` when calling `update_custom_button`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'custom_button_id' in params:
            path_params['customButtonId'] = params['custom_button_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'custom_button' in params:
            body_params = params['custom_button']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'privileges']  # noqa: E501

        return self.api_client.call_api(
            '/custom_buttons/{customButtonId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomButton',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
