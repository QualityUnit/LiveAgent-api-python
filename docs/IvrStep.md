# IvrStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | P - play message (URL in params), R - ring to agent (optional departmentId in params), V - redirect to voicemail, D - choice (choices), G - goto (IVR name in params), T - transfer (optional ivr settings in choices {\&quot;1\&quot;:\&quot;online\&quot;,\&quot;0\&quot;:\&quot;offline\&quot;,\&quot;9\&quot;:\&quot;queue\&quot;}), F - fetch next IVR steps from URL in params, I - wait for DTMF input and then fetch next IVR steps from URL in params, C - request Callback, E - forward to external number | 
**params** | **str** |  | [optional] 
**choices** | [**list[IvrChoice]**](IvrChoice.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


