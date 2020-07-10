# tator_openapi.TatorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**algorithm_launch**](TatorApi.md#algorithm_launch) | **POST** /rest/AlgorithmLaunch/{project} | 
[**create_analysis**](TatorApi.md#create_analysis) | **POST** /rest/Analyses/{project} | 
[**create_leaf_list**](TatorApi.md#create_leaf_list) | **POST** /rest/Leaves/{project} | 
[**create_leaf_type**](TatorApi.md#create_leaf_type) | **POST** /rest/LeafTypes/{project} | 
[**create_localization_list**](TatorApi.md#create_localization_list) | **POST** /rest/Localizations/{project} | 
[**create_localization_type**](TatorApi.md#create_localization_type) | **POST** /rest/LocalizationTypes/{project} | 
[**create_media**](TatorApi.md#create_media) | **POST** /rest/Medias/{project} | 
[**create_media_type**](TatorApi.md#create_media_type) | **POST** /rest/MediaTypes/{project} | 
[**create_membership**](TatorApi.md#create_membership) | **POST** /rest/Memberships/{project} | 
[**create_obtain_auth_token**](TatorApi.md#create_obtain_auth_token) | **POST** /rest/Token | 
[**create_progress_summary_api**](TatorApi.md#create_progress_summary_api) | **POST** /rest/ProgressSummary/{project} | 
[**create_project**](TatorApi.md#create_project) | **POST** /rest/Projects | 
[**create_state_list**](TatorApi.md#create_state_list) | **POST** /rest/States/{project} | 
[**create_state_type**](TatorApi.md#create_state_type) | **POST** /rest/StateTypes/{project} | 
[**create_temporary_file**](TatorApi.md#create_temporary_file) | **POST** /rest/TemporaryFiles/{project} | 
[**create_version**](TatorApi.md#create_version) | **POST** /rest/Versions/{project} | 
[**delete_algorithm**](TatorApi.md#delete_algorithm) | **DELETE** /rest/Algorithm/{id} | 
[**delete_job**](TatorApi.md#delete_job) | **DELETE** /rest/Job/{run_uid} | 
[**delete_job_group**](TatorApi.md#delete_job_group) | **DELETE** /rest/JobGroup/{group_id} | 
[**delete_leaf**](TatorApi.md#delete_leaf) | **DELETE** /rest/Leaf/{id} | 
[**delete_leaf_list**](TatorApi.md#delete_leaf_list) | **DELETE** /rest/Leaves/{project} | 
[**delete_leaf_type**](TatorApi.md#delete_leaf_type) | **DELETE** /rest/LeafType/{id} | 
[**delete_localization**](TatorApi.md#delete_localization) | **DELETE** /rest/Localization/{id} | 
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
[**delete_version**](TatorApi.md#delete_version) | **DELETE** /rest/Version/{id} | 
[**get_algorithm_list**](TatorApi.md#get_algorithm_list) | **GET** /rest/Algorithms/{project} | 
[**get_analysis_list**](TatorApi.md#get_analysis_list) | **GET** /rest/Analyses/{project} | 
[**get_clip**](TatorApi.md#get_clip) | **GET** /rest/GetClip/{id} | 
[**get_frame**](TatorApi.md#get_frame) | **GET** /rest/GetFrame/{id} | 
[**get_leaf**](TatorApi.md#get_leaf) | **GET** /rest/Leaf/{id} | 
[**get_leaf_list**](TatorApi.md#get_leaf_list) | **GET** /rest/Leaves/{project} | 
[**get_leaf_type**](TatorApi.md#get_leaf_type) | **GET** /rest/LeafType/{id} | 
[**get_leaf_type_list**](TatorApi.md#get_leaf_type_list) | **GET** /rest/LeafTypes/{project} | 
[**get_localization**](TatorApi.md#get_localization) | **GET** /rest/Localization/{id} | 
[**get_localization_graphic**](TatorApi.md#get_localization_graphic) | **GET** /rest/LocalizationGraphic/{id} | 
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
[**get_state_graphic**](TatorApi.md#get_state_graphic) | **GET** /rest/StateGraphic/{id} | 
[**get_state_list**](TatorApi.md#get_state_list) | **GET** /rest/States/{project} | 
[**get_state_type**](TatorApi.md#get_state_type) | **GET** /rest/StateType/{id} | 
[**get_state_type_list**](TatorApi.md#get_state_type_list) | **GET** /rest/StateTypes/{project} | 
[**get_temporary_file**](TatorApi.md#get_temporary_file) | **GET** /rest/TemporaryFile/{id} | 
[**get_temporary_file_list**](TatorApi.md#get_temporary_file_list) | **GET** /rest/TemporaryFiles/{project} | 
[**get_user**](TatorApi.md#get_user) | **GET** /rest/User/{id} | 
[**get_version**](TatorApi.md#get_version) | **GET** /rest/Version/{id} | 
[**get_version_list**](TatorApi.md#get_version_list) | **GET** /rest/Versions/{project} | 
[**leaf_suggestion**](TatorApi.md#leaf_suggestion) | **GET** /rest/Leaves/Suggestion/{ancestor}/{project} | 
[**move_video**](TatorApi.md#move_video) | **POST** /rest/MoveVideo/{id} | 
[**notify**](TatorApi.md#notify) | **POST** /rest/Notify | 
[**progress**](TatorApi.md#progress) | **POST** /rest/Progress/{project} | 
[**register_algorithm**](TatorApi.md#register_algorithm) | **POST** /rest/Algorithms/{project} | 
[**save_algorithm_manifest**](TatorApi.md#save_algorithm_manifest) | **POST** /rest/SaveAlgorithmManifest/{project} | 
[**transcode**](TatorApi.md#transcode) | **POST** /rest/Transcode/{project} | 
[**update_leaf**](TatorApi.md#update_leaf) | **PATCH** /rest/Leaf/{id} | 
[**update_leaf_list**](TatorApi.md#update_leaf_list) | **PATCH** /rest/Leaves/{project} | 
[**update_leaf_type**](TatorApi.md#update_leaf_type) | **PATCH** /rest/LeafType/{id} | 
[**update_localization**](TatorApi.md#update_localization) | **PATCH** /rest/Localization/{id} | 
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
[**update_user**](TatorApi.md#update_user) | **PATCH** /rest/User/{id} | 
[**update_version**](TatorApi.md#update_version) | **PATCH** /rest/Version/{id} | 
[**whoami**](TatorApi.md#whoami) | **GET** /rest/User/GetCurrent | 


# **algorithm_launch**
> AlgorithmLaunch algorithm_launch(project, algorithm_launch_spec)



Launch a registered algorithm.  This will create one or more Argo workflows that execute the named algorithm registration. To get a list of available algorithms, use the `Algorithms` endpoint. A media list will be submitted for processing using either a query string or  a list of media IDs. If neither are included, the algorithm will be launched on all media in the project.   Media is divided into batches for based on the `files_per_job` field of the  `Algorithm` object. One batch is submitted to each Argo workflow.  Submitted algorithm jobs may be cancelled via the `Job` or `JobGroup` endpoints. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
algorithm_launch_spec = {"algorithm_name":"My Algorithm","media_ids":[1,5,10]} # AlgorithmLaunchSpec | 

    try:
        api_response = api_instance.algorithm_launch(project, algorithm_launch_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->algorithm_launch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **algorithm_launch_spec** | [**AlgorithmLaunchSpec**](AlgorithmLaunchSpec.md)|  | 

### Return type

[**AlgorithmLaunch**](AlgorithmLaunch.md)

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
> CreateResponse create_analysis(project, analysis_spec)



Create analysis.  Analysis objects are used to display information about filtered media lists and/or annotations on the project detail page of the web UI. Currently only counting analysis is supported. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
analysis_spec = {"data_query":"_meta:1","name":"Boxes"} # AnalysisSpec | 

    try:
        api_response = api_instance.create_analysis(project, analysis_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **analysis_spec** | [**AnalysisSpec**](AnalysisSpec.md)|  | 

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

# **create_leaf_list**
> CreateListResponse create_leaf_list(project, leaf_spec)



Create leaf list.  Leaves are used to define label hierarchies that can be used for autocompletion of string attribute types. Leaves are a type of entity in Tator, meaning they can be described by user-defined attributes.   This method does a bulk create on a list of `LeafSpec` objects. A  maximum of 500 leaves may be created in one request. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
leaf_spec = [tator_openapi.LeafSpec()] # list[LeafSpec] | 

    try:
        api_response = api_instance.create_leaf_list(project, leaf_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_leaf_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **leaf_spec** | [**list[LeafSpec]**](LeafSpec.md)|  | 

### Return type

[**CreateListResponse**](CreateListResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of leaf. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_leaf_type**
> CreateResponse create_leaf_type(project, leaf_type_spec)



Create leaf type.  A leaf type is the metadata definition object for a leaf. It includes name, description, and may have any number of user-defined attribute types associated with it. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
leaf_type_spec = {"attribute_types":[{"default":false,"dtype":"bool","name":"My Boolean"},{"default":0,"dtype":"int","maximum":1,"minimum":-1,"name":"My Integer"},{"default":0.0,"dtype":"float","maximum":1.0,"minimum":-1.0,"name":"My Float"},{"choices":["a","b","c"],"default":"a","dtype":"enum","labels":["a","b","c"],"name":"My Enumeration"},{"autocomplete":{"serviceUrl":"https://www.example.com/suggestion"},"default":"---","dtype":"string","name":"My String"},{"dtype":"datetime","name":"My Datetime","use_current":true},{"default":[-179.0,90.0],"dtype":"geopos","name":"My Geoposition"}],"name":"My leaf type"} # LeafTypeSpec | 

    try:
        api_response = api_instance.create_leaf_type(project, leaf_type_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **leaf_type_spec** | [**LeafTypeSpec**](LeafTypeSpec.md)|  | 

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
**201** | Successful creation of leaf type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_localization_list**
> CreateListResponse create_localization_list(project, localization_spec)



Create localiazation list.  Localizations are shape annotations drawn on a video or image. Available shapes (`dtype`) are  box, line, or dot. Each shape is parameterized by a different subset of data members: - `box` uses `x`, `y`, `width`, `height`. - `line` uses `x`, `y`, `u`, `v`. - `dot` uses `x` and `y`.  Geometry members may be left null when creating a localization, in which case the shapes may be  drawn later using the redraw capability in the web UI. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.   This method does a bulk create on a list of `LocalizationSpec` objects. A  maximum of 500 localizations may be created in one request. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
localization_spec = [{"My First Attribute":"value1","My Second Attribute":"value2","frame":1000,"height":0.4,"media_id":1,"type":1,"width":0.3,"x":0.1,"y":0.2}] # list[LocalizationSpec] | 

    try:
        api_response = api_instance.create_localization_list(project, localization_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_localization_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **localization_spec** | [**list[LocalizationSpec]**](LocalizationSpec.md)|  | 

### Return type

[**CreateListResponse**](CreateListResponse.md)

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
> CreateResponse create_localization_type(project, localization_type_spec)



Create localization type.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and may have any number of user-defined attribute types associated with it. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
localization_type_spec = {"attribute_types":[{"default":false,"dtype":"bool","name":"My Boolean"},{"default":0,"dtype":"int","maximum":1,"minimum":-1,"name":"My Integer"},{"default":0.0,"dtype":"float","maximum":1.0,"minimum":-1.0,"name":"My Float"},{"choices":["a","b","c"],"default":"a","dtype":"enum","labels":["a","b","c"],"name":"My Enumeration"},{"autocomplete":{"serviceUrl":"https://www.example.com/suggestion"},"default":"---","dtype":"string","name":"My String"},{"dtype":"datetime","name":"My Datetime","use_current":true},{"default":[-179.0,90.0],"dtype":"geopos","name":"My Geoposition"}],"dtype":"box","media_types":[1],"name":"My localization type"} # LocalizationTypeSpec | 

    try:
        api_response = api_instance.create_localization_type(project, localization_type_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_localization_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **localization_type_spec** | [**LocalizationTypeSpec**](LocalizationTypeSpec.md)|  | 

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
**201** | Successful creation of localization type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_media**
> CreateResponse create_media(project, media_spec)



Create media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.   This method creates a `Media` object in the database. For images, the  media must already be uploaded and an upload URL must be provided, as well as the group and job IDs associated with the upload. For videos, it is recommended to use the `Transcode` endpoint, which will create the media object itself. This method is only needed for local  transcodes. In that case, it will create an empty Media object; thumbnails, streaming, and archival videos must be subsequently uploaded via tus. Videos must be  moved to the media folder using the `MoveVideo` endpoint,  which also calls the `Media` PATCH method to update the `media_files` field. Thumbnails may be saved by just using the `Media` PATCH method directly. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_spec = tator_openapi.MediaSpec() # MediaSpec | 

    try:
        api_response = api_instance.create_media(project, media_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_spec** | [**MediaSpec**](MediaSpec.md)|  | 

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
**201** | Successful creation of media. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_media_type**
> CreateResponse create_media_type(project, media_type_spec)



Create media type.  A media type is the metadata definition object for media. It includes file format, name, description, and may have any number of user defined attribute types associated with it. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_type_spec = {"attribute_types":[{"default":false,"dtype":"bool","name":"My Boolean"},{"default":0,"dtype":"int","maximum":1,"minimum":-1,"name":"My Integer"},{"default":0.0,"dtype":"float","maximum":1.0,"minimum":-1.0,"name":"My Float"},{"choices":["a","b","c"],"default":"a","dtype":"enum","labels":["a","b","c"],"name":"My Enumeration"},{"autocomplete":{"serviceUrl":"https://www.example.com/suggestion"},"default":"---","dtype":"string","name":"My String"},{"dtype":"datetime","name":"My Datetime","use_current":true},{"default":[-179.0,90.0],"dtype":"geopos","name":"My Geoposition"}],"dtype":"video","name":"My media type"} # MediaTypeSpec | 

    try:
        api_response = api_instance.create_media_type(project, media_type_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_media_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_type_spec** | [**MediaTypeSpec**](MediaTypeSpec.md)|  | 

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
**201** | Successful creation of media type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_membership**
> CreateResponse create_membership(project, membership_spec)



Create membership.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels: - `View Only` can only view a project and not change any data. - `Can Edit` can create, modify, and delete annotations. - `Can Transfer` can upload and download media. - `Can Execute` can launch algorithm workflows. - `Full Control` can change project settings, including inviting new members, project name, and    project metadata schema. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
membership_spec = {"permission":"Full Control","user":1} # MembershipSpec | 

    try:
        api_response = api_instance.create_membership(project, membership_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **membership_spec** | [**MembershipSpec**](MembershipSpec.md)|  | 

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
**201** | Successful creation of membership. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_obtain_auth_token**
> Token create_obtain_auth_token(credentials=credentials)



### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    credentials = tator_openapi.Credentials() # Credentials |  (optional)

    try:
        api_response = api_instance.create_obtain_auth_token(credentials=credentials)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_obtain_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | [**Credentials**](Credentials.md)|  | [optional] 

### Return type

[**Token**](Token.md)

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

# **create_progress_summary_api**
> MessageResponse create_progress_summary_api(project, progress_summary_spec)



Create or update a progress summary.  This endpoint sets a key in redis that indicates how many jobs are in a job group as well as how many are completed. This is used to display summary progress in the progress bar. If not used for a given job group, the job completion is computed from the status of individual jobs in the group. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
progress_summary_spec = tator_openapi.ProgressSummarySpec() # ProgressSummarySpec | 

    try:
        api_response = api_instance.create_progress_summary_api(project, progress_summary_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_progress_summary_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **progress_summary_spec** | [**ProgressSummarySpec**](ProgressSummarySpec.md)|  | 

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
**201** | Successful creation of progress summary message. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> CreateResponse create_project(project_spec)



Create project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project_spec = {"name":"My Project","summary":"First project"} # ProjectSpec | 

    try:
        api_response = api_instance.create_project(project_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_spec** | [**ProjectSpec**](ProjectSpec.md)|  | 

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
**201** | Successful creation of project. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_state_list**
> CreateListResponse create_state_list(project, state_spec)



Create state list.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes.   This method does a bulk create on a list of `StateSpec` objects. A  maximum of 500 states may be created in one request. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
state_spec = [{"My First Attribute":"value1","My Second Attribute":"value2","frame":1000,"media_ids":[1],"type":1}] # list[StateSpec] | 

    try:
        api_response = api_instance.create_state_list(project, state_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_state_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **state_spec** | [**list[StateSpec]**](StateSpec.md)|  | 

### Return type

[**CreateListResponse**](CreateListResponse.md)

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
> CreateResponse create_state_type(project, state_type_spec)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and may have any number of user-defined attribute types associated with it. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
state_type_spec = {"association":"Frame","attribute_types":[{"default":false,"dtype":"bool","name":"My Boolean"},{"default":0,"dtype":"int","maximum":1,"minimum":-1,"name":"My Integer"},{"default":0.0,"dtype":"float","maximum":1.0,"minimum":-1.0,"name":"My Float"},{"choices":["a","b","c"],"default":"a","dtype":"enum","labels":["a","b","c"],"name":"My Enumeration"},{"autocomplete":{"serviceUrl":"https://www.example.com/suggestion"},"default":"---","dtype":"string","name":"My String"},{"dtype":"datetime","name":"My Datetime","use_current":true},{"default":[-179.0,90.0],"dtype":"geopos","name":"My Geoposition"}],"media_types":[1],"name":"My state type"} # StateTypeSpec | 

    try:
        api_response = api_instance.create_state_type(project, state_type_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_state_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **state_type_spec** | [**StateTypeSpec**](StateTypeSpec.md)|  | 

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
> CreateResponse create_temporary_file(project, temporary_file_spec)



Create temporary file.  Temporary files are files stored server side for a defined duration.   The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
temporary_file_spec = tator_openapi.TemporaryFileSpec() # TemporaryFileSpec | 

    try:
        api_response = api_instance.create_temporary_file(project, temporary_file_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_temporary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **temporary_file_spec** | [**TemporaryFileSpec**](TemporaryFileSpec.md)|  | 

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
**201** | Successful creation of temporary file. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_version**
> CreateResponse create_version(project, version_spec)



Create version.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
version_spec = {"bases":[1],"description":"New description","name":"My new version","show_empty":true} # VersionSpec | 

    try:
        api_response = api_instance.create_version(project, version_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->create_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **version_spec** | [**VersionSpec**](VersionSpec.md)|  | 

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

# **delete_algorithm**
> MessageResponse delete_algorithm(id)



Delete registered algorithm workflow

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a registered algorithm workflow.

    try:
        api_response = api_instance.delete_algorithm(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_algorithm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a registered algorithm workflow. | 

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
**200** | Successful deletion of registered algorithm. |  -  |
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
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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
**200** | Successful cancellation of job. |  -  |
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
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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
**200** | Successful cancellation of job group. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_leaf**
> delete_leaf(id)



Delete leaf.  Leaves are used to define label hierarchies that can be used for autocompletion of string attribute types. Leaves are a type of entity in Tator, meaning they can be described by user-defined attributes. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a leaf.

    try:
        api_instance.delete_leaf(id)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_leaf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a leaf. | 

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
**200** | Successful deletion of leaf. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_leaf_list**
> MessageResponse delete_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Delete leaf list.  Leaves are used to define label hierarchies that can be used for autocompletion of string attribute types. Leaves are a type of entity in Tator, meaning they can be described by user-defined attributes.   This method performs a bulk delete on all leaves matching a query. It is  recommended to use a GET request first to check what is being deleted. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
ancestor = 'ancestor_example' # str | Get descendents of a leaf element (inclusive), by path (i.e. ITIS.Animalia). (optional)
type = 56 # int | Unique integer identifying a leaf type. (optional)
name = 'name_example' # str | Name of the leaf element. (optional)
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
        api_response = api_instance.delete_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_leaf_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **ancestor** | **str**| Get descendents of a leaf element (inclusive), by path (i.e. ITIS.Animalia). | [optional] 
 **type** | **int**| Unique integer identifying a leaf type. | [optional] 
 **name** | **str**| Name of the leaf element. | [optional] 
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
**200** | Successful deletion of leaf list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_leaf_type**
> MessageResponse delete_leaf_type(id)



Delete leaf type.  A leaf type is the metadata definition object for a leaf. It includes name, description, and may have any number of user-defined attribute types associated with it. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an leaf type.

    try:
        api_response = api_instance.delete_leaf_type(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an leaf type. | 

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
**200** | Successful deletion of leaf type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization**
> MessageResponse delete_localization(id)



Delete localization.  Localizations are shape annotations drawn on a video or image. Available shapes (`dtype`) are  box, line, or dot. Each shape is parameterized by a different subset of data members: - `box` uses `x`, `y`, `width`, `height`. - `line` uses `x`, `y`, `u`, `v`. - `dot` uses `x` and `y`.  Geometry members may be left null when creating a localization, in which case the shapes may be  drawn later using the redraw capability in the web UI. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a localization.

    try:
        api_response = api_instance.delete_localization(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_localization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization. | 

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
**200** | Successful deletion of localization. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization_list**
> MessageResponse delete_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, exclude_parents=exclude_parents, frame=frame)



Delete localiazation list.  Localizations are shape annotations drawn on a video or image. Available shapes (`dtype`) are  box, line, or dot. Each shape is parameterized by a different subset of data members: - `box` uses `x`, `y`, `width`, `height`. - `line` uses `x`, `y`, `u`, `v`. - `dot` uses `x` and `y`.  Geometry members may be left null when creating a localization, in which case the shapes may be  drawn later using the redraw capability in the web UI. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.   This method performs a bulk delete on all localizations matching a query. It is  recommended to use a GET request first to check what is being deleted. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = [56] # list[int] | List of integers representing versions to fetch (optional)
modified = 1 # int | Whether to return original or modified annotations, 0 or 1. (optional) (default to 1)
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
exclude_parents = 0 # int | If a clone is present, do not send parent. (0 or 1) (optional) (default to 0)
frame = 56 # int | Frame number of this localization if it is in a video. (optional)

    try:
        api_response = api_instance.delete_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, exclude_parents=exclude_parents, frame=frame)
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
 **version** | [**list[int]**](int.md)| List of integers representing versions to fetch | [optional] 
 **modified** | **int**| Whether to return original or modified annotations, 0 or 1. | [optional] [default to 1]
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
 **exclude_parents** | **int**| If a clone is present, do not send parent. (0 or 1) | [optional] [default to 0]
 **frame** | **int**| Frame number of this localization if it is in a video. | [optional] 

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
**200** | Successful deletion of localization list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization_type**
> MessageResponse delete_localization_type(id)



Delete localization type.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and may have any number of user-defined attribute types associated with it.   Note that this will also delete any localizations associated with the localization type. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an localization type.

    try:
        api_response = api_instance.delete_localization_type(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_localization_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an localization type. | 

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
**200** | Successful deletion of localization type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media**
> MessageResponse delete_media(id)



Delete media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a media.

    try:
        api_response = api_instance.delete_media(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media. | 

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
**200** | Successful deletion of media. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media_list**
> MessageResponse delete_media_list(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Delete media list.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.   This method performs a bulk delete on all media matching a query. It is  recommended to use a GET request first to check what is being deleted. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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
**200** | Successful deletion of media list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media_type**
> MessageResponse delete_media_type(id)



Delete media type.  A media type is the metadata definition object for media. It includes file format, name, description, and may have any number of user defined attribute types associated with it.   Note that this will also delete any media associated with the media type. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an media type.

    try:
        api_response = api_instance.delete_media_type(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_media_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an media type. | 

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
**200** | Successful deletion of media type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_membership**
> MessageResponse delete_membership(id)



Delete membership.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels: - `View Only` can only view a project and not change any data. - `Can Edit` can create, modify, and delete annotations. - `Can Transfer` can upload and download media. - `Can Execute` can launch algorithm workflows. - `Full Control` can change project settings, including inviting new members, project name, and    project metadata schema. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a membership.

    try:
        api_response = api_instance.delete_membership(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a membership. | 

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
**200** | Successful deletion of membership. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> MessageResponse delete_project(id)



Delete project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.   Only project owners may delete a project. Note that deleting a project will also delete all media and annotations within a project. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a project.

    try:
        api_response = api_instance.delete_project(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a project. | 

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
**200** | Successful deletion of project. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state**
> MessageResponse delete_state(id)



Delete state.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a state.

    try:
        api_response = api_instance.delete_state(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state. | 

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
**200** | Successful deletion of state. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state_list**
> MessageResponse delete_state_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Delete state list.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes.   This method performs a bulk delete on all states matching a query. It is  recommended to use a GET request first to check what is being deleted. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = [56] # list[int] | List of integers representing versions to fetch (optional)
modified = 1 # int | Whether to return original or modified annotations, 0 or 1. (optional) (default to 1)
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
 **version** | [**list[int]**](int.md)| List of integers representing versions to fetch | [optional] 
 **modified** | **int**| Whether to return original or modified annotations, 0 or 1. | [optional] [default to 1]
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
**200** | Successful deletion of state list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state_type**
> MessageResponse delete_state_type(id)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and may have any number of user-defined attribute types associated with it.   Note that this will also delete any states associated with the state type. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a state type.

    try:
        api_response = api_instance.delete_state_type(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_state_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state type. | 

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
**200** | Successful deletion of state type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_temporary_file**
> MessageResponse delete_temporary_file(id)



Delete temporary file.  Temporary files are files stored server side for a defined duration. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a temporary file.

    try:
        api_response = api_instance.delete_temporary_file(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_temporary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a temporary file. | 

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
**200** | Successful deletion of temporary file. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_temporary_file_list**
> delete_temporary_file_list(project, expired=expired)



Delete temporary file list.  Temporary files are files stored server side for a defined duration.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version**
> MessageResponse delete_version(id)



Delete version.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating.   Note that this will also delete any localizations or states associated with the deleted version. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a version.

    try:
        api_response = api_instance.delete_version(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->delete_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a version. | 

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
**200** | Successful deletion of version. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_algorithm_list**
> list[Algorithm] get_algorithm_list(project)



Get registered algorithms. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**list[Algorithm]**](Algorithm.md)

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
> list[Analysis] get_analysis_list(project)



Get analysis.  Analysis objects are used to display information about filtered media lists and/or annotations on the project detail page of the web UI. Currently only counting analysis is supported. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**list[Analysis]**](Analysis.md)

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

# **get_clip**
> TemporaryFile get_clip(id, frame_ranges, quality=quality)



Get video clip.  Facility to get a clip from the server. Returns a temporary file object that expires in 24 hours. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**TemporaryFile**](TemporaryFile.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of video clip. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_frame**
> file get_frame(id, frames=frames, tile=tile, roi=roi, animate=animate, quality=quality)



Get frame(s) from a video.  Facility to get a frame(jpg/png) of a given video frame, returns a square tile of frames based on the input parameter. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

# **get_leaf**
> Leaf get_leaf(id)



Get leaf.  Leaves are used to define label hierarchies that can be used for autocompletion of string attribute types. Leaves are a type of entity in Tator, meaning they can be described by user-defined attributes. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a leaf.

    try:
        api_response = api_instance.get_leaf(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_leaf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a leaf. | 

### Return type

[**Leaf**](Leaf.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of leaf. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaf_list**
> list[Leaf] get_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Get leaf list.  Leaves are used to define label hierarchies that can be used for autocompletion of string attribute types. Leaves are a type of entity in Tator, meaning they can be described by user-defined attributes.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
ancestor = 'ancestor_example' # str | Get descendents of a leaf element (inclusive), by path (i.e. ITIS.Animalia). (optional)
type = 56 # int | Unique integer identifying a leaf type. (optional)
name = 'name_example' # str | Name of the leaf element. (optional)
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
        api_response = api_instance.get_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_leaf_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **ancestor** | **str**| Get descendents of a leaf element (inclusive), by path (i.e. ITIS.Animalia). | [optional] 
 **type** | **int**| Unique integer identifying a leaf type. | [optional] 
 **name** | **str**| Name of the leaf element. | [optional] 
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

[**list[Leaf]**](Leaf.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of leaf list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaf_type**
> LeafType get_leaf_type(id)



Get leaf type.  A leaf type is the metadata definition object for a leaf. It includes name, description, and may have any number of user-defined attribute types associated with it. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an leaf type.

    try:
        api_response = api_instance.get_leaf_type(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an leaf type. | 

### Return type

[**LeafType**](LeafType.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of leaf type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaf_type_list**
> list[LeafType] get_leaf_type_list(project)



Get leaf type list.  A leaf type is the metadata definition object for a leaf. It includes name, description, and may have any number of user-defined attribute types associated with it. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.

    try:
        api_response = api_instance.get_leaf_type_list(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_leaf_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**list[LeafType]**](LeafType.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of leaf type list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization**
> Localization get_localization(id)



Get localization.  Localizations are shape annotations drawn on a video or image. Available shapes (`dtype`) are  box, line, or dot. Each shape is parameterized by a different subset of data members: - `box` uses `x`, `y`, `width`, `height`. - `line` uses `x`, `y`, `u`, `v`. - `dot` uses `x` and `y`.  Geometry members may be left null when creating a localization, in which case the shapes may be  drawn later using the redraw capability in the web UI. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

# **get_localization_graphic**
> file get_localization_graphic(id, force_scale=force_scale, use_default_margins=use_default_margins, margin_x=margin_x, margin_y=margin_y)



Get localization graphic from a media object. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a localization.
force_scale = 'force_scale_example' # str | Size of final image to return. This forces scaling the image. Default is the localization size and margins define the image size. Example: 100x100  (optional)
use_default_margins = True # bool | Use default margins for localization types.  Default margins (x,y pixels) - dot: (10,10) line:  (10,10) box: (0,0)  (optional) (default to True)
margin_x = 56 # int | Pixel margin to apply to the height of the localization when generating the image. Valid only if use_default_margins is false.  (optional)
margin_y = 56 # int | Pixel margin to apply to the width of the localization when generating the image. Valid only if use_default_margins is false.  (optional)

    try:
        api_response = api_instance.get_localization_graphic(id, force_scale=force_scale, use_default_margins=use_default_margins, margin_x=margin_x, margin_y=margin_y)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_localization_graphic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization. | 
 **force_scale** | **str**| Size of final image to return. This forces scaling the image. Default is the localization size and margins define the image size. Example: 100x100  | [optional] 
 **use_default_margins** | **bool**| Use default margins for localization types.  Default margins (x,y pixels) - dot: (10,10) line:  (10,10) box: (0,0)  | [optional] [default to True]
 **margin_x** | **int**| Pixel margin to apply to the height of the localization when generating the image. Valid only if use_default_margins is false.  | [optional] 
 **margin_y** | **int**| Pixel margin to apply to the width of the localization when generating the image. Valid only if use_default_margins is false.  | [optional] 

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
**200** | Successful retrieval of localization graphic. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_list**
> list[Localization] get_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, exclude_parents=exclude_parents, frame=frame)



Get localization list.  Localizations are shape annotations drawn on a video or image. Available shapes (`dtype`) are  box, line, or dot. Each shape is parameterized by a different subset of data members: - `box` uses `x`, `y`, `width`, `height`. - `line` uses `x`, `y`, `u`, `v`. - `dot` uses `x` and `y`.  Geometry members may be left null when creating a localization, in which case the shapes may be  drawn later using the redraw capability in the web UI. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = [56] # list[int] | List of integers representing versions to fetch (optional)
modified = 1 # int | Whether to return original or modified annotations, 0 or 1. (optional) (default to 1)
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
exclude_parents = 0 # int | If a clone is present, do not send parent. (0 or 1) (optional) (default to 0)
frame = 56 # int | Frame number of this localization if it is in a video. (optional)

    try:
        api_response = api_instance.get_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, exclude_parents=exclude_parents, frame=frame)
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
 **version** | [**list[int]**](int.md)| List of integers representing versions to fetch | [optional] 
 **modified** | **int**| Whether to return original or modified annotations, 0 or 1. | [optional] [default to 1]
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
 **exclude_parents** | **int**| If a clone is present, do not send parent. (0 or 1) | [optional] [default to 0]
 **frame** | **int**| Frame number of this localization if it is in a video. | [optional] 

### Return type

[**list[Localization]**](Localization.md)

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
> LocalizationType get_localization_type(id)



Get localization type.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and may have any number of user-defined attribute types associated with it.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**LocalizationType**](LocalizationType.md)

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
> list[LocalizationType] get_localization_type_list(project, media_id=media_id, type=type)



Get localization type list.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and may have any number of user-defined attribute types associated with it. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**list[LocalizationType]**](LocalizationType.md)

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
> Media get_media(id)



Get media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**Media**](Media.md)

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
> list[Media] get_media_list(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Get media list.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**list[Media]**](Media.md)

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
> MediaNext get_media_next(id, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve ID of next media in a media list.  This endpoint accepts the same query parameters as a GET request to the `Medias` endpoint, but only returns the next media ID from the media passed as a path parameter. This allows iteration through a media list without serializing the entire list, which may be large. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**MediaNext**](MediaNext.md)

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
> MediaPrev get_media_prev(id, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve ID of previous media in a media list.  This endpoint accepts the same query parameters as a GET request to the `Medias` endpoint, but only returns the previous media ID from the media passed as a path parameter. This  allows iteration through a media list without serializing the entire list, which may be  large. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**MediaPrev**](MediaPrev.md)

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
> dict(str, object) get_media_sections(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve media counts by section.  This endpoint accepts the same query parameters as a GET request to the `Medias` endpoint, but only returns the number of images and videos per sections. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

**dict(str, object)**

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
> MediaType get_media_type(id)



Get media type.  A media type is the metadata definition object for media. It includes file format, name, description, and may have any number of user defined attribute types associated with it.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**MediaType**](MediaType.md)

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
> list[MediaType] get_media_type_list(project)



Get media type list.  A media type is the metadata definition object for media. It includes file format, name, description, and may have any number of user defined attribute types associated with it. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**list[MediaType]**](MediaType.md)

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
> Membership get_membership(id)



Get membership.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels: - `View Only` can only view a project and not change any data. - `Can Edit` can create, modify, and delete annotations. - `Can Transfer` can upload and download media. - `Can Execute` can launch algorithm workflows. - `Full Control` can change project settings, including inviting new members, project name, and    project metadata schema. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**Membership**](Membership.md)

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
> list[Membership] get_membership_list(project)



Get membership list.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels: - `View Only` can only view a project and not change any data. - `Can Edit` can create, modify, and delete annotations. - `Can Transfer` can upload and download media. - `Can Execute` can launch algorithm workflows. - `Full Control` can change project settings, including inviting new members, project name, and    project metadata schema. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**list[Membership]**](Membership.md)

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
> Project get_project(id)



Get project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**Project**](Project.md)

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
> list[Project] get_project_list()



Get project list.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.   Returns all projects that a user has access to.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    
    try:
        api_response = api_instance.get_project_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_project_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Project]**](Project.md)

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
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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
> State get_state(id)



Get state.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a state.

    try:
        api_response = api_instance.get_state(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state. | 

### Return type

[**State**](State.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of state. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_graphic**
> file get_state_graphic(id, mode=mode, fps=fps, force_scale=force_scale)



 Get frame(s) of a given localization-associated state.  Use the mode argument to control whether it is an animated gif or a tiled jpg. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a state.
mode = 'animate' # str | Whether to animate or tile. (optional) (default to 'animate')
fps = 2 # float | Frame rate if `mode` is `animate`. (optional) (default to 2)
force_scale = '240x240' # str | wxh to force each tile prior to stich (optional)

    try:
        api_response = api_instance.get_state_graphic(id, mode=mode, fps=fps, force_scale=force_scale)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_state_graphic: %s\n" % e)
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
 - **Accept**: image/*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of state graphic. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_list**
> list[State] get_state_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Get state list.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = [56] # list[int] | List of integers representing versions to fetch (optional)
modified = 1 # int | Whether to return original or modified annotations, 0 or 1. (optional) (default to 1)
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
 **version** | [**list[int]**](int.md)| List of integers representing versions to fetch | [optional] 
 **modified** | **int**| Whether to return original or modified annotations, 0 or 1. | [optional] [default to 1]
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

[**list[State]**](State.md)

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
> StateType get_state_type(id)



Get state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and may have any number of user-defined attribute types associated with it.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**StateType**](StateType.md)

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
> list[StateType] get_state_type_list(project, media_id=media_id, type=type)



Get state type list.  A state type is the metadata definition object for a state. It includes association type, name, description, and may have any number of user-defined attribute types associated with it. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**list[StateType]**](StateType.md)

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
> TemporaryFile get_temporary_file(id)



Get temporary file.  Temporary files are files stored server side for a defined duration. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a temporary file.

    try:
        api_response = api_instance.get_temporary_file(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_temporary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a temporary file. | 

### Return type

[**TemporaryFile**](TemporaryFile.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of temporary file. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_file_list**
> list[TemporaryFile] get_temporary_file_list(project, expired=expired)



Get temporary file list.  Temporary files are files stored server side for a defined duration.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**list[TemporaryFile]**](TemporaryFile.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of temporary file list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(id)



Get user.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**User**](User.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of user. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> Version get_version(id)



Get version.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
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

[**Version**](Version.md)

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

# **get_version_list**
> list[Version] get_version_list(project, media_id=media_id)



Get version list.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
media_id = 56 # int | Unique integer identifying a media. (optional)

    try:
        api_response = api_instance.get_version_list(project, media_id=media_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->get_version_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_id** | **int**| Unique integer identifying a media. | [optional] 

### Return type

[**list[Version]**](Version.md)

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

# **leaf_suggestion**
> list[LeafSuggestion] leaf_suggestion(project, ancestor, query, min_level=min_level)



Get list of autocomplete suggestions.  This endpoint is compatible with devbridge suggestion format. It performs a glob search on leaf objects in the project.  <https://github.com/kraaden/autocomplete> 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
ancestor = 'ancestor_example' # str | Get descendents of a leaf element (inclusive), by path (i.e. ITIS.Animalia).
query = 'query_example' # str | String to search for matching names.
min_level = 56 # int | Integer specifying level of results that may be returned. For example, 2 refers to grandchildren of the level specified by the `ancestor` parameter. (optional)

    try:
        api_response = api_instance.leaf_suggestion(project, ancestor, query, min_level=min_level)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->leaf_suggestion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **ancestor** | **str**| Get descendents of a leaf element (inclusive), by path (i.e. ITIS.Animalia). | 
 **query** | **str**| String to search for matching names. | 
 **min_level** | **int**| Integer specifying level of results that may be returned. For example, 2 refers to grandchildren of the level specified by the &#x60;ancestor&#x60; parameter. | [optional] 

### Return type

[**list[LeafSuggestion]**](LeafSuggestion.md)

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

# **move_video**
> CreateResponse move_video(id, move_video_spec=move_video_spec)



Moves a video file.  This endpoint creates an Argo workflow that moves an uploaded video file into the appropriate project directory. When the move is complete, the workflow will make a PATCH request to the Media endpoint for the given media ID using the given  `media_files` definitions.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. To launch a transcode on raw uploaded video, use the `Transcode` endpoint, which will create an Argo workflow to perform the transcode and save the video using this endpoint; no further REST calls are required. However, if you would like to perform transcodes locally, this endpoint enables that. The module `tator.transcode` in the tator pip package provides local transcode capability using this endpoint. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a media.
move_video_spec = tator_openapi.MoveVideoSpec() # MoveVideoSpec |  (optional)

    try:
        api_response = api_instance.move_video(id, move_video_spec=move_video_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->move_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media. | 
 **move_video_spec** | [**MoveVideoSpec**](MoveVideoSpec.md)|  | [optional] 

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
**201** | Successful creation of move job. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify**
> notify(notify_spec)



Send a notification to administrators.  Uses the Slack API to send a notification to system administrators. This endpoint can only be used by system administrators and must be configured in a Tator deployment's settings. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    notify_spec = tator_openapi.NotifySpec() # NotifySpec | 

    try:
        api_instance.notify(notify_spec)
    except ApiException as e:
        print("Exception when calling TatorApi->notify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notify_spec** | [**NotifySpec**](NotifySpec.md)|  | 

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

# **progress**
> MessageResponse progress(project, progress_spec)



Broadcast progress update.  Progress messages are sent in the web UI via WebSocket, and are displayed as progress bars associated with individual media files and as a summary in the webpage header. All members of a project can see progress bars from uploads and background jobs initiated by other users within the project. This endpoint accepts an array of messages, allowing for progress messages to be batched into a single request. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
progress_spec = [{"gid":"b722e83e-8272-11ea-8e10-000c294f07cf","job_type":"algorithm","media_ids":"1,2","message":"Job started!","name":"name_of_file.mp4","progress":70,"sections":"Section 1,Section 2","state":"started","uid":"b43d7e54-8272-11ea-8e10-000c294f07cf"}] # list[ProgressSpec] | 

    try:
        api_response = api_instance.progress(project, progress_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **progress_spec** | [**list[ProgressSpec]**](ProgressSpec.md)|  | 

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

# **register_algorithm**
> CreateResponse register_algorithm(project, algorithm_spec)



Register an algorithm argo workflow.  This endpoint replicates the algorithm registration through the admin portal. The provided manifest file must have been uploaded and saved by the SaveAlgorithmManifest endpoint. This endpoint will respond with an error if one of the following conditions occur:  - Provided workflow name is not unique (across projects) - Not all the required fields are present - There are syntax errors with the given manifest file 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
algorithm_spec = tator_openapi.AlgorithmSpec() # AlgorithmSpec | 

    try:
        api_response = api_instance.register_algorithm(project, algorithm_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->register_algorithm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **algorithm_spec** | [**AlgorithmSpec**](AlgorithmSpec.md)|  | 

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
**201** | Successful creation of registered algorithm. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_algorithm_manifest**
> AlgorithmManfiest save_algorithm_manifest(project, algorithm_manifest_spec)



Saves an uploaded algorithm manifest to the desired project. It is expected this manifest corresponds with an algorithm workflow to be registered by another endpoint.  Manifest is uploaded via tus, a separate mechanism from the REST API. Once a manifest upload is complete (a .yaml file), the file must be saved to the database using this endpoint. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project
algorithm_manifest_spec = tator_openapi.AlgorithmManifestSpec() # AlgorithmManifestSpec | 

    try:
        api_response = api_instance.save_algorithm_manifest(project, algorithm_manifest_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->save_algorithm_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project | 
 **algorithm_manifest_spec** | [**AlgorithmManifestSpec**](AlgorithmManifestSpec.md)|  | 

### Return type

[**AlgorithmManfiest**](AlgorithmManfiest.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful save of algortihm manifest. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcode**
> Transcode transcode(project, transcode_spec)



Start a transcode.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. This endpoint launches a transcode on raw uploaded video by creating an Argo workflow. The workflow will download the uploaded raw video, transcode it to the proper format, upload the transcoded video, and save the video using the  `SaveVideo` endpoint.  Note that the raw video must be uploaded first via tus, which is a separate mechanism  from the REST API. This endpoint requires a group and run UUID associated with this  upload. If no progress messages were generated during upload, then the group and run  UUIDs can be newly generated.  Transcodes may be cancelled via the `Job` or `JobGroup` endpoints. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
transcode_spec = tator_openapi.TranscodeSpec() # TranscodeSpec | 

    try:
        api_response = api_instance.transcode(project, transcode_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->transcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **transcode_spec** | [**TranscodeSpec**](TranscodeSpec.md)|  | 

### Return type

[**Transcode**](Transcode.md)

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

# **update_leaf**
> MessageResponse update_leaf(id, leaf_update)



Update leaf.  Leaves are used to define label hierarchies that can be used for autocompletion of string attribute types. Leaves are a type of entity in Tator, meaning they can be described by user-defined attributes. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a leaf.
leaf_update = tator_openapi.LeafUpdate() # LeafUpdate | 

    try:
        api_response = api_instance.update_leaf(id, leaf_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_leaf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a leaf. | 
 **leaf_update** | [**LeafUpdate**](LeafUpdate.md)|  | 

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
**200** | Successful update of leaf. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_leaf_list**
> MessageResponse update_leaf_list(project, attribute_bulk_update, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Update leaf list.  Leaves are used to define label hierarchies that can be used for autocompletion of string attribute types. Leaves are a type of entity in Tator, meaning they can be described by user-defined attributes.   This method does a bulk update on all leaves matching a query. Only  user-defined attributes may be bulk updated. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
attribute_bulk_update = tator_openapi.AttributeBulkUpdate() # AttributeBulkUpdate | 
ancestor = 'ancestor_example' # str | Get descendents of a leaf element (inclusive), by path (i.e. ITIS.Animalia). (optional)
type = 56 # int | Unique integer identifying a leaf type. (optional)
name = 'name_example' # str | Name of the leaf element. (optional)
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
        api_response = api_instance.update_leaf_list(project, attribute_bulk_update, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_leaf_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **attribute_bulk_update** | [**AttributeBulkUpdate**](AttributeBulkUpdate.md)|  | 
 **ancestor** | **str**| Get descendents of a leaf element (inclusive), by path (i.e. ITIS.Animalia). | [optional] 
 **type** | **int**| Unique integer identifying a leaf type. | [optional] 
 **name** | **str**| Name of the leaf element. | [optional] 
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

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update of leaf list. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_leaf_type**
> MessageResponse update_leaf_type(id, leaf_type_update)



Update leaf type.  A leaf type is the metadata definition object for a leaf. It includes name, description, and may have any number of user-defined attribute types associated with it. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an leaf type.
leaf_type_update = {"description":"New description","name":"New name"} # LeafTypeUpdate | 

    try:
        api_response = api_instance.update_leaf_type(id, leaf_type_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an leaf type. | 
 **leaf_type_update** | [**LeafTypeUpdate**](LeafTypeUpdate.md)|  | 

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
**200** | Successful update of leaf type. |  -  |
**400** | Bad request. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization**
> MessageResponse update_localization(id, localization_update)



Update localization.  Localizations are shape annotations drawn on a video or image. Available shapes (`dtype`) are  box, line, or dot. Each shape is parameterized by a different subset of data members: - `box` uses `x`, `y`, `width`, `height`. - `line` uses `x`, `y`, `u`, `v`. - `dot` uses `x` and `y`.  Geometry members may be left null when creating a localization, in which case the shapes may be  drawn later using the redraw capability in the web UI. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a localization.
localization_update = {"height":0.25,"width":0.25,"x":0.25,"y":0.25} # LocalizationUpdate | 

    try:
        api_response = api_instance.update_localization(id, localization_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_localization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization. | 
 **localization_update** | [**LocalizationUpdate**](LocalizationUpdate.md)|  | 

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

# **update_localization_list**
> MessageResponse update_localization_list(project, attribute_bulk_update, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, exclude_parents=exclude_parents, frame=frame)



Update localiazation list.  Localizations are shape annotations drawn on a video or image. Available shapes (`dtype`) are  box, line, or dot. Each shape is parameterized by a different subset of data members: - `box` uses `x`, `y`, `width`, `height`. - `line` uses `x`, `y`, `u`, `v`. - `dot` uses `x` and `y`.  Geometry members may be left null when creating a localization, in which case the shapes may be  drawn later using the redraw capability in the web UI. Localizations are a type of entity in Tator, meaning they can be described by user defined attributes.   This method does a bulk update on all localizations matching a query. Only  user-defined attributes may be bulk updated. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
attribute_bulk_update = {"attributes":{"Species":"Tuna"}} # AttributeBulkUpdate | 
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = [56] # list[int] | List of integers representing versions to fetch (optional)
modified = 1 # int | Whether to return original or modified annotations, 0 or 1. (optional) (default to 1)
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
exclude_parents = 0 # int | If a clone is present, do not send parent. (0 or 1) (optional) (default to 0)
frame = 56 # int | Frame number of this localization if it is in a video. (optional)

    try:
        api_response = api_instance.update_localization_list(project, attribute_bulk_update, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, exclude_parents=exclude_parents, frame=frame)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_localization_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **attribute_bulk_update** | [**AttributeBulkUpdate**](AttributeBulkUpdate.md)|  | 
 **media_query** | **str**| Query string used to filter media IDs. If supplied, media_id will be ignored. | [optional] 
 **media_id** | [**list[int]**](int.md)| Comma-separated list of media IDs. | [optional] 
 **type** | **int**| Unique integer identifying a annotation type. | [optional] 
 **version** | [**list[int]**](int.md)| List of integers representing versions to fetch | [optional] 
 **modified** | **int**| Whether to return original or modified annotations, 0 or 1. | [optional] [default to 1]
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
 **exclude_parents** | **int**| If a clone is present, do not send parent. (0 or 1) | [optional] [default to 0]
 **frame** | **int**| Frame number of this localization if it is in a video. | [optional] 

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
> MessageResponse update_localization_type(id, localization_type_update)



Update localization type.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and may have any number of user-defined attribute types associated with it.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an localization type.
localization_type_update = {"description":"New description","name":"New name"} # LocalizationTypeUpdate | 

    try:
        api_response = api_instance.update_localization_type(id, localization_type_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_localization_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an localization type. | 
 **localization_type_update** | [**LocalizationTypeUpdate**](LocalizationTypeUpdate.md)|  | 

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
> MessageResponse update_media(id, media_update)



Update media.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a media.
media_update = tator_openapi.MediaUpdate() # MediaUpdate | 

    try:
        api_response = api_instance.update_media(id, media_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media. | 
 **media_update** | [**MediaUpdate**](MediaUpdate.md)|  | 

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
> MessageResponse update_media_list(project, attribute_bulk_update, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Update media list.  A media may be an image or a video. Media are a type of entity in Tator, meaning they can be described by user defined attributes.   This method does a bulk update on all media matching a query. Only  user-defined attributes may be bulk updated. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
attribute_bulk_update = {"attributes":{"Species":"Tuna"}} # AttributeBulkUpdate | 
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
        api_response = api_instance.update_media_list(project, attribute_bulk_update, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_media_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **attribute_bulk_update** | [**AttributeBulkUpdate**](AttributeBulkUpdate.md)|  | 
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
> MessageResponse update_media_type(id, media_type_update)



Update media type.  A media type is the metadata definition object for media. It includes file format, name, description, and may have any number of user defined attribute types associated with it.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying an media type.
media_type_update = {"description":"New description","name":"New name"} # MediaTypeUpdate | 

    try:
        api_response = api_instance.update_media_type(id, media_type_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_media_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an media type. | 
 **media_type_update** | [**MediaTypeUpdate**](MediaTypeUpdate.md)|  | 

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
> MessageResponse update_membership(id, membership_update)



Update membership.  Memberships specify a permission level of a user to a project. There are currently five cumulative permission levels: - `View Only` can only view a project and not change any data. - `Can Edit` can create, modify, and delete annotations. - `Can Transfer` can upload and download media. - `Can Execute` can launch algorithm workflows. - `Full Control` can change project settings, including inviting new members, project name, and    project metadata schema. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a membership.
membership_update = {"permission":"View Only"} # MembershipUpdate | 

    try:
        api_response = api_instance.update_membership(id, membership_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a membership. | 
 **membership_update** | [**MembershipUpdate**](MembershipUpdate.md)|  | 

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
> MessageResponse update_project(id, project_spec)



Update project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a project.
project_spec = {"name":"New name","summary":"New summary"} # ProjectSpec | 

    try:
        api_response = api_instance.update_project(id, project_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a project. | 
 **project_spec** | [**ProjectSpec**](ProjectSpec.md)|  | 

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
> MessageResponse update_state(id, state_update)



Update state.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a state.
state_update = {"frame":1001} # StateUpdate | 

    try:
        api_response = api_instance.update_state(id, state_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state. | 
 **state_update** | [**StateUpdate**](StateUpdate.md)|  | 

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
> MessageResponse update_state_list(project, attribute_bulk_update, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Update state list.  A state is a description of a collection of other objects. The objects a state describes could be media (image or video), video frames, or localizations. A state referring to a collection of localizations is often referred to as a track. States are a type of entity in Tator, meaning they can be described by user defined attributes.   This method does a bulk update on all states matching a query. Only  user-defined attributes may be bulk updated. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
attribute_bulk_update = {"attributes":{"Species":"Tuna"}} # AttributeBulkUpdate | 
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = [56] # list[int] | List of integers representing versions to fetch (optional)
modified = 1 # int | Whether to return original or modified annotations, 0 or 1. (optional) (default to 1)
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
        api_response = api_instance.update_state_list(project, attribute_bulk_update, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_state_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **attribute_bulk_update** | [**AttributeBulkUpdate**](AttributeBulkUpdate.md)|  | 
 **media_query** | **str**| Query string used to filter media IDs. If supplied, media_id will be ignored. | [optional] 
 **media_id** | [**list[int]**](int.md)| Comma-separated list of media IDs. | [optional] 
 **type** | **int**| Unique integer identifying a annotation type. | [optional] 
 **version** | [**list[int]**](int.md)| List of integers representing versions to fetch | [optional] 
 **modified** | **int**| Whether to return original or modified annotations, 0 or 1. | [optional] [default to 1]
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
> MessageResponse update_state_type(id, state_type_update)



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and may have any number of user-defined attribute types associated with it.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a state type.
state_type_update = {"description":"New description","name":"New name"} # StateTypeUpdate | 

    try:
        api_response = api_instance.update_state_type(id, state_type_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_state_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state type. | 
 **state_type_update** | [**StateTypeUpdate**](StateTypeUpdate.md)|  | 

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

# **update_user**
> update_user(id, user_update)



Update user.

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a localization association.
user_update = tator_openapi.UserUpdate() # UserUpdate | 

    try:
        api_instance.update_user(id, user_update)
    except ApiException as e:
        print("Exception when calling TatorApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization association. | 
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 

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

# **update_version**
> MessageResponse update_version(id, version_update)



Update version.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating.   

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    id = 56 # int | A unique integer identifying a version.
version_update = {"bases":[1],"description":"New description","name":"New name","show_empty":true} # VersionUpdate | 

    try:
        api_response = api_instance.update_version(id, version_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->update_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a version. | 
 **version_update** | [**VersionUpdate**](VersionUpdate.md)|  | 

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

# **whoami**
> User whoami()



Get current user.  Retrieves user making the request. 

### Example

* Api Key Authentication (TokenAuth):
```python
from __future__ import print_function
import time
import tator_openapi
from tator_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator_openapi.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with tator_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator_openapi.TatorApi(api_client)
    
    try:
        api_response = api_instance.whoami()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->whoami: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

