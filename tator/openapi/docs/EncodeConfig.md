# EncodeConfig

Settings for archival video encode. Any additional properties will be passed as command line arguments to ffmpeg. If set to null, the raw file will be used (no transcode).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crf** | **int** | Constant rate factor. | [optional] [default to 23]
**preset** | **str** | Preset for ffmpeg encoding. | [optional] [default to 'fast']
**tune** | **str** | Tune setting for ffmpeg. | [optional] [default to 'fastdecode']
**vcodec** | **str** | Video codec. | [optional] [default to 'libx265']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


