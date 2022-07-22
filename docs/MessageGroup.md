# MessageGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**userid** | **str** |  | [optional] 
**user_full_name** | **str** |  | [optional] 
**type** | **str** | M - OFFLINE_LEGACY C - CHAT P - CALL V - OUTGOING_CALL 1 - INTERNAL_CALL I - INTERNAL U - INTERNAL_OFFLINE Z - INTERNAL_COLLAPSED S - STARTINFO T - TRANSFER R - RESOLVE J - POSTPONE X - DELETE B - SPAM G - TAG F - FACEBOOK W - TWITTER Y - RETWEET A - KNOWLEDGEBASE_START K - KNOWLEDGEBASE O - FORWARD Q - FORWARD_REPLY L - SPLITTED 2 - MERGED 3 - INCOMING_EMAIL 4 - OUTGOING_EMAIL 5 - OFFLINE | [optional] 
**status** | **str** | D - DELETED P - PROMOTED V - VISIBLE S - SPLITTED M - MERGED I - INITIALIZING R - CONNECTING C - CALLING | [optional] 
**datecreated** | **datetime** |  | [optional] 
**datefinished** | **datetime** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**mail_msg_id** | **str** |  | [optional] 
**pop3_msg_id** | **str** |  | [optional] 
**messages** | [**list[Message]**](Message.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


