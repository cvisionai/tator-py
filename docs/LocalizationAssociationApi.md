# tator.LocalizationAssociationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_localization_association**](LocalizationAssociationApi.md#delete_localization_association) | **DELETE** /rest/LocalizationAssociation/{id} | 
[**get_localization_association**](LocalizationAssociationApi.md#get_localization_association) | **GET** /rest/LocalizationAssociation/{id} | 
[**update_localization_association**](LocalizationAssociationApi.md#update_localization_association) | **PATCH** /rest/LocalizationAssociation/{id} | 

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
api_instance = tator.LocalizationAssociationApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a localization association.

try:
    api_instance.delete_localization_association(id)
except ApiException as e:
    print("Exception when calling LocalizationAssociationApi->delete_localization_association: %s\n" % e)
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

# **get_localization_association**
> dict(str, object) get_localization_association(id)



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
api_instance = tator.LocalizationAssociationApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a localization association.

try:
    api_response = api_instance.get_localization_association(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationAssociationApi->get_localization_association: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localization_association**
> InlineResponse2005 update_localization_association(id, body=body)



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
api_instance = tator.LocalizationAssociationApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying a localization association.
body = tator.Body4() # Body4 |  (optional)

try:
    api_response = api_instance.update_localization_association(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationAssociationApi->update_localization_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying a localization association. | 
 **body** | [**Body4**](Body4.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

