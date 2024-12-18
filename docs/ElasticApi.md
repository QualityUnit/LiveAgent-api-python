# liveagent_api.ElasticApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clean_tickets**](ElasticApi.md#clean_tickets) | **POST** /elastic/cleanDeletedData | Remove all es-documents that dont exist in primary db
[**get_index_status**](ElasticApi.md#get_index_status) | **GET** /elastic/status | Get reindex status
[**reindex**](ElasticApi.md#reindex) | **POST** /elastic/reindex | Reindex selected fields
[**reindex_all**](ElasticApi.md#reindex_all) | **POST** /elastic/reindexAll | Reindex all fields
[**update_ticket_check_task**](ElasticApi.md#update_ticket_check_task) | **POST** /elastic/updateTicketCheckTask | Update ticket check task


# **clean_tickets**
> ElasticMessage clean_tickets(type)

Remove all es-documents that dont exist in primary db

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
api_instance = liveagent_api.ElasticApi(liveagent_api.ApiClient(configuration))
type = 'type_example' # str | Type of index

try:
    # Remove all es-documents that dont exist in primary db
    api_response = api_instance.clean_tickets(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElasticApi->clean_tickets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of index | 

### Return type

[**ElasticMessage**](ElasticMessage.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_index_status**
> IndexStatusData get_index_status()

Get reindex status

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
api_instance = liveagent_api.ElasticApi(liveagent_api.ApiClient(configuration))

try:
    # Get reindex status
    api_response = api_instance.get_index_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElasticApi->get_index_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IndexStatusData**](IndexStatusData.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reindex**
> ElasticMessage reindex(reindex_data=reindex_data)

Reindex selected fields

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
api_instance = liveagent_api.ElasticApi(liveagent_api.ApiClient(configuration))
reindex_data = liveagent_api.ReindexData() # ReindexData |  (optional)

try:
    # Reindex selected fields
    api_response = api_instance.reindex(reindex_data=reindex_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElasticApi->reindex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reindex_data** | [**ReindexData**](ReindexData.md)|  | [optional] 

### Return type

[**ElasticMessage**](ElasticMessage.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reindex_all**
> ElasticMessage reindex_all()

Reindex all fields

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
api_instance = liveagent_api.ElasticApi(liveagent_api.ApiClient(configuration))

try:
    # Reindex all fields
    api_response = api_instance.reindex_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElasticApi->reindex_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ElasticMessage**](ElasticMessage.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ticket_check_task**
> OkResponse update_ticket_check_task(date_from)

Update ticket check task

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
api_instance = liveagent_api.ElasticApi(liveagent_api.ApiClient(configuration))
date_from = '2013-10-20T19:20:30+01:00' # datetime | Y-m-d H:i:s

try:
    # Update ticket check task
    api_response = api_instance.update_ticket_check_task(date_from)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElasticApi->update_ticket_check_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_from** | **datetime**| Y-m-d H:i:s | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

