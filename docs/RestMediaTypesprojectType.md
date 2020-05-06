# RestMediaTypesprojectType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the media type. | [optional] [default to '']
**dtype** | **str** | Type of the media, image or video. | [optional] 
**file_format** | **str** | File extension. If omitted, any recognized file extension for the given dtype is accepted for upload. Do not include a dot prefix. | [optional] 
**id** | **int** | Unique integer identifying a media type. | [optional] 
**keep_original** | **bool** | For video dtype, whether to keep the original video file for archival purposes after transcoding. If true, the originally uploaded file will be available for download, otherwise downloads will use the transcoded videos. | [optional] [default to True]
**name** | **str** | Name of the media type. | [optional] 
**resourcetype** | **str** | Type of the media. | [optional] 
**uploadable** | **bool** | Whether this media can be uploaded. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

