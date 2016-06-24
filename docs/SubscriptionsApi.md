# swagger_client.SubscriptionsApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**la_api_v3_proxy_add_usage**](SubscriptionsApi.md#la_api_v3_proxy_add_usage) | **PUT** /subscriptions/{subscriptionId}/usage | Subscription usage
[**la_api_v3_proxy_change_plan**](SubscriptionsApi.md#la_api_v3_proxy_change_plan) | **POST** /subscriptions/{subscriptionId}/_upgrade | Change plan
[**la_api_v3_proxy_get_billing_info**](SubscriptionsApi.md#la_api_v3_proxy_get_billing_info) | **GET** /subscriptions/{subscriptionId}/billingInfo | Billing info
[**la_api_v3_proxy_get_billing_metrics**](SubscriptionsApi.md#la_api_v3_proxy_get_billing_metrics) | **GET** /subscriptions/{subscriptionId}/billingMetrics | Billing metrics
[**la_api_v3_proxy_get_billing_status**](SubscriptionsApi.md#la_api_v3_proxy_get_billing_status) | **GET** /subscriptions/{subscriptionId}/billingStatus | Billing status
[**la_api_v3_proxy_get_domain**](SubscriptionsApi.md#la_api_v3_proxy_get_domain) | **GET** /subscriptions/{subscriptionId}/domain | Domain info
[**la_api_v3_proxy_get_payment_method**](SubscriptionsApi.md#la_api_v3_proxy_get_payment_method) | **GET** /subscriptions/{subscriptionId}/paymentMethod | Payment method
[**la_api_v3_proxy_get_processor_type**](SubscriptionsApi.md#la_api_v3_proxy_get_processor_type) | **GET** /subscriptions/{subscriptionId}/paymentProcessor | Payment processor
[**la_api_v3_proxy_get_subscription**](SubscriptionsApi.md#la_api_v3_proxy_get_subscription) | **GET** /subscriptions/{subscriptionId} | Subscription
[**la_api_v3_proxy_get_subscription_attributes**](SubscriptionsApi.md#la_api_v3_proxy_get_subscription_attributes) | **GET** /subscriptions/{subscriptionId}/attributes/ | Subscription attribute list
[**la_api_v3_proxy_get_subscription_invoices**](SubscriptionsApi.md#la_api_v3_proxy_get_subscription_invoices) | **GET** /subscriptions/{subscriptionId}/invoices/ | Subscription invoice list
[**la_api_v3_proxy_get_variation_upgrades**](SubscriptionsApi.md#la_api_v3_proxy_get_variation_upgrades) | **GET** /subscriptions/{subscriptionId}/upgradeVariations | Upgrade variation list
[**la_api_v3_proxy_resume_billing**](SubscriptionsApi.md#la_api_v3_proxy_resume_billing) | **POST** /subscriptions/{subscriptionId}/_cancelStop | Restart billing
[**la_api_v3_proxy_stop_billing**](SubscriptionsApi.md#la_api_v3_proxy_stop_billing) | **POST** /subscriptions/{subscriptionId}/_stop | Stop billing
[**la_api_v3_proxy_update**](SubscriptionsApi.md#la_api_v3_proxy_update) | **POST** /subscriptions/{subscriptionId}/_update | Update subscription
[**la_api_v3_proxy_update_billing_info**](SubscriptionsApi.md#la_api_v3_proxy_update_billing_info) | **PUT** /subscriptions/{subscriptionId}/billingInfo | Billing info
[**la_api_v3_proxy_update_domain**](SubscriptionsApi.md#la_api_v3_proxy_update_domain) | **PUT** /subscriptions/{subscriptionId}/domain | Custom domain
[**la_api_v3_proxy_update_payment_method**](SubscriptionsApi.md#la_api_v3_proxy_update_payment_method) | **PUT** /subscriptions/{subscriptionId}/paymentMethod | Payment method


# **la_api_v3_proxy_add_usage**
> OkResponse la_api_v3_proxy_add_usage(subscription_id, body=body)

Subscription usage

Get subscription invoices

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
body = swagger_client.UsageData() # UsageData |  (optional)

try: 
    # Subscription usage
    api_response = api_instance.la_api_v3_proxy_add_usage(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_add_usage: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**UsageData**](UsageData.md)|  | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_change_plan**
> OkResponse la_api_v3_proxy_change_plan(subscription_id, body=body)

Change plan

Upgrade subscription to another variation. In case of upgrade from paid to paid, it's possible to change country without changing payment method. If change is between EU and not EU, different payment rules might apply.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
body = swagger_client.Upgrade() # Upgrade |  (optional)

try: 
    # Change plan
    api_response = api_instance.la_api_v3_proxy_change_plan(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_change_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**Upgrade**](Upgrade.md)|  | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_get_billing_info**
> Customer la_api_v3_proxy_get_billing_info(subscription_id)

Billing info

Get billing info

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Billing info
    api_response = api_instance.la_api_v3_proxy_get_billing_info(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_get_billing_info: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**Customer**](Customer.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_get_billing_metrics**
> list[BillingMetric] la_api_v3_proxy_get_billing_metrics(subscription_id)

Billing metrics

Get billing metrics

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Billing metrics
    api_response = api_instance.la_api_v3_proxy_get_billing_metrics(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_get_billing_metrics: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**list[BillingMetric]**](BillingMetric.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_get_billing_status**
> BillingStatus la_api_v3_proxy_get_billing_status(subscription_id)

Billing status

Get billing status

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Billing status
    api_response = api_instance.la_api_v3_proxy_get_billing_status(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_get_billing_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**BillingStatus**](BillingStatus.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_get_domain**
> Domain la_api_v3_proxy_get_domain(subscription_id)

Domain info

Get domain info

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Domain info
    api_response = api_instance.la_api_v3_proxy_get_domain(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_get_domain: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_get_payment_method**
> PaymentInfo la_api_v3_proxy_get_payment_method(subscription_id)

Payment method

Get payment method

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Payment method
    api_response = api_instance.la_api_v3_proxy_get_payment_method(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_get_payment_method: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**PaymentInfo**](PaymentInfo.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_get_processor_type**
> PaymentProcessorType la_api_v3_proxy_get_processor_type(subscription_id, payment_type)

Payment processor

Get payment processor to generate token for when updating payment method

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
payment_type = 'payment_type_example' # str | 

try: 
    # Payment processor
    api_response = api_instance.la_api_v3_proxy_get_processor_type(subscription_id, payment_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_get_processor_type: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **payment_type** | **str**|  | 

### Return type

[**PaymentProcessorType**](PaymentProcessorType.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_get_subscription**
> Subscription la_api_v3_proxy_get_subscription(subscription_id)

Subscription

Get subscription

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Subscription
    api_response = api_instance.la_api_v3_proxy_get_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_get_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_get_subscription_attributes**
> list[AttributeSimple] la_api_v3_proxy_get_subscription_attributes(subscription_id)

Subscription attribute list

Subscription attributes list

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Subscription attribute list
    api_response = api_instance.la_api_v3_proxy_get_subscription_attributes(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_get_subscription_attributes: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**list[AttributeSimple]**](AttributeSimple.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_get_subscription_invoices**
> list[Invoice] la_api_v3_proxy_get_subscription_invoices(subscription_id, page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters)

Subscription invoice list

Subscription invoices list

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
page = 1 # float | Page to display (optional) (default to 1)
per_page = 10 # float | Results per page (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)

try: 
    # Subscription invoice list
    api_response = api_instance.la_api_v3_proxy_get_subscription_invoices(subscription_id, page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_get_subscription_invoices: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
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

# **la_api_v3_proxy_get_variation_upgrades**
> VariationUpgrades la_api_v3_proxy_get_variation_upgrades(subscription_id)

Upgrade variation list

List of variations user can upgrade to and their current variation.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Upgrade variation list
    api_response = api_instance.la_api_v3_proxy_get_variation_upgrades(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_get_variation_upgrades: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**VariationUpgrades**](VariationUpgrades.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_resume_billing**
> OkResponse la_api_v3_proxy_resume_billing(subscription_id)

Restart billing

If account billing is stopped, restart it.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Restart billing
    api_response = api_instance.la_api_v3_proxy_resume_billing(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_resume_billing: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_stop_billing**
> OkResponse la_api_v3_proxy_stop_billing(subscription_id)

Stop billing

Stop account. Account won't be billed anymore and will continue to work till next billing date.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Stop billing
    api_response = api_instance.la_api_v3_proxy_stop_billing(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_stop_billing: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_update**
> OkResponse la_api_v3_proxy_update(subscription_id)

Update subscription

Update subscription to latest version

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Update subscription
    api_response = api_instance.la_api_v3_proxy_update(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_update_billing_info**
> OkResponse la_api_v3_proxy_update_billing_info(subscription_id, body=body)

Billing info

Update billing info

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
body = swagger_client.BillingInfo() # BillingInfo |  (optional)

try: 
    # Billing info
    api_response = api_instance.la_api_v3_proxy_update_billing_info(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_update_billing_info: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**BillingInfo**](BillingInfo.md)|  | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_update_domain**
> OkResponse la_api_v3_proxy_update_domain(subscription_id, body=body)

Custom domain

Park custom domain on an account

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
body = swagger_client.Domain() # Domain |  (optional)

try: 
    # Custom domain
    api_response = api_instance.la_api_v3_proxy_update_domain(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_update_domain: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**Domain**](Domain.md)|  | [optional] 

### Return type

[**OkResponse**](OkResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **la_api_v3_proxy_update_payment_method**
> PaymentInfo la_api_v3_proxy_update_payment_method(subscription_id, body=body)

Payment method

Update payment method

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
body = swagger_client.PaymentMethod() # PaymentMethod |  (optional)

try: 
    # Payment method
    api_response = api_instance.la_api_v3_proxy_update_payment_method(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->la_api_v3_proxy_update_payment_method: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**PaymentMethod**](PaymentMethod.md)|  | [optional] 

### Return type

[**PaymentInfo**](PaymentInfo.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

