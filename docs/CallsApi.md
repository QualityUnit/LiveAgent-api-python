# liveagent_api.CallsApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_add_message**](CallsApi.md#call_add_message) | **POST** /calls/{callId}/messages | Adds a message to the call group in corresponfing ticket
[**call_answer**](CallsApi.md#call_answer) | **POST** /calls/{callId}/_answer | Set call as answered by agent
[**call_create**](CallsApi.md#call_create) | **POST** /calls/{callId} | Create new call
[**call_get_status**](CallsApi.md#call_get_status) | **GET** /calls/{callId}/status | Return the status of call
[**call_reroute**](CallsApi.md#call_reroute) | **POST** /calls/{callId}/_reroute | Let the call ring to another agent
[**call_ring**](CallsApi.md#call_ring) | **POST** /calls/{callId}/_ring | Let the call ring
[**call_stop**](CallsApi.md#call_stop) | **POST** /calls/{callId}/_stop | Stops the call


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

[privileges](../README.md#privileges)

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

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_create**
> Call call_create(call_id, to_number, from_number, ticket_id=ticket_id, direction=direction)

Create new call

Creates new call (ingoing / outcoming / internal)

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
to_number = 'to_number_example' # str | callee number
from_number = 'from_number_example' # str | caller number
ticket_id = 'ticket_id_example' # str | ticket id or code (optional)
direction = 'in' # str | incoming call ('in' - default), outgoing call ('out') or internal call('int') (optional) (default to in)

try: 
    # Create new call
    api_response = api_instance.call_create(call_id, to_number, from_number, ticket_id=ticket_id, direction=direction)
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
 **ticket_id** | **str**| ticket id or code | [optional] 
 **direction** | **str**| incoming call (&#39;in&#39; - default), outgoing call (&#39;out&#39;) or internal call(&#39;int&#39;) | [optional] [default to in]

### Return type

[**Call**](Call.md)

### Authorization

[privileges](../README.md#privileges)

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

[privileges](../README.md#privileges)

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

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
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

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

