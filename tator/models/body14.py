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


class Body14(object):
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
        'user': 'int',
        'permission': 'str'
    }

    attribute_map = {
        'user': 'user',
        'permission': 'permission'
    }

    def __init__(self, user=None, permission=None):  # noqa: E501
        """Body14 - a model defined in Swagger"""  # noqa: E501
        self._user = None
        self._permission = None
        self.discriminator = None
        if user is not None:
            self.user = user
        if permission is not None:
            self.permission = permission

    @property
    def user(self):
        """Gets the user of this Body14.  # noqa: E501

        Unique integer identifying a user.  # noqa: E501

        :return: The user of this Body14.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Body14.

        Unique integer identifying a user.  # noqa: E501

        :param user: The user of this Body14.  # noqa: E501
        :type: int
        """

        self._user = user

    @property
    def permission(self):
        """Gets the permission of this Body14.  # noqa: E501

        User permission level for the project.  # noqa: E501

        :return: The permission of this Body14.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this Body14.

        User permission level for the project.  # noqa: E501

        :param permission: The permission of this Body14.  # noqa: E501
        :type: str
        """
        allowed_values = ["View Only", "Can Edit", "Can Transfer", "Can Execute", "Full Control"]  # noqa: E501
        if permission not in allowed_values:
            raise ValueError(
                "Invalid value for `permission` ({0}), must be one of {1}"  # noqa: E501
                .format(permission, allowed_values)
            )

        self._permission = permission

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
        if issubclass(Body14, dict):
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
        if not isinstance(other, Body14):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
