# liveagent_api.ContactPhonesApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contact_phone**](ContactPhonesApi.md#get_contact_phone) | **GET** /contact_phones/{phone} | Get contact phone
[**get_contact_phones_list**](ContactPhonesApi.md#get_contact_phones_list) | **GET** /contact_phones | Gets list of contact phones


# **get_contact_phone**
> ContactPhone get_contact_phone(phone)

Get contact phone

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
api_instance = liveagent_api.ContactPhonesApi(liveagent_api.ApiClient(configuration))
phone = 'phone_example' # str | 

try:
    # Get contact phone
    api_response = api_instance.get_contact_phone(phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactPhonesApi->get_contact_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 

### Return type

[**ContactPhone**](ContactPhone.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_phones_list**
> list[ContactPhone] get_contact_phones_list(per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, cursor=cursor)

Gets list of contact phones

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
api_instance = liveagent_api.ContactPhonesApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str |  (optional)
filters = 'filters_example' # str | Filters (json object {column:value, ...} or json array [[column,operator,value], ...]) (optional)
cursor = 'cursor_example' # str | used for iteration throght resultset. Cursor identifies specific page in resultset. (optional)

try:
    # Gets list of contact phones
    api_response = api_instance.get_contact_phones_list(per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactPhonesApi->get_contact_phones_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **sort_field** | **str**|  | [optional] 
 **filters** | **str**| Filters (json object {column:value, ...} or json array [[column,operator,value], ...]) | [optional] 
 **cursor** | **str**| used for iteration throght resultset. Cursor identifies specific page in resultset. | [optional] 

### Return type

[**list[ContactPhone]**](ContactPhone.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

