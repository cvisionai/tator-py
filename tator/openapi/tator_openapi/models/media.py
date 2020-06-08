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


class Media(object):
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
        'codec': 'str',
        'created_by': 'int',
        'created_datetime': 'str',
        'file': 'str',
        'fps': 'int',
        'height': 'int',
        'id': 'int',
        'last_edit_end': 'datetime',
        'last_edit_start': 'datetime',
        'md5': 'str',
        'media_files': 'list[str]',
        'meta': 'int',
        'modified_by': 'int',
        'modified_datetime': 'str',
        'name': 'str',
        'num_frames': 'int',
        'original': 'str',
        'project': 'int',
        'segment_info': 'str',
        'thumbnail': 'str',
        'thumbnail_gif': 'str',
        'width': 'int'
    }

    attribute_map = {
        'attributes': 'attributes',
        'codec': 'codec',
        'created_by': 'created_by',
        'created_datetime': 'created_datetime',
        'file': 'file',
        'fps': 'fps',
        'height': 'height',
        'id': 'id',
        'last_edit_end': 'last_edit_end',
        'last_edit_start': 'last_edit_start',
        'md5': 'md5',
        'media_files': 'media_files',
        'meta': 'meta',
        'modified_by': 'modified_by',
        'modified_datetime': 'modified_datetime',
        'name': 'name',
        'num_frames': 'num_frames',
        'original': 'original',
        'project': 'project',
        'segment_info': 'segment_info',
        'thumbnail': 'thumbnail',
        'thumbnail_gif': 'thumbnail_gif',
        'width': 'width'
    }

    def __init__(self, attributes=None, codec=None, created_by=None, created_datetime=None, file=None, fps=None, height=None, id=None, last_edit_end=None, last_edit_start=None, md5=None, media_files=None, meta=None, modified_by=None, modified_datetime=None, name=None, num_frames=None, original=None, project=None, segment_info=None, thumbnail=None, thumbnail_gif=None, width=None, local_vars_configuration=None):  # noqa: E501
        """Media - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attributes = None
        self._codec = None
        self._created_by = None
        self._created_datetime = None
        self._file = None
        self._fps = None
        self._height = None
        self._id = None
        self._last_edit_end = None
        self._last_edit_start = None
        self._md5 = None
        self._media_files = None
        self._meta = None
        self._modified_by = None
        self._modified_datetime = None
        self._name = None
        self._num_frames = None
        self._original = None
        self._project = None
        self._segment_info = None
        self._thumbnail = None
        self._thumbnail_gif = None
        self._width = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if codec is not None:
            self.codec = codec
        if created_by is not None:
            self.created_by = created_by
        if created_datetime is not None:
            self.created_datetime = created_datetime
        if file is not None:
            self.file = file
        if fps is not None:
            self.fps = fps
        if height is not None:
            self.height = height
        if id is not None:
            self.id = id
        if last_edit_end is not None:
            self.last_edit_end = last_edit_end
        if last_edit_start is not None:
            self.last_edit_start = last_edit_start
        if md5 is not None:
            self.md5 = md5
        if media_files is not None:
            self.media_files = media_files
        if meta is not None:
            self.meta = meta
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_datetime is not None:
            self.modified_datetime = modified_datetime
        if name is not None:
            self.name = name
        if num_frames is not None:
            self.num_frames = num_frames
        if original is not None:
            self.original = original
        if project is not None:
            self.project = project
        if segment_info is not None:
            self.segment_info = segment_info
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if thumbnail_gif is not None:
            self.thumbnail_gif = thumbnail_gif
        if width is not None:
            self.width = width

    @property
    def attributes(self):
        """Gets the attributes of this Media.  # noqa: E501

        Object containing attribute values.  # noqa: E501

        :return: The attributes of this Media.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Media.

        Object containing attribute values.  # noqa: E501

        :param attributes: The attributes of this Media.  # noqa: E501
        :type attributes: dict(str, object)
        """

        self._attributes = attributes

    @property
    def codec(self):
        """Gets the codec of this Media.  # noqa: E501

        Codec for videos.  # noqa: E501

        :return: The codec of this Media.  # noqa: E501
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this Media.

        Codec for videos.  # noqa: E501

        :param codec: The codec of this Media.  # noqa: E501
        :type codec: str
        """

        self._codec = codec

    @property
    def created_by(self):
        """Gets the created_by of this Media.  # noqa: E501

        Unique integer identifying user who created this media.  # noqa: E501

        :return: The created_by of this Media.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Media.

        Unique integer identifying user who created this media.  # noqa: E501

        :param created_by: The created_by of this Media.  # noqa: E501
        :type created_by: int
        """

        self._created_by = created_by

    @property
    def created_datetime(self):
        """Gets the created_datetime of this Media.  # noqa: E501

        Datetime when this media was created.  # noqa: E501

        :return: The created_datetime of this Media.  # noqa: E501
        :rtype: str
        """
        return self._created_datetime

    @created_datetime.setter
    def created_datetime(self, created_datetime):
        """Sets the created_datetime of this Media.

        Datetime when this media was created.  # noqa: E501

        :param created_datetime: The created_datetime of this Media.  # noqa: E501
        :type created_datetime: str
        """

        self._created_datetime = created_datetime

    @property
    def file(self):
        """Gets the file of this Media.  # noqa: E501

        URL of the media file. Relative to https://<domain>/media/.  # noqa: E501

        :return: The file of this Media.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Media.

        URL of the media file. Relative to https://<domain>/media/.  # noqa: E501

        :param file: The file of this Media.  # noqa: E501
        :type file: str
        """

        self._file = file

    @property
    def fps(self):
        """Gets the fps of this Media.  # noqa: E501

        Frame rate for videos.  # noqa: E501

        :return: The fps of this Media.  # noqa: E501
        :rtype: int
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        """Sets the fps of this Media.

        Frame rate for videos.  # noqa: E501

        :param fps: The fps of this Media.  # noqa: E501
        :type fps: int
        """

        self._fps = fps

    @property
    def height(self):
        """Gets the height of this Media.  # noqa: E501

        Vertical resolution in pixels.  # noqa: E501

        :return: The height of this Media.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Media.

        Vertical resolution in pixels.  # noqa: E501

        :param height: The height of this Media.  # noqa: E501
        :type height: int
        """

        self._height = height

    @property
    def id(self):
        """Gets the id of this Media.  # noqa: E501

        Unique integer identifying this media.  # noqa: E501

        :return: The id of this Media.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Media.

        Unique integer identifying this media.  # noqa: E501

        :param id: The id of this Media.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def last_edit_end(self):
        """Gets the last_edit_end of this Media.  # noqa: E501

        Datetime of the end of the session when this media or its annotations were last edited.  # noqa: E501

        :return: The last_edit_end of this Media.  # noqa: E501
        :rtype: datetime
        """
        return self._last_edit_end

    @last_edit_end.setter
    def last_edit_end(self, last_edit_end):
        """Sets the last_edit_end of this Media.

        Datetime of the end of the session when this media or its annotations were last edited.  # noqa: E501

        :param last_edit_end: The last_edit_end of this Media.  # noqa: E501
        :type last_edit_end: datetime
        """

        self._last_edit_end = last_edit_end

    @property
    def last_edit_start(self):
        """Gets the last_edit_start of this Media.  # noqa: E501

        Datetime of the start of the session when this media or its annotations were last edited.  # noqa: E501

        :return: The last_edit_start of this Media.  # noqa: E501
        :rtype: datetime
        """
        return self._last_edit_start

    @last_edit_start.setter
    def last_edit_start(self, last_edit_start):
        """Sets the last_edit_start of this Media.

        Datetime of the start of the session when this media or its annotations were last edited.  # noqa: E501

        :param last_edit_start: The last_edit_start of this Media.  # noqa: E501
        :type last_edit_start: datetime
        """

        self._last_edit_start = last_edit_start

    @property
    def md5(self):
        """Gets the md5 of this Media.  # noqa: E501

        MD5 checksum of the media file.  # noqa: E501

        :return: The md5 of this Media.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this Media.

        MD5 checksum of the media file.  # noqa: E501

        :param md5: The md5 of this Media.  # noqa: E501
        :type md5: str
        """

        self._md5 = md5

    @property
    def media_files(self):
        """Gets the media_files of this Media.  # noqa: E501

        Object containing upload urls for the transcoded file and corresponding `VideoDefinition`.  # noqa: E501

        :return: The media_files of this Media.  # noqa: E501
        :rtype: list[str]
        """
        return self._media_files

    @media_files.setter
    def media_files(self, media_files):
        """Sets the media_files of this Media.

        Object containing upload urls for the transcoded file and corresponding `VideoDefinition`.  # noqa: E501

        :param media_files: The media_files of this Media.  # noqa: E501
        :type media_files: list[str]
        """

        self._media_files = media_files

    @property
    def meta(self):
        """Gets the meta of this Media.  # noqa: E501

        Unique integer identifying entity type of this media.  # noqa: E501

        :return: The meta of this Media.  # noqa: E501
        :rtype: int
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Media.

        Unique integer identifying entity type of this media.  # noqa: E501

        :param meta: The meta of this Media.  # noqa: E501
        :type meta: int
        """

        self._meta = meta

    @property
    def modified_by(self):
        """Gets the modified_by of this Media.  # noqa: E501

        Unique integer identifying user who last modified this media.  # noqa: E501

        :return: The modified_by of this Media.  # noqa: E501
        :rtype: int
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Media.

        Unique integer identifying user who last modified this media.  # noqa: E501

        :param modified_by: The modified_by of this Media.  # noqa: E501
        :type modified_by: int
        """

        self._modified_by = modified_by

    @property
    def modified_datetime(self):
        """Gets the modified_datetime of this Media.  # noqa: E501

        Datetime when this media was last modified.  # noqa: E501

        :return: The modified_datetime of this Media.  # noqa: E501
        :rtype: str
        """
        return self._modified_datetime

    @modified_datetime.setter
    def modified_datetime(self, modified_datetime):
        """Sets the modified_datetime of this Media.

        Datetime when this media was last modified.  # noqa: E501

        :param modified_datetime: The modified_datetime of this Media.  # noqa: E501
        :type modified_datetime: str
        """

        self._modified_datetime = modified_datetime

    @property
    def name(self):
        """Gets the name of this Media.  # noqa: E501

        Name of the media.  # noqa: E501

        :return: The name of this Media.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Media.

        Name of the media.  # noqa: E501

        :param name: The name of this Media.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def num_frames(self):
        """Gets the num_frames of this Media.  # noqa: E501

        Number of frames for videos.  # noqa: E501

        :return: The num_frames of this Media.  # noqa: E501
        :rtype: int
        """
        return self._num_frames

    @num_frames.setter
    def num_frames(self, num_frames):
        """Sets the num_frames of this Media.

        Number of frames for videos.  # noqa: E501

        :param num_frames: The num_frames of this Media.  # noqa: E501
        :type num_frames: int
        """

        self._num_frames = num_frames

    @property
    def original(self):
        """Gets the original of this Media.  # noqa: E501

        DEPRECATED. Use media_files. Stores path to original media file.  # noqa: E501

        :return: The original of this Media.  # noqa: E501
        :rtype: str
        """
        return self._original

    @original.setter
    def original(self, original):
        """Sets the original of this Media.

        DEPRECATED. Use media_files. Stores path to original media file.  # noqa: E501

        :param original: The original of this Media.  # noqa: E501
        :type original: str
        """

        self._original = original

    @property
    def project(self):
        """Gets the project of this Media.  # noqa: E501

        Unique integer identifying project of this media.  # noqa: E501

        :return: The project of this Media.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Media.

        Unique integer identifying project of this media.  # noqa: E501

        :param project: The project of this Media.  # noqa: E501
        :type project: int
        """

        self._project = project

    @property
    def segment_info(self):
        """Gets the segment_info of this Media.  # noqa: E501

        Path to segment info.  # noqa: E501

        :return: The segment_info of this Media.  # noqa: E501
        :rtype: str
        """
        return self._segment_info

    @segment_info.setter
    def segment_info(self, segment_info):
        """Sets the segment_info of this Media.

        Path to segment info.  # noqa: E501

        :param segment_info: The segment_info of this Media.  # noqa: E501
        :type segment_info: str
        """

        self._segment_info = segment_info

    @property
    def thumbnail(self):
        """Gets the thumbnail of this Media.  # noqa: E501

        URL of the thumbnail. Relative to https://<domain>/media/.  # noqa: E501

        :return: The thumbnail of this Media.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this Media.

        URL of the thumbnail. Relative to https://<domain>/media/.  # noqa: E501

        :param thumbnail: The thumbnail of this Media.  # noqa: E501
        :type thumbnail: str
        """

        self._thumbnail = thumbnail

    @property
    def thumbnail_gif(self):
        """Gets the thumbnail_gif of this Media.  # noqa: E501

        URL of the thumbnail gif for videos. Relative to https://<domain>/media/.  # noqa: E501

        :return: The thumbnail_gif of this Media.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_gif

    @thumbnail_gif.setter
    def thumbnail_gif(self, thumbnail_gif):
        """Sets the thumbnail_gif of this Media.

        URL of the thumbnail gif for videos. Relative to https://<domain>/media/.  # noqa: E501

        :param thumbnail_gif: The thumbnail_gif of this Media.  # noqa: E501
        :type thumbnail_gif: str
        """

        self._thumbnail_gif = thumbnail_gif

    @property
    def width(self):
        """Gets the width of this Media.  # noqa: E501

        Horizontal resolution in pixels.  # noqa: E501

        :return: The width of this Media.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Media.

        Horizontal resolution in pixels.  # noqa: E501

        :param width: The width of this Media.  # noqa: E501
        :type width: int
        """

        self._width = width

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
        if not isinstance(other, Media):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Media):
            return True

        return self.to_dict() != other.to_dict()
