# liveagent_api.TokenApi

All URIs are relative to *http://localhost/api/v3/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token**](TokenApi.md#get_access_token) | **GET** /token | Access token


# **get_access_token**
> Token get_access_token(username, password)

Access token

Returns access token

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.TokenApi()
username = 'username_example' # str | Username
password = 'password_example' # str | Password

try: 
    # Access token
    api_response = api_instance.get_access_token(username, password)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TokenApi->get_access_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username | 
 **password** | **str**| Password | 

### Return type

[**Token**](Token.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

