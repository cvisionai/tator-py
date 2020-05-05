# tator.TokenApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_obtain_auth_token**](TokenApi.md#create_obtain_auth_token) | **POST** /rest/Token | 

# **create_obtain_auth_token**
> InlineResponse20041 create_obtain_auth_token(body=body)



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
api_instance = tator.TokenApi(tator.ApiClient(configuration))
body = tator.Body34() # Body34 |  (optional)

try:
    api_response = api_instance.create_obtain_auth_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->create_obtain_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body34**](Body34.md)|  | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

