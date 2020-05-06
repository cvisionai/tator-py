# coding: utf-8

"""
    Tator REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tator.configuration import Configuration


class AttributeTypeOneOf2(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'applies_to': 'int',
        'default': 'float',
        'description': 'str',
        'dtype': 'str',
        'lower_bound': 'float',
        'name': 'str',
        'order': 'int',
        'upper_bound': 'float'
    }

    attribute_map = {
        'applies_to': 'applies_to',
        'default': 'default',
        'description': 'description',
        'dtype': 'dtype',
        'lower_bound': 'lower_bound',
        'name': 'name',
        'order': 'order',
        'upper_bound': 'upper_bound'
    }

    def __init__(self, applies_to=None, default=None, description='', dtype=None, lower_bound=None, name=None, order=0, upper_bound=None, local_vars_configuration=None):  # noqa: E501
        """AttributeTypeOneOf2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._applies_to = None
        self._default = None
        self._description = None
        self._dtype = None
        self._lower_bound = None
        self._name = None
        self._order = None
        self._upper_bound = None
        self.discriminator = None

        self.applies_to = applies_to
        if default is not None:
            self.default = default
        if description is not None:
            self.description = description
        self.dtype = dtype
        if lower_bound is not None:
            self.lower_bound = lower_bound
        self.name = name
        if order is not None:
            self.order = order
        if upper_bound is not None:
            self.upper_bound = upper_bound

    @property
    def applies_to(self):
        """Gets the applies_to of this AttributeTypeOneOf2.  # noqa: E501

        Unique integer identifying the entity type that this attribute describes.  # noqa: E501

        :return: The applies_to of this AttributeTypeOneOf2.  # noqa: E501
        :rtype: int
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this AttributeTypeOneOf2.

        Unique integer identifying the entity type that this attribute describes.  # noqa: E501

        :param applies_to: The applies_to of this AttributeTypeOneOf2.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and applies_to is None:  # noqa: E501
            raise ValueError("Invalid value for `applies_to`, must not be `None`")  # noqa: E501

        self._applies_to = applies_to

    @property
    def default(self):
        """Gets the default of this AttributeTypeOneOf2.  # noqa: E501

        Default value for the attribute.  # noqa: E501

        :return: The default of this AttributeTypeOneOf2.  # noqa: E501
        :rtype: float
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this AttributeTypeOneOf2.

        Default value for the attribute.  # noqa: E501

        :param default: The default of this AttributeTypeOneOf2.  # noqa: E501
        :type: float
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this AttributeTypeOneOf2.  # noqa: E501

        Description of the attribute.  # noqa: E501

        :return: The description of this AttributeTypeOneOf2.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AttributeTypeOneOf2.

        Description of the attribute.  # noqa: E501

        :param description: The description of this AttributeTypeOneOf2.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dtype(self):
        """Gets the dtype of this AttributeTypeOneOf2.  # noqa: E501

        Data type of the attribute.  # noqa: E501

        :return: The dtype of this AttributeTypeOneOf2.  # noqa: E501
        :rtype: str
        """
        return self._dtype

    @dtype.setter
    def dtype(self, dtype):
        """Sets the dtype of this AttributeTypeOneOf2.

        Data type of the attribute.  # noqa: E501

        :param dtype: The dtype of this AttributeTypeOneOf2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dtype is None:  # noqa: E501
            raise ValueError("Invalid value for `dtype`, must not be `None`")  # noqa: E501
        allowed_values = ["float"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and dtype not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `dtype` ({0}), must be one of {1}"  # noqa: E501
                .format(dtype, allowed_values)
            )

        self._dtype = dtype

    @property
    def lower_bound(self):
        """Gets the lower_bound of this AttributeTypeOneOf2.  # noqa: E501

        Lower bound.  # noqa: E501

        :return: The lower_bound of this AttributeTypeOneOf2.  # noqa: E501
        :rtype: float
        """
        return self._lower_bound

    @lower_bound.setter
    def lower_bound(self, lower_bound):
        """Sets the lower_bound of this AttributeTypeOneOf2.

        Lower bound.  # noqa: E501

        :param lower_bound: The lower_bound of this AttributeTypeOneOf2.  # noqa: E501
        :type: float
        """

        self._lower_bound = lower_bound

    @property
    def name(self):
        """Gets the name of this AttributeTypeOneOf2.  # noqa: E501

        Name of the attribute.  # noqa: E501

        :return: The name of this AttributeTypeOneOf2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AttributeTypeOneOf2.

        Name of the attribute.  # noqa: E501

        :param name: The name of this AttributeTypeOneOf2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def order(self):
        """Gets the order of this AttributeTypeOneOf2.  # noqa: E501

        Integer specifying relative order this attribute is displayed in the UI. Negative values are hidden by default.  # noqa: E501

        :return: The order of this AttributeTypeOneOf2.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this AttributeTypeOneOf2.

        Integer specifying relative order this attribute is displayed in the UI. Negative values are hidden by default.  # noqa: E501

        :param order: The order of this AttributeTypeOneOf2.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def upper_bound(self):
        """Gets the upper_bound of this AttributeTypeOneOf2.  # noqa: E501

        Upper bound.  # noqa: E501

        :return: The upper_bound of this AttributeTypeOneOf2.  # noqa: E501
        :rtype: float
        """
        return self._upper_bound

    @upper_bound.setter
    def upper_bound(self, upper_bound):
        """Sets the upper_bound of this AttributeTypeOneOf2.

        Upper bound.  # noqa: E501

        :param upper_bound: The upper_bound of this AttributeTypeOneOf2.  # noqa: E501
        :type: float
        """

        self._upper_bound = upper_bound

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AttributeTypeOneOf2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttributeTypeOneOf2):
            return True

        return self.to_dict() != other.to_dict()
