# tator.TreeLeafApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tree_leaf**](TreeLeafApi.md#create_tree_leaf) | **POST** /rest/TreeLeaves/{project} | 
[**delete_tree_leaf**](TreeLeafApi.md#delete_tree_leaf) | **DELETE** /rest/TreeLeaf/{id} | 
[**delete_tree_leaf_list**](TreeLeafApi.md#delete_tree_leaf_list) | **DELETE** /rest/TreeLeaves/{project} | 
[**get_tree_leaf**](TreeLeafApi.md#get_tree_leaf) | **GET** /rest/TreeLeaf/{id} | 
[**get_tree_leaf_list**](TreeLeafApi.md#get_tree_leaf_list) | **GET** /rest/TreeLeaves/{project} | 
[**tree_leaf_suggestion**](TreeLeafApi.md#tree_leaf_suggestion) | **GET** /rest/TreeLeaves/Suggestion/{ancestor}/{project} | 
[**update_tree_leaf**](TreeLeafApi.md#update_tree_leaf) | **PATCH** /rest/TreeLeaf/{id} | 
[**update_tree_leaf_list**](TreeLeafApi.md#update_tree_leaf_list) | **PATCH** /rest/TreeLeaves/{project} | 

# **create_tree_leaf**
> InlineResponse2017 create_tree_leaf(project, body=body)



Interact with a list of tree leaves.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

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
api_instance = tator.TreeLeafApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = NULL # dict(str, object) |  (optional)

try:
    api_response = api_instance.create_tree_leaf(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreeLeafApi->create_tree_leaf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

[**InlineResponse2017**](InlineResponse2017.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tree_leaf**
> delete_tree_leaf(id)



Interact with individual tree leaf.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

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
api_instance = tator.TreeLeafApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a tree leaf.

try:
    api_instance.delete_tree_leaf(id)
except ApiException as e:
    print("Exception when calling TreeLeafApi->delete_tree_leaf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a tree leaf. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tree_leaf_list**
> InlineResponse2043 delete_tree_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with a list of tree leaves.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

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
api_instance = tator.TreeLeafApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
ancestor = 'ancestor_example' # str | Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia). (optional)
type = 56 # int | Unique integer identifying a tree leaf type. (optional)
name = 'name_example' # str | Name of the tree leaf element. (optional)
attribute = 'attribute_example' # str | Attribute equality filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_lt = 'attribute_lt_example' # str | Attribute less than filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_lte = 'attribute_lte_example' # str | Attribute less than or equal filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_gt = 'attribute_gt_example' # str | Attribute greater than filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_gte = 'attribute_gte_example' # str | Attribute greater than or equal filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_contains = 'attribute_contains_example' # str | Attribute contains filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_distance = 'attribute_distance_example' # str | Range filter for geoposition attributes. Format is attribute1::distance_km2::lat2::lon2,[attribute2::distancekm2::lat2::lon2]. (optional)
attribute_null = 'attribute_null_example' # str | Attribute null filter. Returns elements for which a given attribute is not defined. (optional)
operation = 'operation_example' # str | Set to \"count\" to return a count of objects instead of the objects. (optional)
start = 56 # int | Pagination start index. Index of the first item in a larger list to return. (optional)
stop = 56 # int | Pagination start index. Non-inclusive ndex of the last item in a larger list to return. (optional)

try:
    api_response = api_instance.delete_tree_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreeLeafApi->delete_tree_leaf_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **ancestor** | **str**| Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia). | [optional] 
 **type** | **int**| Unique integer identifying a tree leaf type. | [optional] 
 **name** | **str**| Name of the tree leaf element. | [optional] 
 **attribute** | **str**| Attribute equality filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_lt** | **str**| Attribute less than filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_lte** | **str**| Attribute less than or equal filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_gt** | **str**| Attribute greater than filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_gte** | **str**| Attribute greater than or equal filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_contains** | **str**| Attribute contains filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_distance** | **str**| Range filter for geoposition attributes. Format is attribute1::distance_km2::lat2::lon2,[attribute2::distancekm2::lat2::lon2]. | [optional] 
 **attribute_null** | **str**| Attribute null filter. Returns elements for which a given attribute is not defined. | [optional] 
 **operation** | **str**| Set to \&quot;count\&quot; to return a count of objects instead of the objects. | [optional] 
 **start** | **int**| Pagination start index. Index of the first item in a larger list to return. | [optional] 
 **stop** | **int**| Pagination start index. Non-inclusive ndex of the last item in a larger list to return. | [optional] 

### Return type

[**InlineResponse2043**](InlineResponse2043.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree_leaf**
> InlineResponse20031 get_tree_leaf(id)



Interact with individual tree leaf.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

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
api_instance = tator.TreeLeafApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a tree leaf.

try:
    api_response = api_instance.get_tree_leaf(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreeLeafApi->get_tree_leaf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a tree leaf. | 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree_leaf_list**
> list[InlineResponse20031] get_tree_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with a list of tree leaves.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

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
api_instance = tator.TreeLeafApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
ancestor = 'ancestor_example' # str | Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia). (optional)
type = 56 # int | Unique integer identifying a tree leaf type. (optional)
name = 'name_example' # str | Name of the tree leaf element. (optional)
attribute = 'attribute_example' # str | Attribute equality filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_lt = 'attribute_lt_example' # str | Attribute less than filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_lte = 'attribute_lte_example' # str | Attribute less than or equal filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_gt = 'attribute_gt_example' # str | Attribute greater than filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_gte = 'attribute_gte_example' # str | Attribute greater than or equal filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_contains = 'attribute_contains_example' # str | Attribute contains filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_distance = 'attribute_distance_example' # str | Range filter for geoposition attributes. Format is attribute1::distance_km2::lat2::lon2,[attribute2::distancekm2::lat2::lon2]. (optional)
attribute_null = 'attribute_null_example' # str | Attribute null filter. Returns elements for which a given attribute is not defined. (optional)
operation = 'operation_example' # str | Set to \"count\" to return a count of objects instead of the objects. (optional)
start = 56 # int | Pagination start index. Index of the first item in a larger list to return. (optional)
stop = 56 # int | Pagination start index. Non-inclusive ndex of the last item in a larger list to return. (optional)

try:
    api_response = api_instance.get_tree_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreeLeafApi->get_tree_leaf_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **ancestor** | **str**| Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia). | [optional] 
 **type** | **int**| Unique integer identifying a tree leaf type. | [optional] 
 **name** | **str**| Name of the tree leaf element. | [optional] 
 **attribute** | **str**| Attribute equality filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_lt** | **str**| Attribute less than filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_lte** | **str**| Attribute less than or equal filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_gt** | **str**| Attribute greater than filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_gte** | **str**| Attribute greater than or equal filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_contains** | **str**| Attribute contains filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_distance** | **str**| Range filter for geoposition attributes. Format is attribute1::distance_km2::lat2::lon2,[attribute2::distancekm2::lat2::lon2]. | [optional] 
 **attribute_null** | **str**| Attribute null filter. Returns elements for which a given attribute is not defined. | [optional] 
 **operation** | **str**| Set to \&quot;count\&quot; to return a count of objects instead of the objects. | [optional] 
 **start** | **int**| Pagination start index. Index of the first item in a larger list to return. | [optional] 
 **stop** | **int**| Pagination start index. Non-inclusive ndex of the last item in a larger list to return. | [optional] 

### Return type

[**list[InlineResponse20031]**](InlineResponse20031.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tree_leaf_suggestion**
> list[InlineResponse20030] tree_leaf_suggestion(project, ancestor, query, min_level=min_level)



Rest Endpoint compatible with devbridge suggestion format.  <https://github.com/kraaden/autocomplete>

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
api_instance = tator.TreeLeafApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
ancestor = 'ancestor_example' # str | Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia).
query = 'query_example' # str | String to search for matching names.
min_level = 56 # int | Integer specifying level of results that may be returned. For example, 2 refers to grandchildren of the level specified by the `ancestor` parameter. (optional)

try:
    api_response = api_instance.tree_leaf_suggestion(project, ancestor, query, min_level=min_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreeLeafApi->tree_leaf_suggestion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **ancestor** | **str**| Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia). | 
 **query** | **str**| String to search for matching names. | 
 **min_level** | **int**| Integer specifying level of results that may be returned. For example, 2 refers to grandchildren of the level specified by the &#x60;ancestor&#x60; parameter. | [optional] 

### Return type

[**list[InlineResponse20030]**](InlineResponse20030.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tree_leaf**
> InlineResponse20033 update_tree_leaf(id, body=body)



Interact with individual tree leaf.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

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
api_instance = tator.TreeLeafApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a tree leaf.
body = tator.Body26() # Body26 |  (optional)

try:
    api_response = api_instance.update_tree_leaf(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreeLeafApi->update_tree_leaf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a tree leaf. | 
 **body** | [**Body26**](Body26.md)|  | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tree_leaf_list**
> InlineResponse20032 update_tree_leaf_list(project, body=body, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with a list of tree leaves.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

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
api_instance = tator.TreeLeafApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body25() # Body25 |  (optional)
ancestor = 'ancestor_example' # str | Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia). (optional)
type = 56 # int | Unique integer identifying a tree leaf type. (optional)
name = 'name_example' # str | Name of the tree leaf element. (optional)
attribute = 'attribute_example' # str | Attribute equality filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_lt = 'attribute_lt_example' # str | Attribute less than filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_lte = 'attribute_lte_example' # str | Attribute less than or equal filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_gt = 'attribute_gt_example' # str | Attribute greater than filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_gte = 'attribute_gte_example' # str | Attribute greater than or equal filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_contains = 'attribute_contains_example' # str | Attribute contains filter. Format is attribute1::value1,[attribute2::value2]. (optional)
attribute_distance = 'attribute_distance_example' # str | Range filter for geoposition attributes. Format is attribute1::distance_km2::lat2::lon2,[attribute2::distancekm2::lat2::lon2]. (optional)
attribute_null = 'attribute_null_example' # str | Attribute null filter. Returns elements for which a given attribute is not defined. (optional)
operation = 'operation_example' # str | Set to \"count\" to return a count of objects instead of the objects. (optional)
start = 56 # int | Pagination start index. Index of the first item in a larger list to return. (optional)
stop = 56 # int | Pagination start index. Non-inclusive ndex of the last item in a larger list to return. (optional)

try:
    api_response = api_instance.update_tree_leaf_list(project, body=body, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreeLeafApi->update_tree_leaf_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body25**](Body25.md)|  | [optional] 
 **ancestor** | **str**| Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia). | [optional] 
 **type** | **int**| Unique integer identifying a tree leaf type. | [optional] 
 **name** | **str**| Name of the tree leaf element. | [optional] 
 **attribute** | **str**| Attribute equality filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_lt** | **str**| Attribute less than filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_lte** | **str**| Attribute less than or equal filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_gt** | **str**| Attribute greater than filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_gte** | **str**| Attribute greater than or equal filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_contains** | **str**| Attribute contains filter. Format is attribute1::value1,[attribute2::value2]. | [optional] 
 **attribute_distance** | **str**| Range filter for geoposition attributes. Format is attribute1::distance_km2::lat2::lon2,[attribute2::distancekm2::lat2::lon2]. | [optional] 
 **attribute_null** | **str**| Attribute null filter. Returns elements for which a given attribute is not defined. | [optional] 
 **operation** | **str**| Set to \&quot;count\&quot; to return a count of objects instead of the objects. | [optional] 
 **start** | **int**| Pagination start index. Index of the first item in a larger list to return. | [optional] 
 **stop** | **int**| Pagination start index. Non-inclusive ndex of the last item in a larger list to return. | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

