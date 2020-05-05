# tator.StateApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_state**](StateApi.md#create_state) | **POST** /rest/States/{project} | 
[**delete_state**](StateApi.md#delete_state) | **DELETE** /rest/State/{id} | 
[**delete_state_list**](StateApi.md#delete_state_list) | **DELETE** /rest/States/{project} | 
[**get_state**](StateApi.md#get_state) | **GET** /rest/State/{id} | 
[**get_state_list**](StateApi.md#get_state_list) | **GET** /rest/States/{project} | 
[**update_state**](StateApi.md#update_state) | **PATCH** /rest/State/{id} | 
[**update_state_list**](StateApi.md#update_state_list) | **PATCH** /rest/States/{project} | 

# **create_state**
> InlineResponse2015 create_state(project, body=body)



Interact with list of states.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined state attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  It is importarant to know the fields required for a given entity_type_id as they are expected in the request data for this function. As an example, if the entity_type_id has attribute types associated with it named time and position, the JSON object must have them specified as keys.

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
api_instance = tator.StateApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = {
  "summary" : "Frame associated state",
  "value" : {
    "type" : 1,
    "media_ids" : [ 1 ],
    "frame" : 1000,
    "My First Attribute" : "value1",
    "My Second Attribute" : "value2"
  }
} # dict(str, object) |  (optional)

try:
    api_response = api_instance.create_state(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->create_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state**
> delete_state(id)



Interact with an individual state.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a types of entity in Tator, meaning they can be described by user defined attributes.

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
api_instance = tator.StateApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a state.

try:
    api_instance.delete_state(id)
except ApiException as e:
    print("Exception when calling StateApi->delete_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state_list**
> InlineResponse2042 delete_state_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of states.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined state attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  It is importarant to know the fields required for a given entity_type_id as they are expected in the request data for this function. As an example, if the entity_type_id has attribute types associated with it named time and position, the JSON object must have them specified as keys.

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
api_instance = tator.StateApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = 56 # int | Unique integer identifying a version. (optional)
modified = 56 # int | Whether to return original or modified annotations, 0 or 1. (optional)
after = 56 # int | If given, all results returned will be after the localization with this ID. The `start` and `stop` parameters are relative to this modified range. (optional)
search = 'search_example' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
    api_response = api_instance.delete_state_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->delete_state_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_query** | **str**| Query string used to filter media IDs. If supplied, media_id will be ignored. | [optional] 
 **media_id** | [**list[int]**](int.md)| Comma-separated list of media IDs. | [optional] 
 **type** | **int**| Unique integer identifying a annotation type. | [optional] 
 **version** | **int**| Unique integer identifying a version. | [optional] 
 **modified** | **int**| Whether to return original or modified annotations, 0 or 1. | [optional] 
 **after** | **int**| If given, all results returned will be after the localization with this ID. The &#x60;start&#x60; and &#x60;stop&#x60; parameters are relative to this modified range. | [optional] 
 **search** | **str**| Lucene query syntax string for use with Elasticsearch. See &#x60;reference &lt;https://lucene.apache.org/core/2_9_4/queryparsersyntax.html&gt;&#x60;_. | [optional] 
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

[**InlineResponse2042**](InlineResponse2042.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state**
> get_state(id)



Interact with an individual state.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a types of entity in Tator, meaning they can be described by user defined attributes.

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
api_instance = tator.StateApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a state.

try:
    api_instance.get_state(id)
except ApiException as e:
    print("Exception when calling StateApi->get_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_list**
> list[InlineResponse20023] get_state_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of states.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined state attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  It is importarant to know the fields required for a given entity_type_id as they are expected in the request data for this function. As an example, if the entity_type_id has attribute types associated with it named time and position, the JSON object must have them specified as keys.

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
api_instance = tator.StateApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = 56 # int | Unique integer identifying a version. (optional)
modified = 56 # int | Whether to return original or modified annotations, 0 or 1. (optional)
after = 56 # int | If given, all results returned will be after the localization with this ID. The `start` and `stop` parameters are relative to this modified range. (optional)
search = 'search_example' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
    api_response = api_instance.get_state_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->get_state_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_query** | **str**| Query string used to filter media IDs. If supplied, media_id will be ignored. | [optional] 
 **media_id** | [**list[int]**](int.md)| Comma-separated list of media IDs. | [optional] 
 **type** | **int**| Unique integer identifying a annotation type. | [optional] 
 **version** | **int**| Unique integer identifying a version. | [optional] 
 **modified** | **int**| Whether to return original or modified annotations, 0 or 1. | [optional] 
 **after** | **int**| If given, all results returned will be after the localization with this ID. The &#x60;start&#x60; and &#x60;stop&#x60; parameters are relative to this modified range. | [optional] 
 **search** | **str**| Lucene query syntax string for use with Elasticsearch. See &#x60;reference &lt;https://lucene.apache.org/core/2_9_4/queryparsersyntax.html&gt;&#x60;_. | [optional] 
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

[**list[InlineResponse20023]**](InlineResponse20023.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_state**
> InlineResponse20025 update_state(id, body=body)



Interact with an individual state.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a types of entity in Tator, meaning they can be described by user defined attributes.

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
api_instance = tator.StateApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a state.
body = tator.Body20() # Body20 |  (optional)

try:
    api_response = api_instance.update_state(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->update_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state. | 
 **body** | [**Body20**](Body20.md)|  | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_state_list**
> InlineResponse20024 update_state_list(project, body=body, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of states.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined state attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  It is importarant to know the fields required for a given entity_type_id as they are expected in the request data for this function. As an example, if the entity_type_id has attribute types associated with it named time and position, the JSON object must have them specified as keys.

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
api_instance = tator.StateApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body19() # Body19 |  (optional)
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = 56 # int | Unique integer identifying a version. (optional)
modified = 56 # int | Whether to return original or modified annotations, 0 or 1. (optional)
after = 56 # int | If given, all results returned will be after the localization with this ID. The `start` and `stop` parameters are relative to this modified range. (optional)
search = 'search_example' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
    api_response = api_instance.update_state_list(project, body=body, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->update_state_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body19**](Body19.md)|  | [optional] 
 **media_query** | **str**| Query string used to filter media IDs. If supplied, media_id will be ignored. | [optional] 
 **media_id** | [**list[int]**](int.md)| Comma-separated list of media IDs. | [optional] 
 **type** | **int**| Unique integer identifying a annotation type. | [optional] 
 **version** | **int**| Unique integer identifying a version. | [optional] 
 **modified** | **int**| Whether to return original or modified annotations, 0 or 1. | [optional] 
 **after** | **int**| If given, all results returned will be after the localization with this ID. The &#x60;start&#x60; and &#x60;stop&#x60; parameters are relative to this modified range. | [optional] 
 **search** | **str**| Lucene query syntax string for use with Elasticsearch. See &#x60;reference &lt;https://lucene.apache.org/core/2_9_4/queryparsersyntax.html&gt;&#x60;_. | [optional] 
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

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

