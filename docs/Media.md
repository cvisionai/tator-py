# Media

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **dict(str, object)** | Object containing attribute values. | [optional] 
**codec** | **str** | Codec for videos. | [optional] 
**created_by** | **int** | Unique integer identifying user who created this media. | [optional] 
**created_datetime** | **str** | Datetime when this media was created. | [optional] 
**file** | **str** | URL of the media file. Relative to https://&lt;domain&gt;/media/. | [optional] 
**fps** | **int** | Frame rate for videos. | [optional] 
**height** | **int** | Vertical resolution in pixels. | [optional] 
**id** | **int** | Unique integer identifying this media. | [optional] 
**last_edit_end** | **datetime** | Datetime of the end of the session when this media or its annotations were last edited. | [optional] 
**last_edit_start** | **datetime** | Datetime of the start of the session when this media or its annotations were last edited. | [optional] 
**md5** | **str** | MD5 checksum of the media file. | [optional] 
**media_files** | **list[str]** | Object containing upload urls for the transcoded file and corresponding &#x60;VideoDefinition&#x60;. | [optional] 
**meta** | **int** | Unique integer identifying entity type of this media. | [optional] 
**modified_by** | **int** | Unique integer identifying user who last modified this media. | [optional] 
**modified_datetime** | **str** | Datetime when this media was last modified. | [optional] 
**name** | **str** | Name of the media. | [optional] 
**num_frames** | **int** | Number of frames for videos. | [optional] 
**original** | **str** | DEPRECATED. Use media_files. Stores path to original media file. | [optional] 
**project** | **int** | Unique integer identifying project of this media. | [optional] 
**segment_info** | **str** | Path to segment info. | [optional] 
**thumbnail** | **str** | URL of the thumbnail. Relative to https://&lt;domain&gt;/media/. | [optional] 
**thumbnail_gif** | **str** | URL of the thumbnail gif for videos. Relative to https://&lt;domain&gt;/media/. | [optional] 
**width** | **int** | Horizontal resolution in pixels. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

