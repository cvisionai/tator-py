import datetime
import os
import shutil
import time
import tarfile
import yaml
from uuid import uuid1

import pytest
import requests

def pytest_addoption(parser):
    parser.addoption('--host', help='Tator host', default='https://adamant.duckdns.org')
    parser.addoption('--token', help='API token', default='')
    parser.addoption('--bucket', help='Optional path to yaml file containing bucket spec. If '
                                      'given, the project will use this bucket.')
    parser.addoption('--keep', help='Do not delete project when done', action='store_true')

def pytest_generate_tests(metafunc):
    if 'host' in metafunc.fixturenames:
          metafunc.parametrize('host', [metafunc.config.getoption('host')])
    if 'token' in metafunc.fixturenames:
          metafunc.parametrize('token', [metafunc.config.getoption('token')])

def make_attribute_types():
    return [
        dict(
            name='test_bool',
            dtype='bool',
            default=True,
        ),
        dict(
            name='test_int',
            dtype='int',
            default=0,
            minimum=-1000,
            maximum=1000,
        ),
        dict(
            name='test_float',
            dtype='float',
            default=0.0,
            minimum=-1000.0,
            maximum=1000.0,
        ),
        dict(
            name='test_enum',
            dtype='enum',
            choices=['a', 'b', 'c'],
            default='a',
        ),
        dict(
            name='test_string',
            dtype='string',
            default='asdf',
        ),
        dict(
            name='test_datetime',
            dtype='datetime',
            use_current=True,
        ),
        dict(
            name='test_geopos',
            dtype='geopos',
            default=[-179.0, -89.0],
        ),
        dict(
            name='test_float_array',
            dtype='float_array',
            default=[0.0, 0.0, 0.0],
            size=3,
        )
    ]

@pytest.fixture(scope='session')
def organization(request):
    """ Organization ID for a created organization. """
    import tator
    host = request.config.option.host
    token = request.config.option.token
    keep = request.config.option.keep
    tator_api = tator.get_api(host, token)
    current_dt = datetime.datetime.now()
    dt_str = current_dt.strftime('%Y_%m_%d__%H_%M_%S')
    response = tator_api.create_organization(organization_spec={
        'name': f'test_organization_{dt_str}',
    })
    organization_id = response.id
    yield organization_id
    if not keep:
        status = tator_api.delete_organization(organization_id)

@pytest.fixture(scope='session')
def project(request, organization):
    """ Project ID for a created project. """
    import tator
    host = request.config.option.host
    token = request.config.option.token
    bucket = request.config.option.bucket
    keep = request.config.option.keep
    tator_api = tator.get_api(host, token)
    current_dt = datetime.datetime.now()
    dt_str = current_dt.strftime('%Y_%m_%d__%H_%M_%S')
    project_spec = {
        'name': f'test_project_{dt_str}',
        'summary': f'Test project created by tator-py unit tests on {current_dt}',
        'organization': organization,
    }

    # Create bucket object if bucket spec is given.
    if bucket is not None:
        with open(bucket, 'r') as f:
            bucket_spec = yaml.safe_load(f)
        response = tator_api.create_bucket(organization, bucket_spec=bucket_spec)
        project_spec['bucket'] = response.id

    response = tator_api.create_project(project_spec=project_spec)
    project_id = response.id
    yield project_id
    if not keep:
        status = tator_api.delete_project(project_id)

@pytest.fixture(scope='session')
def algo_project(request, organization):
    """ Project ID for a created project. """
    import tator
    host = request.config.option.host
    token = request.config.option.token
    keep = request.config.option.keep
    tator_api = tator.get_api(host, token)
    current_dt = datetime.datetime.now()
    dt_str = current_dt.strftime('%Y_%m_%d__%H_%M_%S')
    response = tator_api.create_project(project_spec={
        'name': f'algo_test_project_{dt_str}',
        'summary': f'Algo test project created by tator-py unit tests on {current_dt}',
        'organization': organization,
    })
    project_id = response.id
    yield project_id
    if not keep:
        status = tator_api.delete_project(project_id)

@pytest.fixture(scope='session')
def image_type(request, project):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_media_type(project, media_type_spec={
        'name': 'image_type',
        'description': 'Test image type',
        'project': project,
        'dtype': 'image',
        'attribute_types': make_attribute_types(),
    })
    image_type_id = response.id
    yield image_type_id

