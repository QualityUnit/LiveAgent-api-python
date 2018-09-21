# Message

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**userid** | **str** |  | [optional] 
**type** | **str** | M - MESSAGE Y - MESSAGE_LEGACY Q - QUOTED_TEXT I - INTERNAL F - FILE T - TITLE E - END D - DISCONNECT H - HEADER R - TRANSFER S - SYSTEM U - USERAGENT G - TAG V - VOICE 1 - VOICE_INTERNAL N - NOTE L - NOTE_FILE Z - FORMFIELD A - TEXT_HEADER O - TEXT_FOOTER J - STATUS B - SPLITTED W - RANKING_FEATURE_REWARD P - RANKING_FEATURE_PUNISHMENT C - RANKING_FEATURE_COMMENT K - SYSTEM_PUBLIC X - SYSTEM_VISITOR 0 - ERROR_FOOTER 2 - MERGED 3 - INVITATION_REROUTE | [optional] 
**datecreated** | **datetime** |  | [optional] 
**format** | **str** | T - TEXT H - HTML J - JSON X - TEXT_LEGACY // text with possibility of internal form links (e.g. note, ranking comment, quoted, header, footer, internal) Y - HTML_LEGACY // html with possibility of internal form links (e.g. tag) Z - JSON_LEGACY // json with possibility of internal form links (e.g. footer) | [optional] 
**message** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


