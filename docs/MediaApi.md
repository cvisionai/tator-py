# tator.MediaApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_media**](MediaApi.md#delete_media) | **DELETE** /rest/Media/{id} | 
[**delete_media_list**](MediaApi.md#delete_media_list) | **DELETE** /rest/Medias/{project} | 
[**get_media**](MediaApi.md#get_media) | **GET** /rest/Media/{id} | 
[**get_media_list**](MediaApi.md#get_media_list) | **GET** /rest/Medias/{project} | 
[**get_media_next**](MediaApi.md#get_media_next) | **GET** /rest/MediaNext/{id} | 
[**get_media_prev**](MediaApi.md#get_media_prev) | **GET** /rest/MediaPrev/{id} | 
[**get_media_sections**](MediaApi.md#get_media_sections) | **GET** /rest/MediaSections/{project} | 
[**update_media**](MediaApi.md#update_media) | **PATCH** /rest/Media/{id} | 
[**update_media_list**](MediaApi.md#update_media_list) | **PATCH** /rest/Medias/{project} | 

# **delete_media**
> delete_media(id)



Interact with individual media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.

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
api_instance = tator.MediaApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a media.

try:
    api_instance.delete_media(id)
except ApiException as e:
    print("Exception when calling MediaApi->delete_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media_list**
> InlineResponse2041 delete_media_list(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  This endpoint does not include a POST method. Creating media must be preceded by an upload, after which a separate media creation endpoint must be called. The media creation endpoints are `Transcode` to launch a transcode of an uploaded video and `SaveImage` to save an uploaded image. If you would like to perform transcodes on local assets, you can use the `SaveVideo` endpoint to save an already transcoded video. Local transcodes may be performed with the script at `scripts/transcoder/transcodePipeline.py` in the Tator source code.

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
api_instance = tator.MediaApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
media_id = [56] # list[int] | List of integers identifying media. (optional)
type = 56 # int | Unique integer identifying media type. (optional)
name = 'name_example' # str | Name of the media to filter on. (optional)
md5 = 'md5_example' # str | MD5 sum of the media file. (optional)
after = 'after_example' # str | If given, all results returned will be after the file with this filename. The `start` and `stop` parameters are relative to this modified range. (optional)
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
    api_response = api_instance.delete_media_list(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->delete_media_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_id** | [**list[int]**](int.md)| List of integers identifying media. | [optional] 
 **type** | **int**| Unique integer identifying media type. | [optional] 
 **name** | **str**| Name of the media to filter on. | [optional] 
 **md5** | **str**| MD5 sum of the media file. | [optional] 
 **after** | **str**| If given, all results returned will be after the file with this filename. The &#x60;start&#x60; and &#x60;stop&#x60; parameters are relative to this modified range. | [optional] 
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

[**InlineResponse2041**](InlineResponse2041.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media**
> InlineResponse20011 get_media(id)



Interact with individual media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.

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
api_instance = tator.MediaApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a media.

try:
    api_response = api_instance.get_media(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media. | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_list**
> list[InlineResponse20011] get_media_list(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  This endpoint does not include a POST method. Creating media must be preceded by an upload, after which a separate media creation endpoint must be called. The media creation endpoints are `Transcode` to launch a transcode of an uploaded video and `SaveImage` to save an uploaded image. If you would like to perform transcodes on local assets, you can use the `SaveVideo` endpoint to save an already transcoded video. Local transcodes may be performed with the script at `scripts/transcoder/transcodePipeline.py` in the Tator source code.

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
api_instance = tator.MediaApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
media_id = [56] # list[int] | List of integers identifying media. (optional)
type = 56 # int | Unique integer identifying media type. (optional)
name = 'name_example' # str | Name of the media to filter on. (optional)
md5 = 'md5_example' # str | MD5 sum of the media file. (optional)
after = 'after_example' # str | If given, all results returned will be after the file with this filename. The `start` and `stop` parameters are relative to this modified range. (optional)
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
    api_response = api_instance.get_media_list(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_media_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_id** | [**list[int]**](int.md)| List of integers identifying media. | [optional] 
 **type** | **int**| Unique integer identifying media type. | [optional] 
 **name** | **str**| Name of the media to filter on. | [optional] 
 **md5** | **str**| MD5 sum of the media file. | [optional] 
 **after** | **str**| If given, all results returned will be after the file with this filename. The &#x60;start&#x60; and &#x60;stop&#x60; parameters are relative to this modified range. | [optional] 
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

[**list[InlineResponse20011]**](InlineResponse20011.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_next**
> InlineResponse20014 get_media_next(id, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve ID of next media in a media list.  This endpoint accepts the same query parameters as a GET request to the `Medias` endpoint, but only returns the next media ID from the media passed as a path parameter. This allows iteration through a media list without serializing the entire list, which may be large.

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
api_instance = tator.MediaApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a media object.
media_id = [56] # list[int] | List of integers identifying media. (optional)
type = 56 # int | Unique integer identifying media type. (optional)
name = 'name_example' # str | Name of the media to filter on. (optional)
md5 = 'md5_example' # str | MD5 sum of the media file. (optional)
after = 'after_example' # str | If given, all results returned will be after the file with this filename. The `start` and `stop` parameters are relative to this modified range. (optional)
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
    api_response = api_instance.get_media_next(id, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_media_next: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media object. | 
 **media_id** | [**list[int]**](int.md)| List of integers identifying media. | [optional] 
 **type** | **int**| Unique integer identifying media type. | [optional] 
 **name** | **str**| Name of the media to filter on. | [optional] 
 **md5** | **str**| MD5 sum of the media file. | [optional] 
 **after** | **str**| If given, all results returned will be after the file with this filename. The &#x60;start&#x60; and &#x60;stop&#x60; parameters are relative to this modified range. | [optional] 
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

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_prev**
> InlineResponse20015 get_media_prev(id, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve ID of previous media in a media list.  This endpoint accepts the same query parameters as a GET request to the `Medias` endpoint, but only returns the previous media ID from the media passed as a path parameter. This  allows iteration through a media list without serializing the entire list, which may be  large.

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
api_instance = tator.MediaApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a media object.
media_id = [56] # list[int] | List of integers identifying media. (optional)
type = 56 # int | Unique integer identifying media type. (optional)
name = 'name_example' # str | Name of the media to filter on. (optional)
md5 = 'md5_example' # str | MD5 sum of the media file. (optional)
after = 'after_example' # str | If given, all results returned will be after the file with this filename. The `start` and `stop` parameters are relative to this modified range. (optional)
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
    api_response = api_instance.get_media_prev(id, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_media_prev: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media object. | 
 **media_id** | [**list[int]**](int.md)| List of integers identifying media. | [optional] 
 **type** | **int**| Unique integer identifying media type. | [optional] 
 **name** | **str**| Name of the media to filter on. | [optional] 
 **md5** | **str**| MD5 sum of the media file. | [optional] 
 **after** | **str**| If given, all results returned will be after the file with this filename. The &#x60;start&#x60; and &#x60;stop&#x60; parameters are relative to this modified range. | [optional] 
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

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_sections**
> dict(str, object) get_media_sections(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve media counts by section.  This endpoint accepts the same query parameters as a GET request to the `Medias` endpoint, but only returns the number of images and videos per sections.

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
api_instance = tator.MediaApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
media_id = [56] # list[int] | List of integers identifying media. (optional)
type = 56 # int | Unique integer identifying media type. (optional)
name = 'name_example' # str | Name of the media to filter on. (optional)
md5 = 'md5_example' # str | MD5 sum of the media file. (optional)
after = 'after_example' # str | If given, all results returned will be after the file with this filename. The `start` and `stop` parameters are relative to this modified range. (optional)
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
    api_response = api_instance.get_media_sections(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_media_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_id** | [**list[int]**](int.md)| List of integers identifying media. | [optional] 
 **type** | **int**| Unique integer identifying media type. | [optional] 
 **name** | **str**| Name of the media to filter on. | [optional] 
 **md5** | **str**| MD5 sum of the media file. | [optional] 
 **after** | **str**| If given, all results returned will be after the file with this filename. The &#x60;start&#x60; and &#x60;stop&#x60; parameters are relative to this modified range. | [optional] 
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

**dict(str, object)**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_media**
> InlineResponse20013 update_media(id, body=body)



Interact with individual media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.

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
api_instance = tator.MediaApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a media.
body = tator.Body11() # Body11 |  (optional)

try:
    api_response = api_instance.update_media(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->update_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media. | 
 **body** | [**Body11**](Body11.md)|  | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_media_list**
> InlineResponse20012 update_media_list(project, body=body, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  This endpoint does not include a POST method. Creating media must be preceded by an upload, after which a separate media creation endpoint must be called. The media creation endpoints are `Transcode` to launch a transcode of an uploaded video and `SaveImage` to save an uploaded image. If you would like to perform transcodes on local assets, you can use the `SaveVideo` endpoint to save an already transcoded video. Local transcodes may be performed with the script at `scripts/transcoder/transcodePipeline.py` in the Tator source code.

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
api_instance = tator.MediaApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body10() # Body10 |  (optional)
media_id = [56] # list[int] | List of integers identifying media. (optional)
type = 56 # int | Unique integer identifying media type. (optional)
name = 'name_example' # str | Name of the media to filter on. (optional)
md5 = 'md5_example' # str | MD5 sum of the media file. (optional)
after = 'after_example' # str | If given, all results returned will be after the file with this filename. The `start` and `stop` parameters are relative to this modified range. (optional)
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
    api_response = api_instance.update_media_list(project, body=body, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->update_media_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body10**](Body10.md)|  | [optional] 
 **media_id** | [**list[int]**](int.md)| List of integers identifying media. | [optional] 
 **type** | **int**| Unique integer identifying media type. | [optional] 
 **name** | **str**| Name of the media to filter on. | [optional] 
 **md5** | **str**| MD5 sum of the media file. | [optional] 
 **after** | **str**| If given, all results returned will be after the file with this filename. The &#x60;start&#x60; and &#x60;stop&#x60; parameters are relative to this modified range. | [optional] 
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

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

