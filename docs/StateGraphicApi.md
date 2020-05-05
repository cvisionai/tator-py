# tator.StateGraphicApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_state_graphic_api**](StateGraphicApi.md#retrieve_state_graphic_api) | **GET** /rest/StateGraphic/{id} | 

# **retrieve_state_graphic_api**
> str retrieve_state_graphic_api(id, mode=mode, fps=fps, force_scale=force_scale)



Get frame(s) of a given localization-associated state.  Use the mode argument to control whether it is an animated gif or a tiled jpg.

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
api_instance = tator.StateGraphicApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a state.
mode = 'animate' # str | Whether to animate or tile. (optional) (default to animate)
fps = 2 # float | Frame rate if `mode` is `animate`. (optional) (default to 2)
force_scale = 'force_scale_example' # str | wxh to force each tile prior to stich (optional)

try:
    api_response = api_instance.retrieve_state_graphic_api(id, mode=mode, fps=fps, force_scale=force_scale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateGraphicApi->retrieve_state_graphic_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state. | 
 **mode** | **str**| Whether to animate or tile. | [optional] [default to animate]
 **fps** | **float**| Frame rate if &#x60;mode&#x60; is &#x60;animate&#x60;. | [optional] [default to 2]
 **force_scale** | **str**| wxh to force each tile prior to stich | [optional] 

### Return type

**str**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, image/*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

