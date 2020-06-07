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

from tator.configuration import Configuration


class StateUpdate(object):
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
        'attributes': 'dict(str, object)',
        'frame': 'int',
        'modified': 'bool'
    }

    attribute_map = {
        'attributes': 'attributes',
        'frame': 'frame',
        'modified': 'modified'
    }

    def __init__(self, attributes=None, frame=None, modified=None, local_vars_configuration=None):  # noqa: E501
        """StateUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attributes = None
        self._frame = None
        self._modified = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if frame is not None:
            self.frame = frame
        self.modified = modified

    @property
    def attributes(self):
        """Gets the attributes of this StateUpdate.  # noqa: E501

        Object containing attribute values.  # noqa: E501

        :return: The attributes of this StateUpdate.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this StateUpdate.

        Object containing attribute values.  # noqa: E501

        :param attributes: The attributes of this StateUpdate.  # noqa: E501
        :type: dict(str, object)
        """

        self._attributes = attributes

    @property
    def frame(self):
        """Gets the frame of this StateUpdate.  # noqa: E501

        Frame number this state applies to.  # noqa: E501

        :return: The frame of this StateUpdate.  # noqa: E501
        :rtype: int
        """
        return self._frame

    @frame.setter
    def frame(self, frame):
        """Sets the frame of this StateUpdate.

        Frame number this state applies to.  # noqa: E501

        :param frame: The frame of this StateUpdate.  # noqa: E501
        :type: int
        """

        self._frame = frame

    @property
    def modified(self):
        """Gets the modified of this StateUpdate.  # noqa: E501

        Whether this state was created in the web UI.  # noqa: E501

        :return: The modified of this StateUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this StateUpdate.

        Whether this state was created in the web UI.  # noqa: E501

        :param modified: The modified of this StateUpdate.  # noqa: E501
        :type: bool
        """

        self._modified = modified

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
        if not isinstance(other, StateUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StateUpdate):
            return True

        return self.to_dict() != other.to_dict()
