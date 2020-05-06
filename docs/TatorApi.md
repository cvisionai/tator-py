# tator.TatorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**algorithm_launch**](TatorApi.md#algorithm_launch) | **POST** /rest/AlgorithmLaunch/{project} | 
[**create_analysis**](TatorApi.md#create_analysis) | **POST** /rest/Analyses/{project} | 
[**create_attribute_type**](TatorApi.md#create_attribute_type) | **POST** /rest/AttributeTypes/{project} | 
[**create_localization**](TatorApi.md#create_localization) | **POST** /rest/Localizations/{project} | 
[**create_localization_type**](TatorApi.md#create_localization_type) | **POST** /rest/LocalizationTypes/{project} | 
[**create_media_type**](TatorApi.md#create_media_type) | **POST** /rest/MediaTypes/{project} | 
[**create_membership**](TatorApi.md#create_membership) | **POST** /rest/Memberships/{project} | 
[**create_obtain_auth_token**](TatorApi.md#create_obtain_auth_token) | **POST** /rest/Token | 
[**create_project**](TatorApi.md#create_project) | **POST** /rest/Projects | 
[**create_state**](TatorApi.md#create_state) | **POST** /rest/States/{project} | 
[**create_state_type**](TatorApi.md#create_state_type) | **POST** /rest/StateTypes/{project} | 
[**create_temporary_file**](TatorApi.md#create_temporary_file) | **POST** /rest/TemporaryFiles/{project} | 
[**create_tree_leaf**](TatorApi.md#create_tree_leaf) | **POST** /rest/TreeLeaves/{project} | 
[**create_tree_leaf_type**](TatorApi.md#create_tree_leaf_type) | **POST** /rest/TreeLeafTypes/{project} | 
[**create_version**](TatorApi.md#create_version) | **POST** /rest/Versions/{project} | 
[**delete_attribute_type**](TatorApi.md#delete_attribute_type) | **DELETE** /rest/AttributeType/{id} | 
[**delete_frame_association**](TatorApi.md#delete_frame_association) | **DELETE** /rest/FrameAssociation/{id} | 
[**delete_job**](TatorApi.md#delete_job) | **DELETE** /rest/Job/{run_uid} | 
[**delete_job_group**](TatorApi.md#delete_job_group) | **DELETE** /rest/JobGroup/{group_id} | 
[**delete_localization**](TatorApi.md#delete_localization) | **DELETE** /rest/Localization/{id} | 
[**delete_localization_association**](TatorApi.md#delete_localization_association) | **DELETE** /rest/LocalizationAssociation/{id} | 
[**delete_localization_list**](TatorApi.md#delete_localization_list) | **DELETE** /rest/Localizations/{project} | 
[**delete_localization_type**](TatorApi.md#delete_localization_type) | **DELETE** /rest/LocalizationType/{id} | 
[**delete_media**](TatorApi.md#delete_media) | **DELETE** /rest/Media/{id} | 
[**delete_media_list**](TatorApi.md#delete_media_list) | **DELETE** /rest/Medias/{project} | 
[**delete_media_type**](TatorApi.md#delete_media_type) | **DELETE** /rest/MediaType/{id} | 
[**delete_membership**](TatorApi.md#delete_membership) | **DELETE** /rest/Membership/{id} | 
[**delete_project**](TatorApi.md#delete_project) | **DELETE** /rest/Project/{id} | 
[**delete_state**](TatorApi.md#delete_state) | **DELETE** /rest/State/{id} | 
[**delete_state_list**](TatorApi.md#delete_state_list) | **DELETE** /rest/States/{project} | 
[**delete_state_type**](TatorApi.md#delete_state_type) | **DELETE** /rest/StateType/{id} | 
[**delete_temporary_file**](TatorApi.md#delete_temporary_file) | **DELETE** /rest/TemporaryFile/{id} | 
[**delete_temporary_file_list**](TatorApi.md#delete_temporary_file_list) | **DELETE** /rest/TemporaryFiles/{project} | 
[**delete_tree_leaf**](TatorApi.md#delete_tree_leaf) | **DELETE** /rest/TreeLeaf/{id} | 
[**delete_tree_leaf_list**](TatorApi.md#delete_tree_leaf_list) | **DELETE** /rest/TreeLeaves/{project} | 
[**delete_tree_leaf_type**](TatorApi.md#delete_tree_leaf_type) | **DELETE** /rest/TreeLeafType/{id} | 
[**delete_version**](TatorApi.md#delete_version) | **DELETE** /rest/Version/{id} | 
[**get_algorithm_list**](TatorApi.md#get_algorithm_list) | **GET** /rest/Algorithms/{project} | 
[**get_analysis_list**](TatorApi.md#get_analysis_list) | **GET** /rest/Analyses/{project} | 
[**get_attribute_type**](TatorApi.md#get_attribute_type) | **GET** /rest/AttributeType/{id} | 
[**get_attribute_type_list**](TatorApi.md#get_attribute_type_list) | **GET** /rest/AttributeTypes/{project} | 
[**get_clip**](TatorApi.md#get_clip) | **GET** /rest/GetClip/{id} | 
[**get_entity_type_schema**](TatorApi.md#get_entity_type_schema) | **GET** /rest/EntityTypeSchema/{id} | 
[**get_frame**](TatorApi.md#get_frame) | **GET** /rest/GetFrame/{id} | 
[**get_frame_association**](TatorApi.md#get_frame_association) | **GET** /rest/FrameAssociation/{id} | 
[**get_localization**](TatorApi.md#get_localization) | **GET** /rest/Localization/{id} | 
[**get_localization_association**](TatorApi.md#get_localization_association) | **GET** /rest/LocalizationAssociation/{id} | 
[**get_localization_list**](TatorApi.md#get_localization_list) | **GET** /rest/Localizations/{project} | 
[**get_localization_type**](TatorApi.md#get_localization_type) | **GET** /rest/LocalizationType/{id} | 
[**get_localization_type_list**](TatorApi.md#get_localization_type_list) | **GET** /rest/LocalizationTypes/{project} | 
[**get_media**](TatorApi.md#get_media) | **GET** /rest/Media/{id} | 
[**get_media_list**](TatorApi.md#get_media_list) | **GET** /rest/Medias/{project} | 
[**get_media_next**](TatorApi.md#get_media_next) | **GET** /rest/MediaNext/{id} | 
[**get_media_prev**](TatorApi.md#get_media_prev) | **GET** /rest/MediaPrev/{id} | 
[**get_media_sections**](TatorApi.md#get_media_sections) | **GET** /rest/MediaSections/{project} | 
[**get_media_type**](TatorApi.md#get_media_type) | **GET** /rest/MediaType/{id} | 
[**get_media_type_list**](TatorApi.md#get_media_type_list) | **GET** /rest/MediaTypes/{project} | 
[**get_membership**](TatorApi.md#get_membership) | **GET** /rest/Membership/{id} | 
[**get_membership_list**](TatorApi.md#get_membership_list) | **GET** /rest/Memberships/{project} | 
[**get_project**](TatorApi.md#get_project) | **GET** /rest/Project/{id} | 
[**get_project_list**](TatorApi.md#get_project_list) | **GET** /rest/Projects | 
[**get_section_analysis**](TatorApi.md#get_section_analysis) | **GET** /rest/SectionAnalysis/{project} | 
[**get_state**](TatorApi.md#get_state) | **GET** /rest/State/{id} | 
[**get_state_list**](TatorApi.md#get_state_list) | **GET** /rest/States/{project} | 
[**get_state_type**](TatorApi.md#get_state_type) | **GET** /rest/StateType/{id} | 
[**get_state_type_list**](TatorApi.md#get_state_type_list) | **GET** /rest/StateTypes/{project} | 
[**get_temporary_file**](TatorApi.md#get_temporary_file) | **GET** /rest/TemporaryFile/{id} | 
[**get_temporary_file_list**](TatorApi.md#get_temporary_file_list) | **GET** /rest/TemporaryFiles/{project} | 
[**get_tree_leaf**](TatorApi.md#get_tree_leaf) | **GET** /rest/TreeLeaf/{id} | 
[**get_tree_leaf_list**](TatorApi.md#get_tree_leaf_list) | **GET** /rest/TreeLeaves/{project} | 
[**get_tree_leaf_type**](TatorApi.md#get_tree_leaf_type) | **GET** /rest/TreeLeafType/{id} | 
[**get_tree_leaf_type_list**](TatorApi.md#get_tree_leaf_type_list) | **GET** /rest/TreeLeafTypes/{project} | 
[**get_user**](TatorApi.md#get_user) | **GET** /rest/User/{id} | 
[**get_version**](TatorApi.md#get_version) | **GET** /rest/Version/{id} | 
[**notify**](TatorApi.md#notify) | **POST** /rest/Notify | 
[**partial_update_save_video_api**](TatorApi.md#partial_update_save_video_api) | **PATCH** /rest/SaveVideo/{project} | 
[**progress**](TatorApi.md#progress) | **POST** /rest/Progress/{project} | 
[**retrieve_state_graphic_api**](TatorApi.md#retrieve_state_graphic_api) | **GET** /rest/StateGraphic/{id} | 
[**retrieve_version_list**](TatorApi.md#retrieve_version_list) | **GET** /rest/Versions/{project} | 
[**save_image**](TatorApi.md#save_image) | **POST** /rest/SaveImage/{project} | 
[**save_video**](TatorApi.md#save_video) | **POST** /rest/SaveVideo/{project} | 
[**transcode**](TatorApi.md#transcode) | **POST** /rest/Transcode/{project} | 
[**tree_leaf_suggestion**](TatorApi.md#tree_leaf_suggestion) | **GET** /rest/TreeLeaves/Suggestion/{ancestor}/{project} | 
[**update_attribute_type**](TatorApi.md#update_attribute_type) | **PATCH** /rest/AttributeType/{id} | 
[**update_frame_association**](TatorApi.md#update_frame_association) | **PATCH** /rest/FrameAssociation/{id} | 
[**update_localization**](TatorApi.md#update_localization) | **PATCH** /rest/Localization/{id} | 
[**update_localization_association**](TatorApi.md#update_localization_association) | **PATCH** /rest/LocalizationAssociation/{id} | 
[**update_localization_list**](TatorApi.md#update_localization_list) | **PATCH** /rest/Localizations/{project} | 
[**update_localization_type**](TatorApi.md#update_localization_type) | **PATCH** /rest/LocalizationType/{id} | 
[**update_media**](TatorApi.md#update_media) | **PATCH** /rest/Media/{id} | 
[**update_media_list**](TatorApi.md#update_media_list) | **PATCH** /rest/Medias/{project} | 
[**update_media_type**](TatorApi.md#update_media_type) | **PATCH** /rest/MediaType/{id} | 
[**update_membership**](TatorApi.md#update_membership) | **PATCH** /rest/Membership/{id} | 
[**update_project**](TatorApi.md#update_project) | **PATCH** /rest/Project/{id} | 
[**update_state**](TatorApi.md#update_state) | **PATCH** /rest/State/{id} | 
[**update_state_list**](TatorApi.md#update_state_list) | **PATCH** /rest/States/{project} | 
[**update_state_type**](TatorApi.md#update_state_type) | **PATCH** /rest/StateType/{id} | 
[**update_tree_leaf**](TatorApi.md#update_tree_leaf) | **PATCH** /rest/TreeLeaf/{id} | 
[**update_tree_leaf_list**](TatorApi.md#update_tree_leaf_list) | **PATCH** /rest/TreeLeaves/{project} | 
[**update_tree_leaf_type**](TatorApi.md#update_tree_leaf_type) | **PATCH** /rest/TreeLeafType/{id} | 
[**update_user**](TatorApi.md#update_user) | **PATCH** /rest/User/{id} | 
[**update_version**](TatorApi.md#update_version) | **PATCH** /rest/Version/{id} | 
[**who_am_i**](TatorApi.md#who_am_i) | **GET** /rest/User/GetCurrent | 


# **algorithm_launch**
> AlgorithmLaunchResponse algorithm_launch(project, algorithm_launch_spec=algorithm_launch_spec)



Start an algorithm.  This will create one or more Argo workflows that execute the named algorithm registration. To get a list of available algorithms, use the `Algorithms` endpoint. A media list will be submitted for processing using either a query string or  a list of media IDs. If neither are included, the algorithm will be launched on all media in the project.   Media is divided into batches for based on the `files_per_job` field of the  `Algorithm` object. One batch is submitted to each Argo workflow.  Submitted algorithm jobs may be cancelled via the `Job` or `JobGroup` endpoints.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
algorithm_launch_spec = {"algorithm_name":"My Algorithm","media_ids":[1,5,10]} # AlgorithmLaunchSpec |  (optional)

    try:
        api_response = api_instance.algorithm_launch(project, algorithm_launch_spec=algorithm_launch_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->algorithm_launch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **algorithm_launch_spec** | [**AlgorithmLaunchSpec**](AlgorithmLaunchSpec.md)|  | [optional] 

### Return type

[**AlgorithmLaunchResponse**](AlgorithmLaunchResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful launch of algorithm. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_analysis**
> CreateResponse create_analysis(project, analysis_spec=analysis_spec)



Create analysis for a project.  Analysis objects are used to display information about filtered media lists and/or annotations on the project detail page of the web UI. Currently only counting analysis is supported.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
analysis_spec = {"data_type":1,"name":"Boxes"} # AnalysisSpec |  (optional)

    try:
        api_response = api_instance.create_analysis(project, analysis_spec=analysis_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **analysis_spec** | [**AnalysisSpec**](AnalysisSpec.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of analysis. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_attribute_type**
> CreateResponse create_attribute_type(project, attribute_type_spec=attribute_type_spec)



Create or list attribute types.  Attribute types are used to define data types that describe entities. An attribute may give information about a media, localization, or state entity  in the form of a boolean, integer, float, string, enumeration, datetime,  or geoposition. Besides the data type, attribute types define attribute defaults, bounds, and other constraints.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
attribute_type_spec = {"applies_to":1,"default":false,"dtype":"bool","name":"My Boolean"} # AttributeTypeSpec |  (optional)

    try:
        api_response = api_instance.create_attribute_type(project, attribute_type_spec=attribute_type_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **attribute_type_spec** | [**AttributeTypeSpec**](AttributeTypeSpec.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of attribute type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_localization**
> MessageResponse create_localization(project, localization_spec=localization_spec)



Interact with list of localizations.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
localization_spec = {"My First Attribute":"value1","My Second Attribute":"value2","frame":1000,"height":0.4,"media_id":1,"type":1,"width":0.3,"x":0.1,"y":0.2} # LocalizationSpec |  (optional)

    try:
        api_response = api_instance.create_localization(project, localization_spec=localization_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_localization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **localization_spec** | [**LocalizationSpec**](LocalizationSpec.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of localization(s). |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_localization_type**
> InlineResponse201 create_localization_type(project, inline_object2=inline_object2)



Create or retrieve localization types.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
inline_object2 = tator.InlineObject2() # InlineObject2 |  (optional)

    try:
        api_response = api_instance.create_localization_type(project, inline_object2=inline_object2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_localization_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of localization type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_media_type**
> InlineResponse201 create_media_type(project, inline_object5=inline_object5)



Create or retrieve localization types.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
inline_object5 = tator.InlineObject5() # InlineObject5 |  (optional)

    try:
        api_response = api_instance.create_media_type(project, inline_object5=inline_object5)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_media_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **inline_object5** | [**InlineObject5**](InlineObject5.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of media type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_membership**
> InlineResponse2011 create_membership(project, inline_object8=inline_object8)



Create or retrieve a list of project memberships.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels. `View Only` can only view a project and not change any data. `Can Edit` can create, modify, and delete annotations. `Can Transfer` can upload and download media. `Can Execute` can launch algorithm workflows. `Full Control` can change project settings, including inviting new members, project name, and project metadata schema.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
inline_object8 = tator.InlineObject8() # InlineObject8 |  (optional)

    try:
        api_response = api_instance.create_membership(project, inline_object8=inline_object8)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **inline_object8** | [**InlineObject8**](InlineObject8.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of membership. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_obtain_auth_token**
> InlineResponse20010 create_obtain_auth_token(inline_object18=inline_object18)



### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    inline_object18 = tator.InlineObject18() # InlineObject18 |  (optional)

    try:
        api_response = api_instance.create_obtain_auth_token(inline_object18=inline_object18)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_obtain_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object18** | [**InlineObject18**](InlineObject18.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login credentials accepted. |  -  |
**400** | Login credentials invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> InlineResponse2012 create_project(inline_object11=inline_object11)



Interact with a list of projects.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Project lists return all projects that the requesting user has access to.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    inline_object11 = tator.InlineObject11() # InlineObject11 |  (optional)

    try:
        api_response = api_instance.create_project(inline_object11=inline_object11)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object11** | [**InlineObject11**](InlineObject11.md)|  | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of project. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_state**
> CreateResponse create_state(project, request_body=request_body)



Interact with list of states.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined state attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  It is importarant to know the fields required for a given entity_type_id as they are expected in the request data for this function. As an example, if the entity_type_id has attribute types associated with it named time and position, the JSON object must have them specified as keys.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
request_body = {"My First Attribute":"value1","My Second Attribute":"value2","frame":1000,"media_ids":[1],"type":1} # dict(str, object) |  (optional)

    try:
        api_response = api_instance.create_state(project, request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **request_body** | [**dict(str, object)**](object.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of state(s). |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_state_type**
> CreateResponse create_state_type(project, inline_object15=inline_object15)



Create or retrieve state types.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
inline_object15 = tator.InlineObject15() # InlineObject15 |  (optional)

    try:
        api_response = api_instance.create_state_type(project, inline_object15=inline_object15)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_state_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **inline_object15** | [**InlineObject15**](InlineObject15.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of state type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_temporary_file**
> object create_temporary_file(project, inline_object17=inline_object17)



Interact with temporary file list.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
inline_object17 = tator.InlineObject17() # InlineObject17 |  (optional)

    try:
        api_response = api_instance.create_temporary_file(project, inline_object17=inline_object17)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_temporary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **inline_object17** | [**InlineObject17**](InlineObject17.md)|  | [optional] 

### Return type

**object**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tree_leaf**
> CreateResponse create_tree_leaf(project, request_body=request_body)



Interact with a list of tree leaves.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
request_body = None # dict(str, object) |  (optional)

    try:
        api_response = api_instance.create_tree_leaf(project, request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_tree_leaf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **request_body** | [**dict(str, object)**](object.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of tree leaf. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tree_leaf_type**
> CreateResponse create_tree_leaf_type(project, inline_object22=inline_object22)



Interact with tree leaf type list.  A tree leaf type is the metadata definition object for a tree leaf. It includes name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
inline_object22 = tator.InlineObject22() # InlineObject22 |  (optional)

    try:
        api_response = api_instance.create_tree_leaf_type(project, inline_object22=inline_object22)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_tree_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **inline_object22** | [**InlineObject22**](InlineObject22.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of tree leaf type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_version**
> CreateResponse create_version(project, inline_object25=inline_object25)



Interact with a list of versions.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
inline_object25 = tator.InlineObject25() # InlineObject25 |  (optional)

    try:
        api_response = api_instance.create_version(project, inline_object25=inline_object25)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **inline_object25** | [**InlineObject25**](InlineObject25.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of version. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attribute_type**
> delete_attribute_type(id)



Interact with an individual attribute type.  Attribute types are used to define data types that describe entities. An attribute may give information about a media, localization, or state entity  in the form of a boolean, integer, float, string, enumeration, datetime,  or geoposition. Besides the data type, attribute types define attribute defaults, bounds, and other constraints.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an attribute type.

    try:
        api_instance.delete_attribute_type(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_attribute_type: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of attribute type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_frame_association**
> delete_frame_association(id)



Modify a frame association.  Frame associations specify which frames that a `State` object applies to.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a frame association.

    try:
        api_instance.delete_frame_association(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_frame_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a frame association. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful delete of frame association. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> MessageResponse delete_job(run_uid)



Cancel a background job.  Algorithms and transcodes create argo workflows that are annotated with two uuid1 strings, one identifying the run and the other identifying the group. Jobs that are submitted together have the same group id, but each workflow has a unique run id.  This endpoint allows the user to cancel a job using the `run_uid` returned by either the `AlgorithmLaunch` or `Transcode` endpoints.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    run_uid = 'run_uid_example' # str | A uuid1 string identifying to single Job.

    try:
        api_response = api_instance.delete_job(run_uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_uid** | **str**| A uuid1 string identifying to single Job. | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful cancellation of job. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_group**
> MessageResponse delete_job_group(group_id)



Cancel a group of background jobs.  Algorithms and transcodes create argo workflows that are annotated with two uuid1 strings, one identifying the run and the other identifying the group. Jobs that are submitted together have the same group id, but each workflow has a unique run id.  This endpoint allows the user to cancel a group of jobs using the `group_id`  returned by either the `AlgorithmLaunch` or `Transcode` endpoints.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    group_id = 'group_id_example' # str | A uuid1 string identifying a group of jobs.

    try:
        api_response = api_instance.delete_job_group(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_job_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A uuid1 string identifying a group of jobs. | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful cancellation of job group. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization**
> delete_localization(id)



Interact with single localization.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a localization.

    try:
        api_instance.delete_localization(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_localization: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of localization. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization_association**
> delete_localization_association(id)



Modify a localization association.  Localization associations specify which localizations that a `State` object applies to.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a localization association.

    try:
        api_instance.delete_localization_association(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_localization_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization association. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful delete of localization association. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization_list**
> MessageResponse delete_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of localizations.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = 56 # int | Unique integer identifying a version. (optional)
modified = 56 # int | Whether to return original or modified annotations, 0 or 1. (optional)
after = 56 # int | If given, all results returned will be after the localization with this ID. The `start` and `stop` parameters are relative to this modified range. (optional)
search = '\"My search string\"' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
        print("Exception when calling TatorApi->delete_localization_list: %s\n" % e)
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

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of localization list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization_type**
> delete_localization_type(id)



Interact with an individual localization type.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an localization type.

    try:
        api_instance.delete_localization_type(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_localization_type: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of localization type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media**
> delete_media(id)



Interact with individual media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a media.

    try:
        api_instance.delete_media(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_media: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of media. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media_list**
> MessageResponse delete_media_list(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  This endpoint does not include a POST method. Creating media must be preceded by an upload, after which a separate media creation endpoint must be called. The media creation endpoints are `Transcode` to launch a transcode of an uploaded video and `SaveImage` to save an uploaded image. If you would like to perform transcodes on local assets, you can use the `SaveVideo` endpoint to save an already transcoded video. Local transcodes may be performed with the script at `scripts/transcoder/transcodePipeline.py` in the Tator source code.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_id = [56] # list[int] | List of integers identifying media. (optional)
type = 56 # int | Unique integer identifying media type. (optional)
name = 'name_example' # str | Name of the media to filter on. (optional)
md5 = 'md5_example' # str | MD5 sum of the media file. (optional)
after = 'after_example' # str | If given, all results returned will be after the file with this filename. The `start` and `stop` parameters are relative to this modified range. (optional)
search = '\"My search string\"' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
        print("Exception when calling TatorApi->delete_media_list: %s\n" % e)
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

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of media list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media_type**
> delete_media_type(id)



Interact with an individual media type.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an media type.

    try:
        api_instance.delete_media_type(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_media_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an media type. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of media type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_membership**
> delete_membership(id)



Interact with an individual project membership.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels. `View Only` can only view a project and not change any data. `Can Edit` can create, modify, and delete annotations. `Can Transfer` can upload and download media. `Can Execute` can launch algorithm workflows. `Full Control` can change project settings, including inviting new members, project name, and project metadata schema.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a membership.

    try:
        api_instance.delete_membership(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_membership: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of membership. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(id)



Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a project.

    try:
        api_instance.delete_project(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_project: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of project. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state**
> delete_state(id)



Interact with an individual state.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a types of entity in Tator, meaning they can be described by user defined attributes.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a state.

    try:
        api_instance.delete_state(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_state: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of state. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state_list**
> MessageResponse delete_state_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of states.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined state attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  It is importarant to know the fields required for a given entity_type_id as they are expected in the request data for this function. As an example, if the entity_type_id has attribute types associated with it named time and position, the JSON object must have them specified as keys.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = 56 # int | Unique integer identifying a version. (optional)
modified = 56 # int | Whether to return original or modified annotations, 0 or 1. (optional)
after = 56 # int | If given, all results returned will be after the localization with this ID. The `start` and `stop` parameters are relative to this modified range. (optional)
search = '\"My search string\"' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
        print("Exception when calling TatorApi->delete_state_list: %s\n" % e)
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

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of state list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state_type**
> delete_state_type(id)



Interact with an individual state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a state type.

    try:
        api_instance.delete_state_type(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_state_type: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of state type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_temporary_file**
> delete_temporary_file(id)



Interact with temporary file.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 'id_example' # str | A unique integer value identifying this temporary file.

    try:
        api_instance.delete_temporary_file(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_temporary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this temporary file. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_temporary_file_list**
> delete_temporary_file_list(project, expired=expired)



Interact with temporary file list.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
expired = 0 # int | If greater than 0 will return only expired files (optional) (default to 0)

    try:
        api_instance.delete_temporary_file_list(project, expired=expired)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_temporary_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **expired** | **int**| If greater than 0 will return only expired files | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tree_leaf**
> delete_tree_leaf(id)



Interact with individual tree leaf.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a tree leaf.

    try:
        api_instance.delete_tree_leaf(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_tree_leaf: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of tree leaf. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tree_leaf_list**
> MessageResponse delete_tree_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with a list of tree leaves.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
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
        print("Exception when calling TatorApi->delete_tree_leaf_list: %s\n" % e)
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

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of tree leaf list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tree_leaf_type**
> delete_tree_leaf_type(id)



Interact with individual tree leaf type.  A tree leaf type is the metadata definition object for a tree leaf. It includes name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an tree_leaf type.

    try:
        api_instance.delete_tree_leaf_type(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_tree_leaf_type: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of tree leaf type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version**
> delete_version(id)



Interact with individual version.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a version.

    try:
        api_instance.delete_version(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a version. | 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful deletion of version. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_algorithm_list**
> list[object] get_algorithm_list(project)



Interact with algorithms that have been registered to a project.  For instructions on how to register an algorithm, visit `GitHub`_.  .. _GitHub:    https://github.com/cvisionai/tator/tree/master/examples/algorithms

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.

    try:
        api_response = api_instance.get_algorithm_list(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_algorithm_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

**list[object]**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of registered algorithms. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_list**
> list[object] get_analysis_list(project)



List analyses for a project.  Analysis objects are used to display information about filtered media lists and/or annotations on the project detail page of the web UI. Currently only counting analysis is supported.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.

    try:
        api_response = api_instance.get_analysis_list(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_analysis_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

**list[object]**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of analyses. |  -  |
**400** | Bad request. |  -  |
**404** | Failure to find project with given ID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_type**
> AttributeType get_attribute_type(id)



Interact with an individual attribute type.  Attribute types are used to define data types that describe entities. An attribute may give information about a media, localization, or state entity  in the form of a boolean, integer, float, string, enumeration, datetime,  or geoposition. Besides the data type, attribute types define attribute defaults, bounds, and other constraints.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an attribute type.

    try:
        api_response = api_instance.get_attribute_type(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an attribute type. | 

### Return type

[**AttributeType**](AttributeType.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of attribute type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_type_list**
> list[OneOfobjectobjectobjectobjectobjectobjectobject] get_attribute_type_list(project, applies_to=applies_to)



Create or list attribute types.  Attribute types are used to define data types that describe entities. An attribute may give information about a media, localization, or state entity  in the form of a boolean, integer, float, string, enumeration, datetime,  or geoposition. Besides the data type, attribute types define attribute defaults, bounds, and other constraints.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
applies_to = 56 # int | Unique integer identifying the entity type that this attribute describes. (optional)

    try:
        api_response = api_instance.get_attribute_type_list(project, applies_to=applies_to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_attribute_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **applies_to** | **int**| Unique integer identifying the entity type that this attribute describes. | [optional] 

### Return type

[**list[OneOfobjectobjectobjectobjectobjectobjectobject]**](OneOfobjectobjectobjectobjectobjectobjectobject.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of attribute type list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clip**
> file get_clip(id, frame_ranges, quality=quality)



Facility to get a clip from the server. Returns a temporary file object that expires in 24 hours.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a media object.
frame_ranges = ['[\"0:30\",\"50:90\"]'] # list[str] | Comma-seperated list of frame ranges to capture.
quality = 56 # int | Source resolution to use (default to highest quality) (optional)

    try:
        api_response = api_instance.get_clip(id, frame_ranges, quality=quality)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_clip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media object. | 
 **frame_ranges** | [**list[str]**](str.md)| Comma-seperated list of frame ranges to capture. | 
 **quality** | **int**| Source resolution to use (default to highest quality) | [optional] 

### Return type

**file**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of video clip. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_type_schema**
> EntityTypeSchema get_entity_type_schema(id)



Output required fields for inserting a new object based on an EntityType.  Various REST calls take a polymorphic argument, which is dependent on what type is being added. This method provides a way to interrogate the service provider for what fields are required for a given addition.  The parameter to this function is the type id (i.e. the EntityTypeState or EntityTypeLocalization*** object that applies to a given media type.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an entity type.

    try:
        api_response = api_instance.get_entity_type_schema(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_entity_type_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an entity type. | 

### Return type

[**EntityTypeSchema**](EntityTypeSchema.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of entity type schema. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_frame**
> file get_frame(id, frames=frames, tile=tile, roi=roi, animate=animate, quality=quality)



Facility to get a frame(jpg/png) of a given video frame, returns a square tile of frames based on the input parameter

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a media object.
frames = [0] # list[int] | Comma-seperated list of frames to capture. (optional) (default to [0])
tile = 'tile_example' # str | wxh, if not supplied is made as squarish as possible. (optional)
roi = 'roi_example' # str | w:h:x:y, optionally crop each frame to a given roi in relative coordinates. (optional)
animate = 56 # int | If not tiling, animate each frame at a given fps in a gif. (optional)
quality = 56 # int | Source resolution to use (default to highest quality) (optional)

    try:
        api_response = api_instance.get_frame(id, frames=frames, tile=tile, roi=roi, animate=animate, quality=quality)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_frame: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media object. | 
 **frames** | [**list[int]**](int.md)| Comma-seperated list of frames to capture. | [optional] [default to [0]]
 **tile** | **str**| wxh, if not supplied is made as squarish as possible. | [optional] 
 **roi** | **str**| w:h:x:y, optionally crop each frame to a given roi in relative coordinates. | [optional] 
 **animate** | **int**| If not tiling, animate each frame at a given fps in a gif. | [optional] 
 **quality** | **int**| Source resolution to use (default to highest quality) | [optional] 

### Return type

**file**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of frame image. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_frame_association**
> dict(str, object) get_frame_association(id)



Modify a frame association.  Frame associations specify which frames that a `State` object applies to.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a frame association.

    try:
        api_response = api_instance.get_frame_association(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_frame_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a frame association. | 

### Return type

**dict(str, object)**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of frame association. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization**
> Localization get_localization(id)



Interact with single localization.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a localization.

    try:
        api_response = api_instance.get_localization(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_localization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization. | 

### Return type

[**Localization**](Localization.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of localization. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_association**
> dict(str, object) get_localization_association(id)



Modify a localization association.  Localization associations specify which localizations that a `State` object applies to.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a localization association.

    try:
        api_response = api_instance.get_localization_association(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_localization_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization association. | 

### Return type

**dict(str, object)**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of localization association. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_list**
> list[LocalizationElement] get_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of localizations.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = 56 # int | Unique integer identifying a version. (optional)
modified = 56 # int | Whether to return original or modified annotations, 0 or 1. (optional)
after = 56 # int | If given, all results returned will be after the localization with this ID. The `start` and `stop` parameters are relative to this modified range. (optional)
search = '\"My search string\"' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
        print("Exception when calling TatorApi->get_localization_list: %s\n" % e)
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

[**list[LocalizationElement]**](LocalizationElement.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of localization list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_type**
> InlineResponse200 get_localization_type(id)



Interact with an individual localization type.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an localization type.

    try:
        api_response = api_instance.get_localization_type(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_localization_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an localization type. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of localization type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_type_list**
> list[InlineResponse200] get_localization_type_list(project, media_id=media_id, type=type)



Create or retrieve localization types.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_id = [56] # list[int] | List of unique integers identifying a media. (optional)
type = 56 # int | Deprecated. Use `LocalizationType` endpoint to retrieve individual localization type by ID. (optional)

    try:
        api_response = api_instance.get_localization_type_list(project, media_id=media_id, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_localization_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_id** | [**list[int]**](int.md)| List of unique integers identifying a media. | [optional] 
 **type** | **int**| Deprecated. Use &#x60;LocalizationType&#x60; endpoint to retrieve individual localization type by ID. | [optional] 

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of localization type list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media**
> InlineResponse2001 get_media(id)



Interact with individual media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a media.

    try:
        api_response = api_instance.get_media(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of media. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_list**
> list[InlineResponse2001] get_media_list(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  This endpoint does not include a POST method. Creating media must be preceded by an upload, after which a separate media creation endpoint must be called. The media creation endpoints are `Transcode` to launch a transcode of an uploaded video and `SaveImage` to save an uploaded image. If you would like to perform transcodes on local assets, you can use the `SaveVideo` endpoint to save an already transcoded video. Local transcodes may be performed with the script at `scripts/transcoder/transcodePipeline.py` in the Tator source code.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_id = [56] # list[int] | List of integers identifying media. (optional)
type = 56 # int | Unique integer identifying media type. (optional)
name = 'name_example' # str | Name of the media to filter on. (optional)
md5 = 'md5_example' # str | MD5 sum of the media file. (optional)
after = 'after_example' # str | If given, all results returned will be after the file with this filename. The `start` and `stop` parameters are relative to this modified range. (optional)
search = '\"My search string\"' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
        print("Exception when calling TatorApi->get_media_list: %s\n" % e)
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

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of media list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_next**
> InlineResponse2002 get_media_next(id, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve ID of next media in a media list.  This endpoint accepts the same query parameters as a GET request to the `Medias` endpoint, but only returns the next media ID from the media passed as a path parameter. This allows iteration through a media list without serializing the entire list, which may be large.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a media object.
media_id = [56] # list[int] | List of integers identifying media. (optional)
type = 56 # int | Unique integer identifying media type. (optional)
name = 'name_example' # str | Name of the media to filter on. (optional)
md5 = 'md5_example' # str | MD5 sum of the media file. (optional)
after = 'after_example' # str | If given, all results returned will be after the file with this filename. The `start` and `stop` parameters are relative to this modified range. (optional)
search = '\"My search string\"' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
        print("Exception when calling TatorApi->get_media_next: %s\n" % e)
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

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ID of next media in the list corresponding to query. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_prev**
> InlineResponse2003 get_media_prev(id, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve ID of previous media in a media list.  This endpoint accepts the same query parameters as a GET request to the `Medias` endpoint, but only returns the previous media ID from the media passed as a path parameter. This  allows iteration through a media list without serializing the entire list, which may be  large.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a media object.
media_id = [56] # list[int] | List of integers identifying media. (optional)
type = 56 # int | Unique integer identifying media type. (optional)
name = 'name_example' # str | Name of the media to filter on. (optional)
md5 = 'md5_example' # str | MD5 sum of the media file. (optional)
after = 'after_example' # str | If given, all results returned will be after the file with this filename. The `start` and `stop` parameters are relative to this modified range. (optional)
search = '\"My search string\"' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
        print("Exception when calling TatorApi->get_media_prev: %s\n" % e)
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

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ID of previous media in the list corresponding to query. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_sections**
> dict(str, InlineResponse2004) get_media_sections(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve media counts by section.  This endpoint accepts the same query parameters as a GET request to the `Medias` endpoint, but only returns the number of images and videos per sections.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_id = [56] # list[int] | List of integers identifying media. (optional)
type = 56 # int | Unique integer identifying media type. (optional)
name = 'name_example' # str | Name of the media to filter on. (optional)
md5 = 'md5_example' # str | MD5 sum of the media file. (optional)
after = 'after_example' # str | If given, all results returned will be after the file with this filename. The `start` and `stop` parameters are relative to this modified range. (optional)
search = '\"My search string\"' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
        print("Exception when calling TatorApi->get_media_sections: %s\n" % e)
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

[**dict(str, InlineResponse2004)**](InlineResponse2004.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of media count per section. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_type**
> InlineResponse2005 get_media_type(id)



Interact with an individual media type.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an media type.

    try:
        api_response = api_instance.get_media_type(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_media_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an media type. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of media type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_type_list**
> list[InlineResponse2005] get_media_type_list(project)



Create or retrieve localization types.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.

    try:
        api_response = api_instance.get_media_type_list(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_media_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**list[InlineResponse2005]**](InlineResponse2005.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of media type list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership**
> InlineResponse2006 get_membership(id)



Interact with an individual project membership.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels. `View Only` can only view a project and not change any data. `Can Edit` can create, modify, and delete annotations. `Can Transfer` can upload and download media. `Can Execute` can launch algorithm workflows. `Full Control` can change project settings, including inviting new members, project name, and project metadata schema.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a membership.

    try:
        api_response = api_instance.get_membership(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a membership. | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of membership. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership_list**
> list[InlineResponse2006] get_membership_list(project)



Create or retrieve a list of project memberships.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels. `View Only` can only view a project and not change any data. `Can Edit` can create, modify, and delete annotations. `Can Transfer` can upload and download media. `Can Execute` can launch algorithm workflows. `Full Control` can change project settings, including inviting new members, project name, and project metadata schema.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.

    try:
        api_response = api_instance.get_membership_list(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_membership_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**list[InlineResponse2006]**](InlineResponse2006.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of membership list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> InlineResponse2007 get_project(id)



Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a project.

    try:
        api_response = api_instance.get_project(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a project. | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of project. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_list**
> list[InlineResponse2007] get_project_list()



Interact with a list of projects.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Project lists return all projects that the requesting user has access to.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    
    try:
        api_response = api_instance.get_project_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_project_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2007]**](InlineResponse2007.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of project list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section_analysis**
> dict(str, object) get_section_analysis(project, media_id=media_id, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve analysis results for a media list.  This endpoint uses objects created with the `Analysis` endpoint to perform analysis on filtered media lists.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_id = [56] # list[int] | Unique integer identifying a media. Use this to do analyis on a single file instead of sections. (optional)
search = '\"My search string\"' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
        api_response = api_instance.get_section_analysis(project, media_id=media_id, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_section_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_id** | [**list[int]**](int.md)| Unique integer identifying a media. Use this to do analyis on a single file instead of sections. | [optional] 
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of section analysis. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state**
> get_state(id)



Interact with an individual state.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a types of entity in Tator, meaning they can be described by user defined attributes.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a state.

    try:
        api_instance.get_state(id)
    except ApiException as e:
        print("Exception when calling TatorApi->get_state: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_list**
> list[InlineResponse2009] get_state_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with list of states.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined state attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  It is importarant to know the fields required for a given entity_type_id as they are expected in the request data for this function. As an example, if the entity_type_id has attribute types associated with it named time and position, the JSON object must have them specified as keys.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = 56 # int | Unique integer identifying a version. (optional)
modified = 56 # int | Whether to return original or modified annotations, 0 or 1. (optional)
after = 56 # int | If given, all results returned will be after the localization with this ID. The `start` and `stop` parameters are relative to this modified range. (optional)
search = '\"My search string\"' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
        print("Exception when calling TatorApi->get_state_list: %s\n" % e)
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

[**list[InlineResponse2009]**](InlineResponse2009.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of state list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_type**
> InlineResponse2008 get_state_type(id)



Interact with an individual state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a state type.

    try:
        api_response = api_instance.get_state_type(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_state_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state type. | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of state type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_type_list**
> list[InlineResponse2008] get_state_type_list(project, media_id=media_id, type=type)



Create or retrieve state types.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_id = [56] # list[int] | List of unique integers identifying a media. (optional)
type = 56 # int | Deprecated. Use `LocalizationType` endpoint to retrieve individual localization type by ID. (optional)

    try:
        api_response = api_instance.get_state_type_list(project, media_id=media_id, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_state_type_list: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of state type list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_file**
> object get_temporary_file(id)



Interact with temporary file.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 'id_example' # str | A unique integer value identifying this temporary file.

    try:
        api_response = api_instance.get_temporary_file(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_temporary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this temporary file. | 

### Return type

**object**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_file_list**
> object get_temporary_file_list(project, expired=expired)



Interact with temporary file list.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
expired = 0 # int | If greater than 0 will return only expired files (optional) (default to 0)

    try:
        api_response = api_instance.get_temporary_file_list(project, expired=expired)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_temporary_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **expired** | **int**| If greater than 0 will return only expired files | [optional] [default to 0]

### Return type

**object**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree_leaf**
> InlineResponse20011 get_tree_leaf(id)



Interact with individual tree leaf.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a tree leaf.

    try:
        api_response = api_instance.get_tree_leaf(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_tree_leaf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a tree leaf. | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of tree leaf. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree_leaf_list**
> list[InlineResponse20011] get_tree_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Interact with a list of tree leaves.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
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
        print("Exception when calling TatorApi->get_tree_leaf_list: %s\n" % e)
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

[**list[InlineResponse20011]**](InlineResponse20011.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of tree leaf list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree_leaf_type**
> InlineResponse20012 get_tree_leaf_type(id)



Interact with individual tree leaf type.  A tree leaf type is the metadata definition object for a tree leaf. It includes name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an tree_leaf type.

    try:
        api_response = api_instance.get_tree_leaf_type(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_tree_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an tree_leaf type. | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of tree leaf type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree_leaf_type_list**
> list[InlineResponse20012] get_tree_leaf_type_list(project)



Interact with tree leaf type list.  A tree leaf type is the metadata definition object for a tree leaf. It includes name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.

    try:
        api_response = api_instance.get_tree_leaf_type_list(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_tree_leaf_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**list[InlineResponse20012]**](InlineResponse20012.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of tree leaf type list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> object get_user(id)



Interact with an individual user.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a localization association.

    try:
        api_response = api_instance.get_user(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization association. | 

### Return type

**object**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> InlineResponse20015 get_version(id)



Interact with individual version.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a version.

    try:
        api_response = api_instance.get_version(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a version. | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of version. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify**
> notify(inline_object9=inline_object9)



Send a notification to administrators.  Uses the Slack API to send a notification to system administrators. This endpoint can only be used by system administrators and must be configured in a Tator deployment's settings.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    inline_object9 = tator.InlineObject9() # InlineObject9 |  (optional)

    try:
        api_instance.notify(inline_object9=inline_object9)
    except ApiException as e:
        print("Exception when calling TatorApi->notify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object9** | [**InlineObject9**](InlineObject9.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Message sent successfully. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |
**503** | Service not available. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_save_video_api**
> partial_update_save_video_api(project, video_update=video_update)



Saves a transcoded video.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. To launch a transcode on raw uploaded video, use the  `Transcode` endpoint, which will create an Argo workflow to perform the transcode and save the video using this endpoint; no further REST calls are required. However, if you would like to perform transcodes locally, this endpoint enables that. The script at `scripts/transcoder/transcodePipeline.py` in the Tator source code provides an example of how to transcode a Tator-compatible video, upload it, and save it to the database using this endpoint.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
video_update = tator.VideoUpdate() # VideoUpdate |  (optional)

    try:
        api_instance.partial_update_save_video_api(project, video_update=video_update)
    except ApiException as e:
        print("Exception when calling TatorApi->partial_update_save_video_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **video_update** | [**VideoUpdate**](VideoUpdate.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **progress**
> MessageResponse progress(project, inline_object=inline_object)



Broadcast progress update.  Progress messages are sent in the web UI via WebSocket, and are displayed as progress bars associated with individual media files and as a summary in the webpage header. All members of a project can see progress bars from uploads and background jobs initiated by other users within the project. This endpoint accepts an array of messages, allowing for progress messages to be batched into a single request.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
inline_object = [{"gid":"b722e83e-8272-11ea-8e10-000c294f07cf","job_type":"algorithm","media_ids":"1,2","message":"Job started!","name":"name_of_file.mp4","progress":70,"sections":"Section 1,Section 2","state":"started","uid":"b43d7e54-8272-11ea-8e10-000c294f07cf"}] # list[InlineObject] |  (optional)

    try:
        api_response = api_instance.progress(project, inline_object=inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **inline_object** | [**list[InlineObject]**](InlineObject.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful creation of progress message. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_state_graphic_api**
> file retrieve_state_graphic_api(id, mode=mode, fps=fps, force_scale=force_scale)



Get frame(s) of a given localization-associated state.  Use the mode argument to control whether it is an animated gif or a tiled jpg.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a state.
mode = 'animate' # str | Whether to animate or tile. (optional) (default to 'animate')
fps = 2 # float | Frame rate if `mode` is `animate`. (optional) (default to 2)
force_scale = '240x240' # str | wxh to force each tile prior to stich (optional)

    try:
        api_response = api_instance.retrieve_state_graphic_api(id, mode=mode, fps=fps, force_scale=force_scale)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->retrieve_state_graphic_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state. | 
 **mode** | **str**| Whether to animate or tile. | [optional] [default to &#39;animate&#39;]
 **fps** | **float**| Frame rate if &#x60;mode&#x60; is &#x60;animate&#x60;. | [optional] [default to 2]
 **force_scale** | **str**| wxh to force each tile prior to stich | [optional] 

### Return type

**file**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of state graphic. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_version_list**
> list[InlineResponse20015] retrieve_version_list(project, media_id=media_id)



Interact with a list of versions.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_id = 56 # int | Unique integer identifying a media. (optional)

    try:
        api_response = api_instance.retrieve_version_list(project, media_id=media_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->retrieve_version_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_id** | **int**| Unique integer identifying a media. | [optional] 

### Return type

[**list[InlineResponse20015]**](InlineResponse20015.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of version list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_image**
> CreateResponse save_image(project, inline_object12=inline_object12)



Saves an uploaded image.  Media is uploaded via tus, a separate mechanism from the REST API. Once an image upload is complete, the image must be saved to the database using this endpoint.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
inline_object12 = tator.InlineObject12() # InlineObject12 |  (optional)

    try:
        api_response = api_instance.save_image(project, inline_object12=inline_object12)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->save_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **inline_object12** | [**InlineObject12**](InlineObject12.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of image. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_video**
> CreateResponse save_video(project, video_spec=video_spec)



Saves a transcoded video.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. To launch a transcode on raw uploaded video, use the  `Transcode` endpoint, which will create an Argo workflow to perform the transcode and save the video using this endpoint; no further REST calls are required. However, if you would like to perform transcodes locally, this endpoint enables that. The script at `scripts/transcoder/transcodePipeline.py` in the Tator source code provides an example of how to transcode a Tator-compatible video, upload it, and save it to the database using this endpoint.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
video_spec = tator.VideoSpec() # VideoSpec |  (optional)

    try:
        api_response = api_instance.save_video(project, video_spec=video_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->save_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **video_spec** | [**VideoSpec**](VideoSpec.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of video. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcode**
> InlineResponse2013 transcode(project, inline_object19=inline_object19)



Start a transcode.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. This endpoint launches a transcode on raw uploaded video by creating an Argo workflow. The workflow will download the uploaded raw video, transcode it to the proper format, upload the transcoded video, and save the video using the  `SaveVideo` endpoint. Optionally, depending on the `keep_original` field of the video  type specified by the `type` parameter, the originally uploaded file may also be saved. Note that the raw video must be uploaded first via tus, which is a separate mechanism  from the REST API. This endpoint requires a group and run UUID associated with this  upload. If no progress messages were generated during upload, then the group and run  UUIDs can be newly generated.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
inline_object19 = tator.InlineObject19() # InlineObject19 |  (optional)

    try:
        api_response = api_instance.transcode(project, inline_object19=inline_object19)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->transcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **inline_object19** | [**InlineObject19**](InlineObject19.md)|  | [optional] 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful save of the video in the database. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tree_leaf_suggestion**
> list[InlineResponse20013] tree_leaf_suggestion(project, ancestor, query, min_level=min_level)



Rest Endpoint compatible with devbridge suggestion format.  <https://github.com/kraaden/autocomplete>

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
ancestor = 'ancestor_example' # str | Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia).
query = 'query_example' # str | String to search for matching names.
min_level = 56 # int | Integer specifying level of results that may be returned. For example, 2 refers to grandchildren of the level specified by the `ancestor` parameter. (optional)

    try:
        api_response = api_instance.tree_leaf_suggestion(project, ancestor, query, min_level=min_level)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->tree_leaf_suggestion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **ancestor** | **str**| Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia). | 
 **query** | **str**| String to search for matching names. | 
 **min_level** | **int**| Integer specifying level of results that may be returned. For example, 2 refers to grandchildren of the level specified by the &#x60;ancestor&#x60; parameter. | [optional] 

### Return type

[**list[InlineResponse20013]**](InlineResponse20013.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of suggestions. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute_type**
> MessageResponse update_attribute_type(id, attribute_type_update=attribute_type_update)



Updates a localization type.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an attribute type.
attribute_type_update = {"description":"New description","name":"New name"} # AttributeTypeUpdate |  (optional)

    try:
        api_response = api_instance.update_attribute_type(id, attribute_type_update=attribute_type_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an attribute type. | 
 **attribute_type_update** | [**AttributeTypeUpdate**](AttributeTypeUpdate.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of attribute type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_frame_association**
> MessageResponse update_frame_association(id, inline_object=inline_object)



Modify a frame association.  Frame associations specify which frames that a `State` object applies to.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a frame association.
inline_object = tator.InlineObject() # InlineObject |  (optional)

    try:
        api_response = api_instance.update_frame_association(id, inline_object=inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_frame_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a frame association. | 
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of frame association. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization**
> MessageResponse update_localization(id, localization_update=localization_update)



Interact with single localization.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a localization.
localization_update = {"height":0.25,"width":0.25,"x":0.25,"y":0.25} # LocalizationUpdate |  (optional)

    try:
        api_response = api_instance.update_localization(id, localization_update=localization_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_localization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization. | 
 **localization_update** | [**LocalizationUpdate**](LocalizationUpdate.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of localization. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization_association**
> MessageResponse update_localization_association(id, localization_association_update=localization_association_update)



Modify a localization association.  Localization associations specify which localizations that a `State` object applies to.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a localization association.
localization_association_update = {"color":"#03a1fc","localizations":[1,5,10]} # LocalizationAssociationUpdate |  (optional)

    try:
        api_response = api_instance.update_localization_association(id, localization_association_update=localization_association_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_localization_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization association. | 
 **localization_association_update** | [**LocalizationAssociationUpdate**](LocalizationAssociationUpdate.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of localization association. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization_list**
> MessageResponse update_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, attribute_bulk_update=attribute_bulk_update)



Interact with list of localizations.  Localizations are shape annotations drawn on a video or image. They are currently of type box, line, or dot. Each shape has slightly different data members. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = 56 # int | Unique integer identifying a version. (optional)
modified = 56 # int | Whether to return original or modified annotations, 0 or 1. (optional)
after = 56 # int | If given, all results returned will be after the localization with this ID. The `start` and `stop` parameters are relative to this modified range. (optional)
search = '\"My search string\"' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
attribute_bulk_update = {"attributes":{"Species":"Tuna"}} # AttributeBulkUpdate |  (optional)

    try:
        api_response = api_instance.update_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, attribute_bulk_update=attribute_bulk_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_localization_list: %s\n" % e)
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
 **attribute_bulk_update** | [**AttributeBulkUpdate**](AttributeBulkUpdate.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of localization list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization_type**
> MessageResponse update_localization_type(id, inline_object1=inline_object1)



Updates a localization type.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an localization type.
inline_object1 = tator.InlineObject1() # InlineObject1 |  (optional)

    try:
        api_response = api_instance.update_localization_type(id, inline_object1=inline_object1)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_localization_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an localization type. | 
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of localization type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_media**
> MessageResponse update_media(id, inline_object3=inline_object3)



Interact with individual media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a media.
inline_object3 = tator.InlineObject3() # InlineObject3 |  (optional)

    try:
        api_response = api_instance.update_media(id, inline_object3=inline_object3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media. | 
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of media. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_media_list**
> MessageResponse update_media_list(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, inline_object6=inline_object6)



Interact with list of media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined localization attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  This endpoint does not include a POST method. Creating media must be preceded by an upload, after which a separate media creation endpoint must be called. The media creation endpoints are `Transcode` to launch a transcode of an uploaded video and `SaveImage` to save an uploaded image. If you would like to perform transcodes on local assets, you can use the `SaveVideo` endpoint to save an already transcoded video. Local transcodes may be performed with the script at `scripts/transcoder/transcodePipeline.py` in the Tator source code.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_id = [56] # list[int] | List of integers identifying media. (optional)
type = 56 # int | Unique integer identifying media type. (optional)
name = 'name_example' # str | Name of the media to filter on. (optional)
md5 = 'md5_example' # str | MD5 sum of the media file. (optional)
after = 'after_example' # str | If given, all results returned will be after the file with this filename. The `start` and `stop` parameters are relative to this modified range. (optional)
search = '\"My search string\"' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
inline_object6 = tator.InlineObject6() # InlineObject6 |  (optional)

    try:
        api_response = api_instance.update_media_list(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, inline_object6=inline_object6)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_media_list: %s\n" % e)
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
 **inline_object6** | [**InlineObject6**](InlineObject6.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of media list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_media_type**
> MessageResponse update_media_type(id, inline_object4=inline_object4)



Interact with an individual media type.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an media type.
inline_object4 = tator.InlineObject4() # InlineObject4 |  (optional)

    try:
        api_response = api_instance.update_media_type(id, inline_object4=inline_object4)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_media_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an media type. | 
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of media type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_membership**
> MessageResponse update_membership(id, inline_object7=inline_object7)



Interact with an individual project membership.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels. `View Only` can only view a project and not change any data. `Can Edit` can create, modify, and delete annotations. `Can Transfer` can upload and download media. `Can Execute` can launch algorithm workflows. `Full Control` can change project settings, including inviting new members, project name, and project metadata schema.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a membership.
inline_object7 = tator.InlineObject7() # InlineObject7 |  (optional)

    try:
        api_response = api_instance.update_membership(id, inline_object7=inline_object7)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a membership. | 
 **inline_object7** | [**InlineObject7**](InlineObject7.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of membership. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> MessageResponse update_project(id, inline_object10=inline_object10)



Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a project.
inline_object10 = tator.InlineObject10() # InlineObject10 |  (optional)

    try:
        api_response = api_instance.update_project(id, inline_object10=inline_object10)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a project. | 
 **inline_object10** | [**InlineObject10**](InlineObject10.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of project. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_state**
> MessageResponse update_state(id, inline_object13=inline_object13)



Interact with an individual state.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a types of entity in Tator, meaning they can be described by user defined attributes.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a state.
inline_object13 = tator.InlineObject13() # InlineObject13 |  (optional)

    try:
        api_response = api_instance.update_state(id, inline_object13=inline_object13)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state. | 
 **inline_object13** | [**InlineObject13**](InlineObject13.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of state. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_state_list**
> MessageResponse update_state_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, inline_object16=inline_object16)



Interact with list of states.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes.  This endpoint supports bulk patch of user-defined state attributes and bulk delete. Both are accomplished using the same query parameters used for a GET request.  It is importarant to know the fields required for a given entity_type_id as they are expected in the request data for this function. As an example, if the entity_type_id has attribute types associated with it named time and position, the JSON object must have them specified as keys.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = 56 # int | Unique integer identifying a version. (optional)
modified = 56 # int | Whether to return original or modified annotations, 0 or 1. (optional)
after = 56 # int | If given, all results returned will be after the localization with this ID. The `start` and `stop` parameters are relative to this modified range. (optional)
search = '\"My search string\"' # str | Lucene query syntax string for use with Elasticsearch. See `reference <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_. (optional)
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
inline_object16 = tator.InlineObject16() # InlineObject16 |  (optional)

    try:
        api_response = api_instance.update_state_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, inline_object16=inline_object16)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_state_list: %s\n" % e)
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
 **inline_object16** | [**InlineObject16**](InlineObject16.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of state list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_state_type**
> MessageResponse update_state_type(id, inline_object14=inline_object14)



Interact with an individual state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a state type.
inline_object14 = tator.InlineObject14() # InlineObject14 |  (optional)

    try:
        api_response = api_instance.update_state_type(id, inline_object14=inline_object14)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_state_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state type. | 
 **inline_object14** | [**InlineObject14**](InlineObject14.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of state type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tree_leaf**
> MessageResponse update_tree_leaf(id, inline_object20=inline_object20)



Interact with individual tree leaf.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a tree leaf.
inline_object20 = tator.InlineObject20() # InlineObject20 |  (optional)

    try:
        api_response = api_instance.update_tree_leaf(id, inline_object20=inline_object20)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_tree_leaf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a tree leaf. | 
 **inline_object20** | [**InlineObject20**](InlineObject20.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of tree leaf. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tree_leaf_list**
> MessageResponse update_tree_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, inline_object23=inline_object23)



Interact with a list of tree leaves.  Tree leaves are used to define label hierarchies that can be used for autocompletion of string attribute types.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
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
inline_object23 = tator.InlineObject23() # InlineObject23 |  (optional)

    try:
        api_response = api_instance.update_tree_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, inline_object23=inline_object23)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_tree_leaf_list: %s\n" % e)
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
 **inline_object23** | [**InlineObject23**](InlineObject23.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of tree leaf list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tree_leaf_type**
> MessageResponse update_tree_leaf_type(id, inline_object21=inline_object21)



Updates a tree leaf type.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an tree_leaf type.
inline_object21 = tator.InlineObject21() # InlineObject21 |  (optional)

    try:
        api_response = api_instance.update_tree_leaf_type(id, inline_object21=inline_object21)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_tree_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an tree_leaf type. | 
 **inline_object21** | [**InlineObject21**](InlineObject21.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of tree leaf type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> object update_user(id, unknown_base_type=unknown_base_type)



Interact with an individual user.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a localization association.
unknown_base_type = tator.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

    try:
        api_response = api_instance.update_user(id, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization association. | 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

**object**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version**
> MessageResponse update_version(id, inline_object24=inline_object24)



Interact with individual version.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a version.
inline_object24 = tator.InlineObject24() # InlineObject24 |  (optional)

    try:
        api_response = api_instance.update_version(id, inline_object24=inline_object24)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a version. | 
 **inline_object24** | [**InlineObject24**](InlineObject24.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of version. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **who_am_i**
> InlineResponse20014 who_am_i()



Returns the current user.  This is the equivalent of a whoami() operation.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator
from tator.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    
    try:
        api_response = api_instance.who_am_i()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->who_am_i: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of user who sent request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