@pytest.fixture(scope='session')
def image_file(request):
    out_path = '/tmp/test1.jpg'
    if not os.path.exists(out_path):
        url = 'https://www.gstatic.com/webp/gallery/1.jpg'
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(out_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
    yield out_path

@pytest.fixture(scope='session')
def image(request, project, image_type, image_file):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    for progress, response in tator.util.upload_media(tator_api, image_type, image_file):
        print(f"Upload image progress: {progress}%")
    print(response.message)

    num_retries = 0
    while True:
        medias = tator_api.get_media_list(project, name='test1.jpg')
        if len(medias) > 0:
            image_id = medias[0].id
            break

        num_retries += 1
        max_retries = 30
        assert num_retries < max_retries
        time.sleep(0.5)

    yield image_id

@pytest.fixture(scope='session')
def image_set(request):
    out_path = '/tmp/lfw.tgz'
    extract_path = '/tmp/lfw'

    # Download Labeled Faces in the Wild dataset.
    if not os.path.exists(out_path):
        url = 'http://vis-www.cs.umass.edu/lfw/lfw.tgz'
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(out_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

    # Extract the images.
    if not os.path.exists(extract_path):
        os.makedirs(extract_path, exist_ok=True)
        tar = tarfile.open(out_path)
        for item in tar:
            tar.extract(item, extract_path)

    image_path = os.path.join(extract_path, 'lfw')
    yield image_path
    shutil.rmtree(extract_path)


@pytest.fixture(scope='session')
def video_type(request, project):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_media_type(project, media_type_spec={
        'name': 'video_type',
        'description': 'Test video type',
        'project': project,
        'dtype': 'video',
        'attribute_types': make_attribute_types(),
        'archive_config': [{'encode': {'vcodec': 'copy', 'crf': 30}}],
    })
    video_type_id = response.id
    yield video_type_id

@pytest.fixture(scope='session')
def multi_type(request, project):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_media_type(project, media_type_spec={
        'name': 'multi_type',
        'description': 'Test multi type',
        'project': project,
        'dtype': 'multi',
        'attribute_types': make_attribute_types(),
    })
    multi_type_id = response.id
    yield multi_type_id

@pytest.fixture(scope='session')
def video_file(request):
    out_path = '/tmp/AudioVideoSyncTest_BallastMedia.mp4'
    if not os.path.exists(out_path):
        url = 'http://www.ballastmedia.com/wp-content/uploads/AudioVideoSyncTest_BallastMedia.mp4'
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(out_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
    yield out_path

@pytest.fixture(scope='session')
def video(request, project, video_type, video_file):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    attributes = {"test_string": str(uuid1())}
    for progress, response in tator.util.upload_media(tator_api, video_type, video_file, attributes=attributes):
        print(f"Upload video progress: {progress}%")
    print(response.message)
    while True:
        response = tator_api.get_media_list(project, name='AudioVideoSyncTest_BallastMedia.mp4')
        print("Waiting for transcode...")
        time.sleep(2.5)
        if len(response) == 0:
            continue
        if response[0].media_files is None:
            continue
        streaming = response[0].media_files.streaming
        have_archival = response[0].media_files.archival is not None
        if streaming and have_archival and len(streaming) == 4:
            video_id = response[0].id
            break
    # Check for proper attribute setting via upload_file
    assert response[0].attributes.get("test_string") == attributes.get("test_string")

    # If all is kosher return the video_id
    yield video_id

## This is an empty video to make tests run faster
@pytest.fixture(scope='session')
def empty_video(request, project, video_type):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_media(project,
    {"name": 'empty.mp4',
    'num_frames': 30000,
    'fps': 20, 'section': 'empty_media', 'md5': '', 'type': video_type})
    yield response.id

@pytest.fixture(scope='function')
def video_temp(request, project, video_type, video_file):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    for progress, response in tator.util.upload_media(tator_api, video_type, video_file):
        print(f"Upload video progress: {progress}%")
    print(response.message)
    while True:
        response = tator_api.get_media_list(project, name='AudioVideoSyncTest_BallastMedia.mp4')
        print("Waiting for transcode...")
        time.sleep(2.5)
        if len(response) == 0:
            continue
        if response[0].media_files is None:
            continue
        have_streaming = response[0].media_files.streaming is not None
        have_archival = response[0].media_files.archival is not None
        if have_streaming and have_archival:
            video_id = response[0].id
            break
    yield video_id

@pytest.fixture(scope='session')
def multi(request, project, multi_type, video):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator.util.make_multi_stream(tator_api, multi_type, [1, 1], 
                                            'Test multi', [video], 'Multi Videos')
    multi_id = response.id
    yield multi_id

@pytest.fixture(scope='session')
def dot_type(request, project, video_type, image_type):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_localization_type(project, localization_type_spec={
        'name': 'dot_type',
        'description': 'Test dot type',
        'project': project,
        'media_types': [video_type, image_type],
        'dtype': 'dot',
        'attribute_types': make_attribute_types(),
    })
    dot_type_id = response.id
    yield dot_type_id

@pytest.fixture(scope='session')
def line_type(request, project, video_type, image_type):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_localization_type(project, localization_type_spec={
        'name': 'line_type',
        'description': 'Test line type',
        'project': project,
        'media_types': [video_type, image_type],
        'dtype': 'line',
        'attribute_types': make_attribute_types(),
    })
    line_type_id = response.id
    yield line_type_id

@pytest.fixture(scope='session')
def box_type(request, project, video_type, image_type):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_localization_type(project, localization_type_spec={
        'name': 'box_type',
        'description': 'Test box type',
        'project': project,
        'media_types': [video_type, image_type],
        'dtype': 'box',
        'attribute_types': make_attribute_types(),
    })
    box_type_id = response.id
    yield box_type_id

@pytest.fixture(scope='session')
def poly_type(request, project, video_type, image_type):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_localization_type(project, localization_type_spec={
        'name': 'poly_type',
        'description': 'Test poly type',
        'project': project,
        'media_types': [video_type, image_type],
        'dtype': 'poly',
        'attribute_types': make_attribute_types(),
    })
    poly_type_id = response.id
    yield poly_type_id

@pytest.fixture(scope='session')
def state_type(request, project, video_type):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_state_type(project, state_type_spec={
        'name': 'state_type',
        'description': 'Test state type',
        'project': project,
        'media_types': [video_type],
        'association': 'Frame',
        'attribute_types': make_attribute_types(),
    })
    state_type_id = response.id
    yield state_type_id

@pytest.fixture(scope='session')
def track_type(request, project, video_type):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_state_type(project, state_type_spec={
        'name': 'track_type',
        'description': 'Test track type',
        'project': project,
        'media_types': [video_type],
        'association': 'Localization',
        'attribute_types': make_attribute_types(),
    })
    state_type_id = response.id
    yield state_type_id

@pytest.fixture(scope='session')
def collection_type(request, project, video_type):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_state_type(project, state_type_spec={
        'name': 'collection_type',
        'description': 'Test collection type',
        'project': project,
        'media_types': [video_type],
        'association': 'Media',
        'attribute_types': make_attribute_types(),
    })
    state_type_id = response.id
    yield state_type_id

@pytest.fixture(scope='session')
def leaf_type(request, project):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_leaf_type(project, leaf_type_spec={
        'name': 'leaf_type',
        'description': 'Test leaf type',
        'attribute_types': make_attribute_types(),
    })
    leaf_type_id = response.id
    yield leaf_type_id

@pytest.fixture(scope='session')
def clone_project(request, organization):
    """ Project ID for a created project. """
    import tator
    host = request.config.option.host
    token = request.config.option.token
    keep = request.config.option.keep
    tator_api = tator.get_api(host, token)
    current_dt = datetime.datetime.now()
    dt_str = current_dt.strftime('%Y_%m_%d__%H_%M_%S')
    response = tator_api.create_project(project_spec={
        'name': f'test_clone_project_{dt_str}',
        'summary': f'Test clone project created by tator-py unit tests on {current_dt}',
        'organization': organization,
    })
    project_id = response.id
    yield project_id
    if not keep:
        status = tator_api.delete_project(project_id)

@pytest.fixture(scope='session')
def clone_leaf_type(request, clone_project):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_leaf_type(clone_project, leaf_type_spec={
        'name': 'leaf_type',
        'description': 'Test leaf type',
        'attribute_types': make_attribute_types(),
    })
    leaf_type_id = response.id
    yield leaf_type_id

# Video fixtures for attribute tests
@pytest.fixture(scope='session')
def attribute_video_type(request, project):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_media_type(project, media_type_spec={
        'name': 'attribute_video_type',
        'description': 'Test video type',
        'project': project,
        'dtype': 'video',
        'attribute_types': make_attribute_types(),
        'archive_config': [{'encode': {'vcodec': 'hevc', 'crf': 30}}],
    })
    video_type_id = response.id
    yield video_type_id

@pytest.fixture(scope="session")
def attribute_video_file(request):
    out_path = f"/tmp/AudioVideoSyncTest_BallastMedia_attribute.mp4"
    if not os.path.exists(out_path):
        url = "http://www.ballastmedia.com/wp-content/uploads/AudioVideoSyncTest_BallastMedia.mp4"
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(out_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
    yield out_path


@pytest.fixture(scope="session")
def attribute_video(request, project, attribute_video_type, attribute_video_file):
    import tator

    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    for progress, response in tator.util.upload_media(tator_api, attribute_video_type, attribute_video_file):
        print(f"Upload video progress: {progress}%")
    print(response.message)
    while True:
        response = tator_api.get_media_list(
            project, name="AudioVideoSyncTest_BallastMedia_attribute.mp4"
        )
        print("Waiting for transcode...")
        time.sleep(2.5)
        if len(response) == 0:
            continue
        if response[0].media_files is None:
            continue
        have_streaming = response[0].media_files.streaming is not None
        have_archival = response[0].media_files.archival is not None
        if have_streaming and have_archival:
            video_id = response[0].id
            break
    yield video_id

@pytest.fixture(scope='session')
def attribute_image_type(request, project):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_media_type(project, media_type_spec={
        'name': 'attribute_image_type',
        'description': 'Test image type',
        'project': project,
        'dtype': 'image',
        'attribute_types': make_attribute_types(),
    })
    image_type_id = response.id
    yield image_type_id

@pytest.fixture(scope='session')
def attribute_box_type(request, project, attribute_video_type, attribute_image_type):
    import tator
    host = request.config.option.host
    token = request.config.option.token
    tator_api = tator.get_api(host, token)
    response = tator_api.create_localization_type(project, localization_type_spec={
        'name': 'box_type',
        'description': 'Test box type',
        'project': project,
        'media_types': [attribute_video_type, attribute_image_type],
        'dtype': 'box',
        'attribute_types': make_attribute_types(),
    })
    box_type_id = response.id
    yield box_type_id
