# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**created_date** | **datetime** | Invoice issued date | [optional] 
**from_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 
**paid_date** | **datetime** |  | [optional] 
**price** | **float** |  | [optional] 
**price_billed** | **float** |  | [optional] 
**vat_rate** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**items** | [**list[InvoiceItem]**](InvoiceItem.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


