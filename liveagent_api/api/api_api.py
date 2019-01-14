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


class ApiApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_api_keys(self, **kwargs):  # noqa: E501
        """Creates api key  # noqa: E501

        Create api key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_api_keys(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiKeyWithPrivileges api_key:
        :return: ApiKeyWithPrivileges
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_api_keys_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_api_keys_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_api_keys_with_http_info(self, **kwargs):  # noqa: E501
        """Creates api key  # noqa: E501

        Create api key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_api_keys_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiKeyWithPrivileges api_key:
        :return: ApiKeyWithPrivileges
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_api_keys" % key
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
        if 'api_key' in params:
            body_params = params['api_key']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'privileges']  # noqa: E501

        return self.api_client.call_api(
            '/apikeys', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiKeyWithPrivileges',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_api_key(self, apikey_id, **kwargs):  # noqa: E501
        """Deletes api key  # noqa: E501

        Delete an api key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_api_key(apikey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float apikey_id: (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_api_key_with_http_info(apikey_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_api_key_with_http_info(apikey_id, **kwargs)  # noqa: E501
            return data

    def delete_api_key_with_http_info(self, apikey_id, **kwargs):  # noqa: E501
        """Deletes api key  # noqa: E501

        Delete an api key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_api_key_with_http_info(apikey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float apikey_id: (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apikey_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_api_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apikey_id' is set
        if ('apikey_id' not in params or
                params['apikey_id'] is None):
            raise ValueError("Missing the required parameter `apikey_id` when calling `delete_api_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apikey_id' in params:
            path_params['apikeyId'] = params['apikey_id']  # noqa: E501

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
            '/apikeys/{apikeyId}', 'DELETE',
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

    def generate_api_key(self, **kwargs):  # noqa: E501
        """Gets new api keys  # noqa: E501

        Get new api key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_api_key(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ApiKey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_api_key_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_api_key_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_api_key_with_http_info(self, **kwargs):  # noqa: E501
        """Gets new api keys  # noqa: E501

        Get new api key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_api_key_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ApiKey
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
                    " to method generate_api_key" % key
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
            '/apikeys/_generate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiKey',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_api_info(self, api_version, **kwargs):  # noqa: E501
        """Gets api info  # noqa: E501

        Get information about api  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: v1 - legacy api version,  v3 - current api version (required)
        :return: ApiInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_api_info_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.get_api_info_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def get_api_info_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Gets api info  # noqa: E501

        Get information about api  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_info_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: v1 - legacy api version,  v3 - current api version (required)
        :return: ApiInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_api_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `get_api_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'api_version' in params:
            path_params['apiVersion'] = params['api_version']  # noqa: E501

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
            '/api/info/{apiVersion}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_api_key(self, apikey_id, **kwargs):  # noqa: E501
        """Gets api keys  # noqa: E501

        Get information about api keys  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_key(apikey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float apikey_id: (required)
        :return: ApiKeyWithPrivileges
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_api_key_with_http_info(apikey_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_api_key_with_http_info(apikey_id, **kwargs)  # noqa: E501
            return data

    def get_api_key_with_http_info(self, apikey_id, **kwargs):  # noqa: E501
        """Gets api keys  # noqa: E501

        Get information about api keys  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_key_with_http_info(apikey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float apikey_id: (required)
        :return: ApiKeyWithPrivileges
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apikey_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_api_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apikey_id' is set
        if ('apikey_id' not in params or
                params['apikey_id'] is None):
            raise ValueError("Missing the required parameter `apikey_id` when calling `get_api_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apikey_id' in params:
            path_params['apikeyId'] = params['apikey_id']  # noqa: E501

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
            '/apikeys/{apikeyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiKeyWithPrivileges',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_api_keys(self, **kwargs):  # noqa: E501
        """Gets api keys  # noqa: E501

        Get information about api keys  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_keys(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param str filters: Filters (json object {column:value, ...})
        :return: list[ApiKey]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_api_keys_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_api_keys_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_api_keys_with_http_info(self, **kwargs):  # noqa: E501
        """Gets api keys  # noqa: E501

        Get information about api keys  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_keys_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param str filters: Filters (json object {column:value, ...})
        :return: list[ApiKey]
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
                    " to method get_api_keys" % key
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
            '/apikeys', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ApiKey]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_api_privileges(self, **kwargs):  # noqa: E501
        """Gets api privileges  # noqa: E501

        Get api privileges  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_privileges(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ApiPrivilege]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_api_privileges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_api_privileges_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_api_privileges_with_http_info(self, **kwargs):  # noqa: E501
        """Gets api privileges  # noqa: E501

        Get api privileges  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_privileges_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ApiPrivilege]
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
                    " to method get_api_privileges" % key
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
            '/api/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ApiPrivilege]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def login(self, **kwargs):  # noqa: E501
        """Creates or returns API key from login.  # noqa: E501

        Creates or returns API key from login and password.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiKeyLogin api_key_login:
        :return: ApiKeyWithPrivileges
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.login_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.login_with_http_info(**kwargs)  # noqa: E501
            return data

    def login_with_http_info(self, **kwargs):  # noqa: E501
        """Creates or returns API key from login.  # noqa: E501

        Creates or returns API key from login and password.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiKeyLogin api_key_login:
        :return: ApiKeyWithPrivileges
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key_login']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method login" % key
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
        if 'api_key_login' in params:
            body_params = params['api_key_login']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/apikeys/_login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiKeyWithPrivileges',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_api_key(self, apikey_id, **kwargs):  # noqa: E501
        """Updates api key  # noqa: E501

        Update an api key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_api_key(apikey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float apikey_id: (required)
        :param ApiKeyWithPrivileges api_key:
        :return: ApiKeyWithPrivileges
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_api_key_with_http_info(apikey_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_api_key_with_http_info(apikey_id, **kwargs)  # noqa: E501
            return data

    def update_api_key_with_http_info(self, apikey_id, **kwargs):  # noqa: E501
        """Updates api key  # noqa: E501

        Update an api key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_api_key_with_http_info(apikey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float apikey_id: (required)
        :param ApiKeyWithPrivileges api_key:
        :return: ApiKeyWithPrivileges
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apikey_id', 'api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_api_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apikey_id' is set
        if ('apikey_id' not in params or
                params['apikey_id'] is None):
            raise ValueError("Missing the required parameter `apikey_id` when calling `update_api_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apikey_id' in params:
            path_params['apikeyId'] = params['apikey_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'api_key' in params:
            body_params = params['api_key']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'privileges']  # noqa: E501

        return self.api_client.call_api(
            '/apikeys/{apikeyId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiKeyWithPrivileges',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
