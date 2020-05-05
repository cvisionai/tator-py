# tator.TreeLeafTypeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tree_leaf_type**](TreeLeafTypeApi.md#create_tree_leaf_type) | **POST** /rest/TreeLeafTypes/{project} | 
[**delete_tree_leaf_type**](TreeLeafTypeApi.md#delete_tree_leaf_type) | **DELETE** /rest/TreeLeafType/{id} | 
[**get_tree_leaf_type**](TreeLeafTypeApi.md#get_tree_leaf_type) | **GET** /rest/TreeLeafType/{id} | 
[**get_tree_leaf_type_list**](TreeLeafTypeApi.md#get_tree_leaf_type_list) | **GET** /rest/TreeLeafTypes/{project} | 
[**update_tree_leaf_type**](TreeLeafTypeApi.md#update_tree_leaf_type) | **PATCH** /rest/TreeLeafType/{id} | 

# **create_tree_leaf_type**
> InlineResponse2018 create_tree_leaf_type(project, body=body)



Interact with tree leaf type list.  A tree leaf type is the metadata definition object for a tree leaf. It includes name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.TreeLeafTypeApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body27() # Body27 |  (optional)

try:
    api_response = api_instance.create_tree_leaf_type(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreeLeafTypeApi->create_tree_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body27**](Body27.md)|  | [optional] 

### Return type

[**InlineResponse2018**](InlineResponse2018.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tree_leaf_type**
> delete_tree_leaf_type(id)



Interact with individual tree leaf type.  A tree leaf type is the metadata definition object for a tree leaf. It includes name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.TreeLeafTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an tree_leaf type.

try:
    api_instance.delete_tree_leaf_type(id)
except ApiException as e:
    print("Exception when calling TreeLeafTypeApi->delete_tree_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an tree_leaf type. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree_leaf_type**
> InlineResponse20035 get_tree_leaf_type(id)



Interact with individual tree leaf type.  A tree leaf type is the metadata definition object for a tree leaf. It includes name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.TreeLeafTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an tree_leaf type.

try:
    api_response = api_instance.get_tree_leaf_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreeLeafTypeApi->get_tree_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an tree_leaf type. | 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree_leaf_type_list**
> list[InlineResponse20034] get_tree_leaf_type_list(project)



Interact with tree leaf type list.  A tree leaf type is the metadata definition object for a tree leaf. It includes name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.TreeLeafTypeApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.get_tree_leaf_type_list(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreeLeafTypeApi->get_tree_leaf_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**list[InlineResponse20034]**](InlineResponse20034.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tree_leaf_type**
> InlineResponse20036 update_tree_leaf_type(id, body=body)



Updates a tree leaf type.

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
api_instance = tator.TreeLeafTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an tree_leaf type.
body = tator.Body28() # Body28 |  (optional)

try:
    api_response = api_instance.update_tree_leaf_type(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreeLeafTypeApi->update_tree_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an tree_leaf type. | 
 **body** | [**Body28**](Body28.md)|  | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

