import os
import glob
import tarfile
import tempfile
import random
import uuid
import datetime

import tator
from .test_localization import random_localization

def random_localization(video_obj):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    w = random.uniform(0.0, 1.0 - x)
    h = random.uniform(0.0, 1.0 - y)
    attributes = {
        'test_bool': random.choice([False, True]),
        'test_int': random.randint(-1000, 1000),
        'test_float': random.uniform(-1000.0, 1000.0),
        'test_enum': random.choice(['a', 'b', 'c']),
        'test_string': str(uuid.uuid1()),
        'test_datetime': datetime.datetime.now().isoformat(),
        'test_geopos': [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
    }
    out = {
        'x': x,
        'y': y,
        'width': w,
        'height': h,
        'frame': random.randint(0, video_obj.num_frames - 1),
    }
    return {**out, **attributes}

def random_state(video_obj):
    attributes = {
        'test_bool': random.choice([False, True]),
        'test_int': random.randint(-1000, 1000),
        'test_float': random.uniform(-1000.0, 1000.0),
        'test_enum': random.choice(['a', 'b', 'c']),
        'test_string': str(uuid.uuid1()),
        'test_datetime': datetime.datetime.now().isoformat(),
        'test_geopos': [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
    }
    out = {
        'frame': random.randint(0, video_obj.num_frames - 1),
    }
    return {**out, **attributes}

def test_upload_file_list(host, token, project, image_type, image_set):
    tator_api = tator.get_api(host, token)
    paths = os.listdir(image_set)
    paths = [os.path.join(image_set, path) for path in paths]
    paths = paths[:100] # Only upload the first 100 files.
    batch_num = 0
    for batch in tator.util.chunked_file_list(paths):
        print(f"Uploading file {batch_num*10} / {len(paths)}")
        for progress, response in tator.util.upload_media_archive(tator_api, project, batch):
            print(f"Archive upload progress: {progress}%")
        batch_num += 1
        assert isinstance(response, tator.models.Transcode)
        print(response.message)
    
def test_upload_archive(host, token, project, image_type, image_set, video_type, video_file, video,
                        box_type, state_type):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)
    video_base = os.path.basename(video_file)

    # Add images to tar file.
    paths = glob.glob(os.path.join(image_set, '**/*.jpg'), recursive=True)
    paths = paths[:10] # Only upload the first 10 files.
    tar_buf = tempfile.NamedTemporaryFile()
    tar_file = tarfile.TarFile(mode='w', fileobj=tar_buf)
    for idx,fp in enumerate(paths):
        tar_file.add(fp, arcname=os.path.basename(fp))

    # Add video to tar file.
    tar_file.add(video_file, arcname=video_base)

    # Make csv with localizations in it.
    with tempfile.NamedTemporaryFile('w') as fp:
        fp.write('frame,x,y,width,height,test_string\n')
        for _ in range(10):
            loc = random_localization(video_obj)
            fp.write(f"{loc['frame']},{loc['x']},{loc['x']},{loc['width']},"
                     f"{loc['height']},{loc['test_string']}\n")
        arcname = os.path.join(os.path.splitext(video_base)[0], 'localizations',
                                                f"{box_type}.csv")
        fp.flush()
        tar_file.add(fp.name, arcname=arcname)

    # Make csv with states in it.
    with tempfile.NamedTemporaryFile('w') as fp:
        fp.write('frame,test_string\n')
        for _ in range(10):
            loc = random_state(video_obj)
            fp.write(f"{loc['frame']},{loc['test_string']}\n")
        arcname = os.path.join(os.path.splitext(video_base)[0], 'states',
                                                f"{state_type}.csv")
        fp.flush()
        tar_file.add(fp.name, arcname=arcname)

    tar_buf.flush()

    # Upload the archive.
    for progress, response in tator.util.upload_media_archive(tator_api, project, tar_buf.name):
        print(f"Archive upload progress: {progress}%")
    assert isinstance(response, tator.models.Transcode)
    print(response.message)
    
