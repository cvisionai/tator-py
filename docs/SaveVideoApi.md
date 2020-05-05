# tator.SaveVideoApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**partial_update_save_video_api**](SaveVideoApi.md#partial_update_save_video_api) | **PATCH** /rest/SaveVideo/{project} | 
[**save_video**](SaveVideoApi.md#save_video) | **POST** /rest/SaveVideo/{project} | 

# **partial_update_save_video_api**
> partial_update_save_video_api(project, body=body)



Saves a transcoded video.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. To launch a transcode on raw uploaded video, use the  `Transcode` endpoint, which will create an Argo workflow to perform the transcode and save the video using this endpoint; no further REST calls are required. However, if you would like to perform transcodes locally, this endpoint enables that. The script at `scripts/transcoder/transcodePipeline.py` in the Tator source code provides an example of how to transcode a Tator-compatible video, upload it, and save it to the database using this endpoint.

### Example
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuth
configuration = tator.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = tator.SaveVideoApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body40() # Body40 |  (optional)

try:
    api_instance.partial_update_save_video_api(project, body=body)
except ApiException as e:
    print("Exception when calling SaveVideoApi->partial_update_save_video_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body40**](Body40.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_video**
> InlineResponse20112 save_video(project, body=body)



Saves a transcoded video.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. To launch a transcode on raw uploaded video, use the  `Transcode` endpoint, which will create an Argo workflow to perform the transcode and save the video using this endpoint; no further REST calls are required. However, if you would like to perform transcodes locally, this endpoint enables that. The script at `scripts/transcoder/transcodePipeline.py` in the Tator source code provides an example of how to transcode a Tator-compatible video, upload it, and save it to the database using this endpoint.

### Example
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuth
configuration = tator.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = tator.SaveVideoApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body39() # Body39 |  (optional)

try:
    api_response = api_instance.save_video(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaveVideoApi->save_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body39**](Body39.md)|  | [optional] 

### Return type

[**InlineResponse20112**](InlineResponse20112.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

