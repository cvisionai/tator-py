# tator.JobApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_job**](JobApi.md#delete_job) | **DELETE** /rest/Job/{run_uid} | 
[**delete_job_group**](JobApi.md#delete_job_group) | **DELETE** /rest/JobGroup/{group_id} | 

# **delete_job**
> InlineResponse2044 delete_job(run_uid)



Cancel a background job.  Algorithms and transcodes create argo workflows that are annotated with two uuid1 strings, one identifying the run and the other identifying the group. Jobs that are submitted together have the same group id, but each workflow has a unique run id.  This endpoint allows the user to cancel a job using the `run_uid` returned by either the `AlgorithmLaunch` or `Transcode` endpoints.

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
api_instance = tator.JobApi(tator.ApiClient(configuration))
run_uid = 'run_uid_example' # str | A uuid1 string identifying to single Job.

try:
    api_response = api_instance.delete_job(run_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->delete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_uid** | **str**| A uuid1 string identifying to single Job. | 

### Return type

[**InlineResponse2044**](InlineResponse2044.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_group**
> InlineResponse2045 delete_job_group(group_id)



Cancel a group of background jobs.  Algorithms and transcodes create argo workflows that are annotated with two uuid1 strings, one identifying the run and the other identifying the group. Jobs that are submitted together have the same group id, but each workflow has a unique run id.  This endpoint allows the user to cancel a group of jobs using the `group_id`  returned by either the `AlgorithmLaunch` or `Transcode` endpoints.

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
api_instance = tator.JobApi(tator.ApiClient(configuration))
group_id = 'group_id_example' # str | A uuid1 string identifying a group of jobs.

try:
    api_response = api_instance.delete_job_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->delete_job_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A uuid1 string identifying a group of jobs. | 

### Return type

[**InlineResponse2045**](InlineResponse2045.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

