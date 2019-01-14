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


class PlansApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_device_department_plan(self, device_id, department_id, **kwargs):  # noqa: E501
        """Get device department plan  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_department_plan(device_id, department_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int device_id: (required)
        :param str department_id: (required)
        :return: list[DeviceDepartmentPlan]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_device_department_plan_with_http_info(device_id, department_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_device_department_plan_with_http_info(device_id, department_id, **kwargs)  # noqa: E501
            return data

    def get_device_department_plan_with_http_info(self, device_id, department_id, **kwargs):  # noqa: E501
        """Get device department plan  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_department_plan_with_http_info(device_id, department_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int device_id: (required)
        :param str department_id: (required)
        :return: list[DeviceDepartmentPlan]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'department_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_department_plan" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `get_device_department_plan`")  # noqa: E501
        # verify the required parameter 'department_id' is set
        if ('department_id' not in params or
                params['department_id'] is None):
            raise ValueError("Missing the required parameter `department_id` when calling `get_device_department_plan`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']  # noqa: E501
        if 'department_id' in params:
            path_params['departmentId'] = params['department_id']  # noqa: E501

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
            '/devices/{deviceId}/departments/{departmentId}/plans', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DeviceDepartmentPlan]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
