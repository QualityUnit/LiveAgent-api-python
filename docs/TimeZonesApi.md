# liveagent_api.TimeZonesApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_timezones_list**](TimeZonesApi.md#get_timezones_list) | **GET** /time_zones | Gets list of timezones


# **get_timezones_list**
> list[TimeZones] get_timezones_list()

Gets list of timezones

Gets list of timezones

### Example
```python
from __future__ import print_function
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = liveagent_api.TimeZonesApi()

try:
    # Gets list of timezones
    api_response = api_instance.get_timezones_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeZonesApi->get_timezones_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TimeZones]**](TimeZones.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

