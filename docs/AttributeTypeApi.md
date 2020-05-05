# tator.AttributeTypeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_attribute_type**](AttributeTypeApi.md#create_attribute_type) | **POST** /rest/AttributeTypes/{project} | 
[**delete_attribute_type**](AttributeTypeApi.md#delete_attribute_type) | **DELETE** /rest/AttributeType/{id} | 
[**get_attribute_type**](AttributeTypeApi.md#get_attribute_type) | **GET** /rest/AttributeType/{id} | 
[**get_attribute_type_list**](AttributeTypeApi.md#get_attribute_type_list) | **GET** /rest/AttributeTypes/{project} | 
[**update_attribute_type**](AttributeTypeApi.md#update_attribute_type) | **PATCH** /rest/AttributeType/{id} | 

# **create_attribute_type**
> InlineResponse2011 create_attribute_type(project, body=body)



Create or list attribute types.  Attribute types are used to define data types that describe entities. An attribute may give information about a media, localization, or state entity  in the form of a boolean, integer, float, string, enumeration, datetime,  or geoposition. Besides the data type, attribute types define attribute defaults, bounds, and other constraints.

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
api_instance = tator.AttributeTypeApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body1() # Body1 |  (optional)

try:
    api_response = api_instance.create_attribute_type(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypeApi->create_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attribute_type**
> delete_attribute_type(id)



Interact with an individual attribute type.  Attribute types are used to define data types that describe entities. An attribute may give information about a media, localization, or state entity  in the form of a boolean, integer, float, string, enumeration, datetime,  or geoposition. Besides the data type, attribute types define attribute defaults, bounds, and other constraints.

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
api_instance = tator.AttributeTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an attribute type.

try:
    api_instance.delete_attribute_type(id)
except ApiException as e:
    print("Exception when calling AttributeTypeApi->delete_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an attribute type. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_type**
> Body1 get_attribute_type(id)



Interact with an individual attribute type.  Attribute types are used to define data types that describe entities. An attribute may give information about a media, localization, or state entity  in the form of a boolean, integer, float, string, enumeration, datetime,  or geoposition. Besides the data type, attribute types define attribute defaults, bounds, and other constraints.

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
api_instance = tator.AttributeTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an attribute type.

try:
    api_response = api_instance.get_attribute_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypeApi->get_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an attribute type. | 

### Return type

[**Body1**](Body1.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_type_list**
> list[Object] get_attribute_type_list(project, applies_to=applies_to)



Create or list attribute types.  Attribute types are used to define data types that describe entities. An attribute may give information about a media, localization, or state entity  in the form of a boolean, integer, float, string, enumeration, datetime,  or geoposition. Besides the data type, attribute types define attribute defaults, bounds, and other constraints.

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
api_instance = tator.AttributeTypeApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
applies_to = 56 # int | Unique integer identifying the entity type that this attribute describes. (optional)

try:
    api_response = api_instance.get_attribute_type_list(project, applies_to=applies_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypeApi->get_attribute_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **applies_to** | **int**| Unique integer identifying the entity type that this attribute describes. | [optional] 

### Return type

[**list[Object]**](Object.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute_type**
> InlineResponse2002 update_attribute_type(id, body=body)



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
api_instance = tator.AttributeTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an attribute type.
body = tator.Body2() # Body2 |  (optional)

try:
    api_response = api_instance.update_attribute_type(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypeApi->update_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an attribute type. | 
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

