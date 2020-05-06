# Body10

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | UUID generated for the job group. This value is returned in the response of the &#x60;AlgorithmLaunch&#x60; and &#x60;Transcode&#x60; endpoints. | 
**job_type** | **str** | Type of background job. | 
**media_ids** | **str** | Comma separated string of media ids, one for each media that this job applies to. Required only for &#x60;job_type&#x60; of &#x60;algorithm&#x60;. | [optional] 
**message** | **str** | Progress message. This should be short to fit in the UI. | 
**name** | **str** | Name of the job. | 
**progress** | **float** | Progress percent completion. This is used to display the progress bar associated with the job. | 
**section** | **str** | Media section name. Required only for &#x60;job_type&#x60; of &#x60;upload&#x60;. | [optional] 
**sections** | **str** | Comma separated string of media sections, one for each media ID that this job applies to. Required only for &#x60;job_type&#x60; of &#x60;algorithm&#x60;. | [optional] 
**state** | **str** | State of the job. | 
**swid** | **str** | UUID generated for the service worker that is doing an upload. This field is required if the &#x60;job_type&#x60; is &#x60;upload&#x60;. | [optional] 
**uid** | **str** | UUID generated for the individual job. This value is returned in the response of the &#x60;AlgorithmLaunch&#x60; and &#x60;Transcode&#x60; endpoints. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

