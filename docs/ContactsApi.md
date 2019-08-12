# liveagent_api.ContactsApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](ContactsApi.md#create_contact) | **POST** /contacts | Create new contact
[**delete_contact**](ContactsApi.md#delete_contact) | **DELETE** /contacts/{contactId} | Delete contact
[**get_contacts_list**](ContactsApi.md#get_contacts_list) | **GET** /contacts | Gets list of contacts
[**get_specific_contact**](ContactsApi.md#get_specific_contact) | **GET** /contacts/{contactId} | Get contact by specific id
[**patch_contact**](ContactsApi.md#patch_contact) | **PATCH** /contacts/{contactId} | Update contact partially
[**register_contact**](ContactsApi.md#register_contact) | **PUT** /contacts/{contactId}/_register | Register contact
[**update_contact**](ContactsApi.md#update_contact) | **PUT** /contacts/{contactId} | Update whole contact


# **create_contact**
> Contact create_contact(contact=contact)

Create new contact

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
api_instance = liveagent_api.ContactsApi(liveagent_api.ApiClient(configuration))
contact = liveagent_api.ContactRequest() # ContactRequest |  (optional)

try:
    # Create new contact
    api_response = api_instance.create_contact(contact=contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**ContactRequest**](ContactRequest.md)|  | [optional] 

### Return type

[**Contact**](Contact.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> OkResponse delete_contact(contact_id, delete_tickets)

Delete contact

Deletes a contact

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
api_instance = liveagent_api.ContactsApi(liveagent_api.ApiClient(configuration))
contact_id = 'contact_id_example' # str | 
delete_tickets = true # bool | <u>true</u>: Delete customer from all lists and also delete all his tickets.<br> <u>false</u>: Delete customer from all lists but leave his tickets intact.

try:
    # Delete contact
    api_response = api_instance.delete_contact(contact_id, delete_tickets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->delete_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **delete_tickets** | **bool**| &lt;u&gt;true&lt;/u&gt;: Delete customer from all lists and also delete all his tickets.&lt;br&gt; &lt;u&gt;false&lt;/u&gt;: Delete customer from all lists but leave his tickets intact. | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts_list**
> list[ContactListItem] get_contacts_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)

Gets list of contacts

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
api_instance = liveagent_api.ContactsApi(liveagent_api.ApiClient(configuration))
page = 1 # int | Page to display. Not used if _from is defined. (optional) (default to 1)
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
_from = 0 # int | Result set start. Takes precedence over _page. (optional) (default to 0)
to = 0 # int | Result set end. Used only if _from is used. (optional) (default to 0)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filters (json object {column:value, ...} or json array [[column,operator,value], ...]) (optional)

try:
    # Gets list of contacts
    api_response = api_instance.get_contacts_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_contacts_list: %s\n" % e)
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
 **filters** | **str**| Filters (json object {column:value, ...} or json array [[column,operator,value], ...]) | [optional] 

### Return type

[**list[ContactListItem]**](ContactListItem.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_contact**
> Contact get_specific_contact(contact_id)

Get contact by specific id

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
api_instance = liveagent_api.ContactsApi(liveagent_api.ApiClient(configuration))
contact_id = 'contact_id_example' # str | 

try:
    # Get contact by specific id
    api_response = api_instance.get_specific_contact(contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_specific_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_contact**
> Contact patch_contact(contact_id, contact=contact)

Update contact partially

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
api_instance = liveagent_api.ContactsApi(liveagent_api.ApiClient(configuration))
contact_id = 'contact_id_example' # str | 
contact = liveagent_api.ContactRequest() # ContactRequest |  (optional)

try:
    # Update contact partially
    api_response = api_instance.patch_contact(contact_id, contact=contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->patch_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **contact** | [**ContactRequest**](ContactRequest.md)|  | [optional] 

### Return type

[**Contact**](Contact.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_contact**
> Contact register_contact(contact_id, registration_email, send_registration_mail=send_registration_mail)

Register contact

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
api_instance = liveagent_api.ContactsApi(liveagent_api.ApiClient(configuration))
contact_id = 'contact_id_example' # str | 
registration_email = 'registration_email_example' # str | 
send_registration_mail = true # bool | If this parameter is false, the registration mail will not be sent (optional) (default to true)

try:
    # Register contact
    api_response = api_instance.register_contact(contact_id, registration_email, send_registration_mail=send_registration_mail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->register_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **registration_email** | **str**|  | 
 **send_registration_mail** | **bool**| If this parameter is false, the registration mail will not be sent | [optional] [default to true]

### Return type

[**Contact**](Contact.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> Contact update_contact(contact_id, contact=contact)

Update whole contact

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
api_instance = liveagent_api.ContactsApi(liveagent_api.ApiClient(configuration))
contact_id = 'contact_id_example' # str | 
contact = liveagent_api.ContactRequest() # ContactRequest |  (optional)

try:
    # Update whole contact
    api_response = api_instance.update_contact(contact_id, contact=contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **contact** | [**ContactRequest**](ContactRequest.md)|  | [optional] 

### Return type

[**Contact**](Contact.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

