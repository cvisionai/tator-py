# tator.FrameAssociationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_frame_association**](FrameAssociationApi.md#delete_frame_association) | **DELETE** /rest/FrameAssociation/{id} | 
[**get_frame_association**](FrameAssociationApi.md#get_frame_association) | **GET** /rest/FrameAssociation/{id} | 
[**update_frame_association**](FrameAssociationApi.md#update_frame_association) | **PATCH** /rest/FrameAssociation/{id} | 

# **delete_frame_association**
> delete_frame_association(id)



Modify a frame association.  Frame associations specify which frames that a `State` object applies to.

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
api_instance = tator.FrameAssociationApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a frame association.

try:
    api_instance.delete_frame_association(id)
except ApiException as e:
    print("Exception when calling FrameAssociationApi->delete_frame_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a frame association. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_frame_association**
> dict(str, object) get_frame_association(id)



Modify a frame association.  Frame associations specify which frames that a `State` object applies to.

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
api_instance = tator.FrameAssociationApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a frame association.

try:
    api_response = api_instance.get_frame_association(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FrameAssociationApi->get_frame_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a frame association. | 

### Return type

**dict(str, object)**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_frame_association**
> InlineResponse2004 update_frame_association(id, body=body)



Modify a frame association.  Frame associations specify which frames that a `State` object applies to.

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
api_instance = tator.FrameAssociationApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a frame association.
body = tator.Body3() # Body3 |  (optional)

try:
    api_response = api_instance.update_frame_association(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FrameAssociationApi->update_frame_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a frame association. | 
 **body** | [**Body3**](Body3.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

