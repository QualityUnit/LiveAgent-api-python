# BillingStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | N - No billing\nA - Billing active\nS &#x3D; Billing stopped\n | [optional] 
**valid_to_date** | **datetime** |  | [optional] 
**next_billing_date** | **datetime** |  | [optional] 
**errors** | **int** | Number of charge errors since last successful billing or account unsuspend. | [optional] 
**last_error_date** | **datetime** | Time an date of the last failed charge attempt. Only present if number or errors is greater than 0. | [optional] 
**payment_compatible** | **bool** | True if used payment method is fully compatible with selected country, false otherwise. False when either payment method or country is not set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


