# TicketListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**useridentifier** | **str** |  | 
**subject** | **str** |  | 
**departmentid** | **str** |  | 
**recipient** | **str** |  | 
**message** | **str** |  | 
**recipient_name** | **str** |  | [optional] 
**carbon_copy** | **str** |  | [optional] 
**blind_carbon_copy** | **str** |  | [optional] 
**status** | **str** | &lt;br&gt; N - new&lt;br&gt; T - chatting&lt;br&gt; P - calling&lt;br&gt; R - resolved&lt;br&gt; X - deleted&lt;br&gt; B - spam&lt;br&gt; A - answered&lt;br&gt; C - open&lt;br&gt; W - postponed | [optional] [default to 'N']
**mail_message_id** | **str** |  | [optional] 
**do_not_send_mail** | **str** | Y - yes, N - no | [optional] [default to 'N']
**use_template** | **str** | Y - yes, N - no | [optional] [default to 'Y']
**is_html_message** | **str** | Y - yes, N - no | [optional] [default to 'N']
**custom_fields** | [**list[CustomFields]**](CustomFields.md) |  | [optional] 
**tags** | **list[str]** | array of tags id | [optional] 
**attachments** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


