# liveagent_api.CheckoutTokenApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_checkout_token**](CheckoutTokenApi.md#get_checkout_token) | **POST** /checkout/_authorize | Checkout token


# **get_checkout_token**
> CheckoutToken get_checkout_token(parameters=parameters)

Checkout token

Returns generated checkout token

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
api_instance = liveagent_api.CheckoutTokenApi(liveagent_api.ApiClient(configuration))
parameters = liveagent_api.CheckoutParameters() # CheckoutParameters |  (optional)

try:
    # Checkout token
    api_response = api_instance.get_checkout_token(parameters=parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutTokenApi->get_checkout_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | [**CheckoutParameters**](CheckoutParameters.md)|  | [optional] 

### Return type

[**CheckoutToken**](CheckoutToken.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

