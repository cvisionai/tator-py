# ColorMap

Maps an attribute value or version to a color/alpha. Use `key` and `map` (optionally `alpha_ranges`) to map an attribute value to colors. Use `version` to map version IDs to colors.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alpha_ranges** | **dict(str, list)** | Map of attribute values to alpha level. | [optional] 
**default** | [**Color**](Color.md) |  | [optional] 
**key** | **str** | Attribute name. | [optional] 
**map** | [**dict(str, Color)**](Color.md) | Map of attribute values to colors. | [optional] 
**version** | [**dict(str, Color)**](Color.md) | Map of version IDs to colors. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


