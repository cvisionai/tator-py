# tator.TemporaryFileApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_temporary_file**](TemporaryFileApi.md#create_temporary_file) | **POST** /rest/TemporaryFiles/{project} | 
[**delete_temporary_file**](TemporaryFileApi.md#delete_temporary_file) | **DELETE** /rest/TemporaryFile/{id} | 
[**delete_temporary_file_list**](TemporaryFileApi.md#delete_temporary_file_list) | **DELETE** /rest/TemporaryFiles/{project} | 
[**get_temporary_file**](TemporaryFileApi.md#get_temporary_file) | **GET** /rest/TemporaryFile/{id} | 
[**get_temporary_file_list**](TemporaryFileApi.md#get_temporary_file_list) | **GET** /rest/TemporaryFiles/{project} | 

# **create_temporary_file**
> InlineResponse20029 create_temporary_file(project, body=body)



Interact with temporary file list.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

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
api_instance = tator.TemporaryFileApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body23() # Body23 |  (optional)

try:
    api_response = api_instance.create_temporary_file(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemporaryFileApi->create_temporary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body23**](Body23.md)|  | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_temporary_file**
> delete_temporary_file(id)



Interact with temporary file.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

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
api_instance = tator.TemporaryFileApi(tator.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this temporary file.

try:
    api_instance.delete_temporary_file(id)
except ApiException as e:
    print("Exception when calling TemporaryFileApi->delete_temporary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this temporary file. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_temporary_file_list**
> delete_temporary_file_list(project, expired=expired)



Interact with temporary file list.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

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
api_instance = tator.TemporaryFileApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
expired = 0 # int | If greater than 0 will return only expired files (optional) (default to 0)

try:
    api_instance.delete_temporary_file_list(project, expired=expired)
except ApiException as e:
    print("Exception when calling TemporaryFileApi->delete_temporary_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **expired** | **int**| If greater than 0 will return only expired files | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_file**
> InlineResponse20029 get_temporary_file(id)



Interact with temporary file.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

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
api_instance = tator.TemporaryFileApi(tator.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this temporary file.

try:
    api_response = api_instance.get_temporary_file(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemporaryFileApi->get_temporary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this temporary file. | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_file_list**
> InlineResponse20029 get_temporary_file_list(project, expired=expired)



Interact with temporary file list.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

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
api_instance = tator.TemporaryFileApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
expired = 0 # int | If greater than 0 will return only expired files (optional) (default to 0)

try:
    api_response = api_instance.get_temporary_file_list(project, expired=expired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemporaryFileApi->get_temporary_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **expired** | **int**| If greater than 0 will return only expired files | [optional] [default to 0]

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

