# swagger_client.CountriesApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**la_api_v3_proxy_get_countries**](CountriesApi.md#la_api_v3_proxy_get_countries) | **GET** /countries/ | Country list


# **la_api_v3_proxy_get_countries**
> list[Country] la_api_v3_proxy_get_countries()

Country list

List of available countries

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CountriesApi()

try: 
    # Country list
    api_response = api_instance.la_api_v3_proxy_get_countries()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CountriesApi->la_api_v3_proxy_get_countries: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Country]**](Country.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

