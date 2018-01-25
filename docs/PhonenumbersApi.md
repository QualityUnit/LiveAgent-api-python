# liveagent_api.PhonenumbersApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_number**](PhonenumbersApi.md#add_number) | **POST** /phone_numbers | Add new number
[**get_phone_number**](PhonenumbersApi.md#get_phone_number) | **GET** /phone_numbers/{phoneNumberId} | Gets phone number
[**get_phone_numbers_list**](PhonenumbersApi.md#get_phone_numbers_list) | **GET** /phone_numbers | Gets list of available phone numbers
[**remove_phone_number**](PhonenumbersApi.md#remove_phone_number) | **DELETE** /phone_numbers/{phoneNumberId} | Remove phone number
[**update_phone_number**](PhonenumbersApi.md#update_phone_number) | **PUT** /phone_numbers/{phoneNumberId} | Update phone number
[**update_phone_number_status**](PhonenumbersApi.md#update_phone_number_status) | **PUT** /phone_numbers/{phoneNumberId}/status | Update phone number status


# **add_number**
> PhoneNumber add_number(type, number, status, dial_out_prefix=dial_out_prefix, record_call=record_call, name=name, departmentid=departmentid, host_settings=host_settings, host=host, port=port, user=user, password=password, providerid=providerid, ivr=ivr)

Add new number

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
api_instance = liveagent_api.PhonenumbersApi()
type = 'type_example' # str | A - API controlled number, T - Twilio number, T-O - Twilio outgoing number, D - Digitale, S - Asterisk
number = 'number_example' # str | 
status = 'status_example' # str | A - Active, I - Inactive
dial_out_prefix = 56 # int | Prefix needed to originate call using this number (optional)
record_call = true # bool |  (optional)
name = 'name_example' # str |  (optional)
departmentid = 'departmentid_example' # str |  (optional)
host_settings = 'host_settings_example' # str | json encoded host settings (optional)
host = 'host_example' # str |  (optional)
port = 'port_example' # str |  (optional)
user = 'user_example' # str |  (optional)
password = 'password_example' # str |  (optional)
providerid = 'providerid_example' # str |  (optional)
ivr = 'ivr_example' # str |  (optional)

try: 
    # Add new number
    api_response = api_instance.add_number(type, number, status, dial_out_prefix=dial_out_prefix, record_call=record_call, name=name, departmentid=departmentid, host_settings=host_settings, host=host, port=port, user=user, password=password, providerid=providerid, ivr=ivr)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PhonenumbersApi->add_number: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| A - API controlled number, T - Twilio number, T-O - Twilio outgoing number, D - Digitale, S - Asterisk | 
 **number** | **str**|  | 
 **status** | **str**| A - Active, I - Inactive | 
 **dial_out_prefix** | **int**| Prefix needed to originate call using this number | [optional] 
 **record_call** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **departmentid** | **str**|  | [optional] 
 **host_settings** | **str**| json encoded host settings | [optional] 
 **host** | **str**|  | [optional] 
 **port** | **str**|  | [optional] 
 **user** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 
 **providerid** | **str**|  | [optional] 
 **ivr** | **str**|  | [optional] 

### Return type

[**PhoneNumber**](PhoneNumber.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone_number**
> PhoneNumber get_phone_number(phone_number_id)

Gets phone number

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
api_instance = liveagent_api.PhonenumbersApi()
phone_number_id = 'phone_number_id_example' # str | 

try: 
    # Gets phone number
    api_response = api_instance.get_phone_number(phone_number_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PhonenumbersApi->get_phone_number: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 

### Return type

[**PhoneNumber**](PhoneNumber.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone_numbers_list**
> list[PhoneNumber] get_phone_numbers_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters, additional_objects=additional_objects)

Gets list of available phone numbers

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
api_instance = liveagent_api.PhonenumbersApi()
page = 1 # int | Page to display. Not used if _from is defined. (optional) (default to 1)
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
_from = 0 # int | Result set start. Takes precedence over _page. (optional) (default to 0)
to = 0 # int | Result set end. Used only if _from is used. (optional) (default to 0)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)
additional_objects = ['additional_objects_example'] # list[str] | Additional objects (optional)

try: 
    # Gets list of available phone numbers
    api_response = api_instance.get_phone_numbers_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters, additional_objects=additional_objects)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PhonenumbersApi->get_phone_numbers_list: %s\n" % e
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
 **filters** | **str**| Filters (json object {column:value, ...}) | [optional] 
 **additional_objects** | [**list[str]**](str.md)| Additional objects | [optional] 

### Return type

[**list[PhoneNumber]**](PhoneNumber.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_phone_number**
> OkResponse remove_phone_number(phone_number_id)

Remove phone number

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.PhonenumbersApi()
phone_number_id = 'phone_number_id_example' # str | 

try: 
    # Remove phone number
    api_response = api_instance.remove_phone_number(phone_number_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PhonenumbersApi->remove_phone_number: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_phone_number**
> PhoneNumber update_phone_number(phone_number_id, phone_number)

Update phone number

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
api_instance = liveagent_api.PhonenumbersApi()
phone_number_id = 'phone_number_id_example' # str | 
phone_number = liveagent_api.PhoneNumber() # PhoneNumber | 

try: 
    # Update phone number
    api_response = api_instance.update_phone_number(phone_number_id, phone_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PhonenumbersApi->update_phone_number: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
 **phone_number** | [**PhoneNumber**](PhoneNumber.md)|  | 

### Return type

[**PhoneNumber**](PhoneNumber.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_phone_number_status**
> PhoneNumber update_phone_number_status(phone_number_id, status)

Update phone number status

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
api_instance = liveagent_api.PhonenumbersApi()
phone_number_id = 'phone_number_id_example' # str | 
status = 'status_example' # str | A - Active, I - Inactive

try: 
    # Update phone number status
    api_response = api_instance.update_phone_number_status(phone_number_id, status)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PhonenumbersApi->update_phone_number_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
 **status** | **str**| A - Active, I - Inactive | 

### Return type

[**PhoneNumber**](PhoneNumber.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

