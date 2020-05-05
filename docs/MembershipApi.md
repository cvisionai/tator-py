# tator.MembershipApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_membership**](MembershipApi.md#create_membership) | **POST** /rest/Memberships/{project} | 
[**delete_membership**](MembershipApi.md#delete_membership) | **DELETE** /rest/Membership/{id} | 
[**get_membership**](MembershipApi.md#get_membership) | **GET** /rest/Membership/{id} | 
[**get_membership_list**](MembershipApi.md#get_membership_list) | **GET** /rest/Memberships/{project} | 
[**update_membership**](MembershipApi.md#update_membership) | **PATCH** /rest/Membership/{id} | 

# **create_membership**
> InlineResponse2013 create_membership(project, body=body)



Create or retrieve a list of project memberships.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels. `View Only` can only view a project and not change any data. `Can Edit` can create, modify, and delete annotations. `Can Transfer` can upload and download media. `Can Execute` can launch algorithm workflows. `Full Control` can change project settings, including inviting new members, project name, and project metadata schema.

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
api_instance = tator.MembershipApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body14() # Body14 |  (optional)

try:
    api_response = api_instance.create_membership(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MembershipApi->create_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body14**](Body14.md)|  | [optional] 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_membership**
> delete_membership(id)



Interact with an individual project membership.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels. `View Only` can only view a project and not change any data. `Can Edit` can create, modify, and delete annotations. `Can Transfer` can upload and download media. `Can Execute` can launch algorithm workflows. `Full Control` can change project settings, including inviting new members, project name, and project metadata schema.

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
api_instance = tator.MembershipApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a membership.

try:
    api_instance.delete_membership(id)
except ApiException as e:
    print("Exception when calling MembershipApi->delete_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a membership. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership**
> InlineResponse20019 get_membership(id)



Interact with an individual project membership.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels. `View Only` can only view a project and not change any data. `Can Edit` can create, modify, and delete annotations. `Can Transfer` can upload and download media. `Can Execute` can launch algorithm workflows. `Full Control` can change project settings, including inviting new members, project name, and project metadata schema.

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
api_instance = tator.MembershipApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a membership.

try:
    api_response = api_instance.get_membership(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MembershipApi->get_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a membership. | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership_list**
> list[InlineResponse20019] get_membership_list(project)



Create or retrieve a list of project memberships.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels. `View Only` can only view a project and not change any data. `Can Edit` can create, modify, and delete annotations. `Can Transfer` can upload and download media. `Can Execute` can launch algorithm workflows. `Full Control` can change project settings, including inviting new members, project name, and project metadata schema.

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
api_instance = tator.MembershipApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.get_membership_list(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MembershipApi->get_membership_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**list[InlineResponse20019]**](InlineResponse20019.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_membership**
> InlineResponse20020 update_membership(id, body=body)



Interact with an individual project membership.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels. `View Only` can only view a project and not change any data. `Can Edit` can create, modify, and delete annotations. `Can Transfer` can upload and download media. `Can Execute` can launch algorithm workflows. `Full Control` can change project settings, including inviting new members, project name, and project metadata schema.

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
api_instance = tator.MembershipApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a membership.
body = tator.Body15() # Body15 |  (optional)

try:
    api_response = api_instance.update_membership(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MembershipApi->update_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a membership. | 
 **body** | [**Body15**](Body15.md)|  | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

