# liveagent_api.CallsApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_add_message**](CallsApi.md#call_add_message) | **POST** /calls/{callId}/messages | Adds a message to the call group in corresponfing ticket
[**call_add_recording**](CallsApi.md#call_add_recording) | **POST** /calls/{callId}/recordings | Adds a recording to the call group in corresponfing ticket
[**call_answer**](CallsApi.md#call_answer) | **POST** /calls/{callId}/_answer | Set call as answered by agent
[**call_change_channel_status**](CallsApi.md#call_change_channel_status) | **PUT** /calls/{callId}/channels/{channelId}/_status | Change channel status
[**call_create**](CallsApi.md#call_create) | **POST** /calls/{callId} | Create new call
[**call_fetch_ivr**](CallsApi.md#call_fetch_ivr) | **POST** /calls/{callId}/_fetchIvr | Fetches IVR for the call from external URL
[**call_get_status**](CallsApi.md#call_get_status) | **GET** /calls/{callId}/status | Return the status of call
[**call_move_channel**](CallsApi.md#call_move_channel) | **POST** /calls/{callId}/channels/{channelId}/_move | Moves existing channel to target call
[**call_remove_channel**](CallsApi.md#call_remove_channel) | **DELETE** /calls/{callId}/channels/{channelId} | Removes channel from the call
[**call_reroute**](CallsApi.md#call_reroute) | **POST** /calls/{callId}/_reroute | Let the call ring to another agent
[**call_ring**](CallsApi.md#call_ring) | **POST** /calls/{callId}/_ring | Let the call ring
[**call_start**](CallsApi.md#call_start) | **POST** /call/_start | Starts new outcoming / internal call
[**call_start_canceled**](CallsApi.md#call_start_canceled) | **POST** /call/_startCanceled | Callback that starting call canceled
[**call_start_failed**](CallsApi.md#call_start_failed) | **POST** /call/_startFailed | Callback that starting call failed
[**call_stop**](CallsApi.md#call_stop) | **POST** /calls/{callId}/_stop | Stops the call
[**call_transfer**](CallsApi.md#call_transfer) | **POST** /calls/{callId}/_transfer | Transfers call to different department / agent
[**confirm_ring**](CallsApi.md#confirm_ring) | **POST** /calls/{callId}/_confirmRing | Confirm that call is ringing
[**dtmf_channel**](CallsApi.md#dtmf_channel) | **POST** /calls/{callId}/channels/{channelId}/_dtmf | Send provided DTMF to channel
[**end_channel**](CallsApi.md#end_channel) | **POST** /calls/{callId}/channels/{channelId}/_end | End channel
[**get_calls_list**](CallsApi.md#get_calls_list) | **GET** /calls | Gets list of calls
[**hold_channel**](CallsApi.md#hold_channel) | **POST** /calls/{callId}/channels/{channelId}/_hold | Hold channel
[**merge**](CallsApi.md#merge) | **POST** /calls/{callId}/_merge | Merge two calls
[**mute_channel**](CallsApi.md#mute_channel) | **POST** /calls/{callId}/channels/{channelId}/_mute | Mute channel
[**stop_ring**](CallsApi.md#stop_ring) | **POST** /calls/{callId}/_stopRing | Stop ringing of call
[**unhol_channel**](CallsApi.md#unhol_channel) | **POST** /calls/{callId}/channels/{channelId}/_unhold | Unhold channel
[**unmute_channel**](CallsApi.md#unmute_channel) | **POST** /calls/{callId}/channels/{channelId}/_unmute | Unmute channel


# **call_add_message**
> OkResponse call_add_message(call_id, body=body)

Adds a message to the call group in corresponfing ticket

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
body = liveagent_api.CallMessage() # CallMessage |  (optional)

try:
    # Adds a message to the call group in corresponfing ticket
    api_response = api_instance.call_add_message(call_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_add_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **body** | [**CallMessage**](CallMessage.md)|  | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_add_recording**
> OkResponse call_add_recording(call_id, file=file)

Adds a recording to the call group in corresponfing ticket

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
file = '/path/to/file.txt' # file |  (optional)

try:
    # Adds a recording to the call group in corresponfing ticket
    api_response = api_instance.call_add_recording(call_id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_add_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **file** | **file**|  | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_answer**
> OkResponse call_answer(call_id, to_number, channel_id=channel_id)

Set call as answered by agent

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
to_number = 'to_number_example' # str | callee number
channel_id = 'channel_id_example' # str | Channel ID (optional)

try:
    # Set call as answered by agent
    api_response = api_instance.call_answer(call_id, to_number, channel_id=channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **to_number** | **str**| callee number | 
 **channel_id** | **str**| Channel ID | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_change_channel_status**
> OkResponse call_change_channel_status(call_id, channel_id, status)

Change channel status

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
channel_id = 'channel_id_example' # str | 
status = 'status_example' # str | run (\"R\" - default), hold (\"H\")

try:
    # Change channel status
    api_response = api_instance.call_change_channel_status(call_id, channel_id, status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_change_channel_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **channel_id** | **str**|  | 
 **status** | **str**| run (\&quot;R\&quot; - default), hold (\&quot;H\&quot;) | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_create**
> Call call_create(call_id, to_number, from_number, channel_id=channel_id, via_number=via_number, ticket_id=ticket_id, direction=direction)

Create new call

Creates new call (ingoing / outcoming / internal). Does not initiate the outgoing call

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
to_number = 'to_number_example' # str | callee number
from_number = 'from_number_example' # str | caller number
channel_id = 'channel_id_example' # str | Channel ID (optional)
via_number = 'via_number_example' # str | trunk number via which call was made / received (optional)
ticket_id = 'ticket_id_example' # str | ticket id or code (optional)
direction = 'in' # str | incoming call ('in' - default), outgoing call ('out'), internal call('int'), auto decide direction of call based on to_number ('auto') (optional) (default to in)

try:
    # Create new call
    api_response = api_instance.call_create(call_id, to_number, from_number, channel_id=channel_id, via_number=via_number, ticket_id=ticket_id, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **to_number** | **str**| callee number | 
 **from_number** | **str**| caller number | 
 **channel_id** | **str**| Channel ID | [optional] 
 **via_number** | **str**| trunk number via which call was made / received | [optional] 
 **ticket_id** | **str**| ticket id or code | [optional] 
 **direction** | **str**| incoming call (&#39;in&#39; - default), outgoing call (&#39;out&#39;), internal call(&#39;int&#39;), auto decide direction of call based on to_number (&#39;auto&#39;) | [optional] [default to in]

### Return type

[**Call**](Call.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_fetch_ivr**
> list[Ivr] call_fetch_ivr(call_id, fetch)

Fetches IVR for the call from external URL

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
fetch = liveagent_api.IvrFetch() # IvrFetch | 

try:
    # Fetches IVR for the call from external URL
    api_response = api_instance.call_fetch_ivr(call_id, fetch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_fetch_ivr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **fetch** | [**IvrFetch**](IvrFetch.md)|  | 

### Return type

[**list[Ivr]**](Ivr.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_get_status**
> CallStatus call_get_status(call_id, unreachable_agents=unreachable_agents)

Return the status of call

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
unreachable_agents = ['unreachable_agents_example'] # list[str] | Identifiers of unreachable agents that should be excluded from routing (optional)

try:
    # Return the status of call
    api_response = api_instance.call_get_status(call_id, unreachable_agents=unreachable_agents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **unreachable_agents** | [**list[str]**](str.md)| Identifiers of unreachable agents that should be excluded from routing | [optional] 

### Return type

[**CallStatus**](CallStatus.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_move_channel**
> OkResponse call_move_channel(call_id, channel_id, to_call_id)

Moves existing channel to target call

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
channel_id = 'channel_id_example' # str | 
to_call_id = 'to_call_id_example' # str | Target call

try:
    # Moves existing channel to target call
    api_response = api_instance.call_move_channel(call_id, channel_id, to_call_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_move_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **channel_id** | **str**|  | 
 **to_call_id** | **str**| Target call | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_remove_channel**
> OkResponse call_remove_channel(call_id, channel_id)

Removes channel from the call

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
channel_id = 'channel_id_example' # str | 

try:
    # Removes channel from the call
    api_response = api_instance.call_remove_channel(call_id, channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_remove_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **channel_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_reroute**
> CallStatus call_reroute(call_id, reason=reason, unreachable_agents=unreachable_agents)

Let the call ring to another agent

Lets the call ring to an another agent if available

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
reason = 'reason_example' # str | T - timeout, D - decline, DNR - device not registered, CHE - channel error (optional)
unreachable_agents = ['unreachable_agents_example'] # list[str] | Identifiers of unreachable agents that should be excluded from routing (optional)

try:
    # Let the call ring to another agent
    api_response = api_instance.call_reroute(call_id, reason=reason, unreachable_agents=unreachable_agents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_reroute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **reason** | **str**| T - timeout, D - decline, DNR - device not registered, CHE - channel error | [optional] 
 **unreachable_agents** | [**list[str]**](str.md)| Identifiers of unreachable agents that should be excluded from routing | [optional] 

### Return type

[**CallStatus**](CallStatus.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_ring**
> CallStatus call_ring(call_id, department_id=department_id, to_number=to_number)

Let the call ring

Lets the call ring to an agent or adds it to queue if all agents are busy

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
department_id = 'department_id_example' # str | Department ID (optional)
to_number = 'to_number_example' # str | callee number (optional)

try:
    # Let the call ring
    api_response = api_instance.call_ring(call_id, department_id=department_id, to_number=to_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_ring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **department_id** | **str**| Department ID | [optional] 
 **to_number** | **str**| callee number | [optional] 

### Return type

[**CallStatus**](CallStatus.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_start**
> OkResponse call_start(to_number, from_number, ticket_id, via_number=via_number)

Starts new outcoming / internal call

Starts new call by ringing agent device and the dialing customer after agent has picked up his phone 

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
to_number = 'to_number_example' # str | callee number
from_number = 'from_number_example' # str | caller number
ticket_id = 'ticket_id_example' # str | ticket id or code
via_number = 'via_number_example' # str | trunk number via which call was made (optional)

try:
    # Starts new outcoming / internal call
    api_response = api_instance.call_start(to_number, from_number, ticket_id, via_number=via_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_number** | **str**| callee number | 
 **from_number** | **str**| caller number | 
 **ticket_id** | **str**| ticket id or code | 
 **via_number** | **str**| trunk number via which call was made | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_start_canceled**
> OkResponse call_start_canceled(call_id)

Callback that starting call canceled

Callback is delivered only of HW phones

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | Call ID

try:
    # Callback that starting call canceled
    api_response = api_instance.call_start_canceled(call_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_start_canceled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**| Call ID | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_start_failed**
> OkResponse call_start_failed(call_id)

Callback that starting call failed

Callback is delivered only of HW phones

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | Call ID

try:
    # Callback that starting call failed
    api_response = api_instance.call_start_failed(call_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_start_failed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**| Call ID | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_stop**
> OkResponse call_stop(call_id, from_number=from_number)

Stops the call

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
from_number = 'from_number_example' # str | from number (optional)

try:
    # Stops the call
    api_response = api_instance.call_stop(call_id, from_number=from_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **from_number** | **str**| from number | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_transfer**
> CallTransferResult call_transfer(call_id, to=to)

Transfers call to different department / agent

Transfer can be called on incoming calls before they start ringing to agents

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
to = 'to_example' # str | Department ID or extension (optional)

try:
    # Transfers call to different department / agent
    api_response = api_instance.call_transfer(call_id, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **to** | **str**| Department ID or extension | [optional] 

### Return type

[**CallTransferResult**](CallTransferResult.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_ring**
> OkResponse confirm_ring(call_id, to_number=to_number, channel_id=channel_id)

Confirm that call is ringing

Confirms that the call is ringing to an agent

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
to_number = 'to_number_example' # str | callee number (optional)
channel_id = 'channel_id_example' # str | Channel ID (optional)

try:
    # Confirm that call is ringing
    api_response = api_instance.confirm_ring(call_id, to_number=to_number, channel_id=channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->confirm_ring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **to_number** | **str**| callee number | [optional] 
 **channel_id** | **str**| Channel ID | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dtmf_channel**
> OkResponse dtmf_channel(call_id, channel_id, dtmf)

Send provided DTMF to channel

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
channel_id = 'channel_id_example' # str | 
dtmf = 'dtmf_example' # str | DTMF To send

try:
    # Send provided DTMF to channel
    api_response = api_instance.dtmf_channel(call_id, channel_id, dtmf)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->dtmf_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **channel_id** | **str**|  | 
 **dtmf** | **str**| DTMF To send | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_channel**
> OkResponse end_channel(call_id, channel_id)

End channel

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
channel_id = 'channel_id_example' # str | 

try:
    # End channel
    api_response = api_instance.end_channel(call_id, channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->end_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **channel_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calls_list**
> list[CallListItem] get_calls_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)

Gets list of calls

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
page = 1 # int | Page to display. Not used if _from is defined. (optional) (default to 1)
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
_from = 0 # int | Result set start. Takes precedence over _page. (optional) (default to 0)
to = 0 # int | Result set end. Used only if _from is used. (optional) (default to 0)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filters (json object {column:value, ...} or json array [[column,operator,value], ...]) (optional)

try:
    # Gets list of calls
    api_response = api_instance.get_calls_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->get_calls_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page to display. Not used if _from is defined. | [optional] [default to 1]
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] [default to 10]
 **_from** | **int**| Result set start. Takes precedence over _page. | [optional] [default to 0]
 **to** | **int**| Result set end. Used only if _from is used. | [optional] [default to 0]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **sort_field** | **str**| Sorting field | [optional] 
 **filters** | **str**| Filters (json object {column:value, ...} or json array [[column,operator,value], ...]) | [optional] 

### Return type

[**list[CallListItem]**](CallListItem.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hold_channel**
> OkResponse hold_channel(call_id, channel_id)

Hold channel

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
channel_id = 'channel_id_example' # str | 

try:
    # Hold channel
    api_response = api_instance.hold_channel(call_id, channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->hold_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **channel_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
sec_call_id = 'sec_call_id_example' # str | Secondary call ID
agent_id = 'agent_id_example' # str | Agent ID for removing from the call (optional)

try:
    # Merge two calls
    api_response = api_instance.merge(call_id, sec_call_id, agent_id=agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->merge: %s\n" % e)
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

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mute_channel**
> OkResponse mute_channel(call_id, channel_id)

Mute channel

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
channel_id = 'channel_id_example' # str | 

try:
    # Mute channel
    api_response = api_instance.mute_channel(call_id, channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->mute_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **channel_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_ring**
> OkResponse stop_ring(call_id)

Stop ringing of call

Call goes to offline state after this

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 

try:
    # Stop ringing of call
    api_response = api_instance.stop_ring(call_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->stop_ring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unhol_channel**
> OkResponse unhol_channel(call_id, channel_id)

Unhold channel

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
channel_id = 'channel_id_example' # str | 

try:
    # Unhold channel
    api_response = api_instance.unhol_channel(call_id, channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->unhol_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **channel_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmute_channel**
> OkResponse unmute_channel(call_id, channel_id)

Unmute channel

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
api_instance = liveagent_api.CallsApi(liveagent_api.ApiClient(configuration))
call_id = 'call_id_example' # str | 
channel_id = 'channel_id_example' # str | 

try:
    # Unmute channel
    api_response = api_instance.unmute_channel(call_id, channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->unmute_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **channel_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

