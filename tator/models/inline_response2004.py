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


class InlineResponse2004(object):
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
        'num_images': 'int',
        'num_videos': 'int'
    }

    attribute_map = {
        'num_images': 'num_images',
        'num_videos': 'num_videos'
    }

    def __init__(self, num_images=None, num_videos=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2004 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._num_images = None
        self._num_videos = None
        self.discriminator = None

        if num_images is not None:
            self.num_images = num_images
        if num_videos is not None:
            self.num_videos = num_videos

    @property
    def num_images(self):
        """Gets the num_images of this InlineResponse2004.  # noqa: E501


        :return: The num_images of this InlineResponse2004.  # noqa: E501
        :rtype: int
        """
        return self._num_images

    @num_images.setter
    def num_images(self, num_images):
        """Sets the num_images of this InlineResponse2004.


        :param num_images: The num_images of this InlineResponse2004.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                num_images is not None and num_images < 0):  # noqa: E501
            raise ValueError("Invalid value for `num_images`, must be a value greater than or equal to `0`")  # noqa: E501

        self._num_images = num_images

    @property
    def num_videos(self):
        """Gets the num_videos of this InlineResponse2004.  # noqa: E501


        :return: The num_videos of this InlineResponse2004.  # noqa: E501
        :rtype: int
        """
        return self._num_videos

    @num_videos.setter
    def num_videos(self, num_videos):
        """Sets the num_videos of this InlineResponse2004.


        :param num_videos: The num_videos of this InlineResponse2004.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                num_videos is not None and num_videos < 0):  # noqa: E501
            raise ValueError("Invalid value for `num_videos`, must be a value greater than or equal to `0`")  # noqa: E501

        self._num_videos = num_videos

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
        if not isinstance(other, InlineResponse2004):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2004):
            return True

        return self.to_dict() != other.to_dict()
