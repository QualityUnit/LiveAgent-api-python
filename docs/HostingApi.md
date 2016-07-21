# liveagent_api.HostingApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hosting_info_get**](HostingApi.md#hosting_info_get) | **GET** /hosting/info | Used hosting system info


# **hosting_info_get**
> HostingInfo hosting_info_get()

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
    api_response = api_instance.hosting_info_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling HostingApi->hosting_info_get: %s\n" % e
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

