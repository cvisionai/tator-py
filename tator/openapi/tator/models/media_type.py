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


class MediaType(object):
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
        'attribute_types': 'list[AttributeType]',
        'default_volume': 'int',
        'description': 'str',
        'dtype': 'str',
        'file_format': 'str',
        'id': 'int',
        'keep_original': 'bool',
        'name': 'str',
        'project': 'int'
    }

    attribute_map = {
        'attribute_types': 'attribute_types',
        'default_volume': 'default_volume',
        'description': 'description',
        'dtype': 'dtype',
        'file_format': 'file_format',
        'id': 'id',
        'keep_original': 'keep_original',
        'name': 'name',
        'project': 'project'
    }

    def __init__(self, attribute_types=None, default_volume=None, description='', dtype=None, file_format=None, id=None, keep_original=True, name=None, project=None, local_vars_configuration=None):  # noqa: E501
        """MediaType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attribute_types = None
        self._default_volume = None
        self._description = None
        self._dtype = None
        self._file_format = None
        self._id = None
        self._keep_original = None
        self._name = None
        self._project = None
        self.discriminator = None

        if attribute_types is not None:
            self.attribute_types = attribute_types
        if default_volume is not None:
            self.default_volume = default_volume
        if description is not None:
            self.description = description
        if dtype is not None:
            self.dtype = dtype
        if file_format is not None:
            self.file_format = file_format
        if id is not None:
            self.id = id
        if keep_original is not None:
            self.keep_original = keep_original
        if name is not None:
            self.name = name
        if project is not None:
            self.project = project

    @property
    def attribute_types(self):
        """Gets the attribute_types of this MediaType.  # noqa: E501

        Attribute type definitions.  # noqa: E501

        :return: The attribute_types of this MediaType.  # noqa: E501
        :rtype: list[AttributeType]
        """
        return self._attribute_types

    @attribute_types.setter
    def attribute_types(self, attribute_types):
        """Sets the attribute_types of this MediaType.

        Attribute type definitions.  # noqa: E501

        :param attribute_types: The attribute_types of this MediaType.  # noqa: E501
        :type attribute_types: list[AttributeType]
        """

        self._attribute_types = attribute_types

    @property
    def default_volume(self):
        """Gets the default_volume of this MediaType.  # noqa: E501

        Default audio volume for this media type.  # noqa: E501

        :return: The default_volume of this MediaType.  # noqa: E501
        :rtype: int
        """
        return self._default_volume

    @default_volume.setter
    def default_volume(self, default_volume):
        """Sets the default_volume of this MediaType.

        Default audio volume for this media type.  # noqa: E501

        :param default_volume: The default_volume of this MediaType.  # noqa: E501
        :type default_volume: int
        """
        if (self.local_vars_configuration.client_side_validation and
                default_volume is not None and default_volume > 100):  # noqa: E501
            raise ValueError("Invalid value for `default_volume`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                default_volume is not None and default_volume < 0):  # noqa: E501
            raise ValueError("Invalid value for `default_volume`, must be a value greater than or equal to `0`")  # noqa: E501

        self._default_volume = default_volume

    @property
    def description(self):
        """Gets the description of this MediaType.  # noqa: E501

        Description of the media type.  # noqa: E501

        :return: The description of this MediaType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MediaType.

        Description of the media type.  # noqa: E501

        :param description: The description of this MediaType.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def dtype(self):
        """Gets the dtype of this MediaType.  # noqa: E501

        Type of the media, image or video.  # noqa: E501

        :return: The dtype of this MediaType.  # noqa: E501
        :rtype: str
        """
        return self._dtype

    @dtype.setter
    def dtype(self, dtype):
        """Sets the dtype of this MediaType.

        Type of the media, image or video.  # noqa: E501

        :param dtype: The dtype of this MediaType.  # noqa: E501
        :type dtype: str
        """
        allowed_values = ["image", "video"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and dtype not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `dtype` ({0}), must be one of {1}"  # noqa: E501
                .format(dtype, allowed_values)
            )

        self._dtype = dtype

    @property
    def file_format(self):
        """Gets the file_format of this MediaType.  # noqa: E501

        File extension. If omitted, any recognized file extension for the given dtype is accepted for upload. Do not include a dot prefix.  # noqa: E501

        :return: The file_format of this MediaType.  # noqa: E501
        :rtype: str
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """Sets the file_format of this MediaType.

        File extension. If omitted, any recognized file extension for the given dtype is accepted for upload. Do not include a dot prefix.  # noqa: E501

        :param file_format: The file_format of this MediaType.  # noqa: E501
        :type file_format: str
        """
        if (self.local_vars_configuration.client_side_validation and
                file_format is not None and len(file_format) > 4):
            raise ValueError("Invalid value for `file_format`, length must be less than or equal to `4`")  # noqa: E501

        self._file_format = file_format

    @property
    def id(self):
        """Gets the id of this MediaType.  # noqa: E501

        Unique integer identifying a media type.  # noqa: E501

        :return: The id of this MediaType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MediaType.

        Unique integer identifying a media type.  # noqa: E501

        :param id: The id of this MediaType.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def keep_original(self):
        """Gets the keep_original of this MediaType.  # noqa: E501

        For video dtype, whether to keep the original video file for archival purposes after transcoding. If true, the originally uploaded file will be available for download, otherwise downloads will use the transcoded videos.  # noqa: E501

        :return: The keep_original of this MediaType.  # noqa: E501
        :rtype: bool
        """
        return self._keep_original

    @keep_original.setter
    def keep_original(self, keep_original):
        """Sets the keep_original of this MediaType.

        For video dtype, whether to keep the original video file for archival purposes after transcoding. If true, the originally uploaded file will be available for download, otherwise downloads will use the transcoded videos.  # noqa: E501

        :param keep_original: The keep_original of this MediaType.  # noqa: E501
        :type keep_original: bool
        """

        self._keep_original = keep_original

    @property
    def name(self):
        """Gets the name of this MediaType.  # noqa: E501

        Name of the media type.  # noqa: E501

        :return: The name of this MediaType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MediaType.

        Name of the media type.  # noqa: E501

        :param name: The name of this MediaType.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def project(self):
        """Gets the project of this MediaType.  # noqa: E501

        Unique integer identifying project for this media type.  # noqa: E501

        :return: The project of this MediaType.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this MediaType.

        Unique integer identifying project for this media type.  # noqa: E501

        :param project: The project of this MediaType.  # noqa: E501
        :type project: int
        """

        self._project = project

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
        if not isinstance(other, MediaType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MediaType):
            return True

        return self.to_dict() != other.to_dict()
