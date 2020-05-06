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


class LineElement(object):
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
        'email': 'str',
        'frame': 'int',
        'height': 'float',
        'id': 'int',
        'media': 'int',
        'meta': 'int',
        'modified': 'bool',
        'project': 'int',
        'thumbnail_image': 'str',
        'version': 'int',
        'width': 'float',
        'x': 'float',
        'y': 'float'
    }

    attribute_map = {
        'attributes': 'attributes',
        'email': 'email',
        'frame': 'frame',
        'height': 'height',
        'id': 'id',
        'media': 'media',
        'meta': 'meta',
        'modified': 'modified',
        'project': 'project',
        'thumbnail_image': 'thumbnail_image',
        'version': 'version',
        'width': 'width',
        'x': 'x',
        'y': 'y'
    }

    def __init__(self, attributes=None, email=None, frame=None, height=None, id=None, media=None, meta=None, modified=None, project=None, thumbnail_image=None, version=None, width=None, x=None, y=None, local_vars_configuration=None):  # noqa: E501
        """LineElement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attributes = None
        self._email = None
        self._frame = None
        self._height = None
        self._id = None
        self._media = None
        self._meta = None
        self._modified = None
        self._project = None
        self._thumbnail_image = None
        self._version = None
        self._width = None
        self._x = None
        self._y = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if email is not None:
            self.email = email
        if frame is not None:
            self.frame = frame
        if height is not None:
            self.height = height
        if id is not None:
            self.id = id
        if media is not None:
            self.media = media
        if meta is not None:
            self.meta = meta
        if modified is not None:
            self.modified = modified
        if project is not None:
            self.project = project
        if thumbnail_image is not None:
            self.thumbnail_image = thumbnail_image
        if version is not None:
            self.version = version
        if width is not None:
            self.width = width
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    @property
    def attributes(self):
        """Gets the attributes of this LineElement.  # noqa: E501

        Object containing attribute values.  # noqa: E501

        :return: The attributes of this LineElement.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this LineElement.

        Object containing attribute values.  # noqa: E501

        :param attributes: The attributes of this LineElement.  # noqa: E501
        :type: dict(str, object)
        """

        self._attributes = attributes

    @property
    def email(self):
        """Gets the email of this LineElement.  # noqa: E501

        Email of last user who modified/created this localization.  # noqa: E501

        :return: The email of this LineElement.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this LineElement.

        Email of last user who modified/created this localization.  # noqa: E501

        :param email: The email of this LineElement.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def frame(self):
        """Gets the frame of this LineElement.  # noqa: E501

        Frame number of this localization if it is in a video.  # noqa: E501

        :return: The frame of this LineElement.  # noqa: E501
        :rtype: int
        """
        return self._frame

    @frame.setter
    def frame(self, frame):
        """Sets the frame of this LineElement.

        Frame number of this localization if it is in a video.  # noqa: E501

        :param frame: The frame of this LineElement.  # noqa: E501
        :type: int
        """

        self._frame = frame

    @property
    def height(self):
        """Gets the height of this LineElement.  # noqa: E501

        Normalized height of bounding box for `box` localization types.  # noqa: E501

        :return: The height of this LineElement.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this LineElement.

        Normalized height of bounding box for `box` localization types.  # noqa: E501

        :param height: The height of this LineElement.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                height is not None and height > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `height`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                height is not None and height < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `height`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._height = height

    @property
    def id(self):
        """Gets the id of this LineElement.  # noqa: E501

        Unique integer identifying this localization.  # noqa: E501

        :return: The id of this LineElement.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LineElement.

        Unique integer identifying this localization.  # noqa: E501

        :param id: The id of this LineElement.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def media(self):
        """Gets the media of this LineElement.  # noqa: E501

        Unique integer identifying media of this localization.  # noqa: E501

        :return: The media of this LineElement.  # noqa: E501
        :rtype: int
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this LineElement.

        Unique integer identifying media of this localization.  # noqa: E501

        :param media: The media of this LineElement.  # noqa: E501
        :type: int
        """

        self._media = media

    @property
    def meta(self):
        """Gets the meta of this LineElement.  # noqa: E501

        Unique integer identifying entity type of this localization.  # noqa: E501

        :return: The meta of this LineElement.  # noqa: E501
        :rtype: int
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this LineElement.

        Unique integer identifying entity type of this localization.  # noqa: E501

        :param meta: The meta of this LineElement.  # noqa: E501
        :type: int
        """

        self._meta = meta

    @property
    def modified(self):
        """Gets the modified of this LineElement.  # noqa: E501

        Indicates whether this localization has been modified in the web UI.  # noqa: E501

        :return: The modified of this LineElement.  # noqa: E501
        :rtype: bool
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this LineElement.

        Indicates whether this localization has been modified in the web UI.  # noqa: E501

        :param modified: The modified of this LineElement.  # noqa: E501
        :type: bool
        """

        self._modified = modified

    @property
    def project(self):
        """Gets the project of this LineElement.  # noqa: E501

        Unique integer identifying project of this localization.  # noqa: E501

        :return: The project of this LineElement.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this LineElement.

        Unique integer identifying project of this localization.  # noqa: E501

        :param project: The project of this LineElement.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def thumbnail_image(self):
        """Gets the thumbnail_image of this LineElement.  # noqa: E501

        URL of thumbnail corresponding to this localization.  # noqa: E501

        :return: The thumbnail_image of this LineElement.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_image

    @thumbnail_image.setter
    def thumbnail_image(self, thumbnail_image):
        """Sets the thumbnail_image of this LineElement.

        URL of thumbnail corresponding to this localization.  # noqa: E501

        :param thumbnail_image: The thumbnail_image of this LineElement.  # noqa: E501
        :type: str
        """

        self._thumbnail_image = thumbnail_image

    @property
    def version(self):
        """Gets the version of this LineElement.  # noqa: E501

        Unique integer identifying a version.  # noqa: E501

        :return: The version of this LineElement.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LineElement.

        Unique integer identifying a version.  # noqa: E501

        :param version: The version of this LineElement.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def width(self):
        """Gets the width of this LineElement.  # noqa: E501

        Normalized width of bounding box for `box` localization types.  # noqa: E501

        :return: The width of this LineElement.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this LineElement.

        Normalized width of bounding box for `box` localization types.  # noqa: E501

        :param width: The width of this LineElement.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                width is not None and width > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `width`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                width is not None and width < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `width`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._width = width

    @property
    def x(self):
        """Gets the x of this LineElement.  # noqa: E501

        Normalized horizontal position of left edge of bounding box.  # noqa: E501

        :return: The x of this LineElement.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this LineElement.

        Normalized horizontal position of left edge of bounding box.  # noqa: E501

        :param x: The x of this LineElement.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                x is not None and x > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `x`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                x is not None and x < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `x`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._x = x

    @property
    def y(self):
        """Gets the y of this LineElement.  # noqa: E501

        Normalized vertical position of top edge of bounding box.  # noqa: E501

        :return: The y of this LineElement.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this LineElement.

        Normalized vertical position of top edge of bounding box.  # noqa: E501

        :param y: The y of this LineElement.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                y is not None and y > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `y`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                y is not None and y < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `y`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._y = y

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
        if not isinstance(other, LineElement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LineElement):
            return True

        return self.to_dict() != other.to_dict()
