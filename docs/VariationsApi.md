# liveagent_api.VariationsApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_variation**](VariationsApi.md#get_variation) | **GET** /variations/{variationId} | Variation


# **get_variation**
> Variation get_variation(variation_id)

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
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

# create an instance of the API class
api_instance = liveagent_api.VariationsApi()
variation_id = 'variation_id_example' # str | 

try: 
    # Variation
    api_response = api_instance.get_variation(variation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VariationsApi->get_variation: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variation_id** | **str**|  | 

### Return type

[**Variation**](Variation.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

