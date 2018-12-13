# coding: utf-8

"""
SlasApi.py
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


class SlasApi(object):
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

    def get_sla(self, level_id, **kwargs):
        """
        Gets sla
        Gets sla

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sla(level_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str level_id:  (required)
        :return: Sla
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['level_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sla" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'level_id' is set
        if ('level_id' not in params) or (params['level_id'] is None):
            raise ValueError("Missing the required parameter `level_id` when calling `get_sla`")

        resource_path = '/slas/{levelId}'.replace('{format}', 'json')
        path_params = {}
        if 'level_id' in params:
            path_params['levelId'] = params['level_id']

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
                                            response_type='Sla',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_sla_ticket_history(self, ticket_id, **kwargs):
        """
        Gets ticket sla history
        Gets ticket sla history

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sla_ticket_history(ticket_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str ticket_id:  (required)
        :return: SlaHistory
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ticket_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sla_ticket_history" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'ticket_id' is set
        if ('ticket_id' not in params) or (params['ticket_id'] is None):
            raise ValueError("Missing the required parameter `ticket_id` when calling `get_sla_ticket_history`")

        resource_path = '/slas/{ticketId}/history'.replace('{format}', 'json')
        path_params = {}
        if 'ticket_id' in params:
            path_params['ticketId'] = params['ticket_id']

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
                                            response_type='SlaHistory',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_slas_list(self, **kwargs):
        """
        Gets list of slas
        Gets list of slas

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_slas_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Sla]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_slas_list" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/slas'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='list[Sla]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
