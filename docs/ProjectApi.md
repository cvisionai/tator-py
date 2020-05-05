# tator.ProjectApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /rest/Projects | 
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /rest/Project/{id} | 
[**get_project**](ProjectApi.md#get_project) | **GET** /rest/Project/{id} | 
[**get_project_list**](ProjectApi.md#get_project_list) | **GET** /rest/Projects | 
[**update_project**](ProjectApi.md#update_project) | **PATCH** /rest/Project/{id} | 

# **create_project**
> InlineResponse2014 create_project(body=body)



Interact with a list of projects.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Project lists return all projects that the requesting user has access to.

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
api_instance = tator.ProjectApi(tator.ApiClient(configuration))
body = tator.Body16() # Body16 |  (optional)

try:
    api_response = api_instance.create_project(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body16**](Body16.md)|  | [optional] 

### Return type

[**InlineResponse2014**](InlineResponse2014.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(id)



Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.

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
api_instance = tator.ProjectApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a project.

try:
    api_instance.delete_project(id)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a project. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> InlineResponse20021 get_project(id)



Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.

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
api_instance = tator.ProjectApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.get_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a project. | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_list**
> list[InlineResponse20021] get_project_list()



Interact with a list of projects.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Project lists return all projects that the requesting user has access to.

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
api_instance = tator.ProjectApi(tator.ApiClient(configuration))

try:
    api_response = api_instance.get_project_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20021]**](InlineResponse20021.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> InlineResponse20022 update_project(id, body=body)



Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.

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
api_instance = tator.ProjectApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a project.
body = tator.Body17() # Body17 |  (optional)

try:
    api_response = api_instance.update_project(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a project. | 
 **body** | [**Body17**](Body17.md)|  | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

