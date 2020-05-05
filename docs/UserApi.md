# tator.UserApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user**](UserApi.md#get_user) | **GET** /rest/User/{id} | 
[**update_user**](UserApi.md#update_user) | **PATCH** /rest/User/{id} | 
[**who_am_i**](UserApi.md#who_am_i) | **GET** /rest/User/GetCurrent | 

# **get_user**
> InlineResponse20037 get_user(id)



Interact with an individual user.

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
api_instance = tator.UserApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a localization association.

try:
    api_response = api_instance.get_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization association. | 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> InlineResponse20037 update_user(id, body=body)



Interact with an individual user.

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
api_instance = tator.UserApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a localization association.
body = tator.Body29() # Body29 |  (optional)

try:
    api_response = api_instance.update_user(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization association. | 
 **body** | [**Body29**](Body29.md)|  | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **who_am_i**
> InlineResponse20038 who_am_i()



Returns the current user.  This is the equivalent of a whoami() operation.

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
api_instance = tator.UserApi(tator.ApiClient(configuration))

try:
    api_response = api_instance.who_am_i()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->who_am_i: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

