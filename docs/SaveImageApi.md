# tator.SaveImageApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**save_image**](SaveImageApi.md#save_image) | **POST** /rest/SaveImage/{project} | 

# **save_image**
> InlineResponse20111 save_image(project, body=body)



Saves an uploaded image.  Media is uploaded via tus, a separate mechanism from the REST API. Once an image upload is complete, the image must be saved to the database using this endpoint.

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
api_instance = tator.SaveImageApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body38() # Body38 |  (optional)

try:
    api_response = api_instance.save_image(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaveImageApi->save_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body38**](Body38.md)|  | [optional] 

### Return type

[**InlineResponse20111**](InlineResponse20111.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

