# liveagent_api.SlackApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slack_conversation_id_get**](SlackApi.md#slack_conversation_id_get) | **GET** /slack/conversation/{id} | Gets info about Slack workspace channel
[**slack_conversations_get**](SlackApi.md#slack_conversations_get) | **GET** /slack/conversations | Gets Slack workspace channels
[**slack_template_id_get**](SlackApi.md#slack_template_id_get) | **GET** /slack/template/{id} | Get Slack template
[**slack_template_id_put**](SlackApi.md#slack_template_id_put) | **PUT** /slack/template/{id} | Save Slack template
[**slack_templates_get**](SlackApi.md#slack_templates_get) | **GET** /slack/templates | Gets Slack notification templates
[**slack_user_id_get**](SlackApi.md#slack_user_id_get) | **GET** /slack/user/{id} | Gets info about Slack user
[**slack_users_get**](SlackApi.md#slack_users_get) | **GET** /slack/users | Gets Slack users in workspace


# **slack_conversation_id_get**
> SlackConversation slack_conversation_id_get(id)

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
    api_response = api_instance.slack_conversation_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->slack_conversation_id_get: %s\n" % e)
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

# **slack_conversations_get**
> list[SlackConversation] slack_conversations_get(cursor=cursor, per_page=per_page)

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
    api_response = api_instance.slack_conversations_get(cursor=cursor, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->slack_conversations_get: %s\n" % e)
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

# **slack_template_id_get**
> SlackTemplate slack_template_id_get(id)

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
    api_response = api_instance.slack_template_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->slack_template_id_get: %s\n" % e)
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

# **slack_template_id_put**
> SlackTemplate slack_template_id_put(id, template=template)

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
    api_response = api_instance.slack_template_id_put(id, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->slack_template_id_put: %s\n" % e)
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

# **slack_templates_get**
> list[SlackTemplate] slack_templates_get()

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
    api_response = api_instance.slack_templates_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->slack_templates_get: %s\n" % e)
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

# **slack_user_id_get**
> SlackUser slack_user_id_get(id)

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
    api_response = api_instance.slack_user_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->slack_user_id_get: %s\n" % e)
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

# **slack_users_get**
> list[SlackUser] slack_users_get(cursor=cursor, per_page=per_page)

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
    api_response = api_instance.slack_users_get(cursor=cursor, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlackApi->slack_users_get: %s\n" % e)
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

