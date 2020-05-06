# tator.TatorApi

All URIs are relative to */*

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
> AlgorithmLaunchResponse algorithm_launch(project, body=body)



Start an algorithm.  This will create one or more Argo workflows that execute the named algorithm registration. To get a list of available algorithms, use the `Algorithms` endpoint. A media list will be submitted for processing using either a query string or  a list of media IDs. If neither are included, the algorithm will be launched on all media in the project.   Media is divided into batches for based on the `files_per_job` field of the  `Algorithm` object. One batch is submitted to each Argo workflow.  Submitted algorithm jobs may be cancelled via the `Job` or `JobGroup` endpoints.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.AlgorithmLaunchSpec() # AlgorithmLaunchSpec |  (optional)

try:
    api_response = api_instance.algorithm_launch(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->algorithm_launch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**AlgorithmLaunchSpec**](AlgorithmLaunchSpec.md)|  | [optional] 

### Return type

[**AlgorithmLaunchResponse**](AlgorithmLaunchResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_analysis**
> CreateResponse create_analysis(project, body=body)



Create analysis for a project.  Analysis objects are used to display information about filtered media lists and/or annotations on the project detail page of the web UI. Currently only counting analysis is supported.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.AnalysisSpec() # AnalysisSpec |  (optional)

try:
    api_response = api_instance.create_analysis(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**AnalysisSpec**](AnalysisSpec.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_attribute_type**
> CreateResponse create_attribute_type(project)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.create_attribute_type(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_localization**
> MessageResponse create_localization(project, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.LocalizationSpec() # LocalizationSpec |  (optional)

try:
    api_response = api_instance.create_localization(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_localization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**LocalizationSpec**](LocalizationSpec.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_localization_type**
> InlineResponse201 create_localization_type(project, body=body)



Create or retrieve localization types.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body2() # Body2 |  (optional)

try:
    api_response = api_instance.create_localization_type(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_localization_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_media_type**
> InlineResponse201 create_media_type(project, body=body)



Create or retrieve localization types.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = {
  "dtype" : "video",
  "name" : "My media type"
} # object |  (optional)

try:
    api_response = api_instance.create_media_type(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_media_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_membership**
> InlineResponse2011 create_membership(project, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body5() # Body5 |  (optional)

try:
    api_response = api_instance.create_membership(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body5**](Body5.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_obtain_auth_token**
> InlineResponse20010 create_obtain_auth_token(body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
body = tator.Body15() # Body15 |  (optional)

try:
    api_response = api_instance.create_obtain_auth_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_obtain_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body15**](Body15.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> InlineResponse2012 create_project(body=body)



Interact with a list of projects.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Project lists return all projects that the requesting user has access to.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
body = {
  "name" : "My Project",
  "summary" : "First project"
} # object |  (optional)

try:
    api_response = api_instance.create_project(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_state**
> CreateResponse create_state(project, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = {
  "summary" : "Frame associated state",
  "value" : {
    "My First Attribute" : "value1",
    "My Second Attribute" : "value2",
    "frame" : 1000,
    "media_ids" : [ 1 ],
    "type" : 1
  }
} # dict(str, object) |  (optional)

try:
    api_response = api_instance.create_state(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_state_type**
> CreateResponse create_state_type(project, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body11() # Body11 |  (optional)

try:
    api_response = api_instance.create_state_type(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_state_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body11**](Body11.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_temporary_file**
> InlineResponse2009 create_temporary_file(project, body=body)



Interact with temporary file list.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body14() # Body14 |  (optional)

try:
    api_response = api_instance.create_temporary_file(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_temporary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body14**](Body14.md)|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tree_leaf**
> CreateResponse create_tree_leaf(project, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = NULL # dict(str, object) |  (optional)

try:
    api_response = api_instance.create_tree_leaf(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_tree_leaf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tree_leaf_type**
> CreateResponse create_tree_leaf_type(project, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = {
  "name" : "My tree leaf type"
} # object |  (optional)

try:
    api_response = api_instance.create_tree_leaf_type(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_tree_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_version**
> CreateResponse create_version(project, body=body)



Interact with a list of versions.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body22() # Body22 |  (optional)

try:
    api_response = api_instance.create_version(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body22**](Body22.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_frame_association**
> delete_frame_association(id)



Modify a frame association.  Frame associations specify which frames that a `State` object applies to.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> MessageResponse delete_job(run_uid)



Cancel a background job.  Algorithms and transcodes create argo workflows that are annotated with two uuid1 strings, one identifying the run and the other identifying the group. Jobs that are submitted together have the same group id, but each workflow has a unique run id.  This endpoint allows the user to cancel a job using the `run_uid` returned by either the `AlgorithmLaunch` or `Transcode` endpoints.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_group**
> MessageResponse delete_job_group(group_id)



Cancel a group of background jobs.  Algorithms and transcodes create argo workflows that are annotated with two uuid1 strings, one identifying the run and the other identifying the group. Jobs that are submitted together have the same group id, but each workflow has a unique run id.  This endpoint allows the user to cancel a group of jobs using the `group_id`  returned by either the `AlgorithmLaunch` or `Transcode` endpoints.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization_association**
> delete_localization_association(id)



Modify a localization association.  Localization associations specify which localizations that a `State` object applies to.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization_list**
> MessageResponse delete_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization_type**
> delete_localization_type(id)



Interact with an individual localization type.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media_list**
> MessageResponse delete_media_list(project)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.delete_media_list(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->delete_media_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media_type**
> delete_media_type(id)



Interact with an individual media type.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(id)



Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state_list**
> MessageResponse delete_state_list(project)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.delete_state_list(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->delete_state_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_temporary_file**
> delete_temporary_file(id)



Interact with temporary file.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_temporary_file_list**
> delete_temporary_file_list(project, expired=expired)



Interact with temporary file list.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tree_leaf_list**
> MessageResponse delete_tree_leaf_list(project, ancestor=ancestor, type=type, name=name)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
ancestor = 'ancestor_example' # str | Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia). (optional)
type = 56 # int | Unique integer identifying a tree leaf type. (optional)
name = 'name_example' # str | Name of the tree leaf element. (optional)

try:
    api_response = api_instance.delete_tree_leaf_list(project, ancestor=ancestor, type=type, name=name)
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

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version**
> delete_version(id)



Interact with individual version.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_algorithm_list**
> AlgorithmList get_algorithm_list(project)



Interact with algorithms that have been registered to a project.  For instructions on how to register an algorithm, visit `GitHub`_.  .. _GitHub:    https://github.com/cvisionai/tator/tree/master/examples/algorithms

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[**AlgorithmList**](AlgorithmList.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_list**
> AnalysisList get_analysis_list(project)



List analyses for a project.  Analysis objects are used to display information about filtered media lists and/or annotations on the project detail page of the web UI. Currently only counting analysis is supported.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[**AnalysisList**](AnalysisList.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_type**
> AttributeType get_attribute_type(id)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_type_list**
> AttributeTypeList get_attribute_type_list(project, applies_to=applies_to)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[**AttributeTypeList**](AttributeTypeList.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clip**
> str get_clip(id, frame_ranges, quality=quality)



Facility to get a clip from the server. Returns a temporary file object that expires in 24 hours.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a media object.
frame_ranges = ['frame_ranges_example'] # list[str] | Comma-seperated list of frame ranges to capture.
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

**str**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_type_schema**
> EntityTypeSchema get_entity_type_schema(id)



Output required fields for inserting a new object based on an EntityType.  Various REST calls take a polymorphic argument, which is dependent on what type is being added. This method provides a way to interrogate the service provider for what fields are required for a given addition.  The parameter to this function is the type id (i.e. the EntityTypeState or EntityTypeLocalization*** object that applies to a given media type.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_frame**
> str get_frame(id, frames=frames, tile=tile, roi=roi, animate=animate, quality=quality)



Facility to get a frame(jpg/png) of a given video frame, returns a square tile of frames based on the input parameter

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a media object.
frames = [[0]] # list[int] | Comma-seperated list of frames to capture. (optional) (default to [0])
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

**str**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_frame_association**
> dict(str, object) get_frame_association(id)



Modify a frame association.  Frame associations specify which frames that a `State` object applies to.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization**
> Localization get_localization(id)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_association**
> LocalizationAssociation get_localization_association(id)



Modify a localization association.  Localization associations specify which localizations that a `State` object applies to.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[**LocalizationAssociation**](LocalizationAssociation.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_list**
> LocalizationList get_localization_list(project)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.get_localization_list(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->get_localization_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**LocalizationList**](LocalizationList.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_type**
> InlineResponse200 get_localization_type(id)



Interact with an individual localization type.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_type_list**
> list get_localization_type_list(project, media_id=media_id, type=type)



Create or retrieve localization types.  A localization type is the metadata definition object for a localization. It includes shape, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

**list**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media**
> InlineResponse2001 get_media(id)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_list**
> list[object] get_media_list(project)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.get_media_list(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->get_media_list: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_next**
> InlineResponse2002 get_media_next(id, media_id=media_id, type=type, name=name, md5=md5, after=after)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a media object.
media_id = [56] # list[int] | List of integers identifying media. (optional)
type = 56 # int | Unique integer identifying media type. (optional)
name = 'name_example' # str | Name of the media to filter on. (optional)
md5 = 'md5_example' # str | MD5 sum of the media file. (optional)
after = 'after_example' # str | If given, all results returned will be after the file with this filename. The `start` and `stop` parameters are relative to this modified range. (optional)

try:
    api_response = api_instance.get_media_next(id, media_id=media_id, type=type, name=name, md5=md5, after=after)
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

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_prev**
> InlineResponse2003 get_media_prev(id)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a media object.

try:
    api_response = api_instance.get_media_prev(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->get_media_prev: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media object. | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_sections**
> dict(str, object) get_media_sections(project)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.get_media_sections(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->get_media_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

**dict(str, object)**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_type**
> InlineResponse2004 get_media_type(id)



Interact with an individual media type.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_type_list**
> list get_media_type_list(project)



Create or retrieve localization types.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

**list**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership**
> InlineResponse2005 get_membership(id)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership_list**
> list get_membership_list(project)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

**list**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> InlineResponse2006 get_project(id)



Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_list**
> list get_project_list()



Interact with a list of projects.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Project lists return all projects that the requesting user has access to.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))

try:
    api_response = api_instance.get_project_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->get_project_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section_analysis**
> dict(str, object) get_section_analysis(project, media_id=media_id)



Retrieve analysis results for a media list.  This endpoint uses objects created with the `Analysis` endpoint to perform analysis on filtered media lists.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
media_id = [56] # list[int] | Unique integer identifying a media. Use this to do analyis on a single file instead of sections. (optional)

try:
    api_response = api_instance.get_section_analysis(project, media_id=media_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->get_section_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_id** | [**list[int]**](int.md)| Unique integer identifying a media. Use this to do analyis on a single file instead of sections. | [optional] 

### Return type

**dict(str, object)**

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_list**
> list[InlineResponse2008] get_state_list(project)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.get_state_list(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->get_state_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

[**list[InlineResponse2008]**](InlineResponse2008.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_type**
> InlineResponse2007 get_state_type(id)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_type_list**
> list get_state_type_list(project)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.

try:
    api_response = api_instance.get_state_type_list(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->get_state_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 

### Return type

**list**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_file**
> InlineResponse2009 get_temporary_file(id)



Interact with temporary file.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_file_list**
> InlineResponse2009 get_temporary_file_list(project, expired=expired)



Interact with temporary file list.  Temporary files are files stored server side for a defined duration. The file must first be uploaded via tus, and can subsequently be saved using this endpoint.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree_leaf**
> InlineResponse20011 get_tree_leaf(id)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree_leaf_list**
> list get_tree_leaf_list(project, ancestor=ancestor, type=type, name=name)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
ancestor = 'ancestor_example' # str | Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia). (optional)
type = 56 # int | Unique integer identifying a tree leaf type. (optional)
name = 'name_example' # str | Name of the tree leaf element. (optional)

try:
    api_response = api_instance.get_tree_leaf_list(project, ancestor=ancestor, type=type, name=name)
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

### Return type

**list**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree_leaf_type**
> InlineResponse20012 get_tree_leaf_type(id)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree_leaf_type_list**
> list get_tree_leaf_type_list(project)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

**list**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> InlineResponse20015 get_user(id)



Interact with an individual user.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> InlineResponse20016 get_version(id)



Interact with individual version.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify**
> notify(body=body)



Send a notification to administrators.  Uses the Slack API to send a notification to system administrators. This endpoint can only be used by system administrators and must be configured in a Tator deployment's settings.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
body = tator.Body6() # Body6 |  (optional)

try:
    api_instance.notify(body=body)
except ApiException as e:
    print("Exception when calling TatorApi->notify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_save_video_api**
> partial_update_save_video_api(project, body=body)



Saves a transcoded video.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. To launch a transcode on raw uploaded video, use the  `Transcode` endpoint, which will create an Argo workflow to perform the transcode and save the video using this endpoint; no further REST calls are required. However, if you would like to perform transcodes locally, this endpoint enables that. The script at `scripts/transcoder/transcodePipeline.py` in the Tator source code provides an example of how to transcode a Tator-compatible video, upload it, and save it to the database using this endpoint.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.VideoUpdate() # VideoUpdate |  (optional)

try:
    api_instance.partial_update_save_video_api(project, body=body)
except ApiException as e:
    print("Exception when calling TatorApi->partial_update_save_video_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**VideoUpdate**](VideoUpdate.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **progress**
> MessageResponse progress(project, body=body)



Broadcast progress update.  Progress messages are sent in the web UI via WebSocket, and are displayed as progress bars associated with individual media files and as a summary in the webpage header. All members of a project can see progress bars from uploads and background jobs initiated by other users within the project. This endpoint accepts an array of messages, allowing for progress messages to be batched into a single request.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = [tator.Body7()] # list[Body7] |  (optional)

try:
    api_response = api_instance.progress(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**list[Body7]**](Body7.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_state_graphic_api**
> str retrieve_state_graphic_api(id, mode=mode, fps=fps, force_scale=force_scale)



Get frame(s) of a given localization-associated state.  Use the mode argument to control whether it is an animated gif or a tiled jpg.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a state.
mode = 'animate' # str | Whether to animate or tile. (optional) (default to animate)
fps = 2 # float | Frame rate if `mode` is `animate`. (optional) (default to 2)
force_scale = 'force_scale_example' # str | wxh to force each tile prior to stich (optional)

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
 **mode** | **str**| Whether to animate or tile. | [optional] [default to animate]
 **fps** | **float**| Frame rate if &#x60;mode&#x60; is &#x60;animate&#x60;. | [optional] [default to 2]
 **force_scale** | **str**| wxh to force each tile prior to stich | [optional] 

### Return type

**str**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_version_list**
> list retrieve_version_list(project, media_id=media_id)



Interact with a list of versions.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

**list**

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_image**
> CreateResponse save_image(project, body=body)



Saves an uploaded image.  Media is uploaded via tus, a separate mechanism from the REST API. Once an image upload is complete, the image must be saved to the database using this endpoint.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body8() # Body8 |  (optional)

try:
    api_response = api_instance.save_image(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->save_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body8**](Body8.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_video**
> CreateResponse save_video(project, body=body)



Saves a transcoded video.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. To launch a transcode on raw uploaded video, use the  `Transcode` endpoint, which will create an Argo workflow to perform the transcode and save the video using this endpoint; no further REST calls are required. However, if you would like to perform transcodes locally, this endpoint enables that. The script at `scripts/transcoder/transcodePipeline.py` in the Tator source code provides an example of how to transcode a Tator-compatible video, upload it, and save it to the database using this endpoint.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.VideoSpec() # VideoSpec |  (optional)

try:
    api_response = api_instance.save_video(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->save_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**VideoSpec**](VideoSpec.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcode**
> InlineResponse2013 transcode(project, body=body)



Start a transcode.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. This endpoint launches a transcode on raw uploaded video by creating an Argo workflow. The workflow will download the uploaded raw video, transcode it to the proper format, upload the transcoded video, and save the video using the  `SaveVideo` endpoint. Optionally, depending on the `keep_original` field of the video  type specified by the `type` parameter, the originally uploaded file may also be saved. Note that the raw video must be uploaded first via tus, which is a separate mechanism  from the REST API. This endpoint requires a group and run UUID associated with this  upload. If no progress messages were generated during upload, then the group and run  UUIDs can be newly generated.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body16() # Body16 |  (optional)

try:
    api_response = api_instance.transcode(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->transcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body16**](Body16.md)|  | [optional] 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tree_leaf_suggestion**
> list[InlineResponse20013] tree_leaf_suggestion(project, ancestor, query, min_level=min_level)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute_type**
> MessageResponse update_attribute_type(id, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an attribute type.
body = tator.AttributeTypeUpdate() # AttributeTypeUpdate |  (optional)

try:
    api_response = api_instance.update_attribute_type(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an attribute type. | 
 **body** | [**AttributeTypeUpdate**](AttributeTypeUpdate.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_frame_association**
> MessageResponse update_frame_association(id, body=body)



Modify a frame association.  Frame associations specify which frames that a `State` object applies to.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a frame association.
body = tator.Body() # Body |  (optional)

try:
    api_response = api_instance.update_frame_association(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_frame_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a frame association. | 
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization**
> MessageResponse update_localization(id, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a localization.
body = tator.LocalizationUpdate() # LocalizationUpdate |  (optional)

try:
    api_response = api_instance.update_localization(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_localization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization. | 
 **body** | [**LocalizationUpdate**](LocalizationUpdate.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization_association**
> MessageResponse update_localization_association(id, body=body)



Modify a localization association.  Localization associations specify which localizations that a `State` object applies to.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a localization association.
body = tator.LocalizationAssociationUpdate() # LocalizationAssociationUpdate |  (optional)

try:
    api_response = api_instance.update_localization_association(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_localization_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization association. | 
 **body** | [**LocalizationAssociationUpdate**](LocalizationAssociationUpdate.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization_list**
> MessageResponse update_localization_list(project, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.LocalizationListUpdate() # LocalizationListUpdate |  (optional)

try:
    api_response = api_instance.update_localization_list(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_localization_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**LocalizationListUpdate**](LocalizationListUpdate.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization_type**
> MessageResponse update_localization_type(id, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an localization type.
body = tator.Body1() # Body1 |  (optional)

try:
    api_response = api_instance.update_localization_type(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_localization_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an localization type. | 
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_media**
> MessageResponse update_media(id, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a media.
body = NULL # object |  (optional)

try:
    api_response = api_instance.update_media(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a media. | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_media_list**
> MessageResponse update_media_list(project, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body3() # Body3 |  (optional)

try:
    api_response = api_instance.update_media_list(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_media_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body3**](Body3.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_media_type**
> MessageResponse update_media_type(id, body=body)



Interact with an individual media type.  A media type is the metadata definition object for media. It includes file format, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an media type.
body = {
  "description" : "New description",
  "name" : "New name"
} # object |  (optional)

try:
    api_response = api_instance.update_media_type(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_media_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an media type. | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_membership**
> MessageResponse update_membership(id, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a membership.
body = tator.Body4() # Body4 |  (optional)

try:
    api_response = api_instance.update_membership(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a membership. | 
 **body** | [**Body4**](Body4.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> MessageResponse update_project(id, body=body)



Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a project.
body = {
  "name" : "New name",
  "summary" : "New summary"
} # object |  (optional)

try:
    api_response = api_instance.update_project(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a project. | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_state**
> MessageResponse update_state(id, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a state.
body = tator.Body9() # Body9 |  (optional)

try:
    api_response = api_instance.update_state(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state. | 
 **body** | [**Body9**](Body9.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_state_list**
> MessageResponse update_state_list(project, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body13() # Body13 |  (optional)

try:
    api_response = api_instance.update_state_list(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_state_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body13**](Body13.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_state_type**
> MessageResponse update_state_type(id, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a state type.
body = tator.Body10() # Body10 |  (optional)

try:
    api_response = api_instance.update_state_type(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_state_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a state type. | 
 **body** | [**Body10**](Body10.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tree_leaf**
> MessageResponse update_tree_leaf(id, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a tree leaf.
body = tator.Body17() # Body17 |  (optional)

try:
    api_response = api_instance.update_tree_leaf(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_tree_leaf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a tree leaf. | 
 **body** | [**Body17**](Body17.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tree_leaf_list**
> MessageResponse update_tree_leaf_list(project, body=body, ancestor=ancestor, type=type, name=name)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body19() # Body19 |  (optional)
ancestor = 'ancestor_example' # str | Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia). (optional)
type = 56 # int | Unique integer identifying a tree leaf type. (optional)
name = 'name_example' # str | Name of the tree leaf element. (optional)

try:
    api_response = api_instance.update_tree_leaf_list(project, body=body, ancestor=ancestor, type=type, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_tree_leaf_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body19**](Body19.md)|  | [optional] 
 **ancestor** | **str**| Get descendents of a tree leaf element (inclusive), by path (i.e. ITIS.Animalia). | [optional] 
 **type** | **int**| Unique integer identifying a tree leaf type. | [optional] 
 **name** | **str**| Name of the tree leaf element. | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tree_leaf_type**
> MessageResponse update_tree_leaf_type(id, body=body)



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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an tree_leaf type.
body = {
  "description" : "New description",
  "name" : "New name"
} # object |  (optional)

try:
    api_response = api_instance.update_tree_leaf_type(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_tree_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an tree_leaf type. | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> InlineResponse20015 update_user(id, body=body)



Interact with an individual user.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a localization association.
body = tator.Body20() # Body20 |  (optional)

try:
    api_response = api_instance.update_user(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization association. | 
 **body** | [**Body20**](Body20.md)|  | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version**
> MessageResponse update_version(id, body=body)



Interact with individual version.  Versions allow for multiple \"layers\" of annotations on the same media. Versions are created at the project level, but are only displayed for a given media if that media contains annotations in that version. The version of an annotation can be set by providing it in a POST operation. Currently only localizations and states can have versions.  Versions are used in conjunction with the `modified` flag to determine whether an annotation should be displayed for a given media while annotating.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a version.
body = tator.Body21() # Body21 |  (optional)

try:
    api_response = api_instance.update_version(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a version. | 
 **body** | [**Body21**](Body21.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **who_am_i**
> InlineResponse20014 who_am_i()



Returns the current user.  This is the equivalent of a whoami() operation.

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
api_instance = tator.TatorApi(tator.ApiClient(configuration))

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

