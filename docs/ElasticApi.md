# liveagent_api.ElasticApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elastic_reindex_all_post**](ElasticApi.md#elastic_reindex_all_post) | **POST** /elastic/reindexAll | 
[**get_index_status**](ElasticApi.md#get_index_status) | **GET** /elastic/status | 
[**reindex**](ElasticApi.md#reindex) | **POST** /elastic/reindex | Reindex selected fields


# **elastic_reindex_all_post**
> ElasticMessage elastic_reindex_all_post()



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
    api_response = api_instance.elastic_reindex_all_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElasticApi->elastic_reindex_all_post: %s\n" % e)
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

# **get_index_status**
> IndexStatusData get_index_status()



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

