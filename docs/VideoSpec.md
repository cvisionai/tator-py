# VideoSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | Unique integer identifying a video type. Use -1 to automatically select the video type if only one video type exists in a project. | 
**gid** | **str** | UUID generated for the job group. This value is returned in the response of the &#x60;AlgorithmLaunch&#x60; and &#x60;Transcode&#x60; endpoints. | 
**uid** | **str** | UUID generated for the individual job. This value is returned in the response of the &#x60;AlgorithmLaunch&#x60; and &#x60;Transcode&#x60; endpoints. | 
**media_files** | **list[str]** | Object containing upload urls for the transcoded file and corresponding &#x60;VideoDefinition&#x60;. | 
**thumbnail_url** | **str** | Upload URL for the thumbnail. | 
**thumbnail_gif_url** | **str** | Upload URL for the thumbnail gif. | 
**section** | **str** | Media section name. | 
**name** | **str** | Name of the file. | 
**md5** | **str** | MD5 sum of the media file. | 
**num_frames** | **int** | Number of frames in the video. | 
**fps** | **float** | Frame rate of the video. | 
**codec** | **str** | Codec of the original video. | 
**width** | **int** | Pixel width of the video. | 
**height** | **int** | Pixel height of the video. | 
**progress_name** | **str** | Name to use for progress update. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

