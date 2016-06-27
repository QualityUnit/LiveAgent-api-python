# liveagent_api.CountriesApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countries_get**](CountriesApi.md#countries_get) | **GET** /countries/ | Country list


# **countries_get**
> list[Country] countries_get()

Country list

List of available countries

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = liveagent_api.CountriesApi()

try: 
    # Country list
    api_response = api_instance.countries_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CountriesApi->countries_get: %s\n" % e
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

