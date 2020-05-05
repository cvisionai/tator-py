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


class ProjectApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_project(self, **kwargs):  # noqa: E501
        """create_project  # noqa: E501

        Interact with a list of projects.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Project lists return all projects that the requesting user has access to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body16 body:
        :return: InlineResponse2014
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_project_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_project_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_project_with_http_info(self, **kwargs):  # noqa: E501
        """create_project  # noqa: E501

        Interact with a list of projects.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Project lists return all projects that the requesting user has access to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body16 body:
        :return: InlineResponse2014
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_project" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/rest/Projects', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_project(self, id, **kwargs):  # noqa: E501
        """delete_project  # noqa: E501

        Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer identifying a project. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_project_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_project_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_project_with_http_info(self, id, **kwargs):  # noqa: E501
        """delete_project  # noqa: E501

        Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer identifying a project. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/rest/Project/{id}', 'DELETE',
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

    def get_project(self, id, **kwargs):  # noqa: E501
        """get_project  # noqa: E501

        Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer identifying a project. (required)
        :return: InlineResponse20021
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_project_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_project_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_project_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_project  # noqa: E501

        Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer identifying a project. (required)
        :return: InlineResponse20021
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/rest/Project/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20021',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project_list(self, **kwargs):  # noqa: E501
        """get_project_list  # noqa: E501

        Interact with a list of projects.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Project lists return all projects that the requesting user has access to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[InlineResponse20021]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_project_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_project_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_project_list_with_http_info(self, **kwargs):  # noqa: E501
        """get_project_list  # noqa: E501

        Interact with a list of projects.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Project lists return all projects that the requesting user has access to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[InlineResponse20021]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/rest/Projects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20021]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_project(self, id, **kwargs):  # noqa: E501
        """update_project  # noqa: E501

        Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_project(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer identifying a project. (required)
        :param Body17 body:
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_project_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_project_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_project_with_http_info(self, id, **kwargs):  # noqa: E501
        """update_project  # noqa: E501

        Interact with an individual project.  Projects are the object under which all data in Tator is grouped, including user access, metadata definitions, media, and annotations. Data does not cross boundaries between projects.  Only the project owner may patch or delete an individual project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_project_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer identifying a project. (required)
        :param Body17 body:
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/rest/Project/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20022',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
