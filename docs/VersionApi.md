# tator.VersionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_version**](VersionApi.md#create_version) | **POST** /rest/Versions/{project} | 
[**delete_version**](VersionApi.md#delete_version) | **DELETE** /rest/Version/{id} | 
[**get_version**](VersionApi.md#get_version) | **GET** /rest/Version/{id} | 
[**retrieve_version_list**](VersionApi.md#retrieve_version_list) | **GET** /rest/Versions/{project} | 
[**update_version**](VersionApi.md#update_version) | **PATCH** /rest/Version/{id} | 

# **create_version**
> InlineResponse2019 create_version(project, body=body)



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
api_instance = tator.VersionApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
body = tator.Body32() # Body32 |  (optional)

try:
    api_response = api_instance.create_version(project, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->create_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **body** | [**Body32**](Body32.md)|  | [optional] 

### Return type

[**InlineResponse2019**](InlineResponse2019.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
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
api_instance = tator.VersionApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a version.

try:
    api_instance.delete_version(id)
except ApiException as e:
    print("Exception when calling VersionApi->delete_version: %s\n" % e)
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

# **get_version**
> InlineResponse20039 get_version(id)



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
api_instance = tator.VersionApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a version.

try:
    api_response = api_instance.get_version(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->get_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a version. | 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_version_list**
> list[InlineResponse20039] retrieve_version_list(project, media_id=media_id)



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
api_instance = tator.VersionApi(tator.ApiClient(configuration))
project = 56 # int | A unique integer identifying a project.
media_id = 56 # int | Unique integer identifying a media. (optional)

try:
    api_response = api_instance.retrieve_version_list(project, media_id=media_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->retrieve_version_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| A unique integer identifying a project. | 
 **media_id** | **int**| Unique integer identifying a media. | [optional] 

### Return type

[**list[InlineResponse20039]**](InlineResponse20039.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version**
> InlineResponse20040 update_version(id, body=body)



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
api_instance = tator.VersionApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a version.
body = tator.Body33() # Body33 |  (optional)

try:
    api_response = api_instance.update_version(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->update_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a version. | 
 **body** | [**Body33**](Body33.md)|  | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

