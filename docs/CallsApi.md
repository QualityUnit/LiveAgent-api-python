# swagger_client.CallsApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**la_api_v3_call_add_message**](CallsApi.md#la_api_v3_call_add_message) | **POST** /calls/{callId}/messages | Adds a message to the call
[**la_api_v3_call_answer**](CallsApi.md#la_api_v3_call_answer) | **POST** /calls/{callId}/_answer | Set call as answered by agent
[**la_api_v3_call_create**](CallsApi.md#la_api_v3_call_create) | **POST** /calls/{callId} | Create new call
[**la_api_v3_call_reroute**](CallsApi.md#la_api_v3_call_reroute) | **POST** /calls/{callId}/_reroute | Let the call ring to another agent
[**la_api_v3_call_ring**](CallsApi.md#la_api_v3_call_ring) | **POST** /calls/{callId}/_ring | Let the call ring
[**la_api_v3_call_status**](CallsApi.md#la_api_v3_call_status) | **GET** /calls/{callId}/status | Return the status of call
[**la_api_v3_call_stop**](CallsApi.md#la_api_v3_call_stop) | **POST** /calls/{callId}/_stop | Stops the call


# **la_api_v3_call_add_message**
> OkResponse la_api_v3_call_add_message(call_id, body=body)

Adds a message to the call

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallsApi()
call_id = 'call_id_example' # str | 
body = swagger_client.CallMessage() # CallMessage |  (optional)

try: 
    # Adds a message to the call
    api_response = api_instance.la_api_v3_call_add_message(call_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->la_api_v3_call_add_message: %s\n" % e
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

# **la_api_v3_call_answer**
> OkResponse la_api_v3_call_answer(call_id, to_number)

Set call as answered by agent

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallsApi()
call_id = 'call_id_example' # str | 
to_number = 'to_number_example' # str | callee number

try: 
    # Set call as answered by agent
    api_response = api_instance.la_api_v3_call_answer(call_id, to_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->la_api_v3_call_answer: %s\n" % e
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

# **la_api_v3_call_create**
> Call la_api_v3_call_create(call_id, to_number, from_number, direction=direction)

Create new call

Creates new call (ingoing / outcoming)

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallsApi()
call_id = 'call_id_example' # str | 
to_number = 'to_number_example' # str | callee number
from_number = 'from_number_example' # str | caller number
direction = 'in' # str | incoming call ('in' - default) or outgoing call ('out') (optional) (default to in)

try: 
    # Create new call
    api_response = api_instance.la_api_v3_call_create(call_id, to_number, from_number, direction=direction)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->la_api_v3_call_create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 
 **to_number** | **str**| callee number | 
 **from_number** | **str**| caller number | 
 **direction** | **str**| incoming call (&#39;in&#39; - default) or outgoing call (&#39;out&#39;) | [optional] [default to in]

### Return type

[**Call**](Call.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_call_reroute**
> CallStatus la_api_v3_call_reroute(call_id)

Let the call ring to another agent

Lets the call ring to an another agent if available

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallsApi()
call_id = 'call_id_example' # str | 

try: 
    # Let the call ring to another agent
    api_response = api_instance.la_api_v3_call_reroute(call_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->la_api_v3_call_reroute: %s\n" % e
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

# **la_api_v3_call_ring**
> CallStatus la_api_v3_call_ring(call_id)

Let the call ring

Lets the call ring to an agent or adds it to queue if all agents are busy

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallsApi()
call_id = 'call_id_example' # str | 

try: 
    # Let the call ring
    api_response = api_instance.la_api_v3_call_ring(call_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->la_api_v3_call_ring: %s\n" % e
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

# **la_api_v3_call_status**
> CallStatus la_api_v3_call_status(call_id)

Return the status of call

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallsApi()
call_id = 'call_id_example' # str | 

try: 
    # Return the status of call
    api_response = api_instance.la_api_v3_call_status(call_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->la_api_v3_call_status: %s\n" % e
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

# **la_api_v3_call_stop**
> OkResponse la_api_v3_call_stop(call_id)

Stops the call

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CallsApi()
call_id = 'call_id_example' # str | 

try: 
    # Stops the call
    api_response = api_instance.la_api_v3_call_stop(call_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CallsApi->la_api_v3_call_stop: %s\n" % e
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

