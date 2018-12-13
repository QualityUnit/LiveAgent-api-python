# liveagent_api.SlasApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sla**](SlasApi.md#get_sla) | **GET** /slas/{levelId} | Gets sla
[**get_sla_ticket_history**](SlasApi.md#get_sla_ticket_history) | **GET** /slas/{ticketId}/history | Gets ticket sla history
[**get_slas_list**](SlasApi.md#get_slas_list) | **GET** /slas | Gets list of slas


# **get_sla**
> Sla get_sla(level_id)

Gets sla

Gets sla

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
api_instance = liveagent_api.SlasApi()
level_id = 'level_id_example' # str | 

try: 
    # Gets sla
    api_response = api_instance.get_sla(level_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SlasApi->get_sla: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level_id** | **str**|  | 

### Return type

[**Sla**](Sla.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sla_ticket_history**
> SlaHistory get_sla_ticket_history(ticket_id)

Gets ticket sla history

Gets ticket sla history

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
api_instance = liveagent_api.SlasApi()
ticket_id = 'ticket_id_example' # str | 

try: 
    # Gets ticket sla history
    api_response = api_instance.get_sla_ticket_history(ticket_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SlasApi->get_sla_ticket_history: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 

### Return type

[**SlaHistory**](SlaHistory.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slas_list**
> list[Sla] get_slas_list()

Gets list of slas

Gets list of slas

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
api_instance = liveagent_api.SlasApi()

try: 
    # Gets list of slas
    api_response = api_instance.get_slas_list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SlasApi->get_slas_list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Sla]**](Sla.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

