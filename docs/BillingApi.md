# swagger_client.BillingApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**la_api_v3_proxy_check_vat**](BillingApi.md#la_api_v3_proxy_check_vat) | **POST** /billing/_check_vat | Vat validity


# **la_api_v3_proxy_check_vat**
> OkResponse la_api_v3_proxy_check_vat(vat_id)

Vat validity

Vat validity check

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingApi()
vat_id = 'vat_id_example' # str | 

try: 
    # Vat validity
    api_response = api_instance.la_api_v3_proxy_check_vat(vat_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling BillingApi->la_api_v3_proxy_check_vat: %s\n" % e
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

