# coding: utf-8

"""
    Tator REST API

    Interface to the Tator backend.  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tator_openapi.configuration import Configuration


class LeafSuggestion(object):
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
        'data': 'dict(str, AttributeValue)',
        'group': 'str',
        'value': 'str'
    }

    attribute_map = {
        'data': 'data',
        'group': 'group',
        'value': 'value'
    }

    def __init__(self, data=None, group=None, value=None, local_vars_configuration=None):  # noqa: E501
        """LeafSuggestion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._group = None
        self._value = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if group is not None:
            self.group = group
        if value is not None:
            self.value = value

    @property
    def data(self):
        """Gets the data of this LeafSuggestion.  # noqa: E501

        Auxiliary data associated with the leaf.  # noqa: E501

        :return: The data of this LeafSuggestion.  # noqa: E501
        :rtype: dict(str, AttributeValue)
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this LeafSuggestion.

        Auxiliary data associated with the leaf.  # noqa: E501

        :param data: The data of this LeafSuggestion.  # noqa: E501
        :type data: dict(str, AttributeValue)
        """

        self._data = data

    @property
    def group(self):
        """Gets the group of this LeafSuggestion.  # noqa: E501

        Group of the suggestion.  # noqa: E501

        :return: The group of this LeafSuggestion.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this LeafSuggestion.

        Group of the suggestion.  # noqa: E501

        :param group: The group of this LeafSuggestion.  # noqa: E501
        :type group: str
        """

        self._group = group

    @property
    def value(self):
        """Gets the value of this LeafSuggestion.  # noqa: E501

        Name of the suggestion.  # noqa: E501

        :return: The value of this LeafSuggestion.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this LeafSuggestion.

        Name of the suggestion.  # noqa: E501

        :param value: The value of this LeafSuggestion.  # noqa: E501
        :type value: str
        """

        self._value = value

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
        if not isinstance(other, LeafSuggestion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LeafSuggestion):
            return True

        return self.to_dict() != other.to_dict()
