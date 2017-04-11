# liveagent_api.CallsApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_add_message**](CallsApi.md#call_add_message) | **POST** /calls/{callId}/messages | Adds a message to the call group in corresponfing ticket
[**call_answer**](CallsApi.md#call_answer) | **POST** /calls/{callId}/_answer | Set call as answered by agent
[**call_create**](CallsApi.md#call_create) | **POST** /calls/{callId} | Create new call
[**call_get_status**](CallsApi.md#call_get_status) | **GET** /calls/{callId}/status | Return the status of call
[**call_move_channel**](CallsApi.md#call_move_channel) | **POST** /calls/{callId}/channels | Moves existing channel to this call
[**call_remove_channel**](CallsApi.md#call_remove_channel) | **DELETE** /calls/{callId}/channels/{channelId} | Removes channel from the call
[**call_reroute**](CallsApi.md#call_reroute) | **POST** /calls/{callId}/_reroute | Let the call ring to another agent
[**call_ring**](CallsApi.md#call_ring) | **POST** /calls/{callId}/_ring | Let the call ring
[**call_start**](CallsApi.md#call_start) | **POST** /call/_start | Starts new outcoming / internal call
[**call_stop**](CallsApi.md#call_stop) | **POST** /calls/{callId}/_stop | Stops the call
[**confirm_ring**](CallsApi.md#confirm_ring) | **POST** /calls/{callId}/_confirmRing | Confirm that call is ringing
[**merge**](CallsApi.md#merge) | **POST** /calls/{callId}/_merge | Merge two calls


# **call_add_message**
> OkResponse call_add_message(call_id, body=body)

Adds a message to the call group in corresponfing ticket

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
    # Adds a message to the call group in corresponfing ticket
    api_response = api_instance.call_add_message(call_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->call_add_message: %s\n" % e
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

# **call_answer**
> OkResponse call_answer(call_id, to_number)

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
    api_response = api_instance.call_answer(call_id, to_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->call_answer: %s\n" % e
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

# **call_create**
> Call call_create(call_id, to_number, from_number, channel_id=channel_id, ticket_id=ticket_id, direction=direction)

Create new call

Creates new call (ingoing / outcoming / internal). Does not initiate the outgoing call

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
channel_id = 'channel_id_example' # str | Channel ID (optional)
ticket_id = 'ticket_id_example' # str | ticket id or code (optional)
direction = 'in' # str | incoming call ('in' - default), outgoing call ('out') or internal call('int') (optional) (default to in)

try: 
    # Create new call
    api_response = api_instance.call_create(call_id, to_number, from_number, channel_id=channel_id, ticket_id=ticket_id, direction=direction)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->call_create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **to_number** | **str**| callee number | 
 **from_number** | **str**| caller number | 
 **channel_id** | **str**| Channel ID | [optional] 
 **ticket_id** | **str**| ticket id or code | [optional] 
 **direction** | **str**| incoming call (&#39;in&#39; - default), outgoing call (&#39;out&#39;) or internal call(&#39;int&#39;) | [optional] [default to in]

### Return type

[**Call**](Call.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_get_status**
> CallStatus call_get_status(call_id)

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
    api_response = api_instance.call_get_status(call_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->call_get_status: %s\n" % e
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

# **call_move_channel**
> OkResponse call_move_channel(call_id, body=body)

Moves existing channel to this call

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.CallsApi()
call_id = 'call_id_example' # str | 
body = liveagent_api.CallChannel() # CallChannel |  (optional)

try: 
    # Moves existing channel to this call
    api_response = api_instance.call_move_channel(call_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->call_move_channel: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **body** | [**CallChannel**](CallChannel.md)|  | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_remove_channel**
> OkResponse call_remove_channel(call_id, channel_id)

Removes channel from the call

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.CallsApi()
call_id = 'call_id_example' # str | 
channel_id = 'channel_id_example' # str | 

try: 
    # Removes channel from the call
    api_response = api_instance.call_remove_channel(call_id, channel_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->call_remove_channel: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **channel_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_reroute**
> CallStatus call_reroute(call_id)

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
    api_response = api_instance.call_reroute(call_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->call_reroute: %s\n" % e
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

# **call_ring**
> CallStatus call_ring(call_id)

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
    api_response = api_instance.call_ring(call_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->call_ring: %s\n" % e
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

# **call_start**
> OkResponse call_start(to_number, from_number, ticket_id=ticket_id)

Starts new outcoming / internal call

Starts new call by ringing agent device and the dialing customer after agent has picked up his phone\n

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.CallsApi()
to_number = 'to_number_example' # str | callee number
from_number = 'from_number_example' # str | caller number
ticket_id = 'ticket_id_example' # str | ticket id or code (optional)

try: 
    # Starts new outcoming / internal call
    api_response = api_instance.call_start(to_number, from_number, ticket_id=ticket_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->call_start: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_number** | **str**| callee number | 
 **from_number** | **str**| caller number | 
 **ticket_id** | **str**| ticket id or code | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_stop**
> OkResponse call_stop(call_id)

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
    api_response = api_instance.call_stop(call_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->call_stop: %s\n" % e
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

# **confirm_ring**
> OkResponse confirm_ring(call_id, agent_id=agent_id, channel_id=channel_id)

Confirm that call is ringing

Confirms that the call is ringing to an agent

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.CallsApi()
call_id = 'call_id_example' # str | 
agent_id = 'agent_id_example' # str | Agent ID (optional)
channel_id = 'channel_id_example' # str | Channel ID (optional)

try: 
    # Confirm that call is ringing
    api_response = api_instance.confirm_ring(call_id, agent_id=agent_id, channel_id=channel_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->confirm_ring: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **agent_id** | **str**| Agent ID | [optional] 
 **channel_id** | **str**| Channel ID | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge**
> OkResponse merge(call_id, sec_call_id, agent_id=agent_id)

Merge two calls

Merge secondary call into main call

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.CallsApi()
call_id = 'call_id_example' # str | 
sec_call_id = 'sec_call_id_example' # str | Secondary call ID
agent_id = 'agent_id_example' # str | Agent ID for removing from the call (optional)

try: 
    # Merge two calls
    api_response = api_instance.merge(call_id, sec_call_id, agent_id=agent_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->merge: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **sec_call_id** | **str**| Secondary call ID | 
 **agent_id** | **str**| Agent ID for removing from the call | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

