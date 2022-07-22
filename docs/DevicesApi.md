# liveagent_api.DevicesApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device**](DevicesApi.md#create_device) | **POST** /devices | Create new device
[**create_device_department_plans**](DevicesApi.md#create_device_department_plans) | **POST** /devices/{deviceId}/departments/{departmentId}/plans | Create device department plans
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /devices/{deviceId} | Delete device
[**delete_device_department_plans**](DevicesApi.md#delete_device_department_plans) | **DELETE** /devices/{deviceId}/departments/{departmentId}/plans | Delete device department plans
[**get_device**](DevicesApi.md#get_device) | **GET** /devices/{deviceId} | Get device by id
[**get_device_department**](DevicesApi.md#get_device_department) | **GET** /devices/{deviceId}/departments/{departmentId} | Get device department by id
[**get_device_departments**](DevicesApi.md#get_device_departments) | **GET** /devices/{deviceId}/departments | Get device departments
[**get_device_departments_by_department_id**](DevicesApi.md#get_device_departments_by_department_id) | **GET** /devices/departments/{departmentId} | Get device departments by department id
[**get_device_plans**](DevicesApi.md#get_device_plans) | **GET** /devices/{deviceId}/plans | Get device plans
[**get_devices_list**](DevicesApi.md#get_devices_list) | **GET** /devices | Gets list of devices
[**get_my_mobile_devices_list**](DevicesApi.md#get_my_mobile_devices_list) | **GET** /devices/_app_ | Gets list of current agent&#39;s mobile devices. Creates new one if there are no devices.
[**update_device**](DevicesApi.md#update_device) | **PUT** /devices/{deviceId} | Update device
[**update_device_department**](DevicesApi.md#update_device_department) | **PUT** /devices/{deviceId}/departments/{departmentId} | Update device department
[**update_device_departments**](DevicesApi.md#update_device_departments) | **PUT** /devices/departments/update | Update device departments


# **create_device**
> Device create_device(device=device)

Create new device

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))
device = liveagent_api.Device() # Device |  (optional)

try:
    # Create new device
    api_response = api_instance.create_device(device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**Device**](Device.md)|  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_department_plans**
> list[DeviceDepartmentPlan] create_device_department_plans(device_id, department_id, plan=plan)

Create device department plans

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))
device_id = 56 # int | 
department_id = 'department_id_example' # str | 
plan = liveagent_api.DeviceDepartmentPlanList() # DeviceDepartmentPlanList |  (optional)

try:
    # Create device department plans
    api_response = api_instance.create_device_department_plans(device_id, department_id, plan=plan)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device_department_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **department_id** | **str**|  | 
 **plan** | [**DeviceDepartmentPlanList**](DeviceDepartmentPlanList.md)|  | [optional] 

### Return type

[**list[DeviceDepartmentPlan]**](DeviceDepartmentPlan.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> OkResponse delete_device(device_id)

Delete device

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))
device_id = 56 # int | 

try:
    # Delete device
    api_response = api_instance.delete_device(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_department_plans**
> OkResponse delete_device_department_plans(device_id, department_id)

Delete device department plans

Deletes a device department plans

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))
device_id = 56 # int | 
department_id = 'department_id_example' # str | 

try:
    # Delete device department plans
    api_response = api_instance.delete_device_department_plans(device_id, department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device_department_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **department_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**
> Device get_device(device_id)

Get device by id

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))
device_id = 56 # int | 

try:
    # Get device by id
    api_response = api_instance.get_device(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 

### Return type

[**Device**](Device.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_department**
> DeviceDepartment get_device_department(device_id, department_id)

Get device department by id

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))
device_id = 56 # int | 
department_id = 'department_id_example' # str | 

try:
    # Get device department by id
    api_response = api_instance.get_device_department(device_id, department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **department_id** | **str**|  | 

### Return type

[**DeviceDepartment**](DeviceDepartment.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_departments**
> list[DeviceDepartment] get_device_departments(device_id, page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, sort_fields=sort_fields, filters=filters)

Get device departments

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))
device_id = 56 # int | 
page = 1 # int | Page to display. Not used if _from is defined. (optional) (default to 1)
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
_from = 0 # int | Result set start. Takes precedence over _page. (optional) (default to 0)
to = 0 # int | Result set end. Used only if _from is used. (optional) (default to 0)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
sort_fields = 'sort_fields_example' # str | 'Sort fields (json object {column:direction, ...}).'<br> Direction can be:<br> - \"ASC\" (ascending)<br> - \"DESC\" (descending) If _sortFields is defined, _sortField and _sortDir is ignored. (optional)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Get device departments
    api_response = api_instance.get_device_departments(device_id, page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, sort_fields=sort_fields, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_departments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **page** | **int**| Page to display. Not used if _from is defined. | [optional] [default to 1]
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] [default to 10]
 **_from** | **int**| Result set start. Takes precedence over _page. | [optional] [default to 0]
 **to** | **int**| Result set end. Used only if _from is used. | [optional] [default to 0]
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to ASC]
 **sort_field** | **str**| Sorting field | [optional] 
 **sort_fields** | **str**| &#39;Sort fields (json object {column:direction, ...}).&#39;&lt;br&gt; Direction can be:&lt;br&gt; - \&quot;ASC\&quot; (ascending)&lt;br&gt; - \&quot;DESC\&quot; (descending) If _sortFields is defined, _sortField and _sortDir is ignored. | [optional] 
 **filters** | **str**| Filter as json object {\&quot;column1\&quot;:\&quot;value\&quot;, \&quot;column2\&quot;:\&quot;value\&quot;, ...} or list of filters as json array [[\&quot;column\&quot;,\&quot;operator\&quot;,\&quot;value\&quot;], ...] | [optional] 

### Return type

[**list[DeviceDepartment]**](DeviceDepartment.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_departments_by_department_id**
> list[DeviceDepartment] get_device_departments_by_department_id(department_id)

Get device departments by department id

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))
department_id = 'department_id_example' # str | 

try:
    # Get device departments by department id
    api_response = api_instance.get_device_departments_by_department_id(department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_departments_by_department_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **str**|  | 

### Return type

[**list[DeviceDepartment]**](DeviceDepartment.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_plans**
> list[IndexedDeviceDepartmentPlans] get_device_plans(device_id)

Get device plans

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))
device_id = 56 # int | 

try:
    # Get device plans
    api_response = api_instance.get_device_plans(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 

### Return type

[**list[IndexedDeviceDepartmentPlans]**](IndexedDeviceDepartmentPlans.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_list**
> list[Device] get_devices_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)

Gets list of devices

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))
page = 1 # int | Page to display. Not used if _from is defined. (optional) (default to 1)
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
_from = 0 # int | Result set start. Takes precedence over _page. (optional) (default to 0)
to = 0 # int | Result set end. Used only if _from is used. (optional) (default to 0)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filter as json object {\"column1\":\"value\", \"column2\":\"value\", ...} or list of filters as json array [[\"column\",\"operator\",\"value\"], ...] (optional)

try:
    # Gets list of devices
    api_response = api_instance.get_devices_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices_list: %s\n" % e)
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

[**list[Device]**](Device.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_mobile_devices_list**
> list[Device] get_my_mobile_devices_list()

Gets list of current agent's mobile devices. Creates new one if there are no devices.

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))

try:
    # Gets list of current agent's mobile devices. Creates new one if there are no devices.
    api_response = api_instance.get_my_mobile_devices_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_my_mobile_devices_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Device]**](Device.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> Device update_device(device_id, device=device)

Update device

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))
device_id = 56 # int | 
device = liveagent_api.Device() # Device |  (optional)

