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


class MediaSpec(object):
    """
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'gid': 'str',
        'md5': 'str',
        'name': 'str',
        'section': 'str',
        'thumbnail_url': 'str',
        'type': 'int',
        'uid': 'str',
        'url': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'md5': 'md5',
        'name': 'name',
        'section': 'section',
        'thumbnail_url': 'thumbnail_url',
        'type': 'type',
        'uid': 'uid',
        'url': 'url'
    }

    def __init__(self, gid=None, md5=None, name=None, section=None, thumbnail_url=None, type=None, uid=None, url=None, local_vars_configuration=None):  # noqa: E501
        """MediaSpec - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gid = None
        self._md5 = None
        self._name = None
        self._section = None
        self._thumbnail_url = None
        self._type = None
        self._uid = None
        self._url = None
        self.discriminator = None

        if gid is not None:
            self.gid = gid
        self.md5 = md5
        self.name = name
        self.section = section
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        self.type = type
        if uid is not None:
            self.uid = uid
        if url is not None:
            self.url = url

    @property
    def gid(self):
        """
        UUID corresponding to a group of uploads if this is an image type.

        :return: The gid of this MediaSpec. 
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """
        UUID corresponding to a group of uploads if this is an image type.

        :param gid: The gid of this MediaSpec.
        :type: str
        """

        self._gid = gid

    @property
    def md5(self):
        """
        MD5 sum of the media file.

        :return: The md5 of this MediaSpec. 
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """
        MD5 sum of the media file.

        :param md5: The md5 of this MediaSpec.
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and md5 is None:  # noqa: E501
            raise ValueError("Invalid value for `md5`, must not be `None`")  # noqa: E501

        self._md5 = md5

    @property
    def name(self):
        """
        Name of the file.

        :return: The name of this MediaSpec. 
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Name of the file.

        :param name: The name of this MediaSpec.
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def section(self):
        """
        Media section name.

        :return: The section of this MediaSpec. 
        :rtype: str
        """
        return self._section

    @section.setter
    def section(self, section):
        """
        Media section name.

        :param section: The section of this MediaSpec.
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and section is None:  # noqa: E501
            raise ValueError("Invalid value for `section`, must not be `None`")  # noqa: E501

        self._section = section

    @property
    def thumbnail_url(self):
        """
        Upload URL for the image thumbnail if already generated. If not an image, this field is ignored.

        :return: The thumbnail_url of this MediaSpec. 
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """
        Upload URL for the image thumbnail if already generated. If not an image, this field is ignored.

        :param thumbnail_url: The thumbnail_url of this MediaSpec.
        :type: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def type(self):
        """
        Unique integer identifying a media type. Use -1 to automatically select the media type if only one media type exists in a project.

        :return: The type of this MediaSpec. 
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Unique integer identifying a media type. Use -1 to automatically select the media type if only one media type exists in a project.

        :param type: The type of this MediaSpec.
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and type < -1):  # noqa: E501
            raise ValueError("Invalid value for `type`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._type = type

    @property
    def uid(self):
        """
        UUID corresponding to an upload if this is an image type.

        :return: The uid of this MediaSpec. 
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        UUID corresponding to an upload if this is an image type.

        :param uid: The uid of this MediaSpec.
        :type: str
        """

        self._uid = uid

    @property
    def url(self):
        """
        Upload URL for the image if this is an image type. If not an image, this field is ignored.

        :return: The url of this MediaSpec. 
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Upload URL for the image if this is an image type. If not an image, this field is ignored.

        :param url: The url of this MediaSpec.
        :type: str
        """

        self._url = url

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
        if not isinstance(other, MediaSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MediaSpec):
            return True

        return self.to_dict() != other.to_dict()
