# tator.ProgressApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**progress**](ProgressApi.md#progress) | **POST** /rest/Progress/{project} | 

# **progress**
> InlineResponse20042 progress(project, body=body)



Broadcast progress update.  Progress messages are sent in the web UI via WebSocket, and are displayed as progress bars associated with individual media files and as a summary in the webpage header. All members of a project can see progress bars from uploads and background jobs initiated by other users within the project. This endpoint accepts an array of messages, allowing for progress messages to be batched into a single request.

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
api_instance = tator.ProgressApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = [tator.Body37()] # list[Body37] |  (optional)

try:
    api_response = api_instance.progress(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgressApi->progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**list[Body37]**](Body37.md)|  | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

