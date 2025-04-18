# liveagent_api.PhoneNumbersApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_number**](PhoneNumbersApi.md#add_number) | **POST** /phone_numbers | Add new number
[**get_available_prefix**](PhoneNumbersApi.md#get_available_prefix) | **GET** /phone_numbers/availablePrefix | Gets available dial out prefix
[**get_phone_number**](PhoneNumbersApi.md#get_phone_number) | **GET** /phone_numbers/{phoneNumberId} | Gets phone number
[**get_phone_numbers_list**](PhoneNumbersApi.md#get_phone_numbers_list) | **GET** /phone_numbers | Gets list of available phone numbers
[**remove_phone_number**](PhoneNumbersApi.md#remove_phone_number) | **DELETE** /phone_numbers/{phoneNumberId} | Remove phone number
[**update_phone_number**](PhoneNumbersApi.md#update_phone_number) | **PUT** /phone_numbers/{phoneNumberId} | Update phone number
[**update_phone_number_status**](PhoneNumbersApi.md#update_phone_number_status) | **PUT** /phone_numbers/{phoneNumberId}/status | Update phone number status


# **add_number**
> PhoneNumber add_number(type, number, status, dial_out_prefix=dial_out_prefix, record_in_call=record_in_call, record_out_call=record_out_call, name=name, departmentid=departmentid, host_settings=host_settings, host=host, port=port, user=user, auth_user=auth_user, password=password, proxy_host=proxy_host, proxy_port=proxy_port, proxy_user=proxy_user, providerid=providerid, ivr=ivr)

Add new number

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
api_instance = liveagent_api.PhoneNumbersApi(liveagent_api.ApiClient(configuration))
type = 'type_example' # str | A - API controlled number, T - Twilio number, T-O - Twilio outgoing number, S - Asterisk
number = 'number_example' # str | 
status = 'status_example' # str | A - Active, I - Inactive
dial_out_prefix = 56 # int | Prefix needed to originate call using this number (optional)
record_in_call = true # bool |  (optional)
record_out_call = true # bool |  (optional)
name = 'name_example' # str |  (optional)
departmentid = 'departmentid_example' # str |  (optional)
host_settings = 'host_settings_example' # str | json encoded host settings (optional)
host = 'host_example' # str |  (optional)
port = 'port_example' # str |  (optional)
user = 'user_example' # str |  (optional)
auth_user = 'auth_user_example' # str |  (optional)
password = 'password_example' # str |  (optional)
proxy_host = 'proxy_host_example' # str |  (optional)
proxy_port = 'proxy_port_example' # str |  (optional)
proxy_user = 'proxy_user_example' # str |  (optional)
providerid = 'providerid_example' # str |  (optional)
ivr = 'ivr_example' # str |  (optional)

try:
    # Add new number
    api_response = api_instance.add_number(type, number, status, dial_out_prefix=dial_out_prefix, record_in_call=record_in_call, record_out_call=record_out_call, name=name, departmentid=departmentid, host_settings=host_settings, host=host, port=port, user=user, auth_user=auth_user, password=password, proxy_host=proxy_host, proxy_port=proxy_port, proxy_user=proxy_user, providerid=providerid, ivr=ivr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->add_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| A - API controlled number, T - Twilio number, T-O - Twilio outgoing number, S - Asterisk | 
 **number** | **str**|  | 
 **status** | **str**| A - Active, I - Inactive | 
 **dial_out_prefix** | **int**| Prefix needed to originate call using this number | [optional] 
 **record_in_call** | **bool**|  | [optional] 
 **record_out_call** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **departmentid** | **str**|  | [optional] 
 **host_settings** | **str**| json encoded host settings | [optional] 
 **host** | **str**|  | [optional] 
 **port** | **str**|  | [optional] 
 **user** | **str**|  | [optional] 
 **auth_user** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 
 **proxy_host** | **str**|  | [optional] 
 **proxy_port** | **str**|  | [optional] 
 **proxy_user** | **str**|  | [optional] 
 **providerid** | **str**|  | [optional] 
 **ivr** | **str**|  | [optional] 

### Return type

[**PhoneNumber**](PhoneNumber.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_prefix**
> AvailablePrefix get_available_prefix()

Gets available dial out prefix

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
api_instance = liveagent_api.PhoneNumbersApi(liveagent_api.ApiClient(configuration))

try:
    # Gets available dial out prefix
    api_response = api_instance.get_available_prefix()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->get_available_prefix: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AvailablePrefix**](AvailablePrefix.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone_number**
> PhoneNumber get_phone_number(phone_number_id)

Gets phone number

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
api_instance = liveagent_api.PhoneNumbersApi(liveagent_api.ApiClient(configuration))
phone_number_id = 'phone_number_id_example' # str | 

try:
    # Gets phone number
    api_response = api_instance.get_phone_number(phone_number_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->get_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 

### Return type

[**PhoneNumber**](PhoneNumber.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone_numbers_list**
> list[PhoneNumber] get_phone_numbers_list(per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, cursor=cursor, additional_objects=additional_objects)

Gets list of available phone numbers

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
api_instance = liveagent_api.PhoneNumbersApi(liveagent_api.ApiClient(configuration))
per_page = 10 # int | Results per page. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str |  (optional)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)
cursor = 'cursor_example' # str | used for iteration through resultset. Cursor identifies specific page in resultset. (optional)
additional_objects = ['additional_objects_example'] # list[str] | Additional objects (optional)

try:
    # Gets list of available phone numbers
    api_response = api_instance.get_phone_numbers_list(per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, cursor=cursor, additional_objects=additional_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->get_phone_numbers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Results per page. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **sort_field** | **str**|  | [optional] 
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 
 **cursor** | **str**| used for iteration through resultset. Cursor identifies specific page in resultset. | [optional] 
 **additional_objects** | [**list[str]**](str.md)| Additional objects | [optional] 

### Return type

[**list[PhoneNumber]**](PhoneNumber.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_phone_number**
> OkResponse remove_phone_number(phone_number_id)

Remove phone number

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
api_instance = liveagent_api.PhoneNumbersApi(liveagent_api.ApiClient(configuration))
phone_number_id = 'phone_number_id_example' # str | 

try:
    # Remove phone number
    api_response = api_instance.remove_phone_number(phone_number_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->remove_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_phone_number**
> PhoneNumber update_phone_number(phone_number_id, phone_number)

Update phone number

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
api_instance = liveagent_api.PhoneNumbersApi(liveagent_api.ApiClient(configuration))
phone_number_id = 'phone_number_id_example' # str | 
phone_number = liveagent_api.PhoneNumber() # PhoneNumber | 

try:
    # Update phone number
    api_response = api_instance.update_phone_number(phone_number_id, phone_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->update_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
 **phone_number** | [**PhoneNumber**](PhoneNumber.md)|  | 

### Return type

[**PhoneNumber**](PhoneNumber.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_phone_number_status**
> PhoneNumber update_phone_number_status(phone_number_id, status)

Update phone number status

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
api_instance = liveagent_api.PhoneNumbersApi(liveagent_api.ApiClient(configuration))
phone_number_id = 'phone_number_id_example' # str | 
status = 'status_example' # str | A - Active, I - Inactive

try:
    # Update phone number status
    api_response = api_instance.update_phone_number_status(phone_number_id, status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->update_phone_number_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
 **status** | **str**| A - Active, I - Inactive | 

### Return type

[**PhoneNumber**](PhoneNumber.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

