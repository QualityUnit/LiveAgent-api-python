# liveagent_api.GridApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agents_grid_list**](GridApi.md#get_agents_grid_list) | **GET** /grid/agents | Gets list of agents for grid
[**get_agents_grid_list_count**](GridApi.md#get_agents_grid_list_count) | **GET** /grid/agents/count | Gets count of agents for agents grid
[**get_calls_sla_log_grid_list**](GridApi.md#get_calls_sla_log_grid_list) | **GET** /grid/calls/sla | Gets list of call slas for grid
[**get_calls_sla_log_grid_list_count**](GridApi.md#get_calls_sla_log_grid_list_count) | **GET** /grid/calls/sla/count | Gets count of calls for tickets sla grid
[**get_chats_grid_list**](GridApi.md#get_chats_grid_list) | **GET** /grid/chats | Gets list of chats for chats grid
[**get_chats_grid_list_count**](GridApi.md#get_chats_grid_list_count) | **GET** /grid/chats/count | Gets count of chats for chats grid
[**get_chats_sla_log_grid_list**](GridApi.md#get_chats_sla_log_grid_list) | **GET** /grid/chats/sla | Gets list of chat slas for grid
[**get_chats_sla_log_grid_list_count**](GridApi.md#get_chats_sla_log_grid_list_count) | **GET** /grid/chats/sla/count | Gets count of chats for chats sla grid
[**get_customer_groups_grid_list**](GridApi.md#get_customer_groups_grid_list) | **GET** /grid/customer_groups | Gets list of customer groups for grid
[**get_departmens_grid_list_count**](GridApi.md#get_departmens_grid_list_count) | **GET** /grid/departments/count | Gets count of departments for department grid
[**get_departments_grid_list**](GridApi.md#get_departments_grid_list) | **GET** /grid/departments | Gets list of departments for grid
[**get_event_logs_grid_list**](GridApi.md#get_event_logs_grid_list) | **GET** /grid/eventlogs | Gets list of event logs for grid
[**get_event_logs_grid_list_count**](GridApi.md#get_event_logs_grid_list_count) | **GET** /grid/eventlogs/count | Gets count of logs for event logs grid
[**get_invite_agents_grid_list**](GridApi.md#get_invite_agents_grid_list) | **GET** /grid/{departmentId}/invite/agents | Gets list of invite agents for grid
[**get_languages_grid_list**](GridApi.md#get_languages_grid_list) | **GET** /grid/languages | Gets list of languages for grid
[**get_languages_grid_list_count**](GridApi.md#get_languages_grid_list_count) | **GET** /grid/languages/count | Gets count of languages for languages grid
[**get_plugind_grid_list**](GridApi.md#get_plugind_grid_list) | **GET** /grid/plugins | Gets plugins  for grid
[**get_tags_grid_list**](GridApi.md#get_tags_grid_list) | **GET** /grid/tags | Gets list of tags for grid
[**get_tickets_grid_list**](GridApi.md#get_tickets_grid_list) | **GET** /grid/tickets | Gets list of tickets for tickets grid
[**get_tickets_grid_list_count**](GridApi.md#get_tickets_grid_list_count) | **GET** /grid/tickets/count | Gets count of tickets for tickets grid
[**get_tickets_sla_log_grid_list**](GridApi.md#get_tickets_sla_log_grid_list) | **GET** /grid/tickets/sla | Gets list of ticket slas for grid
[**get_tickets_sla_log_grid_list_count**](GridApi.md#get_tickets_sla_log_grid_list_count) | **GET** /grid/tickets/sla/count | Gets count of tickets for tickets sla grid
[**get_time_reports_grid_list**](GridApi.md#get_time_reports_grid_list) | **GET** /grid/reports/time | Gets list of reports for time reports grid
[**get_time_reports_grid_list_count**](GridApi.md#get_time_reports_grid_list_count) | **GET** /grid/reports/time/count | Gets count of time reporst grid


# **get_agents_grid_list**
> list[AgentRow] get_agents_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field)

Gets list of agents for grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
sort_field = 'sort_field_example' # str |  (optional)

try:
    # Gets list of agents for grid
    api_response = api_instance.get_agents_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_agents_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Results per page. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 
 **sort_field** | **str**|  | [optional] 

### Return type

[**list[AgentRow]**](AgentRow.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents_grid_list_count**
> Count get_agents_grid_list_count(filters=filters)

Gets count of agents for agents grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets count of agents for agents grid
    api_response = api_instance.get_agents_grid_list_count(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_agents_grid_list_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calls_sla_log_grid_list**
> list[SlaLogRow] get_calls_sla_log_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field, timezone_offset=timezone_offset)

Gets list of call slas for grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
sort_field = 'sort_field_example' # str |  (optional)
timezone_offset = 56 # int | difference between client and server time in seconds (optional)

try:
    # Gets list of call slas for grid
    api_response = api_instance.get_calls_sla_log_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field, timezone_offset=timezone_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_calls_sla_log_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Results per page. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **timezone_offset** | **int**| difference between client and server time in seconds | [optional] 

### Return type

[**list[SlaLogRow]**](SlaLogRow.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calls_sla_log_grid_list_count**
> Count get_calls_sla_log_grid_list_count(filters=filters)

Gets count of calls for tickets sla grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets count of calls for tickets sla grid
    api_response = api_instance.get_calls_sla_log_grid_list_count(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_calls_sla_log_grid_list_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chats_grid_list**
> list[ChatRow] get_chats_grid_list(per_page=per_page, filters=filters, cursor=cursor, timezone_offset=timezone_offset)

Gets list of chats for chats grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. (optional) (default to 10)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
timezone_offset = 56 # int | difference between client and server time in seconds (optional)

try:
    # Gets list of chats for chats grid
    api_response = api_instance.get_chats_grid_list(per_page=per_page, filters=filters, cursor=cursor, timezone_offset=timezone_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_chats_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Results per page. | [optional] [default to 10]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 
 **timezone_offset** | **int**| difference between client and server time in seconds | [optional] 

### Return type

[**list[ChatRow]**](ChatRow.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chats_grid_list_count**
> Count get_chats_grid_list_count(filters=filters)

Gets count of chats for chats grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets count of chats for chats grid
    api_response = api_instance.get_chats_grid_list_count(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_chats_grid_list_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chats_sla_log_grid_list**
> list[SlaLogRow] get_chats_sla_log_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field, timezone_offset=timezone_offset)

Gets list of chat slas for grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
sort_field = 'sort_field_example' # str |  (optional)
timezone_offset = 56 # int | difference between client and server time in seconds (optional)

try:
    # Gets list of chat slas for grid
    api_response = api_instance.get_chats_sla_log_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field, timezone_offset=timezone_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_chats_sla_log_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Results per page. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **timezone_offset** | **int**| difference between client and server time in seconds | [optional] 

### Return type

[**list[SlaLogRow]**](SlaLogRow.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chats_sla_log_grid_list_count**
> Count get_chats_sla_log_grid_list_count(filters=filters)

Gets count of chats for chats sla grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets count of chats for chats sla grid
    api_response = api_instance.get_chats_sla_log_grid_list_count(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_chats_sla_log_grid_list_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_groups_grid_list**
> list[TagRow] get_customer_groups_grid_list(sort_dir=sort_dir, filters=filters)

Gets list of customer groups for grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets list of customer groups for grid
    api_response = api_instance.get_customer_groups_grid_list(sort_dir=sort_dir, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_customer_groups_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**list[TagRow]**](TagRow.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_departmens_grid_list_count**
> Count get_departmens_grid_list_count(filters=filters)

Gets count of departments for department grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets count of departments for department grid
    api_response = api_instance.get_departmens_grid_list_count(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_departmens_grid_list_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_departments_grid_list**
> list[DepartmentRow] get_departments_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field)

Gets list of departments for grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
sort_field = 'sort_field_example' # str |  (optional)

try:
    # Gets list of departments for grid
    api_response = api_instance.get_departments_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_departments_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Results per page. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 
 **sort_field** | **str**|  | [optional] 

### Return type

[**list[DepartmentRow]**](DepartmentRow.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_logs_grid_list**
> list[EventLogRow] get_event_logs_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field, timezone_offset=timezone_offset)

Gets list of event logs for grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
sort_field = 'sort_field_example' # str |  (optional)
timezone_offset = 56 # int | difference between client and server time in seconds (optional)

try:
    # Gets list of event logs for grid
    api_response = api_instance.get_event_logs_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field, timezone_offset=timezone_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_event_logs_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Results per page. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **timezone_offset** | **int**| difference between client and server time in seconds | [optional] 

### Return type

[**list[EventLogRow]**](EventLogRow.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_logs_grid_list_count**
> Count get_event_logs_grid_list_count(filters=filters)

Gets count of logs for event logs grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets count of logs for event logs grid
    api_response = api_instance.get_event_logs_grid_list_count(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_event_logs_grid_list_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invite_agents_grid_list**
> list[InviteAgentRow] get_invite_agents_grid_list(department_id, per_page=per_page, filters=filters)

Gets list of invite agents for grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
department_id = 'department_id_example' # str | 
per_page = 10 # int | Results per page. (optional) (default to 10)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets list of invite agents for grid
    api_response = api_instance.get_invite_agents_grid_list(department_id, per_page=per_page, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_invite_agents_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **str**|  | 
 **per_page** | **int**| Results per page. | [optional] [default to 10]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**list[InviteAgentRow]**](InviteAgentRow.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_languages_grid_list**
> list[LanguageRow] get_languages_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field)

Gets list of languages for grid

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

# create an instance of the API class
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
sort_field = 'sort_field_example' # str |  (optional)

try:
    # Gets list of languages for grid
    api_response = api_instance.get_languages_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_languages_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 
 **sort_field** | **str**|  | [optional] 

### Return type

[**list[LanguageRow]**](LanguageRow.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_languages_grid_list_count**
> Count get_languages_grid_list_count(filters=filters)

Gets count of languages for languages grid

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

# create an instance of the API class
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets count of languages for languages grid
    api_response = api_instance.get_languages_grid_list_count(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_languages_grid_list_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugind_grid_list**
> list[PluginRow] get_plugind_grid_list(sort_dir=sort_dir, filters=filters)

Gets plugins  for grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets plugins  for grid
    api_response = api_instance.get_plugind_grid_list(sort_dir=sort_dir, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_plugind_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**list[PluginRow]**](PluginRow.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_grid_list**
> list[TagRow] get_tags_grid_list(sort_dir=sort_dir, filters=filters)

Gets list of tags for grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets list of tags for grid
    api_response = api_instance.get_tags_grid_list(sort_dir=sort_dir, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_tags_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**list[TagRow]**](TagRow.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tickets_grid_list**
> list[TicketRow] get_tickets_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field, timezone_offset=timezone_offset)

Gets list of tickets for tickets grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
sort_field = 'sort_field_example' # str |  (optional)
timezone_offset = 56 # int | difference between client and server time in seconds (optional)

try:
    # Gets list of tickets for tickets grid
    api_response = api_instance.get_tickets_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field, timezone_offset=timezone_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_tickets_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Results per page. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **timezone_offset** | **int**| difference between client and server time in seconds | [optional] 

### Return type

[**list[TicketRow]**](TicketRow.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tickets_grid_list_count**
> Count get_tickets_grid_list_count(filters=filters, timezone_offset=timezone_offset)

Gets count of tickets for tickets grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
timezone_offset = 56 # int | difference between client and server time in seconds (optional)

try:
    # Gets count of tickets for tickets grid
    api_response = api_instance.get_tickets_grid_list_count(filters=filters, timezone_offset=timezone_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_tickets_grid_list_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 
 **timezone_offset** | **int**| difference between client and server time in seconds | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tickets_sla_log_grid_list**
> list[SlaLogRow] get_tickets_sla_log_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field, timezone_offset=timezone_offset)

Gets list of ticket slas for grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
sort_field = 'sort_field_example' # str |  (optional)
timezone_offset = 56 # int | difference between client and server time in seconds (optional)

try:
    # Gets list of ticket slas for grid
    api_response = api_instance.get_tickets_sla_log_grid_list(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field, timezone_offset=timezone_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_tickets_sla_log_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Results per page. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **timezone_offset** | **int**| difference between client and server time in seconds | [optional] 

### Return type

[**list[SlaLogRow]**](SlaLogRow.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tickets_sla_log_grid_list_count**
> Count get_tickets_sla_log_grid_list_count(filters=filters)

Gets count of tickets for tickets sla grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets count of tickets for tickets sla grid
    api_response = api_instance.get_tickets_sla_log_grid_list_count(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_tickets_sla_log_grid_list_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_reports_grid_list**
> list[TimeReportRow] get_time_reports_grid_list(per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, cursor=cursor)

Gets list of reports for time reports grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)

try:
    # Gets list of reports for time reports grid
    api_response = api_instance.get_time_reports_grid_list(per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_time_reports_grid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Results per page. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **sort_field** | **str**| Sorting field | [optional] 
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 

### Return type

[**list[TimeReportRow]**](TimeReportRow.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_reports_grid_list_count**
> Count get_time_reports_grid_list_count(filters=filters)

Gets count of time reporst grid

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
api_instance = liveagent_api.GridApi(liveagent_api.ApiClient(configuration))
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets count of time reporst grid
    api_response = api_instance.get_time_reports_grid_list_count(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->get_time_reports_grid_list_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

