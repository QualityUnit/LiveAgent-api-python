# liveagent_api.SubscriptionsApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptions_subscription_id_attributes_get**](SubscriptionsApi.md#subscriptions_subscription_id_attributes_get) | **GET** /subscriptions/{subscriptionId}/attributes/ | Subscription attribute list
[**subscriptions_subscription_id_billing_info_get**](SubscriptionsApi.md#subscriptions_subscription_id_billing_info_get) | **GET** /subscriptions/{subscriptionId}/billingInfo | Billing info
[**subscriptions_subscription_id_billing_info_put**](SubscriptionsApi.md#subscriptions_subscription_id_billing_info_put) | **PUT** /subscriptions/{subscriptionId}/billingInfo | Billing info
[**subscriptions_subscription_id_billing_metrics_get**](SubscriptionsApi.md#subscriptions_subscription_id_billing_metrics_get) | **GET** /subscriptions/{subscriptionId}/billingMetrics | Billing metrics
[**subscriptions_subscription_id_billing_status_get**](SubscriptionsApi.md#subscriptions_subscription_id_billing_status_get) | **GET** /subscriptions/{subscriptionId}/billingStatus | Billing status
[**subscriptions_subscription_id_cancel_stop_post**](SubscriptionsApi.md#subscriptions_subscription_id_cancel_stop_post) | **POST** /subscriptions/{subscriptionId}/_cancelStop | Restart billing
[**subscriptions_subscription_id_domain_get**](SubscriptionsApi.md#subscriptions_subscription_id_domain_get) | **GET** /subscriptions/{subscriptionId}/domain | Domain info
[**subscriptions_subscription_id_domain_put**](SubscriptionsApi.md#subscriptions_subscription_id_domain_put) | **PUT** /subscriptions/{subscriptionId}/domain | Custom domain
[**subscriptions_subscription_id_get**](SubscriptionsApi.md#subscriptions_subscription_id_get) | **GET** /subscriptions/{subscriptionId} | Subscription
[**subscriptions_subscription_id_invoices_get**](SubscriptionsApi.md#subscriptions_subscription_id_invoices_get) | **GET** /subscriptions/{subscriptionId}/invoices/ | Subscription invoice list
[**subscriptions_subscription_id_payment_method_get**](SubscriptionsApi.md#subscriptions_subscription_id_payment_method_get) | **GET** /subscriptions/{subscriptionId}/paymentMethod | Payment method
[**subscriptions_subscription_id_payment_method_put**](SubscriptionsApi.md#subscriptions_subscription_id_payment_method_put) | **PUT** /subscriptions/{subscriptionId}/paymentMethod | Payment method
[**subscriptions_subscription_id_payment_processor_get**](SubscriptionsApi.md#subscriptions_subscription_id_payment_processor_get) | **GET** /subscriptions/{subscriptionId}/paymentProcessor | Payment processor
[**subscriptions_subscription_id_stop_post**](SubscriptionsApi.md#subscriptions_subscription_id_stop_post) | **POST** /subscriptions/{subscriptionId}/_stop | Stop billing
[**subscriptions_subscription_id_update_post**](SubscriptionsApi.md#subscriptions_subscription_id_update_post) | **POST** /subscriptions/{subscriptionId}/_update | Update subscription
[**subscriptions_subscription_id_upgrade_post**](SubscriptionsApi.md#subscriptions_subscription_id_upgrade_post) | **POST** /subscriptions/{subscriptionId}/_upgrade | Change plan
[**subscriptions_subscription_id_upgrade_variations_get**](SubscriptionsApi.md#subscriptions_subscription_id_upgrade_variations_get) | **GET** /subscriptions/{subscriptionId}/upgradeVariations | Upgrade variation list
[**subscriptions_subscription_id_usage_put**](SubscriptionsApi.md#subscriptions_subscription_id_usage_put) | **PUT** /subscriptions/{subscriptionId}/usage | Subscription usage


# **subscriptions_subscription_id_attributes_get**
> list[AttributeSimple] subscriptions_subscription_id_attributes_get(subscription_id)

Subscription attribute list

Subscription attributes list

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Subscription attribute list
    api_response = api_instance.subscriptions_subscription_id_attributes_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_attributes_get: %s\n" % e
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

# **subscriptions_subscription_id_billing_info_get**
> Customer subscriptions_subscription_id_billing_info_get(subscription_id)

Billing info

Get billing info

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Billing info
    api_response = api_instance.subscriptions_subscription_id_billing_info_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_billing_info_get: %s\n" % e
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

# **subscriptions_subscription_id_billing_info_put**
> OkResponse subscriptions_subscription_id_billing_info_put(subscription_id, body=body)

Billing info

Update billing info

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
body = liveagent_api.BillingInfo() # BillingInfo |  (optional)

try: 
    # Billing info
    api_response = api_instance.subscriptions_subscription_id_billing_info_put(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_billing_info_put: %s\n" % e
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

# **subscriptions_subscription_id_billing_metrics_get**
> list[BillingMetric] subscriptions_subscription_id_billing_metrics_get(subscription_id)

Billing metrics

Get billing metrics

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Billing metrics
    api_response = api_instance.subscriptions_subscription_id_billing_metrics_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_billing_metrics_get: %s\n" % e
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

# **subscriptions_subscription_id_billing_status_get**
> BillingStatus subscriptions_subscription_id_billing_status_get(subscription_id)

Billing status

Get billing status

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Billing status
    api_response = api_instance.subscriptions_subscription_id_billing_status_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_billing_status_get: %s\n" % e
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

# **subscriptions_subscription_id_cancel_stop_post**
> OkResponse subscriptions_subscription_id_cancel_stop_post(subscription_id)

Restart billing

If account billing is stopped, restart it.

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Restart billing
    api_response = api_instance.subscriptions_subscription_id_cancel_stop_post(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_cancel_stop_post: %s\n" % e
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

# **subscriptions_subscription_id_domain_get**
> Domain subscriptions_subscription_id_domain_get(subscription_id)

Domain info

Get domain info

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Domain info
    api_response = api_instance.subscriptions_subscription_id_domain_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_domain_get: %s\n" % e
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

# **subscriptions_subscription_id_domain_put**
> OkResponse subscriptions_subscription_id_domain_put(subscription_id, body=body)

Custom domain

Park custom domain on an account

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
body = liveagent_api.Domain() # Domain |  (optional)

try: 
    # Custom domain
    api_response = api_instance.subscriptions_subscription_id_domain_put(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_domain_put: %s\n" % e
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

# **subscriptions_subscription_id_get**
> Subscription subscriptions_subscription_id_get(subscription_id)

Subscription

Get subscription

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Subscription
    api_response = api_instance.subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_get: %s\n" % e
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

# **subscriptions_subscription_id_invoices_get**
> list[Invoice] subscriptions_subscription_id_invoices_get(subscription_id, page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters)

Subscription invoice list

Subscription invoices list

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
page = 1 # float | Page to display (optional) (default to 1)
per_page = 10 # float | Results per page (optional) (default to 10)
sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to ASC)
sort_field = 'sort_field_example' # str | Sorting field (optional)
filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)

try: 
    # Subscription invoice list
    api_response = api_instance.subscriptions_subscription_id_invoices_get(subscription_id, page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_invoices_get: %s\n" % e
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

# **subscriptions_subscription_id_payment_method_get**
> PaymentInfo subscriptions_subscription_id_payment_method_get(subscription_id)

Payment method

Get payment method

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Payment method
    api_response = api_instance.subscriptions_subscription_id_payment_method_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_payment_method_get: %s\n" % e
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

# **subscriptions_subscription_id_payment_method_put**
> PaymentInfo subscriptions_subscription_id_payment_method_put(subscription_id, body=body)

Payment method

Update payment method

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
body = liveagent_api.PaymentMethod() # PaymentMethod |  (optional)

try: 
    # Payment method
    api_response = api_instance.subscriptions_subscription_id_payment_method_put(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_payment_method_put: %s\n" % e
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

# **subscriptions_subscription_id_payment_processor_get**
> PaymentProcessorType subscriptions_subscription_id_payment_processor_get(subscription_id, payment_type)

Payment processor

Get payment processor to generate token for when updating payment method

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
payment_type = 'payment_type_example' # str | 

try: 
    # Payment processor
    api_response = api_instance.subscriptions_subscription_id_payment_processor_get(subscription_id, payment_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_payment_processor_get: %s\n" % e
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

# **subscriptions_subscription_id_stop_post**
> OkResponse subscriptions_subscription_id_stop_post(subscription_id)

Stop billing

Stop account. Account won't be billed anymore and will continue to work till next billing date.

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Stop billing
    api_response = api_instance.subscriptions_subscription_id_stop_post(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_stop_post: %s\n" % e
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

# **subscriptions_subscription_id_update_post**
> OkResponse subscriptions_subscription_id_update_post(subscription_id)

Update subscription

Update subscription to latest version

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Update subscription
    api_response = api_instance.subscriptions_subscription_id_update_post(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_update_post: %s\n" % e
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

# **subscriptions_subscription_id_upgrade_post**
> OkResponse subscriptions_subscription_id_upgrade_post(subscription_id, body=body)

Change plan

Upgrade subscription to another variation. In case of upgrade from paid to paid, it's possible to change country without changing payment method. If change is between EU and not EU, different payment rules might apply.

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
body = liveagent_api.Upgrade() # Upgrade |  (optional)

try: 
    # Change plan
    api_response = api_instance.subscriptions_subscription_id_upgrade_post(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_upgrade_post: %s\n" % e
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

# **subscriptions_subscription_id_upgrade_variations_get**
> VariationUpgrades subscriptions_subscription_id_upgrade_variations_get(subscription_id)

Upgrade variation list

List of variations user can upgrade to and their current variation.

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 

try: 
    # Upgrade variation list
    api_response = api_instance.subscriptions_subscription_id_upgrade_variations_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_upgrade_variations_get: %s\n" % e
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

# **subscriptions_subscription_id_usage_put**
> OkResponse subscriptions_subscription_id_usage_put(subscription_id, body=body)

Subscription usage

Get subscription invoices

### Example 
```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = liveagent_api.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
body = liveagent_api.UsageData() # UsageData |  (optional)

try: 
    # Subscription usage
    api_response = api_instance.subscriptions_subscription_id_usage_put(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->subscriptions_subscription_id_usage_put: %s\n" % e
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

