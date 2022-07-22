# liveagent_api.VariationsApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_variation**](VariationsApi.md#get_variation) | **GET** /variations/{variationId} | Variation
[**validate_limits**](VariationsApi.md#validate_limits) | **GET** /variations/{variationId}/validate-limits | Validate Limits


# **get_variation**
> Variation get_variation(variation_id)

Variation

Get variation

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
api_instance = liveagent_api.VariationsApi(liveagent_api.ApiClient(configuration))
variation_id = 'variation_id_example' # str | 

try:
    # Variation
    api_response = api_instance.get_variation(variation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariationsApi->get_variation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variation_id** | **str**|  | 

### Return type

[**Variation**](Variation.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_limits**
> list[LimitValidationFail] validate_limits(variation_id)

Validate Limits

Validate Limits

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
api_instance = liveagent_api.VariationsApi(liveagent_api.ApiClient(configuration))
variation_id = 'variation_id_example' # str | 

try:
    # Validate Limits
    api_response = api_instance.validate_limits(variation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariationsApi->validate_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variation_id** | **str**|  | 

### Return type

[**list[LimitValidationFail]**](LimitValidationFail.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

