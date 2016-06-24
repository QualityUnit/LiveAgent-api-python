# swagger_client.InvoicesApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**la_api_v3_proxy_download_invoice**](InvoicesApi.md#la_api_v3_proxy_download_invoice) | **GET** /invoices/{invoiceNumber}/_download | Download invoice
[**la_api_v3_proxy_get_invoices**](InvoicesApi.md#la_api_v3_proxy_get_invoices) | **GET** /invoices/ | Invoice list


# **la_api_v3_proxy_download_invoice**
> file la_api_v3_proxy_download_invoice(invoice_number)

Download invoice

Download invoice

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
invoice_number = 'invoice_number_example' # str | 

try: 
    # Download invoice
    api_response = api_instance.la_api_v3_proxy_download_invoice(invoice_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->la_api_v3_proxy_download_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_number** | **str**|  | 

### Return type

[**file**](file.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_get_invoices**
> list[Invoice] la_api_v3_proxy_get_invoices(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters)

Invoice list

Invoices list

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
page = 1 # float | Page to display (optional) (default to 1)
per_page = 10 # float | Results per page (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)

try: 
    # Invoice list
    api_response = api_instance.la_api_v3_proxy_get_invoices(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->la_api_v3_proxy_get_invoices: %s\n" % e
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

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

