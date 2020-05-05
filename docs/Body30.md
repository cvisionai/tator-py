# Body30

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | Unique integer identifying an image type. Use -1 to automatically select the image type if only one image type exists in a project. | 
**gid** | **str** | UUID generated for the job group. This value is returned in the response of the &#x60;AlgorithmLaunch&#x60; and &#x60;Transcode&#x60; endpoints. | 
**uid** | **str** | UUID generated for the individual job. This value is returned in the response of the &#x60;AlgorithmLaunch&#x60; and &#x60;Transcode&#x60; endpoints. | 
**url** | **str** | Upload URL for the image. | 
**thumbnail_url** | **str** | Upload URL for the thumbnail if already generated. | [optional] 
**section** | **str** | Media section name. | 
**name** | **str** | Name of the file. | 
**md5** | **str** | MD5 sum of the media file. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

