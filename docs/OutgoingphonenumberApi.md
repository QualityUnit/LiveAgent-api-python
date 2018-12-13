# liveagent_api.OutgoingphonenumberApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_outgoing_phone_number**](OutgoingphonenumberApi.md#get_outgoing_phone_number) | **GET** /outgoing_phone_numbers/{phoneNumber} | Get outgoing phone number
[**get_outgoing_phone_numbers_list**](OutgoingphonenumberApi.md#get_outgoing_phone_numbers_list) | **GET** /outgoing_phone_numbers | Gets list of outgoing phone numbers


# **get_outgoing_phone_number**
> OutgoingPhoneNumber get_outgoing_phone_number(phone_number)

Get outgoing phone number

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

# create an instance of the API class
api_instance = liveagent_api.OutgoingphonenumberApi()
phone_number = 'phone_number_example' # str | 

try: 
    # Get outgoing phone number
    api_response = api_instance.get_outgoing_phone_number(phone_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OutgoingphonenumberApi->get_outgoing_phone_number: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 

### Return type

[**OutgoingPhoneNumber**](OutgoingPhoneNumber.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outgoing_phone_numbers_list**
> list[OutgoingPhoneNumber] get_outgoing_phone_numbers_list(_from=_from, to=to, filters=filters)

Gets list of outgoing phone numbers

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

# create an instance of the API class
api_instance = liveagent_api.OutgoingphonenumberApi()
_from = 0 # int | Result set start. Takes precedence over _page. (optional) (default to 0)
to = 0 # int | Result set end. Used only if _from is used. (optional) (default to 0)
filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)

try: 
    # Gets list of outgoing phone numbers
    api_response = api_instance.get_outgoing_phone_numbers_list(_from=_from, to=to, filters=filters)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OutgoingphonenumberApi->get_outgoing_phone_numbers_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Result set start. Takes precedence over _page. | [optional] [default to 0]
 **to** | **int**| Result set end. Used only if _from is used. | [optional] [default to 0]
 **filters** | **str**| Filters (json object {column:value, ...}) | [optional] 

### Return type

[**list[OutgoingPhoneNumber]**](OutgoingPhoneNumber.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

