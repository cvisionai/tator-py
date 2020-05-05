# tator.EntityTypeSchemaApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entity_type_schema**](EntityTypeSchemaApi.md#get_entity_type_schema) | **GET** /rest/EntityTypeSchema/{id} | 

# **get_entity_type_schema**
> InlineResponse2003 get_entity_type_schema(id)



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
api_instance = tator.EntityTypeSchemaApi(tator.ApiClient(configuration))
id = 56 # int | A unique integer identifying an entity type.

try:
    api_response = api_instance.get_entity_type_schema(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityTypeSchemaApi->get_entity_type_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer identifying an entity type. | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[TokenAuth](../README.md#TokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

