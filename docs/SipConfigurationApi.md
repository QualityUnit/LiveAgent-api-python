# liveagent_api.SipConfigurationApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_entities**](SipConfigurationApi.md#update_entities) | **POST** /sip_configuration/restore | Restore all data in VoIP DB


# **update_entities**
> OkResponse update_entities()

Restore all data in VoIP DB

Restore all data in VoIP DB

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
api_instance = liveagent_api.SipConfigurationApi(liveagent_api.ApiClient(configuration))

try:
    # Restore all data in VoIP DB
    api_response = api_instance.update_entities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SipConfigurationApi->update_entities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

