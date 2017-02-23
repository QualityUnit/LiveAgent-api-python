# liveagent_api.ContactsApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](ContactsApi.md#create_contact) | **POST** /contacts | Create new contact
[**get_contacts_list**](ContactsApi.md#get_contacts_list) | **GET** /contacts | Gets list of contacts. Special filters hasEmail (Y/N), hasPhone (Y/N)\nY - Yes, N - No\n
[**get_specific_contact**](ContactsApi.md#get_specific_contact) | **GET** /contacts/{contactId} | Get contact by specific id
[**update_contact**](ContactsApi.md#update_contact) | **PUT** /contacts/{contactId} | Update contact


# **create_contact**
> list[Contact] create_contact(contact=contact)

Create new contact

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.ContactsApi()
contact = liveagent_api.Contact() # Contact |  (optional)

try: 
    # Create new contact
    api_response = api_instance.create_contact(contact=contact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactsApi->create_contact: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**Contact**](Contact.md)|  | [optional] 

### Return type

[**list[Contact]**](Contact.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts_list**
> list[ContactListItem] get_contacts_list(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters)

Gets list of contacts. Special filters hasEmail (Y/N), hasPhone (Y/N)\nY - Yes, N - No\n

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.ContactsApi()
page = 1 # int | Page to display. Not used if _from is defined. (optional) (default to 1)
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)

try: 
    # Gets list of contacts. Special filters hasEmail (Y/N), hasPhone (Y/N)\nY - Yes, N - No\n
    api_response = api_instance.get_contacts_list(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactsApi->get_contacts_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page to display. Not used if _from is defined. | [optional] [default to 1]
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **sort_field** | **str**| Sorting field | [optional] 
 **filters** | **str**| Filters (json object {column:value, ...}) | [optional] 

### Return type

[**list[ContactListItem]**](ContactListItem.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_contact**
> list[Contact] get_specific_contact(contact_id)

Get contact by specific id

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.ContactsApi()
contact_id = 'contact_id_example' # str | 

try: 
    # Get contact by specific id
    api_response = api_instance.get_specific_contact(contact_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactsApi->get_specific_contact: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 

### Return type

[**list[Contact]**](Contact.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> list[Contact] update_contact(contact_id, contact=contact)

Update contact

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.ContactsApi()
contact_id = 'contact_id_example' # str | 
contact = liveagent_api.Contact() # Contact |  (optional)

try: 
    # Update contact
    api_response = api_instance.update_contact(contact_id, contact=contact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactsApi->update_contact: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **contact** | [**Contact**](Contact.md)|  | [optional] 

### Return type

[**list[Contact]**](Contact.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
