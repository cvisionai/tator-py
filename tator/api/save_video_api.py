# coding: utf-8

"""
    Tator REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tator.api_client import ApiClient


class SaveVideoApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def partial_update_save_video_api(self, project, **kwargs):  # noqa: E501
        """partial_update_save_video_api  # noqa: E501

        Saves a transcoded video.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. To launch a transcode on raw uploaded video, use the  `Transcode` endpoint, which will create an Argo workflow to perform the transcode and save the video using this endpoint; no further REST calls are required. However, if you would like to perform transcodes locally, this endpoint enables that. The script at `scripts/transcoder/transcodePipeline.py` in the Tator source code provides an example of how to transcode a Tator-compatible video, upload it, and save it to the database using this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_save_video_api(project, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project: A unique integer identifying a project. (required)
        :param Body40 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.partial_update_save_video_api_with_http_info(project, **kwargs)  # noqa: E501
        else:
            (data) = self.partial_update_save_video_api_with_http_info(project, **kwargs)  # noqa: E501
            return data

    def partial_update_save_video_api_with_http_info(self, project, **kwargs):  # noqa: E501
        """partial_update_save_video_api  # noqa: E501

        Saves a transcoded video.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. To launch a transcode on raw uploaded video, use the  `Transcode` endpoint, which will create an Argo workflow to perform the transcode and save the video using this endpoint; no further REST calls are required. However, if you would like to perform transcodes locally, this endpoint enables that. The script at `scripts/transcoder/transcodePipeline.py` in the Tator source code provides an example of how to transcode a Tator-compatible video, upload it, and save it to the database using this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_save_video_api_with_http_info(project, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project: A unique integer identifying a project. (required)
        :param Body40 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method partial_update_save_video_api" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project' is set
        if ('project' not in params or
                params['project'] is None):
            raise ValueError("Missing the required parameter `project` when calling `partial_update_save_video_api`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project' in params:
            path_params['project'] = params['project']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/rest/SaveVideo/{project}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_video(self, project, **kwargs):  # noqa: E501
        """save_video  # noqa: E501

        Saves a transcoded video.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. To launch a transcode on raw uploaded video, use the  `Transcode` endpoint, which will create an Argo workflow to perform the transcode and save the video using this endpoint; no further REST calls are required. However, if you would like to perform transcodes locally, this endpoint enables that. The script at `scripts/transcoder/transcodePipeline.py` in the Tator source code provides an example of how to transcode a Tator-compatible video, upload it, and save it to the database using this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_video(project, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project: A unique integer identifying a project. (required)
        :param Body39 body:
        :return: InlineResponse20112
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_video_with_http_info(project, **kwargs)  # noqa: E501
        else:
            (data) = self.save_video_with_http_info(project, **kwargs)  # noqa: E501
            return data

    def save_video_with_http_info(self, project, **kwargs):  # noqa: E501
        """save_video  # noqa: E501

        Saves a transcoded video.  Videos in Tator must be transcoded to a multi-resolution streaming format before they can be viewed or annotated. To launch a transcode on raw uploaded video, use the  `Transcode` endpoint, which will create an Argo workflow to perform the transcode and save the video using this endpoint; no further REST calls are required. However, if you would like to perform transcodes locally, this endpoint enables that. The script at `scripts/transcoder/transcodePipeline.py` in the Tator source code provides an example of how to transcode a Tator-compatible video, upload it, and save it to the database using this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_video_with_http_info(project, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project: A unique integer identifying a project. (required)
        :param Body39 body:
        :return: InlineResponse20112
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_video" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project' is set
        if ('project' not in params or
                params['project'] is None):
            raise ValueError("Missing the required parameter `project` when calling `save_video`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project' in params:
            path_params['project'] = params['project']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/rest/SaveVideo/{project}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20112',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
