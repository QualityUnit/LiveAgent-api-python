# liveagent_api.BillingApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_vat**](BillingApi.md#check_vat) | **POST** /billing/_check_vat | Vat validity


# **check_vat**
> OkResponse check_vat(vat_id)

Vat validity

Vat validity check

### Example
```python
from __future__ import print_function
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = liveagent_api.BillingApi()
vat_id = 'vat_id_example' # str | 

try:
    # Vat validity
    api_response = api_instance.check_vat(vat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->check_vat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vat_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

