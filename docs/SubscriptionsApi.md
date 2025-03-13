# liveagent_api.SubscriptionsApi

All URIs are relative to *https://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_billing_status**](SubscriptionsApi.md#get_billing_status) | **GET** /subscriptions/{subscriptionId}/billingStatus | Billing status
[**get_domain_info**](SubscriptionsApi.md#get_domain_info) | **GET** /subscriptions/{subscriptionId}/domain | Domain info
[**get_subscription_discounts**](SubscriptionsApi.md#get_subscription_discounts) | **GET** /subscriptions/{subscriptionId}/discounts | Subscription discounts
[**set_custom_domain**](SubscriptionsApi.md#set_custom_domain) | **PUT** /subscriptions/{subscriptionId}/custom_domain | Custom domain


# **get_billing_status**
> BillingStatus get_billing_status(subscription_id)

Billing status

Get billing status

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
api_instance = liveagent_api.SubscriptionsApi(liveagent_api.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 

try:
    # Billing status
    api_response = api_instance.get_billing_status(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_billing_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**BillingStatus**](BillingStatus.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_info**
> Domain get_domain_info(subscription_id)

Domain info

Get domain info

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
api_instance = liveagent_api.SubscriptionsApi(liveagent_api.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 

try:
    # Domain info
    api_response = api_instance.get_domain_info(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_domain_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_discounts**
> list[DiscountValue] get_subscription_discounts(subscription_id)

Subscription discounts

Returns all active discounts for specified subscription

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
api_instance = liveagent_api.SubscriptionsApi(liveagent_api.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 

try:
    # Subscription discounts
    api_response = api_instance.get_subscription_discounts(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscription_discounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**list[DiscountValue]**](DiscountValue.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_custom_domain**
> OkResponse set_custom_domain(subscription_id, body=body)

Custom domain

Park custom domain on an account

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
api_instance = liveagent_api.SubscriptionsApi(liveagent_api.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = liveagent_api.CustomDomain() # CustomDomain | Custom domain can be set only with both key and certificate present, or empty domain to reset. (optional)

try:
    # Custom domain
    api_response = api_instance.set_custom_domain(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->set_custom_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**CustomDomain**](CustomDomain.md)| Custom domain can be set only with both key and certificate present, or empty domain to reset. | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[apikey](../README.md#apikey), [privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

