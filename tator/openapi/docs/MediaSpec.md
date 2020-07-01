# MediaSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | UUID corresponding to a group of uploads if this is an image type. | [optional] 
**md5** | **str** | MD5 sum of the media file. | 
**name** | **str** | Name of the file. | 
**progress_name** | **str** | Replaces name in progress message. | [optional] 
**section** | **str** | Media section name. | 
**thumbnail_url** | **str** | Upload URL for the image thumbnail if already generated. If not an image, this field is ignored. | [optional] 
**type** | **int** | Unique integer identifying a media type. Use -1 to automatically select the media type if only one media type exists in a project. | 
**uid** | **str** | UUID corresponding to an upload if this is an image type. | [optional] 
**url** | **str** | Upload URL for the image if this is an image type. If not an image, this field is ignored. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


