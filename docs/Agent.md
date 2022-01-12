# Agent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**email** | **str** |  | 
**role** | **str** |  | [optional] [default to 'agent']
**avatar_url** | **str** |  | [optional] 
**online_status** | **str** | F - offline, N - online, P - paused, C - mobile  | [optional] 
**status** | **str** | A - active, X - deleted  | [optional] 
**gender** | **str** | M - male, F - female, X - unspecified  | [optional] [default to 'X']
**last_pswd_change** | **datetime** |  | [optional] 
**twofactor_auth** | **str** | Y - active, N - not active  | [optional] [default to 'N']
**voice_status** | **str** | F - Agents are unable to receive calls, however, are able to make calls. N - Agents are able to make and receive calls.  | [optional] 
**sip_phone_id** | **str** |  | [optional] 
**api_phone_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


