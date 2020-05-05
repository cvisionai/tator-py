# tator.GetClipApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_get_clip_api**](GetClipApi.md#retrieve_get_clip_api) | **GET** /rest/GetClip/{id} | 

# **retrieve_get_clip_api**
> str retrieve_get_clip_api(id, frame_ranges, quality=quality)



Facility to get a clip from the server. Returns a temporary file object that expires in 24 hours.

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
api_instance = tator.GetClipApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a media object.
frame_ranges = ['frame_ranges_example'] # list[str] | Comma-seperated list of frame ranges to capture.
quality = 56 # int | Source resolution to use (default to highest quality) (optional)

try:
    api_response = api_instance.retrieve_get_clip_api(id, frame_ranges, quality=quality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetClipApi->retrieve_get_clip_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media object. | 
 **frame_ranges** | [**list[str]**](str.md)| Comma-seperated list of frame ranges to capture. | 
 **quality** | **int**| Source resolution to use (default to highest quality) | [optional] 

### Return type

**str**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, video/*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

