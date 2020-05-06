# tator
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import tator
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import tator
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TatorApi* | [**algorithm_launch**](docs/TatorApi.md#algorithm_launch) | **POST** /rest/AlgorithmLaunch/{project} | 
*TatorApi* | [**create_analysis**](docs/TatorApi.md#create_analysis) | **POST** /rest/Analyses/{project} | 
*TatorApi* | [**create_attribute_type**](docs/TatorApi.md#create_attribute_type) | **POST** /rest/AttributeTypes/{project} | 
*TatorApi* | [**create_localization**](docs/TatorApi.md#create_localization) | **POST** /rest/Localizations/{project} | 
*TatorApi* | [**create_localization_type**](docs/TatorApi.md#create_localization_type) | **POST** /rest/LocalizationTypes/{project} | 
*TatorApi* | [**create_media_type**](docs/TatorApi.md#create_media_type) | **POST** /rest/MediaTypes/{project} | 
*TatorApi* | [**create_membership**](docs/TatorApi.md#create_membership) | **POST** /rest/Memberships/{project} | 
*TatorApi* | [**create_obtain_auth_token**](docs/TatorApi.md#create_obtain_auth_token) | **POST** /rest/Token | 
*TatorApi* | [**create_project**](docs/TatorApi.md#create_project) | **POST** /rest/Projects | 
*TatorApi* | [**create_state**](docs/TatorApi.md#create_state) | **POST** /rest/States/{project} | 
*TatorApi* | [**create_state_type**](docs/TatorApi.md#create_state_type) | **POST** /rest/StateTypes/{project} | 
*TatorApi* | [**create_temporary_file**](docs/TatorApi.md#create_temporary_file) | **POST** /rest/TemporaryFiles/{project} | 
*TatorApi* | [**create_tree_leaf**](docs/TatorApi.md#create_tree_leaf) | **POST** /rest/TreeLeaves/{project} | 
*TatorApi* | [**create_tree_leaf_type**](docs/TatorApi.md#create_tree_leaf_type) | **POST** /rest/TreeLeafTypes/{project} | 
*TatorApi* | [**create_version**](docs/TatorApi.md#create_version) | **POST** /rest/Versions/{project} | 
*TatorApi* | [**delete_attribute_type**](docs/TatorApi.md#delete_attribute_type) | **DELETE** /rest/AttributeType/{id} | 
*TatorApi* | [**delete_frame_association**](docs/TatorApi.md#delete_frame_association) | **DELETE** /rest/FrameAssociation/{id} | 
*TatorApi* | [**delete_job**](docs/TatorApi.md#delete_job) | **DELETE** /rest/Job/{run_uid} | 
*TatorApi* | [**delete_job_group**](docs/TatorApi.md#delete_job_group) | **DELETE** /rest/JobGroup/{group_id} | 
*TatorApi* | [**delete_localization**](docs/TatorApi.md#delete_localization) | **DELETE** /rest/Localization/{id} | 
*TatorApi* | [**delete_localization_association**](docs/TatorApi.md#delete_localization_association) | **DELETE** /rest/LocalizationAssociation/{id} | 
*TatorApi* | [**delete_localization_list**](docs/TatorApi.md#delete_localization_list) | **DELETE** /rest/Localizations/{project} | 
*TatorApi* | [**delete_localization_type**](docs/TatorApi.md#delete_localization_type) | **DELETE** /rest/LocalizationType/{id} | 
*TatorApi* | [**delete_media**](docs/TatorApi.md#delete_media) | **DELETE** /rest/Media/{id} | 
*TatorApi* | [**delete_media_list**](docs/TatorApi.md#delete_media_list) | **DELETE** /rest/Medias/{project} | 
*TatorApi* | [**delete_media_type**](docs/TatorApi.md#delete_media_type) | **DELETE** /rest/MediaType/{id} | 
*TatorApi* | [**delete_membership**](docs/TatorApi.md#delete_membership) | **DELETE** /rest/Membership/{id} | 
*TatorApi* | [**delete_project**](docs/TatorApi.md#delete_project) | **DELETE** /rest/Project/{id} | 
*TatorApi* | [**delete_state**](docs/TatorApi.md#delete_state) | **DELETE** /rest/State/{id} | 
*TatorApi* | [**delete_state_list**](docs/TatorApi.md#delete_state_list) | **DELETE** /rest/States/{project} | 
*TatorApi* | [**delete_state_type**](docs/TatorApi.md#delete_state_type) | **DELETE** /rest/StateType/{id} | 
*TatorApi* | [**delete_temporary_file**](docs/TatorApi.md#delete_temporary_file) | **DELETE** /rest/TemporaryFile/{id} | 
*TatorApi* | [**delete_temporary_file_list**](docs/TatorApi.md#delete_temporary_file_list) | **DELETE** /rest/TemporaryFiles/{project} | 
*TatorApi* | [**delete_tree_leaf**](docs/TatorApi.md#delete_tree_leaf) | **DELETE** /rest/TreeLeaf/{id} | 
*TatorApi* | [**delete_tree_leaf_list**](docs/TatorApi.md#delete_tree_leaf_list) | **DELETE** /rest/TreeLeaves/{project} | 
*TatorApi* | [**delete_tree_leaf_type**](docs/TatorApi.md#delete_tree_leaf_type) | **DELETE** /rest/TreeLeafType/{id} | 
*TatorApi* | [**delete_version**](docs/TatorApi.md#delete_version) | **DELETE** /rest/Version/{id} | 
*TatorApi* | [**get_algorithm_list**](docs/TatorApi.md#get_algorithm_list) | **GET** /rest/Algorithms/{project} | 
*TatorApi* | [**get_analysis_list**](docs/TatorApi.md#get_analysis_list) | **GET** /rest/Analyses/{project} | 
*TatorApi* | [**get_attribute_type**](docs/TatorApi.md#get_attribute_type) | **GET** /rest/AttributeType/{id} | 
*TatorApi* | [**get_attribute_type_list**](docs/TatorApi.md#get_attribute_type_list) | **GET** /rest/AttributeTypes/{project} | 
*TatorApi* | [**get_clip**](docs/TatorApi.md#get_clip) | **GET** /rest/GetClip/{id} | 
*TatorApi* | [**get_entity_type_schema**](docs/TatorApi.md#get_entity_type_schema) | **GET** /rest/EntityTypeSchema/{id} | 
*TatorApi* | [**get_frame**](docs/TatorApi.md#get_frame) | **GET** /rest/GetFrame/{id} | 
*TatorApi* | [**get_frame_association**](docs/TatorApi.md#get_frame_association) | **GET** /rest/FrameAssociation/{id} | 
*TatorApi* | [**get_localization**](docs/TatorApi.md#get_localization) | **GET** /rest/Localization/{id} | 
*TatorApi* | [**get_localization_association**](docs/TatorApi.md#get_localization_association) | **GET** /rest/LocalizationAssociation/{id} | 
*TatorApi* | [**get_localization_list**](docs/TatorApi.md#get_localization_list) | **GET** /rest/Localizations/{project} | 
*TatorApi* | [**get_localization_type**](docs/TatorApi.md#get_localization_type) | **GET** /rest/LocalizationType/{id} | 
*TatorApi* | [**get_localization_type_list**](docs/TatorApi.md#get_localization_type_list) | **GET** /rest/LocalizationTypes/{project} | 
*TatorApi* | [**get_media**](docs/TatorApi.md#get_media) | **GET** /rest/Media/{id} | 
*TatorApi* | [**get_media_list**](docs/TatorApi.md#get_media_list) | **GET** /rest/Medias/{project} | 
*TatorApi* | [**get_media_next**](docs/TatorApi.md#get_media_next) | **GET** /rest/MediaNext/{id} | 
*TatorApi* | [**get_media_prev**](docs/TatorApi.md#get_media_prev) | **GET** /rest/MediaPrev/{id} | 
*TatorApi* | [**get_media_sections**](docs/TatorApi.md#get_media_sections) | **GET** /rest/MediaSections/{project} | 
*TatorApi* | [**get_media_type**](docs/TatorApi.md#get_media_type) | **GET** /rest/MediaType/{id} | 
*TatorApi* | [**get_media_type_list**](docs/TatorApi.md#get_media_type_list) | **GET** /rest/MediaTypes/{project} | 
*TatorApi* | [**get_membership**](docs/TatorApi.md#get_membership) | **GET** /rest/Membership/{id} | 
*TatorApi* | [**get_membership_list**](docs/TatorApi.md#get_membership_list) | **GET** /rest/Memberships/{project} | 
*TatorApi* | [**get_project**](docs/TatorApi.md#get_project) | **GET** /rest/Project/{id} | 
*TatorApi* | [**get_project_list**](docs/TatorApi.md#get_project_list) | **GET** /rest/Projects | 
*TatorApi* | [**get_section_analysis**](docs/TatorApi.md#get_section_analysis) | **GET** /rest/SectionAnalysis/{project} | 
*TatorApi* | [**get_state**](docs/TatorApi.md#get_state) | **GET** /rest/State/{id} | 
*TatorApi* | [**get_state_list**](docs/TatorApi.md#get_state_list) | **GET** /rest/States/{project} | 
*TatorApi* | [**get_state_type**](docs/TatorApi.md#get_state_type) | **GET** /rest/StateType/{id} | 
*TatorApi* | [**get_state_type_list**](docs/TatorApi.md#get_state_type_list) | **GET** /rest/StateTypes/{project} | 
*TatorApi* | [**get_temporary_file**](docs/TatorApi.md#get_temporary_file) | **GET** /rest/TemporaryFile/{id} | 
*TatorApi* | [**get_temporary_file_list**](docs/TatorApi.md#get_temporary_file_list) | **GET** /rest/TemporaryFiles/{project} | 
*TatorApi* | [**get_tree_leaf**](docs/TatorApi.md#get_tree_leaf) | **GET** /rest/TreeLeaf/{id} | 
*TatorApi* | [**get_tree_leaf_list**](docs/TatorApi.md#get_tree_leaf_list) | **GET** /rest/TreeLeaves/{project} | 
*TatorApi* | [**get_tree_leaf_type**](docs/TatorApi.md#get_tree_leaf_type) | **GET** /rest/TreeLeafType/{id} | 
*TatorApi* | [**get_tree_leaf_type_list**](docs/TatorApi.md#get_tree_leaf_type_list) | **GET** /rest/TreeLeafTypes/{project} | 
*TatorApi* | [**get_user**](docs/TatorApi.md#get_user) | **GET** /rest/User/{id} | 
*TatorApi* | [**get_version**](docs/TatorApi.md#get_version) | **GET** /rest/Version/{id} | 
*TatorApi* | [**notify**](docs/TatorApi.md#notify) | **POST** /rest/Notify | 
*TatorApi* | [**partial_update_save_video_api**](docs/TatorApi.md#partial_update_save_video_api) | **PATCH** /rest/SaveVideo/{project} | 
*TatorApi* | [**progress**](docs/TatorApi.md#progress) | **POST** /rest/Progress/{project} | 
*TatorApi* | [**retrieve_state_graphic_api**](docs/TatorApi.md#retrieve_state_graphic_api) | **GET** /rest/StateGraphic/{id} | 
*TatorApi* | [**retrieve_version_list**](docs/TatorApi.md#retrieve_version_list) | **GET** /rest/Versions/{project} | 
*TatorApi* | [**save_image**](docs/TatorApi.md#save_image) | **POST** /rest/SaveImage/{project} | 
*TatorApi* | [**save_video**](docs/TatorApi.md#save_video) | **POST** /rest/SaveVideo/{project} | 
*TatorApi* | [**transcode**](docs/TatorApi.md#transcode) | **POST** /rest/Transcode/{project} | 
*TatorApi* | [**tree_leaf_suggestion**](docs/TatorApi.md#tree_leaf_suggestion) | **GET** /rest/TreeLeaves/Suggestion/{ancestor}/{project} | 
*TatorApi* | [**update_attribute_type**](docs/TatorApi.md#update_attribute_type) | **PATCH** /rest/AttributeType/{id} | 
*TatorApi* | [**update_frame_association**](docs/TatorApi.md#update_frame_association) | **PATCH** /rest/FrameAssociation/{id} | 
*TatorApi* | [**update_localization**](docs/TatorApi.md#update_localization) | **PATCH** /rest/Localization/{id} | 
*TatorApi* | [**update_localization_association**](docs/TatorApi.md#update_localization_association) | **PATCH** /rest/LocalizationAssociation/{id} | 
*TatorApi* | [**update_localization_list**](docs/TatorApi.md#update_localization_list) | **PATCH** /rest/Localizations/{project} | 
*TatorApi* | [**update_localization_type**](docs/TatorApi.md#update_localization_type) | **PATCH** /rest/LocalizationType/{id} | 
*TatorApi* | [**update_media**](docs/TatorApi.md#update_media) | **PATCH** /rest/Media/{id} | 
*TatorApi* | [**update_media_list**](docs/TatorApi.md#update_media_list) | **PATCH** /rest/Medias/{project} | 
*TatorApi* | [**update_media_type**](docs/TatorApi.md#update_media_type) | **PATCH** /rest/MediaType/{id} | 
*TatorApi* | [**update_membership**](docs/TatorApi.md#update_membership) | **PATCH** /rest/Membership/{id} | 
*TatorApi* | [**update_project**](docs/TatorApi.md#update_project) | **PATCH** /rest/Project/{id} | 
*TatorApi* | [**update_state**](docs/TatorApi.md#update_state) | **PATCH** /rest/State/{id} | 
*TatorApi* | [**update_state_list**](docs/TatorApi.md#update_state_list) | **PATCH** /rest/States/{project} | 
*TatorApi* | [**update_state_type**](docs/TatorApi.md#update_state_type) | **PATCH** /rest/StateType/{id} | 
*TatorApi* | [**update_tree_leaf**](docs/TatorApi.md#update_tree_leaf) | **PATCH** /rest/TreeLeaf/{id} | 
*TatorApi* | [**update_tree_leaf_list**](docs/TatorApi.md#update_tree_leaf_list) | **PATCH** /rest/TreeLeaves/{project} | 
*TatorApi* | [**update_tree_leaf_type**](docs/TatorApi.md#update_tree_leaf_type) | **PATCH** /rest/TreeLeafType/{id} | 
*TatorApi* | [**update_user**](docs/TatorApi.md#update_user) | **PATCH** /rest/User/{id} | 
*TatorApi* | [**update_version**](docs/TatorApi.md#update_version) | **PATCH** /rest/Version/{id} | 
*TatorApi* | [**who_am_i**](docs/TatorApi.md#who_am_i) | **GET** /rest/User/GetCurrent | 


## Documentation For Models

 - [AlgorithmLaunchResponse](docs/AlgorithmLaunchResponse.md)
 - [AlgorithmLaunchSpec](docs/AlgorithmLaunchSpec.md)
 - [AnalysisSpec](docs/AnalysisSpec.md)
 - [AttributeBulkUpdate](docs/AttributeBulkUpdate.md)
 - [AttributeType](docs/AttributeType.md)
 - [AttributeTypeOneOf](docs/AttributeTypeOneOf.md)
 - [AttributeTypeOneOf1](docs/AttributeTypeOneOf1.md)
 - [AttributeTypeOneOf2](docs/AttributeTypeOneOf2.md)
 - [AttributeTypeOneOf3](docs/AttributeTypeOneOf3.md)
 - [AttributeTypeOneOf4](docs/AttributeTypeOneOf4.md)
 - [AttributeTypeOneOf5](docs/AttributeTypeOneOf5.md)
 - [AttributeTypeOneOf6](docs/AttributeTypeOneOf6.md)
 - [AttributeTypeSpec](docs/AttributeTypeSpec.md)
 - [AttributeTypeUpdate](docs/AttributeTypeUpdate.md)
 - [Box](docs/Box.md)
 - [BoxElement](docs/BoxElement.md)
 - [BoxSpec](docs/BoxSpec.md)
 - [BoxUpdate](docs/BoxUpdate.md)
 - [CreateResponse](docs/CreateResponse.md)
 - [Dot](docs/Dot.md)
 - [DotElement](docs/DotElement.md)
 - [DotSpec](docs/DotSpec.md)
 - [DotUpdate](docs/DotUpdate.md)
 - [EntityTypeSchema](docs/EntityTypeSchema.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject10](docs/InlineObject10.md)
 - [InlineObject11](docs/InlineObject11.md)
 - [InlineObject12](docs/InlineObject12.md)
 - [InlineObject13](docs/InlineObject13.md)
 - [InlineObject14](docs/InlineObject14.md)
 - [InlineObject15](docs/InlineObject15.md)
 - [InlineObject16](docs/InlineObject16.md)
 - [InlineObject17](docs/InlineObject17.md)
 - [InlineObject18](docs/InlineObject18.md)
 - [InlineObject19](docs/InlineObject19.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject20](docs/InlineObject20.md)
 - [InlineObject21](docs/InlineObject21.md)
 - [InlineObject22](docs/InlineObject22.md)
 - [InlineObject23](docs/InlineObject23.md)
 - [InlineObject24](docs/InlineObject24.md)
 - [InlineObject25](docs/InlineObject25.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [InlineObject5](docs/InlineObject5.md)
 - [InlineObject6](docs/InlineObject6.md)
 - [InlineObject7](docs/InlineObject7.md)
 - [InlineObject8](docs/InlineObject8.md)
 - [InlineObject9](docs/InlineObject9.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20012Type](docs/InlineResponse20012Type.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2005Type](docs/InlineResponse2005Type.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2008Type](docs/InlineResponse2008Type.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse200Type](docs/InlineResponse200Type.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineResponse2012](docs/InlineResponse2012.md)
 - [InlineResponse2013](docs/InlineResponse2013.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [InlineResponse404](docs/InlineResponse404.md)
 - [Line](docs/Line.md)
 - [LineElement](docs/LineElement.md)
 - [LineSpec](docs/LineSpec.md)
 - [LineUpdate](docs/LineUpdate.md)
 - [Localization](docs/Localization.md)
 - [LocalizationAssociationUpdate](docs/LocalizationAssociationUpdate.md)
 - [LocalizationList](docs/LocalizationList.md)
 - [LocalizationSpec](docs/LocalizationSpec.md)
 - [LocalizationUpdate](docs/LocalizationUpdate.md)
 - [MessageResponse](docs/MessageResponse.md)
 - [VideoSpec](docs/VideoSpec.md)
 - [VideoUpdate](docs/VideoUpdate.md)


## Documentation For Authorization


## TokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




