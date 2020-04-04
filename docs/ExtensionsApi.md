# liveagent_api.ExtensionsApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_extension**](ExtensionsApi.md#get_extension) | **GET** /extensions/{extensionId} | Gets Extension
[**get_extensions_count**](ExtensionsApi.md#get_extensions_count) | **GET** /extensions/count | Gets count for extensions
[**get_extensions_list**](ExtensionsApi.md#get_extensions_list) | **GET** /extensions | Gets list of extensions
[**set_extension**](ExtensionsApi.md#set_extension) | **PUT** /extensions/{extensionId} | Set extension


# **get_extension**
> Extension get_extension(extension_id)

Gets Extension

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
api_instance = liveagent_api.ExtensionsApi(liveagent_api.ApiClient(configuration))
extension_id = 'extension_id_example' # str | 

try:
    # Gets Extension
    api_response = api_instance.get_extension(extension_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsApi->get_extension: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**|  | 

### Return type

[**Extension**](Extension.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extensions_count**
> Count get_extensions_count(filters=filters)

Gets count for extensions

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
api_instance = liveagent_api.ExtensionsApi(liveagent_api.ApiClient(configuration))
filters = 'filters_example' # str | Filters (json object {column:value, ...} or json array [[column,operator,value], ...]) (optional)

try:
    # Gets count for extensions
    api_response = api_instance.get_extensions_count(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsApi->get_extensions_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filters (json object {column:value, ...} or json array [[column,operator,value], ...]) | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extensions_list**
> list[Extension] get_extensions_list(per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, cursor=cursor)

Gets list of extensions

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
api_instance = liveagent_api.ExtensionsApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filters (json object {column:value, ...} or json array [[column,operator,value], ...]) (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)

try:
    # Gets list of extensions
    api_response = api_instance.get_extensions_list(per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsApi->get_extensions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Results per page. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **sort_field** | **str**| Sorting field | [optional] 
 **filters** | **str**| Filters (json object {column:value, ...} or json array [[column,operator,value], ...]) | [optional] 
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 

### Return type

[**list[Extension]**](Extension.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_extension**
> Extension set_extension(extension_id, number=number, department_id=department_id, status=status)

Set extension

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
api_instance = liveagent_api.ExtensionsApi(liveagent_api.ApiClient(configuration))
extension_id = 'extension_id_example' # str | 
number = 'number_example' # str |  (optional)
department_id = 'department_id_example' # str |  (optional)
status = 'status_example' # str | E - Enabled, D - Disabled (optional)

try:
    # Set extension
    api_response = api_instance.set_extension(extension_id, number=number, department_id=department_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsApi->set_extension: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**|  | 
 **number** | **str**|  | [optional] 
 **department_id** | **str**|  | [optional] 
 **status** | **str**| E - Enabled, D - Disabled | [optional] 

### Return type

[**Extension**](Extension.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

