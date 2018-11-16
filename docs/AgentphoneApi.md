# liveagent_api.AgentPhoneApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_phone**](AgentPhoneApi.md#get_agent_phone) | **GET** /agent_phone/{agentId} | Gets phone currently used by agent (use me as agentId for self)
[**set_agent_phone**](AgentPhoneApi.md#set_agent_phone) | **PUT** /agent_phone/{agentId} | Sets phone currently used by agent (use me as agentId for self)


# **get_agent_phone**
> PhoneDevice get_agent_phone(agent_id, type=type)

Gets phone currently used by agent (use me as agentId for self)

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
api_instance = liveagent_api.AgentPhoneApi(liveagent_api.ApiClient(configuration))
agent_id = 'agent_id_example' # str | 
type = 'I' # str | API (I - default), SIP (S) (optional) (default to I)

try:
    # Gets phone currently used by agent (use me as agentId for self)
    api_response = api_instance.get_agent_phone(agent_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPhoneApi->get_agent_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **type** | **str**| API (I - default), SIP (S) | [optional] [default to I]

### Return type

[**PhoneDevice**](PhoneDevice.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_agent_phone**
> OkResponse set_agent_phone(agent_id, phone_id)

Sets phone currently used by agent (use me as agentId for self)

### Example
```python
from __future__ import print_function
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
configuration = liveagent_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.AgentPhoneApi(liveagent_api.ApiClient(configuration))
agent_id = 'agent_id_example' # str | 
phone_id = 'phone_id_example' # str | New phone ID

try:
    # Sets phone currently used by agent (use me as agentId for self)
    api_response = api_instance.set_agent_phone(agent_id, phone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPhoneApi->set_agent_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **phone_id** | **str**| New phone ID | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

