# coding: utf-8

"""
    Tator REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Body1(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'dtype': 'str',
        'media_types': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'dtype': 'dtype',
        'media_types': 'media_types'
    }

    def __init__(self, name=None, description='', dtype=None, media_types=None):  # noqa: E501
        """Body1 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._dtype = None
        self._media_types = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        self.dtype = dtype
        self.media_types = media_types

    @property
    def name(self):
        """Gets the name of this Body1.  # noqa: E501

        Name of the localization type.  # noqa: E501

        :return: The name of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body1.

        Name of the localization type.  # noqa: E501

        :param name: The name of this Body1.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Body1.  # noqa: E501

        Description of the localization type.  # noqa: E501

        :return: The description of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Body1.

        Description of the localization type.  # noqa: E501

        :param description: The description of this Body1.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dtype(self):
        """Gets the dtype of this Body1.  # noqa: E501

        Shape of the localization.  # noqa: E501

        :return: The dtype of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._dtype

    @dtype.setter
    def dtype(self, dtype):
        """Sets the dtype of this Body1.

        Shape of the localization.  # noqa: E501

        :param dtype: The dtype of this Body1.  # noqa: E501
        :type: str
        """
        if dtype is None:
            raise ValueError("Invalid value for `dtype`, must not be `None`")  # noqa: E501
        allowed_values = ["box", "line", "dot"]  # noqa: E501
        if dtype not in allowed_values:
            raise ValueError(
                "Invalid value for `dtype` ({0}), must be one of {1}"  # noqa: E501
                .format(dtype, allowed_values)
            )

        self._dtype = dtype

    @property
    def media_types(self):
        """Gets the media_types of this Body1.  # noqa: E501

        List of integers identifying media types that this localization type may apply to.  # noqa: E501

        :return: The media_types of this Body1.  # noqa: E501
        :rtype: list[int]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """Sets the media_types of this Body1.

        List of integers identifying media types that this localization type may apply to.  # noqa: E501

        :param media_types: The media_types of this Body1.  # noqa: E501
        :type: list[int]
        """
        if media_types is None:
            raise ValueError("Invalid value for `media_types`, must not be `None`")  # noqa: E501

        self._media_types = media_types

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Body1, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Body1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
