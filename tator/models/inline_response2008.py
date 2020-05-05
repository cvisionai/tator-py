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


class InlineResponse2008(object):
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
        'type': 'RestLocalizationTypesprojectType',
        'columns': 'list[OneOfinlineResponse2008ColumnsItems]'
    }

    attribute_map = {
        'type': 'type',
        'columns': 'columns'
    }

    def __init__(self, type=None, columns=None):  # noqa: E501
        """InlineResponse2008 - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._columns = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if columns is not None:
            self.columns = columns

    @property
    def type(self):
        """Gets the type of this InlineResponse2008.  # noqa: E501


        :return: The type of this InlineResponse2008.  # noqa: E501
        :rtype: RestLocalizationTypesprojectType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2008.


        :param type: The type of this InlineResponse2008.  # noqa: E501
        :type: RestLocalizationTypesprojectType
        """

        self._type = type

    @property
    def columns(self):
        """Gets the columns of this InlineResponse2008.  # noqa: E501

        Attribute types associated with this localization type.  # noqa: E501

        :return: The columns of this InlineResponse2008.  # noqa: E501
        :rtype: list[OneOfinlineResponse2008ColumnsItems]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this InlineResponse2008.

        Attribute types associated with this localization type.  # noqa: E501

        :param columns: The columns of this InlineResponse2008.  # noqa: E501
        :type: list[OneOfinlineResponse2008ColumnsItems]
        """

        self._columns = columns

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
        if issubclass(InlineResponse2008, dict):
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
        if not isinstance(other, InlineResponse2008):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
