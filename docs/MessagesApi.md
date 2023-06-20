# liveagent_api.MessagesApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_message**](MessagesApi.md#delete_message) | **DELETE** /messages/{messageId} | Delete message
[**get_message**](MessagesApi.md#get_message) | **GET** /messages/{messageId} | Get message


# **delete_message**
> OkResponse delete_message(message_id)

Delete message

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

try:
    # Delete message
    api_response = api_instance.delete_message(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->delete_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **int**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message**
> Message get_message(message_id, sub_string_start=sub_string_start, sub_string_length=sub_string_length)

Get message

Only for legacy messages that can be loaded from qu_la_messages

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
sub_string_start = 56 # int | Set start of message. (optional)
sub_string_length = 56 # int | Set length of message. (optional)

try:
    # Get message
    api_response = api_instance.get_message(message_id, sub_string_start=sub_string_start, sub_string_length=sub_string_length)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->get_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **int**|  | 
 **sub_string_start** | **int**| Set start of message. | [optional] 
 **sub_string_length** | **int**| Set length of message. | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

