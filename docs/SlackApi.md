# liveagent_api.SlackApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conversation**](SlackApi.md#get_conversation) | **GET** /slack/conversation/{id} | Gets info about Slack workspace channel
[**get_conversations**](SlackApi.md#get_conversations) | **GET** /slack/conversations | Gets Slack workspace channels
[**get_slack_user**](SlackApi.md#get_slack_user) | **GET** /slack/user/{id} | Gets info about Slack user
[**get_template**](SlackApi.md#get_template) | **GET** /slack/template/{id} | Get Slack template
[**get_templates**](SlackApi.md#get_templates) | **GET** /slack/templates | Gets Slack notification templates
[**get_users**](SlackApi.md#get_users) | **GET** /slack/users | Gets Slack users in workspace
[**save_template**](SlackApi.md#save_template) | **PUT** /slack/template/{id} | Save Slack template


# **get_conversation**
> SlackConversation get_conversation(id)

Gets info about Slack workspace channel

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
api_instance = liveagent_api.SlackApi(liveagent_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Gets info about Slack workspace channel
    api_response = api_instance.get_conversation(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->get_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SlackConversation**](SlackConversation.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversations**
> list[SlackConversation] get_conversations(cursor=cursor, per_page=per_page)

Gets Slack workspace channels

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
api_instance = liveagent_api.SlackApi(liveagent_api.ApiClient(configuration))
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
per_page = 10 # int | Results per page. (optional) (default to 10)

try:
    # Gets Slack workspace channels
    api_response = api_instance.get_conversations(cursor=cursor, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->get_conversations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 
 **per_page** | **int**| Results per page. | [optional] [default to 10]

### Return type

[**list[SlackConversation]**](SlackConversation.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slack_user**
> SlackUser get_slack_user(id)

Gets info about Slack user

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
api_instance = liveagent_api.SlackApi(liveagent_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Gets info about Slack user
    api_response = api_instance.get_slack_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->get_slack_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SlackUser**](SlackUser.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> SlackTemplate get_template(id)

Get Slack template

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
api_instance = liveagent_api.SlackApi(liveagent_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Slack template
    api_response = api_instance.get_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->get_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SlackTemplate**](SlackTemplate.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates**
> list[SlackTemplate] get_templates()

Gets Slack notification templates

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
api_instance = liveagent_api.SlackApi(liveagent_api.ApiClient(configuration))

try:
    # Gets Slack notification templates
    api_response = api_instance.get_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->get_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SlackTemplate]**](SlackTemplate.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[SlackUser] get_users(cursor=cursor, per_page=per_page)

Gets Slack users in workspace

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
api_instance = liveagent_api.SlackApi(liveagent_api.ApiClient(configuration))
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
per_page = 10 # int | Results per page. (optional) (default to 10)

try:
    # Gets Slack users in workspace
    api_response = api_instance.get_users(cursor=cursor, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 
 **per_page** | **int**| Results per page. | [optional] [default to 10]

### Return type

[**list[SlackUser]**](SlackUser.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_template**
> SlackTemplate save_template(id, template=template)

Save Slack template

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
api_instance = liveagent_api.SlackApi(liveagent_api.ApiClient(configuration))
id = 'id_example' # str | 
template = liveagent_api.SlackTemplate() # SlackTemplate |  (optional)

try:
    # Save Slack template
    api_response = api_instance.save_template(id, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->save_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **template** | [**SlackTemplate**](SlackTemplate.md)|  | [optional] 

### Return type

[**SlackTemplate**](SlackTemplate.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

