# liveagent_api.DefaultApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping**](DefaultApi.md#ping) | **GET** /ping | Check that API is responding


# **ping**
> OkResponse ping()

Check that API is responding

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.DefaultApi()

try: 
    # Check that API is responding
    api_response = api_instance.ping()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->ping: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

