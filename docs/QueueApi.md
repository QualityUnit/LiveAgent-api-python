# liveagent_api.QueueApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_queue_batch**](QueueApi.md#get_queue_batch) | **GET** /queue/batch/{batchId} | Retrieves the batch status and remaining items to process


# **get_queue_batch**
> Batch get_queue_batch(batch_id)

Retrieves the batch status and remaining items to process

Retrieves the batch status and remaining items to process

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
api_instance = liveagent_api.QueueApi(liveagent_api.ApiClient(configuration))
batch_id = 'batch_id_example' # str | 

try:
    # Retrieves the batch status and remaining items to process
    api_response = api_instance.get_queue_batch(batch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueueApi->get_queue_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**|  | 

### Return type

[**Batch**](Batch.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

