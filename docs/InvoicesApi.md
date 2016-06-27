# liveagent_api.InvoicesApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoices_get**](InvoicesApi.md#invoices_get) | **GET** /invoices/ | Invoice list
[**invoices_invoice_number_download_get**](InvoicesApi.md#invoices_invoice_number_download_get) | **GET** /invoices/{invoiceNumber}/_download | Download invoice


# **invoices_get**
> list[Invoice] invoices_get(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters)

Invoice list

Invoices list

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
api_instance = liveagent_api.InvoicesApi()
page = 1 # float | Page to display (optional) (default to 1)
per_page = 10 # float | Results per page (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)

try: 
    # Invoice list
    api_response = api_instance.invoices_get(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->invoices_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Page to display | [optional] [default to 1]
 **per_page** | **float**| Results per page | [optional] [default to 10]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **sort_field** | **str**| Sorting field | [optional] 
 **filters** | **str**| Filters (json object {column:value, ...}) | [optional] 

### Return type

[**list[Invoice]**](Invoice.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_invoice_number_download_get**
> file invoices_invoice_number_download_get(invoice_number)

Download invoice

Download invoice

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
api_instance = liveagent_api.InvoicesApi()
invoice_number = 'invoice_number_example' # str | 

try: 
    # Download invoice
    api_response = api_instance.invoices_invoice_number_download_get(invoice_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->invoices_invoice_number_download_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_number** | **str**|  | 

### Return type

[**file**](file.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

