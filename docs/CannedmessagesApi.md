# liveagent_api.CannedmessagesApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_canned_message**](CannedmessagesApi.md#create_canned_message) | **POST** /canned_messages | Create canned message
[**delete_canned_message**](CannedmessagesApi.md#delete_canned_message) | **DELETE** /canned_messages/{cannedMessageId} | Canned message
[**get_canned_message**](CannedmessagesApi.md#get_canned_message) | **GET** /canned_messages/{cannedMessageId} | Gets canned message
[**get_canned_messages_list**](CannedmessagesApi.md#get_canned_messages_list) | **GET** /canned_messages | Gets list of canned messages
[**update_canned_message**](CannedmessagesApi.md#update_canned_message) | **PUT** /canned_messages/{cannedMessageId} | Update canned message


# **create_canned_message**
> CannedMessage create_canned_message(canned_message=canned_message)

Create canned message

Create new canned message

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
api_instance = liveagent_api.CannedmessagesApi()
canned_message = liveagent_api.CannedMessage() # CannedMessage |  (optional)

try: 
    # Create canned message
    api_response = api_instance.create_canned_message(canned_message=canned_message)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CannedmessagesApi->create_canned_message: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **canned_message** | [**CannedMessage**](CannedMessage.md)|  | [optional] 

### Return type

[**CannedMessage**](CannedMessage.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_canned_message**
> OkResponse delete_canned_message(canned_message_id)

Canned message

Deletes a canned message

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
api_instance = liveagent_api.CannedmessagesApi()
canned_message_id = 'canned_message_id_example' # str | 

try: 
    # Canned message
    api_response = api_instance.delete_canned_message(canned_message_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CannedmessagesApi->delete_canned_message: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **canned_message_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_canned_message**
> CannedMessage get_canned_message(canned_message_id)

Gets canned message

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
api_instance = liveagent_api.CannedmessagesApi()
canned_message_id = 'canned_message_id_example' # str | 

try: 
    # Gets canned message
    api_response = api_instance.get_canned_message(canned_message_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CannedmessagesApi->get_canned_message: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **canned_message_id** | **str**|  | 

### Return type

[**CannedMessage**](CannedMessage.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_canned_messages_list**
> list[CannedMessage] get_canned_messages_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)

Gets list of canned messages

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
api_instance = liveagent_api.CannedmessagesApi()
page = 1 # int | Page to display. Not used if _from is defined. (optional) (default to 1)
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
_from = 0 # int | Result set start. Takes precedence over _page. (optional) (default to 0)
to = 0 # int | Result set end. Used only if _from is used. (optional) (default to 0)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)

try: 
    # Gets list of canned messages
    api_response = api_instance.get_canned_messages_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CannedmessagesApi->get_canned_messages_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page to display. Not used if _from is defined. | [optional] [default to 1]
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] [default to 10]
 **_from** | **int**| Result set start. Takes precedence over _page. | [optional] [default to 0]
 **to** | **int**| Result set end. Used only if _from is used. | [optional] [default to 0]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **sort_field** | **str**| Sorting field | [optional] 
 **filters** | **str**| Filters (json object {column:value, ...}) | [optional] 

### Return type

[**list[CannedMessage]**](CannedMessage.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_canned_message**
> CannedMessage update_canned_message(canned_message_id, canned_message=canned_message)

Update canned message

Update a canned message

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
api_instance = liveagent_api.CannedmessagesApi()
canned_message_id = 'canned_message_id_example' # str | 
canned_message = liveagent_api.CannedMessage() # CannedMessage |  (optional)

try: 
    # Update canned message
    api_response = api_instance.update_canned_message(canned_message_id, canned_message=canned_message)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CannedmessagesApi->update_canned_message: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **canned_message_id** | **str**|  | 
 **canned_message** | [**CannedMessage**](CannedMessage.md)|  | [optional] 

### Return type

[**CannedMessage**](CannedMessage.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