try:
    # Update device
    api_response = api_instance.update_device(device_id, device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device** | [**Device**](Device.md)|  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_department**
> DeviceDepartment update_device_department(device_id, department_id, device_department=device_department)

Update device department

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))
device_id = 56 # int | 
department_id = 'department_id_example' # str | 
device_department = liveagent_api.DeviceDepartment() # DeviceDepartment |  (optional)

try:
    # Update device department
    api_response = api_instance.update_device_department(device_id, department_id, device_department=device_department)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **department_id** | **str**|  | 
 **device_department** | [**DeviceDepartment**](DeviceDepartment.md)|  | [optional] 

### Return type

[**DeviceDepartment**](DeviceDepartment.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_departments**
> list[DeviceDepartment] update_device_departments(device_departments=device_departments)

Update device departments

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
api_instance = liveagent_api.DevicesApi(liveagent_api.ApiClient(configuration))
device_departments = liveagent_api.DeviceDepartmentList() # DeviceDepartmentList |  (optional)

try:
    # Update device departments
    api_response = api_instance.update_device_departments(device_departments=device_departments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device_departments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_departments** | [**DeviceDepartmentList**](DeviceDepartmentList.md)|  | [optional] 

### Return type

[**list[DeviceDepartment]**](DeviceDepartment.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

