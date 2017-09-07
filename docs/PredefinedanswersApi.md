# liveagent_api.PredefinedanswersApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_predefined_answer**](PredefinedanswersApi.md#create_predefined_answer) | **POST** /predefined_answers | Create predefined answer
[**delete_predefined_answer**](PredefinedanswersApi.md#delete_predefined_answer) | **DELETE** /predefined_answers/{predefinedAnswerId} | Predefined answer
[**get_predefined_answer**](PredefinedanswersApi.md#get_predefined_answer) | **GET** /predefined_answers/{predefinedAnswerId} | Gets canned message
[**get_predefined_answers_list**](PredefinedanswersApi.md#get_predefined_answers_list) | **GET** /predefined_answers | Gets list of predefined answers
[**update_predefined_answer**](PredefinedanswersApi.md#update_predefined_answer) | **PUT** /predefined_answers/{predefinedAnswerId} | Update predefined answer


# **create_predefined_answer**
> PredefinedAnswer create_predefined_answer(predefined_answer=predefined_answer)

Create predefined answer

Create new predefined answer

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
api_instance = liveagent_api.PredefinedanswersApi()
predefined_answer = liveagent_api.PredefinedAnswer() # PredefinedAnswer |  (optional)

try: 
    # Create predefined answer
    api_response = api_instance.create_predefined_answer(predefined_answer=predefined_answer)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PredefinedanswersApi->create_predefined_answer: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **predefined_answer** | [**PredefinedAnswer**](PredefinedAnswer.md)|  | [optional] 

### Return type

[**PredefinedAnswer**](PredefinedAnswer.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_predefined_answer**
> OkResponse delete_predefined_answer(predefined_answer_id)

Predefined answer

Deletes a predefined answer

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
api_instance = liveagent_api.PredefinedanswersApi()
predefined_answer_id = 'predefined_answer_id_example' # str | 

try: 
    # Predefined answer
    api_response = api_instance.delete_predefined_answer(predefined_answer_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PredefinedanswersApi->delete_predefined_answer: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **predefined_answer_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_predefined_answer**
> PredefinedAnswer get_predefined_answer(predefined_answer_id)

Gets canned message

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
api_instance = liveagent_api.PredefinedanswersApi()
predefined_answer_id = 'predefined_answer_id_example' # str | 

try: 
    # Gets canned message
    api_response = api_instance.get_predefined_answer(predefined_answer_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PredefinedanswersApi->get_predefined_answer: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **predefined_answer_id** | **str**|  | 

### Return type

[**PredefinedAnswer**](PredefinedAnswer.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_predefined_answers_list**
> list[PredefinedAnswer] get_predefined_answers_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)

Gets list of predefined answers

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
api_instance = liveagent_api.PredefinedanswersApi()
page = 1 # int | Page to display. Not used if _from is defined. (optional) (default to 1)
per_page = 10 # int | Results per page. Used only if _page is used. (optional) (default to 10)
_from = 0 # int | Result set start. Takes precedence over _page. (optional) (default to 0)
to = 0 # int | Result set end. Used only if _from is used. (optional) (default to 0)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)

try: 
    # Gets list of predefined answers
    api_response = api_instance.get_predefined_answers_list(page=page, per_page=per_page, _from=_from, to=to, sort_dir=sort_dir, sort_field=sort_field, filters=filters)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PredefinedanswersApi->get_predefined_answers_list: %s\n" % e
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

### Return type

[**list[PredefinedAnswer]**](PredefinedAnswer.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_predefined_answer**
> PredefinedAnswer update_predefined_answer(predefined_answer_id, canned_message=canned_message)

Update predefined answer

Update a predefined answer

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
api_instance = liveagent_api.PredefinedanswersApi()
predefined_answer_id = 'predefined_answer_id_example' # str | 
canned_message = liveagent_api.PredefinedAnswer() # PredefinedAnswer |  (optional)

try: 
    # Update predefined answer
    api_response = api_instance.update_predefined_answer(predefined_answer_id, canned_message=canned_message)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PredefinedanswersApi->update_predefined_answer: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **predefined_answer_id** | **str**|  | 
 **canned_message** | [**PredefinedAnswer**](PredefinedAnswer.md)|  | [optional] 

### Return type

[**PredefinedAnswer**](PredefinedAnswer.md)

### Authorization

[privileges](../README.md#privileges), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

