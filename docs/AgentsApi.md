# liveagent_api.AgentsApi

All URIs are relative to *http://localhost/api/v3/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent**](AgentsApi.md#create_agent) | **POST** /agents/ | Create agent
[**delete_agent**](AgentsApi.md#delete_agent) | **DELETE** /agents/{userId} | Agent
[**get_agent**](AgentsApi.md#get_agent) | **GET** /agents/{userId} | Agent
[**get_agent_statuses**](AgentsApi.md#get_agent_statuses) | **GET** /agents/{userId}/status | Get agent statuses in departments
[**get_agents**](AgentsApi.md#get_agents) | **GET** /agents/ | Agent list
[**login_agent**](AgentsApi.md#login_agent) | **POST** /agents/{userId}/_login | Login agent
[**logout_agent**](AgentsApi.md#logout_agent) | **POST** /agents/{userId}/_logout | Logout agent
[**pause_agent**](AgentsApi.md#pause_agent) | **POST** /agents/{userId}/_pause | Pause agent
[**update_agent**](AgentsApi.md#update_agent) | **PUT** /agents/{userId} | Update agent
[**update_agent_statuses**](AgentsApi.md#update_agent_statuses) | **PUT** /agents/{userId}/status | Update agent statuses in departments


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
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

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

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

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
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

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

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

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
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

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

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_statuses**
> list[AgentStatus] get_agent_statuses(user_id)

Get agent statuses in departments

Gets agent statuses in departments

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
api_instance = liveagent_api.AgentsApi()
user_id = 'user_id_example' # str | 

try: 
    # Get agent statuses in departments
    api_response = api_instance.get_agent_statuses(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->get_agent_statuses: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**list[AgentStatus]**](AgentStatus.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

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
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

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

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_agent**
> ErrorResponse login_agent(user_id)

Login agent

Login agent

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
api_instance = liveagent_api.AgentsApi()
user_id = 'user_id_example' # str | 

try: 
    # Login agent
    api_response = api_instance.login_agent(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->login_agent: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_agent**
> OkResponse logout_agent(user_id)

Logout agent

Logout an agent

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
api_instance = liveagent_api.AgentsApi()
user_id = 'user_id_example' # str | 

try: 
    # Logout agent
    api_response = api_instance.logout_agent(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->logout_agent: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_agent**
> OkResponse pause_agent(user_id)

Pause agent

Pauses an agent

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
api_instance = liveagent_api.AgentsApi()
user_id = 'user_id_example' # str | 

try: 
    # Pause agent
    api_response = api_instance.pause_agent(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->pause_agent: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

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
# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'BEARER'

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

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_statuses**
> list[AgentStatus] update_agent_statuses(user_id, agent_statuses=agent_statuses)

Update agent statuses in departments

Updates agent statuses in departments

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
api_instance = liveagent_api.AgentsApi()
user_id = 'user_id_example' # str | 
agent_statuses = liveagent_api.AgentStatuses() # AgentStatuses |  (optional)

try: 
    # Update agent statuses in departments
    api_response = api_instance.update_agent_statuses(user_id, agent_statuses=agent_statuses)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentsApi->update_agent_statuses: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **agent_statuses** | [**AgentStatuses**](AgentStatuses.md)|  | [optional] 

### Return type

[**list[AgentStatus]**](AgentStatus.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

