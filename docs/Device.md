# Device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**agent_id** | **str** |  | 
**phone_id** | **str** |  | [optional] 
**phone** | [**PhoneDevice**](PhoneDevice.md) |  | [optional] 
**type** | **str** | W - WEB A - MOBILE APP E - EXTERNAL (Corresponds to the phone types: SIP, API, PSTN, SIP Provider Extension) | 
**service_type** | **str** | M - MESSAGE T - CHAT P - PHONE | 
**online_status** | **str** | N - ONLINE F - OFFLINE | [optional] [default to 'N']
**preset_status** | **str** | N - ONLINE F - OFFLINE | 
**route_if_offline** | **str** | Y - Yes N - No | [optional] [default to 'Y']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


