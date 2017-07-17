# liveagent_api.HostingApi

All URIs are relative to *http://localhost/api/v3/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_info**](HostingApi.md#get_info) | **GET** /hosting/info | Used hosting system info


# **get_info**
> HostingInfo get_info()

Used hosting system info

Used hosting system info

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = liveagent_api.HostingApi()

try: 
    # Used hosting system info
    api_response = api_instance.get_info()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling HostingApi->get_info: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HostingInfo**](HostingInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

