# AttributeType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to** | **int** | Unique integer identifying the entity type that this attribute describes. | 
**default** | **list[float]** | Default value for the attribute. Order is lon, lat. | [optional] 
**description** | **str** | Description of the attribute. | [optional] [default to '']
**dtype** | **str** | Data type of the attribute. | 
**name** | **str** | Name of the attribute. | 
**order** | **int** | Integer specifying relative order this attribute is displayed in the UI. Negative values are hidden by default. | [optional] [default to 0]
**lower_bound** | **float** | Lower bound. | [optional] 
**upper_bound** | **float** | Upper bound. | [optional] 
**autocomplete** | [**object**](.md) | Object indicating URL of autocomplete service for string dtype. | [optional] 
**choices** | **list[str]** | Array of possible values. | [optional] 
**labels** | **list[str]** | Array of labels. | [optional] 
**use_current** | **bool** | True to use current datetime as default for datetime dtype. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


