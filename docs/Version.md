# Version

Version object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bases** | **list[int]** | Array of other version IDs that are dependencies of this version. | [optional] 
**created_by** | **str** | Name of user who created the last unmodified annotation in this version. | [optional] 
**created_datetime** | **str** | Datetime when the last unmodified annotation was created. | [optional] 
**description** | **str** | Description of the version. | [optional] [default to '']
**id** | **int** | Unique integer identifying a membership. | [optional] 
**modified_by** | **str** | Name of user who modified annotations in this version most recently. | [optional] 
**modified_datetime** | **str** | Datetime when last annotation was modified in the web interface. | [optional] 
**name** | **str** | Name of the version. | [optional] 
**num_created** | **int** | Number of created annotations in this version. | [optional] 
**num_modified** | **int** | Number of modified annotations in this version. | [optional] 
**number** | **int** | Version number. | [optional] 
**project** | **int** | Unique integer identifying a project. | [optional] 
**show_empty** | **bool** | Whether to show this version on media for which no annotations exist. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


