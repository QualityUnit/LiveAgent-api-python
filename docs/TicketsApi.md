# liveagent_api.TicketsApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ticket**](TicketsApi.md#create_ticket) | **POST** /tickets | Create ticket
[**delete_ticket**](TicketsApi.md#delete_ticket) | **DELETE** /tickets/{ticketId} | Deletes ticket
[**get_ticket**](TicketsApi.md#get_ticket) | **GET** /tickets/{ticketId} | Gets ticket
[**get_ticket_attribute**](TicketsApi.md#get_ticket_attribute) | **GET** /tickets/{ticketId}/attributes/{attributeName} | Gets ticket attribute
[**get_ticket_history**](TicketsApi.md#get_ticket_history) | **GET** /tickets/history | Gets ticket
[**get_ticket_history_0**](TicketsApi.md#get_ticket_history_0) | **GET** /tickets/{ticketId}/history | Gets ticket history
[**get_ticket_history_count**](TicketsApi.md#get_ticket_history_count) | **GET** /tickets/history/count | Gets count for ticket history
[**get_ticket_message_groups**](TicketsApi.md#get_ticket_message_groups) | **GET** /tickets/{ticketId}/messages | Gets ticket message groups and messages
[**get_ticket_sla**](TicketsApi.md#get_ticket_sla) | **GET** /tickets/{ticketId}/sla | Gets ticket Sla
[**get_tickets_list**](TicketsApi.md#get_tickets_list) | **GET** /tickets | Gets list of tickets
[**set_ticket_attribute**](TicketsApi.md#set_ticket_attribute) | **PUT** /tickets/{ticketId}/attributes/{attributeName} | Sets ticket attribute
[**set_ticket_postpone**](TicketsApi.md#set_ticket_postpone) | **PUT** /tickets/{ticketId}/postpone | Sets postpone status to ticket
[**update_ticket**](TicketsApi.md#update_ticket) | **PUT** /tickets/{ticketId} | Updates ticket


# **create_ticket**
> TicketInformation create_ticket(ticket=ticket)

Create ticket

Create new ticket

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
api_instance = liveagent_api.TicketsApi(liveagent_api.ApiClient(configuration))
ticket = liveagent_api.TicketListItem() # TicketListItem |  (optional)

try:
    # Create ticket
    api_response = api_instance.create_ticket(ticket=ticket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->create_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket** | [**TicketListItem**](TicketListItem.md)|  | [optional] 

### Return type

[**TicketInformation**](TicketInformation.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ticket**
> OkResponse delete_ticket(ticket_id)

Deletes ticket

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
api_instance = liveagent_api.TicketsApi(liveagent_api.ApiClient(configuration))
ticket_id = 'ticket_id_example' # str | 

try:
    # Deletes ticket
    api_response = api_instance.delete_ticket(ticket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->delete_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ticket**
> Ticket get_ticket(ticket_id)

Gets ticket

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
api_instance = liveagent_api.TicketsApi(liveagent_api.ApiClient(configuration))
ticket_id = 'ticket_id_example' # str | 

try:
    # Gets ticket
    api_response = api_instance.get_ticket(ticket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->get_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ticket_attribute**
> TicketAttribute get_ticket_attribute(ticket_id, attribute_name)

Gets ticket attribute

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
api_instance = liveagent_api.TicketsApi(liveagent_api.ApiClient(configuration))
ticket_id = 'ticket_id_example' # str | 
attribute_name = 'attribute_name_example' # str | 

try:
    # Gets ticket attribute
    api_response = api_instance.get_ticket_attribute(ticket_id, attribute_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->get_ticket_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **attribute_name** | **str**|  | 

### Return type

[**TicketAttribute**](TicketAttribute.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ticket_history**
> list[TicketHistory] get_ticket_history(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field, timezone_offset=timezone_offset)

Gets ticket

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
api_instance = liveagent_api.TicketsApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
sort_field = 'sort_field_example' # str |  (optional)
timezone_offset = 56 # int | difference between client and server time in seconds (optional)

try:
    # Gets ticket
    api_response = api_instance.get_ticket_history(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field, timezone_offset=timezone_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->get_ticket_history: %s\n" % e)
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

[**list[TicketHistory]**](TicketHistory.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ticket_history_0**
> list[TicketHistory] get_ticket_history_0(ticket_id)

Gets ticket history

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
api_instance = liveagent_api.TicketsApi(liveagent_api.ApiClient(configuration))
ticket_id = 'ticket_id_example' # str | 

try:
    # Gets ticket history
    api_response = api_instance.get_ticket_history_0(ticket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->get_ticket_history_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 

### Return type

[**list[TicketHistory]**](TicketHistory.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ticket_history_count**
> Count get_ticket_history_count(filters=filters)

Gets count for ticket history

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
api_instance = liveagent_api.TicketsApi(liveagent_api.ApiClient(configuration))
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets count for ticket history
    api_response = api_instance.get_ticket_history_count(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->get_ticket_history_count: %s\n" % e)
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

# **get_ticket_message_groups**
> list[MessageGroup] get_ticket_message_groups(ticket_id, include_quoted_messages=include_quoted_messages, page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, _from=_from, to=to)

Gets ticket message groups and messages

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
api_instance = liveagent_api.TicketsApi(liveagent_api.ApiClient(configuration))
ticket_id = 'ticket_id_example' # str | 
include_quoted_messages = false # bool | If set, response will include quoted messages context, otherwise - only metadata. (optional) (default to false)
page = 1 # int | Page to display. Not used if _from is defined. (optional) (default to 1)
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
_from = 0 # int | Result set start. Takes precedence over _page. (optional) (default to 0)
to = 0 # int | Result set end. Used only if _from is used. (optional) (default to 0)

try:
    # Gets ticket message groups and messages
    api_response = api_instance.get_ticket_message_groups(ticket_id, include_quoted_messages=include_quoted_messages, page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->get_ticket_message_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **include_quoted_messages** | **bool**| If set, response will include quoted messages context, otherwise - only metadata. | [optional] [default to false]
 **page** | **int**| Page to display. Not used if _from is defined. | [optional] [default to 1]
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **sort_field** | **str**| Sorting field | [optional] 
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 
 **_from** | **int**| Result set start. Takes precedence over _page. | [optional] [default to 0]
 **to** | **int**| Result set end. Used only if _from is used. | [optional] [default to 0]

### Return type

[**list[MessageGroup]**](MessageGroup.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ticket_sla**
> TicketSla get_ticket_sla(ticket_id)

Gets ticket Sla

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
api_instance = liveagent_api.TicketsApi(liveagent_api.ApiClient(configuration))
ticket_id = 'ticket_id_example' # str | 

try:
    # Gets ticket Sla
    api_response = api_instance.get_ticket_sla(ticket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->get_ticket_sla: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 

### Return type

[**TicketSla**](TicketSla.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tickets_list**
> list[Ticket] get_tickets_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)

Gets list of tickets

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
api_instance = liveagent_api.TicketsApi(liveagent_api.ApiClient(configuration))
page = 1 # int | Page to display. Not used if _from is defined. (optional) (default to 1)
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
_from = 0 # int | Result set start. Takes precedence over _page. (optional) (default to 0)
to = 0 # int | Result set end. Used only if _from is used. (optional) (default to 0)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'date_created' # str |  (optional) (default to date_created)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets list of tickets
    api_response = api_instance.get_tickets_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->get_tickets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page to display. Not used if _from is defined. | [optional] [default to 1]
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] [default to 10]
 **_from** | **int**| Result set start. Takes precedence over _page. | [optional] [default to 0]
 **to** | **int**| Result set end. Used only if _from is used. | [optional] [default to 0]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **sort_field** | **str**|  | [optional] [default to date_created]
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**list[Ticket]**](Ticket.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ticket_attribute**
> OkResponse set_ticket_attribute(ticket_id, attribute_name, value)

Sets ticket attribute

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
api_instance = liveagent_api.TicketsApi(liveagent_api.ApiClient(configuration))
ticket_id = 'ticket_id_example' # str | 
attribute_name = 'attribute_name_example' # str | 
value = 'value_example' # str | New attribute value

try:
    # Sets ticket attribute
    api_response = api_instance.set_ticket_attribute(ticket_id, attribute_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->set_ticket_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **attribute_name** | **str**|  | 
 **value** | **str**| New attribute value | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ticket_postpone**
> OkResponse set_ticket_postpone(ticket_id, postpone_data=postpone_data)

Sets postpone status to ticket

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
api_instance = liveagent_api.TicketsApi(liveagent_api.ApiClient(configuration))
ticket_id = 'ticket_id_example' # str | 
postpone_data = liveagent_api.TicketPostpone() # TicketPostpone |  (optional)

try:
    # Sets postpone status to ticket
    api_response = api_instance.set_ticket_postpone(ticket_id, postpone_data=postpone_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->set_ticket_postpone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **postpone_data** | [**TicketPostpone**](TicketPostpone.md)|  | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ticket**
> Ticket update_ticket(ticket_id, ticket=ticket)

Updates ticket

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
api_instance = liveagent_api.TicketsApi(liveagent_api.ApiClient(configuration))
ticket_id = 'ticket_id_example' # str | 
ticket = liveagent_api.TicketUpdatable() # TicketUpdatable |  (optional)

try:
    # Updates ticket
    api_response = api_instance.update_ticket(ticket_id, ticket=ticket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->update_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **ticket** | [**TicketUpdatable**](TicketUpdatable.md)|  | [optional] 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

