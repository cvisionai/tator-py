from datetime import datetime
import os
from random import randint
import tempfile
from time import sleep
from urllib.parse import parse_qs, urlparse
from uuid import uuid1

import tator
from tator.openapi.tator_openapi import CreateListResponse


def test_make_multi_stream(host, token, project, video, video_temp, multi_type):
    tator_api = tator.get_api(host, token)

    assert video != video_temp
    multi_ids = [video, video_temp]
    response = tator.util.make_multi_stream(
        tator_api, multi_type, [1, 2], 'Test multi', multi_ids, 'Multi Videos'
    )

    assert isinstance(response, CreateListResponse)
    multi_obj = tator_api.get_media(response.id[0])
    assert multi_obj.media_files.ids == multi_ids
