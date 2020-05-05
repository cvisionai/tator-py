# tator.LocalizationTypeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_localization_type**](LocalizationTypeApi.md#create_localization_type) | **POST** /rest/LocalizationTypes/{project} | 
[**delete_localization_type**](LocalizationTypeApi.md#delete_localization_type) | **DELETE** /rest/LocalizationType/{id} | 
[**get_localization_type**](LocalizationTypeApi.md#get_localization_type) | **GET** /rest/LocalizationType/{id} | 
[**get_localization_type_list**](LocalizationTypeApi.md#get_localization_type_list) | **GET** /rest/LocalizationTypes/{project} | 
[**update_localization_type**](LocalizationTypeApi.md#update_localization_type) | **PATCH** /rest/LocalizationType/{id} | 

# **create_localization_type**
> InlineResponse2011 create_localization_type(project, body=body)



Create or retrieve localization types.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.LocalizationTypeApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body8() # Body8 |  (optional)

try:
    api_response = api_instance.create_localization_type(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationTypeApi->create_localization_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body8**](Body8.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization_type**
> delete_localization_type(id)



Interact with an individual localization type.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.LocalizationTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an localization type.

try:
    api_instance.delete_localization_type(id)
except ApiException as e:
    print("Exception when calling LocalizationTypeApi->delete_localization_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an localization type. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_type**
> InlineResponse2009 get_localization_type(id)



Interact with an individual localization type.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.LocalizationTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an localization type.

try:
    api_response = api_instance.get_localization_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationTypeApi->get_localization_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an localization type. | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_type_list**
> list[InlineResponse2008] get_localization_type_list(project, media_id=media_id, type=type)



Create or retrieve localization types.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.LocalizationTypeApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
media_id = [56] # list[int] | List of unique integers identifying a media. (optional)
type = 56 # int | Deprecated. Use `LocalizationType` endpoint to retrieve individual localization type by ID. (optional)

try:
    api_response = api_instance.get_localization_type_list(project, media_id=media_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationTypeApi->get_localization_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_id** | [**list[int]**](int.md)| List of unique integers identifying a media. | [optional] 
 **type** | **int**| Deprecated. Use &#x60;LocalizationType&#x60; endpoint to retrieve individual localization type by ID. | [optional] 

### Return type

[**list[InlineResponse2008]**](InlineResponse2008.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization_type**
> InlineResponse20010 update_localization_type(id, body=body)



Updates a localization type.

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
api_instance = tator.LocalizationTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an localization type.
body = tator.Body9() # Body9 |  (optional)

try:
    api_response = api_instance.update_localization_type(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationTypeApi->update_localization_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an localization type. | 
 **body** | [**Body9**](Body9.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

