# AttributeType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autocomplete** | [**AutocompleteService**](AutocompleteService.md) |  | [optional] 
**choices** | **list[str]** | Array of possible values for enum dtype. | [optional] 
**default** | [**OneOfbooleannumberstringarray**](OneOfbooleannumberstringarray.md) | Default value for the attribute. | [optional] 
**description** | **str** | Description of the attribute. | [optional] [default to '']
**dtype** | **str** | Data type of the attribute. | [optional] 
**labels** | **list[str]** | Array of labels for enum dtype. | [optional] 
**maximum** | **float** | Upper bound for int or float dtype. | [optional] 
**minimum** | **float** | Lower bound for int or float dtype. | [optional] 
**name** | **str** | Name of the attribute. | [optional] 
**order** | **int** | Integer specifying relative order this attribute is displayed in the UI. Negative values are hidden by default. | [optional] [default to 0]
**required** | **bool** | True if this attribute is required for POST requests. | [optional] [default to False]
**use_current** | **bool** | True to use current datetime as default for datetime dtype. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


