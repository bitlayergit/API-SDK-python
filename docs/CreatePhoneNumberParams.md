# CreatePhoneNumberParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **object** | Phone number | [optional] 
**route** | **object** | Route lookup object | [optional] 
**name** | **str** | Phone Name | [optional] 
**block_incoming** | **bool** | Block incoming calls | [optional] 
**block_anonymous** | **bool** | Block anonymous calls | [optional] 
**caller_id_name** | **str** | Caller ID name | [optional] 
**caller_id_type** | **str** | Caller ID type | [optional] 
**sms_forwarding_type** | **str** | &#39;application&#39; or &#39;extension&#39; | [optional] 
**sms_forwarding_application** | **object** | Application lookup object | [optional] 
**sms_forwarding_extension** | **object** | Extension lookup object | [optional] 
**call_notifications_emails** | **list[str]** | Call notifications for emails. Can be a single email or an array of emails | [optional] 
**call_notifications_sms** | **str** | Call notification for SMS | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

