# LineSpec

Single line localization.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frame** | **int** | Frame number of this localization if it is in a video. | 
**media_id** | **int** | Unique integer identifying a media. Required if &#x60;many&#x60; is not given. | 
**modified** | **bool** | Whether this localization was created in the web UI. | [optional] [default to False]
**type** | **int** | Unique integer identifying a localization type.Required if &#x60;many&#x60; is not given. | 
**version** | **int** | Unique integer identifying the version. | [optional] 
**x0** | **float** | Normalized horizontal position of start of line for &#x60;line&#x60; localization types. | 
**x1** | **float** | Normalized horizontal position of end of line for &#x60;line&#x60; localization types. | 
**y0** | **float** | Normalized vertical position of start of line for &#x60;line&#x60; localization types. | 
**y1** | **float** | Normalized vertical position of end of line for &#x60;line&#x60; localization types. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


