# coding: utf-8

"""
PhonesApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PhonesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_phone(self, number, **kwargs):
        """
        Creates external phone
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_phone(number, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str number:  (required)
        :param str type: S - SIP phone, E - PSTN phone
        :param str name: 
        :return: PhoneDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['number', 'type', 'name']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_phone" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'number' is set
        if ('number' not in params) or (params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `create_phone`")

        resource_path = '/phones'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'number' in params:
            query_params['number'] = params['number']
        if 'type' in params:
            query_params['type'] = params['type']
        if 'name' in params:
            query_params['name'] = params['name']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PhoneDevice',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_phone(self, phone_id, **kwargs):
        """
        Gets phone device (use _app_ for LiveAgent Phone app device and _web_ for web device)
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_phone(phone_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str phone_id:  (required)
        :return: PhoneDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_phone" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'phone_id' is set
        if ('phone_id' not in params) or (params['phone_id'] is None):
            raise ValueError("Missing the required parameter `phone_id` when calling `get_phone`")

        resource_path = '/phones/{phoneId}'.replace('{format}', 'json')
        path_params = {}
        if 'phone_id' in params:
            path_params['phoneId'] = params['phone_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PhoneDevice',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_phones_list(self, **kwargs):
        """
        Gets list of available phone devices.\nSpecial filters (userId - filter phones available for specified user only)\n
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_phones_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
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

        all_params = ['page', 'per_page', '_from', 'to', 'sort_dir', 'sort_field', 'filters']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_phones_list" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/phones'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['_page'] = params['page']
        if 'per_page' in params:
            query_params['_perPage'] = params['per_page']
        if '_from' in params:
            query_params['_from'] = params['_from']
        if 'to' in params:
            query_params['_to'] = params['to']
        if 'sort_dir' in params:
            query_params['_sortDir'] = params['sort_dir']
        if 'sort_field' in params:
            query_params['_sortField'] = params['sort_field']
        if 'filters' in params:
            query_params['_filters'] = params['filters']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[PhoneDevice]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def remove_phone(self, phone_id, **kwargs):
        """
        Remove phone
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_phone(phone_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str phone_id:  (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_phone" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'phone_id' is set
        if ('phone_id' not in params) or (params['phone_id'] is None):
            raise ValueError("Missing the required parameter `phone_id` when calling `remove_phone`")

        resource_path = '/phones/{phoneId}'.replace('{format}', 'json')
        path_params = {}
        if 'phone_id' in params:
            path_params['phoneId'] = params['phone_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='OkResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_phone_params(self, phone_id, params, **kwargs):
        """
        Update phone paramas
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_phone_params(phone_id, params, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str phone_id:  (required)
        :param str params: New params (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_id', 'params']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_phone_params" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'phone_id' is set
        if ('phone_id' not in params) or (params['phone_id'] is None):
            raise ValueError("Missing the required parameter `phone_id` when calling `update_phone_params`")
        # verify the required parameter 'params' is set
        if ('params' not in params) or (params['params'] is None):
            raise ValueError("Missing the required parameter `params` when calling `update_phone_params`")

        resource_path = '/phones/{phoneId}/_updateParams'.replace('{format}', 'json')
        path_params = {}
        if 'phone_id' in params:
            path_params['phoneId'] = params['phone_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'params' in params:
            form_params.append(('params', params['params']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='OkResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
