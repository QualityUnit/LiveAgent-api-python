# Call

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**ticket_id** | **str** |  | 
**direction** | **str** | incoming call (&#39;in&#39; - default), outgoing call (&#39;out&#39;), internal call(&#39;int&#39;) | [optional] 
**callee_status** | **str** | O - online, F - offline, U - unknown | [optional] 
**ivrs** | [**list[Ivr]**](Ivr.md) |  | [optional] 
**record_call** | **bool** |  | [optional] [default to False]
**reroute_time** | **float** |  | [optional] 
**online_ivr** | **str** | Name of IVR in case the service is online. If empty, call starts ringing to agents | [optional] 
**offline_ivr** | **str** | Name of IVR in case the service is offline. If empty, call hangs up with not available tone | [optional] 
**queue_ivr** | **str** | Name of IVR while waiting in queue. If empty, default in queue music is played | [optional] 
**from_number** | **str** | Caller number | [optional] 
**caller_name** | **str** | Name of the caller in case it is known | [optional] 
**to_number** | **str** | Callee number | [optional] 
**via_number** | **str** | trunk number via which call was made / received (if applicable) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


