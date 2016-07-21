# liveagent_api.AgentsApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agents_get**](AgentsApi.md#agents_get) | **GET** /agents/ | Agent list
[**agents_post**](AgentsApi.md#agents_post) | **POST** /agents/ | Create agent
[**agents_user_id_delete**](AgentsApi.md#agents_user_id_delete) | **DELETE** /agents/{userId} | Agent
[**agents_user_id_get**](AgentsApi.md#agents_user_id_get) | **GET** /agents/{userId} | Agent
[**agents_user_id_put**](AgentsApi.md#agents_user_id_put) | **PUT** /agents/{userId} | Update agent


# **agents_get**
> list[Agent] agents_get()

Agent list

List of agents

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.AgentsApi()

try: 
    # Agent list
    api_response = api_instance.agents_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->agents_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Agent]**](Agent.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agents_post**
> Agent agents_post(agent=agent)

Create agent

Create new agent user

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.AgentsApi()
agent = liveagent_api.Agent() # Agent |  (optional)

try: 
    # Create agent
    api_response = api_instance.agents_post(agent=agent)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->agents_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent** | [**Agent**](Agent.md)|  | [optional] 

### Return type

[**Agent**](Agent.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agents_user_id_delete**
> OkResponse agents_user_id_delete(user_id)

Agent

Deletes an agent

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.AgentsApi()
user_id = 'user_id_example' # str | 

try: 
    # Agent
    api_response = api_instance.agents_user_id_delete(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->agents_user_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agents_user_id_get**
> Agent agents_user_id_get(user_id)

Agent

Retrieves an agent

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.AgentsApi()
user_id = 'user_id_example' # str | 

try: 
    # Agent
    api_response = api_instance.agents_user_id_get(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->agents_user_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**Agent**](Agent.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agents_user_id_put**
> Agent agents_user_id_put(user_id, agent=agent)

Update agent

Update an agent

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.AgentsApi()
user_id = 'user_id_example' # str | 
agent = liveagent_api.Agent() # Agent |  (optional)

try: 
    # Update agent
    api_response = api_instance.agents_user_id_put(user_id, agent=agent)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->agents_user_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **agent** | [**Agent**](Agent.md)|  | [optional] 

### Return type

[**Agent**](Agent.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

