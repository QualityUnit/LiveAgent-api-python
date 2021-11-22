# liveagent_api.PageVisitsApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_page_visit_by_contact_id**](PageVisitsApi.md#get_page_visit_by_contact_id) | **GET** /page_visits/{contactId}/contact | Gets a page visits


# **get_page_visit_by_contact_id**
> list[PageVisit] get_page_visit_by_contact_id(contact_id, sort_dir=sort_dir, sort_field=sort_field, page=page, per_page=per_page, _from=_from, to=to)

Gets a page visits

Gets a page visits for user contact id. If elastic search is enabled and it throws exception, error is logged and empty array is returned. 

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
api_instance = liveagent_api.PageVisitsApi(liveagent_api.ApiClient(configuration))
contact_id = 'contact_id_example' # str | 
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
page = 1 # int | Page to display. Not used if _from is defined. (optional) (default to 1)
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
_from = 0 # int | Result set start. Takes precedence over _page. (optional) (default to 0)
to = 0 # int | Result set end. Used only if _from is used. (optional) (default to 0)

try:
    # Gets a page visits
    api_response = api_instance.get_page_visit_by_contact_id(contact_id, sort_dir=sort_dir, sort_field=sort_field, page=page, per_page=per_page, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageVisitsApi->get_page_visit_by_contact_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **sort_field** | **str**| Sorting field | [optional] 
 **page** | **int**| Page to display. Not used if _from is defined. | [optional] [default to 1]
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] [default to 10]
 **_from** | **int**| Result set start. Takes precedence over _page. | [optional] [default to 0]
 **to** | **int**| Result set end. Used only if _from is used. | [optional] [default to 0]

### Return type

[**list[PageVisit]**](PageVisit.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

