# Body41

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | Unique integer identifying a video type. | 
**gid** | **str** | UUID generated for the job group. This value may be associated with messages generated during upload via the &#x60;Progress&#x60; endpoint, or it may be newly generated. The transcode workflow will use this value to generate progress messages. | 
**uid** | **str** | UUID generated for the individual job. This value may be associated with messages generated during upload via the &#x60;Progress&#x60; endpoint, or it may be newly generated. The transcode workflow will use this value to generate progress messages. | 
**url** | **str** | Upload URL for the raw video. | 
**section** | **str** | Media section name to upload to. | 
**name** | **str** | Name of the file. | 
**md5** | **str** | MD5 sum of the media file. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

