# liveagent_api.MessagesApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_message**](MessagesApi.md#get_message) | **GET** /messages/{messageId} | Get message


# **get_message**
> Message get_message(message_id, _from=_from, to=to)

Get message

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
api_instance = liveagent_api.MessagesApi(liveagent_api.ApiClient(configuration))
message_id = 56 # int | 
_from = 0 # int | Result set start. Takes precedence over _page. (optional) (default to 0)
to = 0 # int | Result set end. Used only if _from is used. (optional) (default to 0)

try:
    # Get message
    api_response = api_instance.get_message(message_id, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->get_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **int**|  | 
 **_from** | **int**| Result set start. Takes precedence over _page. | [optional] [default to 0]
 **to** | **int**| Result set end. Used only if _from is used. | [optional] [default to 0]

### Return type

[**Message**](Message.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

