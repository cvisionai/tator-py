# tator.StateTypeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_state_type**](StateTypeApi.md#create_state_type) | **POST** /rest/StateTypes/{project} | 
[**delete_state_type**](StateTypeApi.md#delete_state_type) | **DELETE** /rest/StateType/{id} | 
[**get_state_type**](StateTypeApi.md#get_state_type) | **GET** /rest/StateType/{id} | 
[**get_state_type_list**](StateTypeApi.md#get_state_type_list) | **GET** /rest/StateTypes/{project} | 
[**update_state_type**](StateTypeApi.md#update_state_type) | **PATCH** /rest/StateType/{id} | 

# **create_state_type**
> InlineResponse2016 create_state_type(project, body=body)



Create or retrieve state types.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.StateTypeApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body21() # Body21 |  (optional)

try:
    api_response = api_instance.create_state_type(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateTypeApi->create_state_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body21**](Body21.md)|  | [optional] 

### Return type

[**InlineResponse2016**](InlineResponse2016.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state_type**
> delete_state_type(id)



Interact with an individual state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.StateTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a state type.

try:
    api_instance.delete_state_type(id)
except ApiException as e:
    print("Exception when calling StateTypeApi->delete_state_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state type. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_type**
> InlineResponse20027 get_state_type(id)



Interact with an individual state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.StateTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a state type.

try:
    api_response = api_instance.get_state_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateTypeApi->get_state_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state type. | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_type_list**
> list[InlineResponse20026] get_state_type_list(project, media_id=media_id, type=type)



Create or retrieve state types.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.StateTypeApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
media_id = [56] # list[int] | List of unique integers identifying a media. (optional)
type = 56 # int | Deprecated. Use `LocalizationType` endpoint to retrieve individual localization type by ID. (optional)

try:
    api_response = api_instance.get_state_type_list(project, media_id=media_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateTypeApi->get_state_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_id** | [**list[int]**](int.md)| List of unique integers identifying a media. | [optional] 
 **type** | **int**| Deprecated. Use &#x60;LocalizationType&#x60; endpoint to retrieve individual localization type by ID. | [optional] 

### Return type

[**list[InlineResponse20026]**](InlineResponse20026.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_state_type**
> InlineResponse20028 update_state_type(id, body=body)



Interact with an individual state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.StateTypeApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a state type.
body = tator.Body22() # Body22 |  (optional)

try:
    api_response = api_instance.update_state_type(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateTypeApi->update_state_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state type. | 
 **body** | [**Body22**](Body22.md)|  | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

