# tator.AnalysisApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_analysis**](AnalysisApi.md#create_analysis) | **POST** /rest/Analyses/{project} | 
[**get_analysis_list**](AnalysisApi.md#get_analysis_list) | **GET** /rest/Analyses/{project} | 

# **create_analysis**
> InlineResponse201 create_analysis(project, body=body)



Create analysis for a project.  Analysis objects are used to display information about filtered media lists and/or annotations on the project detail page of the web UI. Currently only counting analysis is supported.

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
api_instance = tator.AnalysisApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body() # Body |  (optional)

try:
    api_response = api_instance.create_analysis(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->create_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_list**
> list[InlineResponse2001] get_analysis_list(project)



List analyses for a project.  Analysis objects are used to display information about filtered media lists and/or annotations on the project detail page of the web UI. Currently only counting analysis is supported.

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
api_instance = tator.AnalysisApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.get_analysis_list(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->get_analysis_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

