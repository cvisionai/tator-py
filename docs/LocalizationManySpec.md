# LocalizationManySpec

Many localizations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frame** | **int** | Frame number of this localization if it is in a video. | [optional] 
**many** | [**list[LocalizationProps]**](LocalizationProps.md) | List of localizations if this request is for bulkcreate. | 
**media_id** | **int** | Unique integer identifying a media. Required if &#x60;many&#x60; is not given. | 
**modified** | **bool** | Whether this localization was created in the web UI. | [optional] [default to False]
**type** | **int** | Unique integer identifying a localization type.Required if &#x60;many&#x60; is not given. | 
**version** | **int** | Unique integer identifying the version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


