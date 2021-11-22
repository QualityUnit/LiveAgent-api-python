# liveagent_api.ApiApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_keys**](ApiApi.md#create_api_keys) | **POST** /apikeys | Creates api key
[**delete_api_key**](ApiApi.md#delete_api_key) | **DELETE** /apikeys/{apikeyId} | Deletes api key
[**generate_api_key**](ApiApi.md#generate_api_key) | **POST** /apikeys/_generate | Gets new api keys
[**generate_sso_key**](ApiApi.md#generate_sso_key) | **POST** /sso | Generate SSO key
[**get_api_info**](ApiApi.md#get_api_info) | **GET** /api/info/{apiVersion} | Gets api info
[**get_api_key**](ApiApi.md#get_api_key) | **GET** /apikeys/{apikeyId} | Gets api keys
[**get_api_keys**](ApiApi.md#get_api_keys) | **GET** /apikeys | Gets api keys
[**get_api_privileges**](ApiApi.md#get_api_privileges) | **GET** /api/privileges | Gets api privileges
[**get_api_v3_keys_count**](ApiApi.md#get_api_v3_keys_count) | **GET** /api/v3/count | Gets count for api v3 keys
[**get_sso_key**](ApiApi.md#get_sso_key) | **GET** /sso | Get SSO key
[**login**](ApiApi.md#login) | **POST** /apikeys/_login | Creates or returns API key from login.
[**update_api_key**](ApiApi.md#update_api_key) | **PUT** /apikeys/{apikeyId} | Updates api key


# **create_api_keys**
> ApiKeyWithPrivileges create_api_keys(api_key=api_key)

Creates api key

Create api key

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
api_instance = liveagent_api.ApiApi(liveagent_api.ApiClient(configuration))
api_key = liveagent_api.ApiKeyWithPrivileges() # ApiKeyWithPrivileges |  (optional)

try:
    # Creates api key
    api_response = api_instance.create_api_keys(api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->create_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | [**ApiKeyWithPrivileges**](ApiKeyWithPrivileges.md)|  | [optional] 

### Return type

[**ApiKeyWithPrivileges**](ApiKeyWithPrivileges.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> OkResponse delete_api_key(apikey_id)

Deletes api key

Delete an api key

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
api_instance = liveagent_api.ApiApi(liveagent_api.ApiClient(configuration))
apikey_id = 8.14 # float | 

try:
    # Deletes api key
    api_response = api_instance.delete_api_key(apikey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey_id** | **float**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_api_key**
> ApiKey generate_api_key()

Gets new api keys

Get new api key

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
api_instance = liveagent_api.ApiApi(liveagent_api.ApiClient(configuration))

try:
    # Gets new api keys
    api_response = api_instance.generate_api_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->generate_api_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_sso_key**
> SSOKey generate_sso_key()

Generate SSO key

Generate Single Sign On key

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
api_instance = liveagent_api.ApiApi(liveagent_api.ApiClient(configuration))

try:
    # Generate SSO key
    api_response = api_instance.generate_sso_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->generate_sso_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SSOKey**](SSOKey.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_info**
> ApiInfo get_api_info(api_version)

Gets api info

Get information about api

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
api_instance = liveagent_api.ApiApi(liveagent_api.ApiClient(configuration))
api_version = 'api_version_example' # str | v1 - legacy api version,  v3 - current api version

try:
    # Gets api info
    api_response = api_instance.get_api_info(api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_api_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| v1 - legacy api version,  v3 - current api version | 

### Return type

[**ApiInfo**](ApiInfo.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> ApiKeyWithPrivileges get_api_key(apikey_id)

Gets api keys

Get information about api keys

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
api_instance = liveagent_api.ApiApi(liveagent_api.ApiClient(configuration))
apikey_id = 8.14 # float | 

try:
    # Gets api keys
    api_response = api_instance.get_api_key(apikey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey_id** | **float**|  | 

### Return type

[**ApiKeyWithPrivileges**](ApiKeyWithPrivileges.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys**
> list[ApiKey] get_api_keys(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field)

Gets api keys

Get information about api keys

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
api_instance = liveagent_api.ApiApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
sort_field = 'sort_field_example' # str |  (optional)

try:
    # Gets api keys
    api_response = api_instance.get_api_keys(per_page=per_page, sort_dir=sort_dir, filters=filters, cursor=cursor, sort_field=sort_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_api_keys: %s\n" % e)
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

[**list[ApiKey]**](ApiKey.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_privileges**
> list[ApiPrivilege] get_api_privileges()

Gets api privileges

Get api privileges

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
api_instance = liveagent_api.ApiApi(liveagent_api.ApiClient(configuration))

try:
    # Gets api privileges
    api_response = api_instance.get_api_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_api_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiPrivilege]**](ApiPrivilege.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v3_keys_count**
> Count get_api_v3_keys_count(filters=filters)

Gets count for api v3 keys

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
api_instance = liveagent_api.ApiApi(liveagent_api.ApiClient(configuration))
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets count for api v3 keys
    api_response = api_instance.get_api_v3_keys_count(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_api_v3_keys_count: %s\n" % e)
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

# **get_sso_key**
> SSOKey get_sso_key()

Get SSO key

Get Single Sign On key

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
api_instance = liveagent_api.ApiApi(liveagent_api.ApiClient(configuration))

try:
    # Get SSO key
    api_response = api_instance.get_sso_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_sso_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SSOKey**](SSOKey.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> ApiKeyWithPrivileges login(api_key_login=api_key_login)

Creates or returns API key from login.

Creates or returns API key from login and password.

### Example
```python
from __future__ import print_function
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = liveagent_api.ApiApi()
api_key_login = liveagent_api.ApiKeyLogin() # ApiKeyLogin |  (optional)

try:
    # Creates or returns API key from login.
    api_response = api_instance.login(api_key_login=api_key_login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_login** | [**ApiKeyLogin**](ApiKeyLogin.md)|  | [optional] 

### Return type

[**ApiKeyWithPrivileges**](ApiKeyWithPrivileges.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> ApiKeyWithPrivileges update_api_key(apikey_id, api_key=api_key)

Updates api key

Update an api key

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
api_instance = liveagent_api.ApiApi(liveagent_api.ApiClient(configuration))
apikey_id = 8.14 # float | 
api_key = liveagent_api.ApiKeyWithPrivileges() # ApiKeyWithPrivileges |  (optional)

try:
    # Updates api key
    api_response = api_instance.update_api_key(apikey_id, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->update_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey_id** | **float**|  | 
 **api_key** | [**ApiKeyWithPrivileges**](ApiKeyWithPrivileges.md)|  | [optional] 

### Return type

[**ApiKeyWithPrivileges**](ApiKeyWithPrivileges.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

