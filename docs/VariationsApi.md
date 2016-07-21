# liveagent_api.VariationsApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**variations_variation_id_get**](VariationsApi.md#variations_variation_id_get) | **GET** /variations/{variationId} | Variation


# **variations_variation_id_get**
> Variation variations_variation_id_get(variation_id)

Variation

Get variation

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.VariationsApi()
variation_id = 'variation_id_example' # str | 

try: 
    # Variation
    api_response = api_instance.variations_variation_id_get(variation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VariationsApi->variations_variation_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variation_id** | **str**|  | 

### Return type

[**Variation**](Variation.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

