# tator.TatorApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**algorithm_launch**](TatorApi.md#algorithm_launch) | **POST** /rest/AlgorithmLaunch/{project} | 
[**create_analysis**](TatorApi.md#create_analysis) | **POST** /rest/Analyses/{project} | 
[**create_leaf_list**](TatorApi.md#create_leaf_list) | **POST** /rest/Leaves/{project} | 
[**create_leaf_type**](TatorApi.md#create_leaf_type) | **POST** /rest/LeafTypes/{project} | 
[**create_localization_list**](TatorApi.md#create_localization_list) | **POST** /rest/Localizations/{project} | 
[**create_localization_type**](TatorApi.md#create_localization_type) | **POST** /rest/LocalizationTypes/{project} | 
[**create_media_type**](TatorApi.md#create_media_type) | **POST** /rest/MediaTypes/{project} | 
[**create_membership**](TatorApi.md#create_membership) | **POST** /rest/Memberships/{project} | 
[**create_obtain_auth_token**](TatorApi.md#create_obtain_auth_token) | **POST** /rest/Token | 
[**create_progress_summary_api**](TatorApi.md#create_progress_summary_api) | **POST** /rest/ProgressSummary/{project} | 
[**create_project**](TatorApi.md#create_project) | **POST** /rest/Projects | 
[**create_state_list**](TatorApi.md#create_state_list) | **POST** /rest/States/{project} | 
[**create_state_type**](TatorApi.md#create_state_type) | **POST** /rest/StateTypes/{project} | 
[**create_temporary_file**](TatorApi.md#create_temporary_file) | **POST** /rest/TemporaryFiles/{project} | 
[**create_version**](TatorApi.md#create_version) | **POST** /rest/Versions/{project} | 
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
[**notify**](TatorApi.md#notify) | **POST** /rest/Notify | 
[**progress**](TatorApi.md#progress) | **POST** /rest/Progress/{project} | 
[**save_image**](TatorApi.md#save_image) | **POST** /rest/SaveImage/{project} | 
[**save_video**](TatorApi.md#save_video) | **POST** /rest/SaveVideo/{project} | 
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
[**update_video**](TatorApi.md#update_video) | **PATCH** /rest/SaveVideo/{project} | 
[**whoami**](TatorApi.md#whoami) | **GET** /rest/User/GetCurrent | 

# **algorithm_launch**
> AlgorithmLaunch algorithm_launch(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**AlgorithmLaunch**](AlgorithmLaunch.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_analysis**
> CreateResponse create_analysis(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

# **create_leaf_list**
> CreateListResponse create_leaf_list(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = [tator.Leaf()] # list[Leaf] |  (optional)

try:
    api_response = api_instance.create_leaf_list(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_leaf_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**list[Leaf]**](Leaf.md)|  | [optional] 

### Return type

[**CreateListResponse**](CreateListResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_leaf_type**
> CreateResponse create_leaf_type(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.LeafTypeSpec() # LeafTypeSpec |  (optional)

try:
    api_response = api_instance.create_leaf_type(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**LeafTypeSpec**](LeafTypeSpec.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_localization_list**
> CreateListResponse create_localization_list(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = [tator.LocalizationSpec()] # list[LocalizationSpec] |  (optional)

try:
    api_response = api_instance.create_localization_list(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_localization_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**list[LocalizationSpec]**](LocalizationSpec.md)|  | [optional] 

### Return type

[**CreateListResponse**](CreateListResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_localization_type**
> CreateResponse create_localization_type(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.LocalizationTypeSpec() # LocalizationTypeSpec |  (optional)

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
 **body** | [**LocalizationTypeSpec**](LocalizationTypeSpec.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_media_type**
> CreateResponse create_media_type(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.MediaTypeSpec() # MediaTypeSpec |  (optional)

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
 **body** | [**MediaTypeSpec**](MediaTypeSpec.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_membership**
> CreateResponse create_membership(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.MembershipSpec() # MembershipSpec |  (optional)

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
 **body** | [**MembershipSpec**](MembershipSpec.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_obtain_auth_token**
> Token create_obtain_auth_token(body=body)



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
body = tator.Credentials() # Credentials |  (optional)

try:
    api_response = api_instance.create_obtain_auth_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_obtain_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Credentials**](Credentials.md)|  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_progress_summary_api**
> MessageResponse create_progress_summary_api(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.ProgressSummarySpec() # ProgressSummarySpec |  (optional)

try:
    api_response = api_instance.create_progress_summary_api(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_progress_summary_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**ProgressSummarySpec**](ProgressSummarySpec.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> CreateResponse create_project(body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.ProjectSpec() # ProjectSpec |  (optional)

try:
    api_response = api_instance.create_project(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectSpec**](ProjectSpec.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_state_list**
> CreateListResponse create_state_list(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = [tator.StateSpec()] # list[StateSpec] |  (optional)

try:
    api_response = api_instance.create_state_list(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->create_state_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**list[StateSpec]**](StateSpec.md)|  | [optional] 

### Return type

[**CreateListResponse**](CreateListResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_state_type**
> CreateResponse create_state_type(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.StateTypeSpec() # StateTypeSpec |  (optional)

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
 **body** | [**StateTypeSpec**](StateTypeSpec.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_temporary_file**
> CreateResponse create_temporary_file(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.TemporaryFileSpec() # TemporaryFileSpec |  (optional)

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
 **body** | [**TemporaryFileSpec**](TemporaryFileSpec.md)|  | [optional] 

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



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.VersionSpec() # VersionSpec |  (optional)

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
 **body** | [**VersionSpec**](VersionSpec.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> MessageResponse delete_job(run_uid)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

# **delete_leaf**
> delete_leaf(id)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_leaf_list**
> MessageResponse delete_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_leaf_type**
> MessageResponse delete_leaf_type(id)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization**
> MessageResponse delete_localization(id)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization_list**
> MessageResponse delete_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, exclude_parents=exclude_parents, frame=frame)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
version = [56] # list[int] | List of integers representing versions to fetch (optional)
modified = 1 # int | Whether to return original or modified annotations, 0 or 1. (optional) (default to 1)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization_type**
> MessageResponse delete_localization_type(id)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media**
> MessageResponse delete_media(id)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media_list**
> MessageResponse delete_media_list(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media_type**
> MessageResponse delete_media_type(id)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_membership**
> MessageResponse delete_membership(id)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> MessageResponse delete_project(id)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state**
> MessageResponse delete_state(id)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state_list**
> MessageResponse delete_state_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
version = [56] # list[int] | List of integers representing versions to fetch (optional)
modified = 1 # int | Whether to return original or modified annotations, 0 or 1. (optional) (default to 1)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state_type**
> MessageResponse delete_state_type(id)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_temporary_file**
> MessageResponse delete_temporary_file(id)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_temporary_file_list**
> delete_temporary_file_list(project, expired=expired)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version**
> MessageResponse delete_version(id)



Delete state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_algorithm_list**
> list[Algorithm] get_algorithm_list(project)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**list[Algorithm]**](Algorithm.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_list**
> list[Analysis] get_analysis_list(project)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**list[Analysis]**](Analysis.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clip**
> str get_clip(id, frame_ranges, quality=quality)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

# **get_frame**
> str get_frame(id, frames=frames, tile=tile, roi=roi, animate=animate, quality=quality)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

# **get_leaf**
> Leaf get_leaf(id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaf_list**
> list[Leaf] get_leaf_list(project, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaf_type**
> LeafType get_leaf_type(id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaf_type_list**
> list[LeafType] get_leaf_type_list(project)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization**
> Localization get_localization(id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

# **get_localization_list**
> list[Localization] get_localization_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, exclude_parents=exclude_parents, frame=frame)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
version = [56] # list[int] | List of integers representing versions to fetch (optional)
modified = 1 # int | Whether to return original or modified annotations, 0 or 1. (optional) (default to 1)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_type**
> LocalizationType get_localization_type(id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**LocalizationType**](LocalizationType.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_type_list**
> list[LocalizationType] get_localization_type_list(project, media_id=media_id, type=type)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**list[LocalizationType]**](LocalizationType.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media**
> Media get_media(id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**Media**](Media.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_list**
> list[Media] get_media_list(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_next**
> MediaNext get_media_next(id, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_prev**
> MediaPrev get_media_prev(id, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_sections**
> MediaSections get_media_sections(project, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**MediaSections**](MediaSections.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_type**
> MediaType get_media_type(id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**MediaType**](MediaType.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_type_list**
> list[MediaType] get_media_type_list(project)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**list[MediaType]**](MediaType.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership**
> Membership get_membership(id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**Membership**](Membership.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership_list**
> list[Membership] get_membership_list(project)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**list[Membership]**](Membership.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**Project**](Project.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_list**
> list[Project] get_project_list()



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**list[Project]**](Project.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section_analysis**
> SectionAnalysis get_section_analysis(project, media_id=media_id, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**SectionAnalysis**](SectionAnalysis.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state**
> get_state(id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

# **get_state_graphic**
> str get_state_graphic(id, mode=mode, fps=fps, force_scale=force_scale)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
    api_response = api_instance.get_state_graphic(id, mode=mode, fps=fps, force_scale=force_scale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->get_state_graphic: %s\n" % e)
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

# **get_state_list**
> list[State] get_state_list(project, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
version = [56] # list[int] | List of integers representing versions to fetch (optional)
modified = 1 # int | Whether to return original or modified annotations, 0 or 1. (optional) (default to 1)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_type**
> StateType get_state_type(id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**StateType**](StateType.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_type_list**
> list[StateType] get_state_type_list(project, media_id=media_id, type=type)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_file**
> TemporaryFile get_temporary_file(id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_file_list**
> list[TemporaryFile] get_temporary_file_list(project, expired=expired)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**list[TemporaryFile]**](TemporaryFile.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**User**](User.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> Version get_version(id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[**Version**](Version.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_list**
> list[Version] get_version_list(project, media_id=media_id)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaf_suggestion**
> list[LeafSuggestion] leaf_suggestion(project, ancestor, query, min_level=min_level)



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.NotifySpec() # NotifySpec |  (optional)

try:
    api_instance.notify(body=body)
except ApiException as e:
    print("Exception when calling TatorApi->notify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotifySpec**](NotifySpec.md)|  | [optional] 

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



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = [tator.ProgressSpec()] # list[ProgressSpec] |  (optional)

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
 **body** | [**list[ProgressSpec]**](ProgressSpec.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_image**
> CreateResponse save_image(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.ImageSpec() # ImageSpec |  (optional)

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
 **body** | [**ImageSpec**](ImageSpec.md)|  | [optional] 

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



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
> Transcode transcode(project, body=body)



Create state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.TranscodeSpec() # TranscodeSpec |  (optional)

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
 **body** | [**TranscodeSpec**](TranscodeSpec.md)|  | [optional] 

### Return type

[**Transcode**](Transcode.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_leaf**
> MessageResponse update_leaf(id, body=body)



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
id = 56 # int | A unique integer identifying a leaf.
body = tator.LeafUpdate() # LeafUpdate |  (optional)

try:
    api_response = api_instance.update_leaf(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_leaf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a leaf. | 
 **body** | [**LeafUpdate**](LeafUpdate.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_leaf_list**
> MessageResponse update_leaf_list(project, body=body, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.AttributeBulkUpdate() # AttributeBulkUpdate |  (optional)
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
    api_response = api_instance.update_leaf_list(project, body=body, ancestor=ancestor, type=type, name=name, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_leaf_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**AttributeBulkUpdate**](AttributeBulkUpdate.md)|  | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_leaf_type**
> MessageResponse update_leaf_type(id, body=body)



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
id = 56 # int | A unique integer identifying an leaf type.
body = tator.LeafTypeUpdate() # LeafTypeUpdate |  (optional)

try:
    api_response = api_instance.update_leaf_type(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_leaf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an leaf type. | 
 **body** | [**LeafTypeUpdate**](LeafTypeUpdate.md)|  | [optional] 

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



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

# **update_localization_list**
> MessageResponse update_localization_list(project, body=body, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, exclude_parents=exclude_parents, frame=frame)



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.AttributeBulkUpdate() # AttributeBulkUpdate |  (optional)
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = [56] # list[int] | List of integers representing versions to fetch (optional)
modified = 1 # int | Whether to return original or modified annotations, 0 or 1. (optional) (default to 1)
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
exclude_parents = 0 # int | If a clone is present, do not send parent. (0 or 1) (optional) (default to 0)
frame = 56 # int | Frame number of this localization if it is in a video. (optional)

try:
    api_response = api_instance.update_localization_list(project, body=body, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop, exclude_parents=exclude_parents, frame=frame)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TatorApi->update_localization_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**AttributeBulkUpdate**](AttributeBulkUpdate.md)|  | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization_type**
> MessageResponse update_localization_type(id, body=body)



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.LocalizationTypeUpdate() # LocalizationTypeUpdate |  (optional)

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
 **body** | [**LocalizationTypeUpdate**](LocalizationTypeUpdate.md)|  | [optional] 

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



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.MediaUpdate() # MediaUpdate |  (optional)

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
 **body** | [**MediaUpdate**](MediaUpdate.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_media_list**
> MessageResponse update_media_list(project, body=body, media_id=media_id, type=type, name=name, md5=md5, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.AttributeBulkUpdate() # AttributeBulkUpdate |  (optional)
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
    print("Exception when calling TatorApi->update_media_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**AttributeBulkUpdate**](AttributeBulkUpdate.md)|  | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_media_type**
> MessageResponse update_media_type(id, body=body)



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.MediaTypeUpdate() # MediaTypeUpdate |  (optional)

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
 **body** | [**MediaTypeUpdate**](MediaTypeUpdate.md)|  | [optional] 

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



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.MembershipUpdate() # MembershipUpdate |  (optional)

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
 **body** | [**MembershipUpdate**](MembershipUpdate.md)|  | [optional] 

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



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.ProjectSpec() # ProjectSpec |  (optional)

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
 **body** | [**ProjectSpec**](ProjectSpec.md)|  | [optional] 

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



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.StateUpdate() # StateUpdate |  (optional)

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
 **body** | [**StateUpdate**](StateUpdate.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_state_list**
> MessageResponse update_state_list(project, body=body, media_query=media_query, media_id=media_id, type=type, version=version, modified=modified, after=after, search=search, attribute=attribute, attribute_lt=attribute_lt, attribute_lte=attribute_lte, attribute_gt=attribute_gt, attribute_gte=attribute_gte, attribute_contains=attribute_contains, attribute_distance=attribute_distance, attribute_null=attribute_null, operation=operation, start=start, stop=stop)



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.AttributeBulkUpdate() # AttributeBulkUpdate |  (optional)
media_query = 'media_query_example' # str | Query string used to filter media IDs. If supplied, media_id will be ignored. (optional)
media_id = [56] # list[int] | Comma-separated list of media IDs. (optional)
type = 56 # int | Unique integer identifying a annotation type. (optional)
version = [56] # list[int] | List of integers representing versions to fetch (optional)
modified = 1 # int | Whether to return original or modified annotations, 0 or 1. (optional) (default to 1)
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
    print("Exception when calling TatorApi->update_state_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**AttributeBulkUpdate**](AttributeBulkUpdate.md)|  | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_state_type**
> MessageResponse update_state_type(id, body=body)



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.StateTypeUpdate() # StateTypeUpdate |  (optional)

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
 **body** | [**StateTypeUpdate**](StateTypeUpdate.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(id, body=body)



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.UserUpdate() # UserUpdate |  (optional)

try:
    api_instance.update_user(id, body=body)
except ApiException as e:
    print("Exception when calling TatorApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization association. | 
 **body** | [**UserUpdate**](UserUpdate.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version**
> MessageResponse update_version(id, body=body)



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
body = tator.VersionUpdate() # VersionUpdate |  (optional)

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
 **body** | [**VersionUpdate**](VersionUpdate.md)|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_video**
> update_video(project, body=body)



Update state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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
    api_instance.update_video(project, body=body)
except ApiException as e:
    print("Exception when calling TatorApi->update_video: %s\n" % e)
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

# **whoami**
> User whoami()



Retrieve state type.  A state type is the metadata definition object for a state. It includes association type, name, description, and (like other entity types) may have any number of attribute types associated with it.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

