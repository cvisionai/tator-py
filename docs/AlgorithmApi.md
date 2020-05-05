# tator.AlgorithmApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**algorithm_launch**](AlgorithmApi.md#algorithm_launch) | **POST** /rest/AlgorithmLaunch/{project} | 
[**get_algorithm_list**](AlgorithmApi.md#get_algorithm_list) | **GET** /rest/Algorithms/{project} | 

# **algorithm_launch**
> InlineResponse20110 algorithm_launch(project, body=body)



Start an algorithm.  This will create one or more Argo workflows that execute the named algorithm registration. To get a list of available algorithms, use the `Algorithms` endpoint. A media list will be submitted for processing using either a query string or  a list of media IDs. If neither are included, the algorithm will be launched on all media in the project.   Media is divided into batches for based on the `files_per_job` field of the  `Algorithm` object. One batch is submitted to each Argo workflow.  Submitted algorithm jobs may be cancelled via the `Job` or `JobGroup` endpoints.

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
api_instance = tator.AlgorithmApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body35() # Body35 |  (optional)

try:
    api_response = api_instance.algorithm_launch(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlgorithmApi->algorithm_launch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body35**](Body35.md)|  | [optional] 

### Return type

[**InlineResponse20110**](InlineResponse20110.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_algorithm_list**
> list[InlineResponse200] get_algorithm_list(project)



Interact with algorithms that have been registered to a project.  For instructions on how to register an algorithm, visit `GitHub`_.  .. _GitHub:    https://github.com/cvisionai/tator/tree/master/examples/algorithms

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
api_instance = tator.AlgorithmApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.get_algorithm_list(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlgorithmApi->get_algorithm_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

