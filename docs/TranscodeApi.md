# tator.TranscodeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transcode**](TranscodeApi.md#transcode) | **POST** /rest/Transcode/{project} | 

# **transcode**
> InlineResponse20113 transcode(project, body=body)



Start a transcode.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. This endpoint launches a transcode on raw uploaded video by creating an Argo workflow. The workflow will download the uploaded raw video, transcode it to the proper format, upload the transcoded video, and save the video using the  `SaveVideo` endpoint. Optionally, depending on the `keep_original` field of the video  type specified by the `type` parameter, the originally uploaded file may also be saved. Note that the raw video must be uploaded first via tus, which is a separate mechanism  from the REST API. This endpoint requires a group and run UUID associated with this  upload. If no progress messages were generated during upload, then the group and run  UUIDs can be newly generated.

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
api_instance = tator.TranscodeApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body41() # Body41 |  (optional)

try:
    api_response = api_instance.transcode(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranscodeApi->transcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body41**](Body41.md)|  | [optional] 

### Return type

[**InlineResponse20113**](InlineResponse20113.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

