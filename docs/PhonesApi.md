# liveagent_api.PhonesApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_phone**](PhonesApi.md#create_phone) | **POST** /phones | Creates external phone
[**get_phone**](PhonesApi.md#get_phone) | **GET** /phones/{phoneId} | Gets phone device (use _app_ for LiveAgent Phone app device and _web_ for web device)
[**get_phones_list**](PhonesApi.md#get_phones_list) | **GET** /phones | Gets list of available phone devices. Special filters (userId - filter phones available for specified user only) 
[**remove_phone**](PhonesApi.md#remove_phone) | **DELETE** /phones/{phoneId} | Remove phone
[**update_phone**](PhonesApi.md#update_phone) | **PUT** /phones/{phoneId} | Update phone
[**update_phone_params**](PhonesApi.md#update_phone_params) | **PUT** /phones/{phoneId}/_updateParams | Update phone params
[**update_reg_status**](PhonesApi.md#update_reg_status) | **PUT** /phones/{phoneId}/_updateRegStatus | Update registration status


# **create_phone**
> PhoneDevice create_phone(number, type=type, name=name, trunk_id=trunk_id, agent_id=agent_id, pass_original_caller_id=pass_original_caller_id)

Creates external phone

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
api_instance = liveagent_api.PhonesApi(liveagent_api.ApiClient(configuration))
number = 'number_example' # str | 
type = 'S' # str | S - SIP phone, E - PSTN phone, R - SIP provider extension (optional) (default to S)
name = 'name_example' # str |  (optional)
trunk_id = 8.14 # float |  (optional)
agent_id = 'agent_id_example' # str |  (optional)
pass_original_caller_id = 'pass_original_caller_id_example' # str |  (optional)

try:
    # Creates external phone
    api_response = api_instance.create_phone(number, type=type, name=name, trunk_id=trunk_id, agent_id=agent_id, pass_original_caller_id=pass_original_caller_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhonesApi->create_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**|  | 
 **type** | **str**| S - SIP phone, E - PSTN phone, R - SIP provider extension | [optional] [default to S]
 **name** | **str**|  | [optional] 
 **trunk_id** | **float**|  | [optional] 
 **agent_id** | **str**|  | [optional] 
 **pass_original_caller_id** | **str**|  | [optional] 

### Return type

[**PhoneDevice**](PhoneDevice.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone**
> PhoneDevice get_phone(phone_id)

Gets phone device (use _app_ for LiveAgent Phone app device and _web_ for web device)

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
api_instance = liveagent_api.PhonesApi(liveagent_api.ApiClient(configuration))
phone_id = 'phone_id_example' # str | 

try:
    # Gets phone device (use _app_ for LiveAgent Phone app device and _web_ for web device)
    api_response = api_instance.get_phone(phone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhonesApi->get_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **str**|  | 

### Return type

[**PhoneDevice**](PhoneDevice.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phones_list**
> list[PhoneDevice] get_phones_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)

Gets list of available phone devices. Special filters (userId - filter phones available for specified user only) 

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
api_instance = liveagent_api.PhonesApi(liveagent_api.ApiClient(configuration))
page = 1 # int | Page to display. Not used if _from is defined. (optional) (default to 1)
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
_from = 0 # int | Result set start. Takes precedence over _page. (optional) (default to 0)
to = 0 # int | Result set end. Used only if _from is used. (optional) (default to 0)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets list of available phone devices. Special filters (userId - filter phones available for specified user only) 
    api_response = api_instance.get_phones_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhonesApi->get_phones_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page to display. Not used if _from is defined. | [optional] [default to 1]
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] [default to 10]
 **_from** | **int**| Result set start. Takes precedence over _page. | [optional] [default to 0]
 **to** | **int**| Result set end. Used only if _from is used. | [optional] [default to 0]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **sort_field** | **str**| Sorting field | [optional] 
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**list[PhoneDevice]**](PhoneDevice.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_phone**
> OkResponse remove_phone(phone_id)

Remove phone

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
api_instance = liveagent_api.PhonesApi(liveagent_api.ApiClient(configuration))
phone_id = 'phone_id_example' # str | 

try:
    # Remove phone
    api_response = api_instance.remove_phone(phone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhonesApi->remove_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_phone**
> PhoneDevice update_phone(phone_id, number=number, name=name, trunk_id=trunk_id, pass_original_caller_id=pass_original_caller_id)

Update phone

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
api_instance = liveagent_api.PhonesApi(liveagent_api.ApiClient(configuration))
phone_id = 'phone_id_example' # str | 
number = 'number_example' # str |  (optional)
name = 'name_example' # str |  (optional)
trunk_id = 56 # int |  (optional)
pass_original_caller_id = 'pass_original_caller_id_example' # str |  (optional)

try:
    # Update phone
    api_response = api_instance.update_phone(phone_id, number=number, name=name, trunk_id=trunk_id, pass_original_caller_id=pass_original_caller_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhonesApi->update_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **str**|  | 
 **number** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **trunk_id** | **int**|  | [optional] 
 **pass_original_caller_id** | **str**|  | [optional] 

### Return type

[**PhoneDevice**](PhoneDevice.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_phone_params**
> OkResponse update_phone_params(phone_id, params)

Update phone params

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
api_instance = liveagent_api.PhonesApi(liveagent_api.ApiClient(configuration))
phone_id = 'phone_id_example' # str | 
params = 'params_example' # str | New params

try:
    # Update phone params
    api_response = api_instance.update_phone_params(phone_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhonesApi->update_phone_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **str**|  | 
 **params** | **str**| New params | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reg_status**
> OkResponse update_reg_status(phone_id, reg_status)

Update registration status

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
api_instance = liveagent_api.PhonesApi(liveagent_api.ApiClient(configuration))
phone_id = 'phone_id_example' # str | 
reg_status = 'reg_status_example' # str | F - Phone is not registered (offline). N - Phone is registered (online). 

try:
    # Update registration status
    api_response = api_instance.update_reg_status(phone_id, reg_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhonesApi->update_reg_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **str**|  | 
 **reg_status** | **str**| F - Phone is not registered (offline). N - Phone is registered (online).  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

