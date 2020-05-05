# tator.LocalizationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_localization**](LocalizationApi.md#create_localization) | **POST** /rest/Localizations/{project} | 
[**delete_localization**](LocalizationApi.md#delete_localization) | **DELETE** /rest/Localization/{id} | 
[**delete_localization_list**](LocalizationApi.md#delete_localization_list) | **DELETE** /rest/Localizations/{project} | 
[**get_localization**](LocalizationApi.md#get_localization) | **GET** /rest/Localization/{id} | 
[**get_localization_list**](LocalizationApi.md#get_localization_list) | **GET** /rest/Localizations/{project} | 
[**update_localization**](LocalizationApi.md#update_localization) | **PATCH** /rest/Localization/{id} | 
[**update_localization_list**](LocalizationApi.md#update_localization_list) | **PATCH** /rest/Localizations/{project} | 

# **create_localization**
> InlineResponse2012 create_localization(project, body=body)



Interact with list of localizations.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.

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
api_instance = tator.LocalizationApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body5() # Body5 |  (optional)

try:
    api_response = api_instance.create_localization(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationApi->create_localization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body5**](Body5.md)|  | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization**
> delete_localization(id)



Interact with single localization.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.

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
api_instance = tator.LocalizationApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a localization.

try:
    api_instance.delete_localization(id)
except ApiException as e:
    print("Exception when calling LocalizationApi->delete_localization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization_list**
> InlineResponse204 delete_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of localizations.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.

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
api_instance = tator.LocalizationApi(tator.ApiClient(configuration))
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
    api_response = api_instance.delete_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationApi->delete_localization_list: %s\n" % e)
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

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization**
> list[Object] get_localization(id)



Interact with single localization.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.

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
api_instance = tator.LocalizationApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a localization.

try:
    api_response = api_instance.get_localization(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationApi->get_localization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization. | 

### Return type

[**list[Object]**](Object.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_list**
> list[Object] get_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of localizations.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.

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
api_instance = tator.LocalizationApi(tator.ApiClient(configuration))
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
    api_response = api_instance.get_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationApi->get_localization_list: %s\n" % e)
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

[**list[Object]**](Object.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization**
> InlineResponse2007 update_localization(id, body=body)



Interact with single localization.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.

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
api_instance = tator.LocalizationApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a localization.
body = tator.Body7() # Body7 |  (optional)

try:
    api_response = api_instance.update_localization(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationApi->update_localization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization. | 
 **body** | [**Body7**](Body7.md)|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization_list**
> InlineResponse2006 update_localization_list(project, body=body, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of localizations.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.

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
api_instance = tator.LocalizationApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body6() # Body6 |  (optional)
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
    api_response = api_instance.update_localization_list(project, body=body, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationApi->update_localization_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body6**](Body6.md)|  | [optional] 
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

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

