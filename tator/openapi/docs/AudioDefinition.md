# AudioDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codec** | **str** | Human readable codec. | 
**codec_description** | **str** | Description other than codec. | [optional] 
**codec_mime** | **str** | Example mime: \&quot;video/mp4; codecs&#x3D;\&quot;avc1.64001e\&quot;\&quot;. Only relevant for streaming files, will assume example above if not present. | [optional] 
**host** | **str** | If supplied will use this instead of currently connected host, e.g. https://example.com | [optional] 
**http_auth** | **str** | If specified will be used for HTTP authorization in request for media, i.e. \&quot;bearer &lt;token&gt;\&quot;. | [optional] 
**path** | **str** | Relative URL to the file. | [optional] 
**url** | **str** | Required when this object is used with the MoveVideo endpoint, this field is the upload URL of the audio file. It is is used for the src path and to create &#x60;path&#x60; field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


