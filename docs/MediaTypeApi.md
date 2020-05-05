# tator.MediaTypeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_media_type**](MediaTypeApi.md#create_media_type) | **POST** /rest/MediaTypes/{project} | 
[**delete_media_type**](MediaTypeApi.md#delete_media_type) | **DELETE** /rest/MediaType/{id} | 
[**get_media_type**](MediaTypeApi.md#get_media_type) | **GET** /rest/MediaType/{id} | 
[**get_media_type_list**](MediaTypeApi.md#get_media_type_list) | **GET** /rest/MediaTypes/{project} | 
[**update_media_type**](MediaTypeApi.md#update_media_type) | **PATCH** /rest/MediaType/{id} | 

# **create_media_type**
> InlineResponse2011 create_media_type(project, body=body)



Create or retrieve localization types.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.MediaTypeApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body12() # Body12 |  (optional)

try:
    api_response = api_instance.create_media_type(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaTypeApi->create_media_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body12**](Body12.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media_type**
> delete_media_type(id)



Interact with an individual media type.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.MediaTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an media type.

try:
    api_instance.delete_media_type(id)
except ApiException as e:
    print("Exception when calling MediaTypeApi->delete_media_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an media type. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_type**
> InlineResponse20017 get_media_type(id)



Interact with an individual media type.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.MediaTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an media type.

try:
    api_response = api_instance.get_media_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaTypeApi->get_media_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an media type. | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_type_list**
> list[InlineResponse20016] get_media_type_list(project)



Create or retrieve localization types.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.MediaTypeApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.get_media_type_list(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaTypeApi->get_media_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**list[InlineResponse20016]**](InlineResponse20016.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_media_type**
> InlineResponse20018 update_media_type(id, body=body)



Interact with an individual media type.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.MediaTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an media type.
body = tator.Body13() # Body13 |  (optional)

try:
    api_response = api_instance.update_media_type(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaTypeApi->update_media_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an media type. | 
 **body** | [**Body13**](Body13.md)|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

