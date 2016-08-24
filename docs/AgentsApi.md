# liveagent_api.AgentsApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent**](AgentsApi.md#create_agent) | **POST** /agents/ | Create agent
[**delete_agent**](AgentsApi.md#delete_agent) | **DELETE** /agents/{userId} | Agent
[**get_agent**](AgentsApi.md#get_agent) | **GET** /agents/{userId} | Agent
[**get_agents**](AgentsApi.md#get_agents) | **GET** /agents/ | Agent list
[**update_agent**](AgentsApi.md#update_agent) | **PUT** /agents/{userId} | Update agent


# **create_agent**
> Agent create_agent(agent=agent)

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
    api_response = api_instance.create_agent(agent=agent)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->create_agent: %s\n" % e
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

# **delete_agent**
> OkResponse delete_agent(user_id)

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
    api_response = api_instance.delete_agent(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->delete_agent: %s\n" % e
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

# **get_agent**
> Agent get_agent(user_id)

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
    api_response = api_instance.get_agent(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->get_agent: %s\n" % e
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

# **get_agents**
> list[Agent] get_agents()

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
    api_response = api_instance.get_agents()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->get_agents: %s\n" % e
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

# **update_agent**
> Agent update_agent(user_id, agent=agent)

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
    api_response = api_instance.update_agent(user_id, agent=agent)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->update_agent: %s\n" % e
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

