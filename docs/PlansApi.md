# liveagent_api.PlansApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_department_plan**](PlansApi.md#get_device_department_plan) | **GET** /devices/{deviceId}/departments/{departmentId}/plans | Get device department plan


# **get_device_department_plan**
> list[DeviceDepartmentPlan] get_device_department_plan(device_id, department_id)

Get device department plan

### Example
```python
from __future__ import print_function
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = liveagent_api.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'
# Configure OAuth2 access token for authorization: privileges
configuration = liveagent_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.PlansApi(liveagent_api.ApiClient(configuration))
device_id = 56 # int | 
department_id = 'department_id_example' # str | 

try:
    # Get device department plan
    api_response = api_instance.get_device_department_plan(device_id, department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->get_device_department_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **department_id** | **str**|  | 

### Return type

[**list[DeviceDepartmentPlan]**](DeviceDepartmentPlan.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

