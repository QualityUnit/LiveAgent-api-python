# liveagent_api.MyAccountApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_my_account_link**](MyAccountApi.md#get_my_account_link) | **GET** /my_account/_link | Link to &#39;My account&#39;


# **get_my_account_link**
> MyAccountLink get_my_account_link()

Link to 'My account'

Returns the created link to 'My account'

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
api_instance = liveagent_api.MyAccountApi(liveagent_api.ApiClient(configuration))

try:
    # Link to 'My account'
    api_response = api_instance.get_my_account_link()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyAccountApi->get_my_account_link: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MyAccountLink**](MyAccountLink.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

