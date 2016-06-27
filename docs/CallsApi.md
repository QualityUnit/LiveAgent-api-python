# liveagent_api.CallsApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calls_call_id_answer_post**](CallsApi.md#calls_call_id_answer_post) | **POST** /calls/{callId}/_answer | Set call as answered by agent
[**calls_call_id_messages_post**](CallsApi.md#calls_call_id_messages_post) | **POST** /calls/{callId}/messages | Adds a message to the call
[**calls_call_id_post**](CallsApi.md#calls_call_id_post) | **POST** /calls/{callId} | Create new call
[**calls_call_id_reroute_post**](CallsApi.md#calls_call_id_reroute_post) | **POST** /calls/{callId}/_reroute | Let the call ring to another agent
[**calls_call_id_ring_post**](CallsApi.md#calls_call_id_ring_post) | **POST** /calls/{callId}/_ring | Let the call ring
[**calls_call_id_status_get**](CallsApi.md#calls_call_id_status_get) | **GET** /calls/{callId}/status | Return the status of call
[**calls_call_id_stop_post**](CallsApi.md#calls_call_id_stop_post) | **POST** /calls/{callId}/_stop | Stops the call


# **calls_call_id_answer_post**
> OkResponse calls_call_id_answer_post(call_id, to_number)

Set call as answered by agent

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

# create an instance of the API class
api_instance = liveagent_api.CallsApi()
call_id = 'call_id_example' # str | 
to_number = 'to_number_example' # str | callee number

try: 
    # Set call as answered by agent
    api_response = api_instance.calls_call_id_answer_post(call_id, to_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->calls_call_id_answer_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **to_number** | **str**| callee number | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calls_call_id_messages_post**
> OkResponse calls_call_id_messages_post(call_id, body=body)

Adds a message to the call

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

# create an instance of the API class
api_instance = liveagent_api.CallsApi()
call_id = 'call_id_example' # str | 
body = liveagent_api.CallMessage() # CallMessage |  (optional)

try: 
    # Adds a message to the call
    api_response = api_instance.calls_call_id_messages_post(call_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->calls_call_id_messages_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **body** | [**CallMessage**](CallMessage.md)|  | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calls_call_id_post**
> Call calls_call_id_post(call_id, to_number, from_number, ticket_id=ticket_id, direction=direction)

Create new call

Creates new call (ingoing / outcoming)

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

# create an instance of the API class
api_instance = liveagent_api.CallsApi()
call_id = 'call_id_example' # str | 
to_number = 'to_number_example' # str | callee number
from_number = 'from_number_example' # str | caller number
ticket_id = 'ticket_id_example' # str | ticket id or code (optional)
direction = 'in' # str | incoming call ('in' - default) or outgoing call ('out') (optional) (default to in)

try: 
    # Create new call
    api_response = api_instance.calls_call_id_post(call_id, to_number, from_number, ticket_id=ticket_id, direction=direction)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->calls_call_id_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **to_number** | **str**| callee number | 
 **from_number** | **str**| caller number | 
 **ticket_id** | **str**| ticket id or code | [optional] 
 **direction** | **str**| incoming call (&#39;in&#39; - default) or outgoing call (&#39;out&#39;) | [optional] [default to in]

### Return type

[**Call**](Call.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calls_call_id_reroute_post**
> CallStatus calls_call_id_reroute_post(call_id)

Let the call ring to another agent

Lets the call ring to an another agent if available

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

# create an instance of the API class
api_instance = liveagent_api.CallsApi()
call_id = 'call_id_example' # str | 

try: 
    # Let the call ring to another agent
    api_response = api_instance.calls_call_id_reroute_post(call_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->calls_call_id_reroute_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 

### Return type

[**CallStatus**](CallStatus.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calls_call_id_ring_post**
> CallStatus calls_call_id_ring_post(call_id)

Let the call ring

Lets the call ring to an agent or adds it to queue if all agents are busy

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

# create an instance of the API class
api_instance = liveagent_api.CallsApi()
call_id = 'call_id_example' # str | 

try: 
    # Let the call ring
    api_response = api_instance.calls_call_id_ring_post(call_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->calls_call_id_ring_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 

### Return type

[**CallStatus**](CallStatus.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calls_call_id_status_get**
> CallStatus calls_call_id_status_get(call_id)

Return the status of call

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

# create an instance of the API class
api_instance = liveagent_api.CallsApi()
call_id = 'call_id_example' # str | 

try: 
    # Return the status of call
    api_response = api_instance.calls_call_id_status_get(call_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->calls_call_id_status_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 

### Return type

[**CallStatus**](CallStatus.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calls_call_id_stop_post**
> OkResponse calls_call_id_stop_post(call_id)

Stops the call

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

# create an instance of the API class
api_instance = liveagent_api.CallsApi()
call_id = 'call_id_example' # str | 

try: 
    # Stops the call
    api_response = api_instance.calls_call_id_stop_post(call_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->calls_call_id_stop_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

