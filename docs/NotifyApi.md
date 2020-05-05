# tator.NotifyApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notify**](NotifyApi.md#notify) | **POST** /rest/Notify | 

# **notify**
> notify(body=body)



Send a notification to administrators.  Uses the Slack API to send a notification to system administrators. This endpoint can only be used by system administrators and must be configured in a Tator deployment's settings.

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
api_instance = tator.NotifyApi(tator.ApiClient(configuration))
body = tator.Body36() # Body36 |  (optional)

try:
    api_instance.notify(body=body)
except ApiException as e:
    print("Exception when calling NotifyApi->notify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body36**](Body36.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

