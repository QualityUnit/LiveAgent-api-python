# liveagent_api.BillingApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_check_vat_post**](BillingApi.md#billing_check_vat_post) | **POST** /billing/_check_vat | Vat validity


# **billing_check_vat_post**
> OkResponse billing_check_vat_post(vat_id)

Vat validity

Vat validity check

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = liveagent_api.BillingApi()
vat_id = 'vat_id_example' # str | 

try: 
    # Vat validity
    api_response = api_instance.billing_check_vat_post(vat_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling BillingApi->billing_check_vat_post: %s\n" % e
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

