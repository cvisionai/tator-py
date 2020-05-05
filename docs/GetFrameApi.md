# tator.GetFrameApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_get_frame_api**](GetFrameApi.md#retrieve_get_frame_api) | **GET** /rest/GetFrame/{id} | 

# **retrieve_get_frame_api**
> str retrieve_get_frame_api(id, frames=frames, tile=tile, roi=roi, animate=animate, quality=quality)



Facility to get a frame(jpg/png) of a given video frame, returns a square tile of frames based on the input parameter

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
api_instance = tator.GetFrameApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a media object.
frames = [[0]] # list[int] | Comma-seperated list of frames to capture. (optional) (default to [0])
tile = 'tile_example' # str | wxh, if not supplied is made as squarish as possible. (optional)
roi = 'roi_example' # str | w:h:x:y, optionally crop each frame to a given roi in relative coordinates. (optional)
animate = 56 # int | If not tiling, animate each frame at a given fps in a gif. (optional)
quality = 56 # int | Source resolution to use (default to highest quality) (optional)

try:
    api_response = api_instance.retrieve_get_frame_api(id, frames=frames, tile=tile, roi=roi, animate=animate, quality=quality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetFrameApi->retrieve_get_frame_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media object. | 
 **frames** | [**list[int]**](int.md)| Comma-seperated list of frames to capture. | [optional] [default to [0]]
 **tile** | **str**| wxh, if not supplied is made as squarish as possible. | [optional] 
 **roi** | **str**| w:h:x:y, optionally crop each frame to a given roi in relative coordinates. | [optional] 
 **animate** | **int**| If not tiling, animate each frame at a given fps in a gif. | [optional] 
 **quality** | **int**| Source resolution to use (default to highest quality) | [optional] 

### Return type

**str**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

