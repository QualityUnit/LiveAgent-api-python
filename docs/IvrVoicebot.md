# IvrVoicebot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot** | **str** | ID of the voice AI agent | 
**budget** | **str** | ID of the AI budget the conversation is paid from | 
**handoff** | [**list[IvrVoicebotHandoff]**](IvrVoicebotHandoff.md) | Handoff targets the bot can choose from, with the IVR each one continues in | [optional] 
**escape_key** | **str** | DTMF key the caller presses to leave the bot for the default handoff target | [optional] 
**max_duration** | **int** | Seconds after which the bot hands off to the default handoff target | [optional] 
**on_error** | **str** | Name of IVR to continue in when the bot fails | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


