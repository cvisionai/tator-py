# coding: utf-8

"""
    Tator REST API

    Interface to the Tator backend.  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import tator
from tator.api.tator_api import TatorApi  # noqa: E501
from tator.rest import ApiException


class TestTatorApi(unittest.TestCase):
    """TatorApi unit test stubs"""

    def setUp(self):
        self.api = tator.api.tator_api.TatorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_algorithm_launch(self):
        """Test case for algorithm_launch

        """
        pass

    def test_create_analysis(self):
        """Test case for create_analysis

        """
        pass

    def test_create_leaf(self):
        """Test case for create_leaf

        """
        pass

    def test_create_leaf_type(self):
        """Test case for create_leaf_type

        """
        pass

    def test_create_localization(self):
        """Test case for create_localization

        """
        pass

    def test_create_localization_type(self):
        """Test case for create_localization_type

        """
        pass

    def test_create_media_type(self):
        """Test case for create_media_type

        """
        pass

    def test_create_membership(self):
        """Test case for create_membership

        """
        pass

    def test_create_obtain_auth_token(self):
        """Test case for create_obtain_auth_token

        """
        pass

    def test_create_progress_summary_api(self):
        """Test case for create_progress_summary_api

        """
        pass

    def test_create_project(self):
        """Test case for create_project

        """
        pass

    def test_create_state(self):
        """Test case for create_state

        """
        pass

    def test_create_state_type(self):
        """Test case for create_state_type

        """
        pass

    def test_create_temporary_file(self):
        """Test case for create_temporary_file

        """
        pass

    def test_create_version(self):
        """Test case for create_version

        """
        pass

    def test_delete_job(self):
        """Test case for delete_job

        """
        pass

    def test_delete_job_group(self):
        """Test case for delete_job_group

        """
        pass

    def test_delete_leaf(self):
        """Test case for delete_leaf

        """
        pass

    def test_delete_leaf_list(self):
        """Test case for delete_leaf_list

        """
        pass

    def test_delete_leaf_type(self):
        """Test case for delete_leaf_type

        """
        pass

    def test_delete_localization(self):
        """Test case for delete_localization

        """
        pass

    def test_delete_localization_list(self):
        """Test case for delete_localization_list

        """
        pass

    def test_delete_localization_type(self):
        """Test case for delete_localization_type

        """
        pass

    def test_delete_media(self):
        """Test case for delete_media

        """
        pass

    def test_delete_media_list(self):
        """Test case for delete_media_list

        """
        pass

    def test_delete_media_type(self):
        """Test case for delete_media_type

        """
        pass

    def test_delete_membership(self):
        """Test case for delete_membership

        """
        pass

    def test_delete_project(self):
        """Test case for delete_project

        """
        pass

    def test_delete_state(self):
        """Test case for delete_state

        """
        pass

    def test_delete_state_list(self):
        """Test case for delete_state_list

        """
        pass

    def test_delete_state_type(self):
        """Test case for delete_state_type

        """
        pass

    def test_delete_temporary_file(self):
        """Test case for delete_temporary_file

        """
        pass

    def test_delete_temporary_file_list(self):
        """Test case for delete_temporary_file_list

        """
        pass

    def test_delete_version(self):
        """Test case for delete_version

        """
        pass

    def test_get_algorithm_list(self):
        """Test case for get_algorithm_list

        """
        pass

    def test_get_analysis_list(self):
        """Test case for get_analysis_list

        """
        pass

    def test_get_clip(self):
        """Test case for get_clip

        """
        pass

    def test_get_frame(self):
        """Test case for get_frame

        """
        pass

    def test_get_leaf(self):
        """Test case for get_leaf

        """
        pass

    def test_get_leaf_list(self):
        """Test case for get_leaf_list

        """
        pass

    def test_get_leaf_type(self):
        """Test case for get_leaf_type

        """
        pass

    def test_get_leaf_type_list(self):
        """Test case for get_leaf_type_list

        """
        pass

    def test_get_localization(self):
        """Test case for get_localization

        """
        pass

    def test_get_localization_list(self):
        """Test case for get_localization_list

        """
        pass

    def test_get_localization_type(self):
        """Test case for get_localization_type

        """
        pass

    def test_get_localization_type_list(self):
        """Test case for get_localization_type_list

        """
        pass

    def test_get_media(self):
        """Test case for get_media

        """
        pass

    def test_get_media_list(self):
        """Test case for get_media_list

        """
        pass

    def test_get_media_next(self):
        """Test case for get_media_next

        """
        pass

    def test_get_media_prev(self):
        """Test case for get_media_prev

        """
        pass

    def test_get_media_sections(self):
        """Test case for get_media_sections

        """
        pass

    def test_get_media_type(self):
        """Test case for get_media_type

        """
        pass

    def test_get_media_type_list(self):
        """Test case for get_media_type_list

        """
        pass

    def test_get_membership(self):
        """Test case for get_membership

        """
        pass

    def test_get_membership_list(self):
        """Test case for get_membership_list

        """
        pass

    def test_get_project(self):
        """Test case for get_project

        """
        pass

    def test_get_project_list(self):
        """Test case for get_project_list

        """
        pass

    def test_get_section_analysis(self):
        """Test case for get_section_analysis

        """
        pass

    def test_get_state(self):
        """Test case for get_state

        """
        pass

    def test_get_state_list(self):
        """Test case for get_state_list

        """
        pass

    def test_get_state_type(self):
        """Test case for get_state_type

        """
        pass

    def test_get_state_type_list(self):
        """Test case for get_state_type_list

        """
        pass

    def test_get_temporary_file(self):
        """Test case for get_temporary_file

        """
        pass

    def test_get_temporary_file_list(self):
        """Test case for get_temporary_file_list

        """
        pass

    def test_get_user(self):
        """Test case for get_user

        """
        pass

    def test_get_version(self):
        """Test case for get_version

        """
        pass

    def test_leaf_suggestion(self):
        """Test case for leaf_suggestion

        """
        pass

    def test_notify(self):
        """Test case for notify

        """
        pass

    def test_partial_update_save_video_api(self):
        """Test case for partial_update_save_video_api

        """
        pass

    def test_progress(self):
        """Test case for progress

        """
        pass

    def test_retrieve_state_graphic_api(self):
        """Test case for retrieve_state_graphic_api

        """
        pass

    def test_retrieve_version_list(self):
        """Test case for retrieve_version_list

        """
        pass

    def test_save_image(self):
        """Test case for save_image

        """
        pass

    def test_save_video(self):
        """Test case for save_video

        """
        pass

    def test_transcode(self):
        """Test case for transcode

        """
        pass

    def test_update_leaf(self):
        """Test case for update_leaf

        """
        pass

    def test_update_leaf_list(self):
        """Test case for update_leaf_list

        """
        pass

    def test_update_leaf_type(self):
        """Test case for update_leaf_type

        """
        pass

    def test_update_localization(self):
        """Test case for update_localization

        """
        pass

    def test_update_localization_list(self):
        """Test case for update_localization_list

        """
        pass

    def test_update_localization_type(self):
        """Test case for update_localization_type

        """
        pass

    def test_update_media(self):
        """Test case for update_media

        """
        pass

    def test_update_media_list(self):
        """Test case for update_media_list

        """
        pass

    def test_update_media_type(self):
        """Test case for update_media_type

        """
        pass

    def test_update_membership(self):
        """Test case for update_membership

        """
        pass

    def test_update_project(self):
        """Test case for update_project

        """
        pass

    def test_update_state(self):
        """Test case for update_state

        """
        pass

    def test_update_state_list(self):
        """Test case for update_state_list

        """
        pass

    def test_update_state_type(self):
        """Test case for update_state_type

        """
        pass

    def test_update_user(self):
        """Test case for update_user

        """
        pass

    def test_update_version(self):
        """Test case for update_version

        """
        pass

    def test_whoami(self):
        """Test case for whoami

        """
        pass


if __name__ == '__main__':
    unittest.main()
