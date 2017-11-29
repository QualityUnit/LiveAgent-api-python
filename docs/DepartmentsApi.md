# liveagent_api.DepartmentsApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_department_list**](DepartmentsApi.md#get_department_list) | **GET** /departments | Gets list of departments
[**get_specific_department**](DepartmentsApi.md#get_specific_department) | **GET** /departments/{departmentId} | Get department by specific id
[**if_agent_is_in_department**](DepartmentsApi.md#if_agent_is_in_department) | **GET** /departments/{departmentId}/{agentId} | Is agent is department


# **get_department_list**
> list[Department] get_department_list()

Gets list of departments

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
api_instance = liveagent_api.DepartmentsApi()

try: 
    # Gets list of departments
    api_response = api_instance.get_department_list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DepartmentsApi->get_department_list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Department]**](Department.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_department**
> list[Department] get_specific_department(department_id)

Get department by specific id

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
api_instance = liveagent_api.DepartmentsApi()
department_id = 'department_id_example' # str | 

try: 
    # Get department by specific id
    api_response = api_instance.get_specific_department(department_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DepartmentsApi->get_specific_department: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **str**|  | 

### Return type

[**list[Department]**](Department.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **if_agent_is_in_department**
> OkResponse if_agent_is_in_department(department_id, agent_id)

Is agent is department

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
api_instance = liveagent_api.DepartmentsApi()
department_id = 'department_id_example' # str | 
agent_id = 'agent_id_example' # str | 

try: 
    # Is agent is department
    api_response = api_instance.if_agent_is_in_department(department_id, agent_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DepartmentsApi->if_agent_is_in_department: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **str**|  | 
 **agent_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

