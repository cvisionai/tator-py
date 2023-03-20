import time
import subprocess

import tator
import uuid
import json


def _assert_subprocess(cmd, desired_result=True):
    out = subprocess.run(cmd, capture_output=True)

    if desired_result:
        assert out.returncode == 0, out.stderr
    else:
        assert out.returncode != 0, out.stdout


def _get_stream_info(path):
    cmd = [
        "ffprobe",
        "-v","error",
        "-show_entries", "stream",
        "-print_format", "json",
        "-select_streams", "v",
        path,
    ]
    p = subprocess.run(cmd, stdout=subprocess.PIPE)
    return json.loads(p.stdout.decode())['streams'][0]

def test_local_transcode(host, token, project, video_type, video_file):
    unique_name = f"{uuid.uuid4()}.mp4"
    cmd = [
        'python3', '-m', 'tator.transcode', video_file,
        '--host', host,
        '--token', token,
        '--project', str(project),
        '--type', str(video_type),
        '--section', 'Locally transcoded',
        '--name', unique_name
    ]
    _assert_subprocess(cmd)
    _assert_subprocess(cmd)
    api = tator.get_api(host, token)
    media_obj = api.get_media_list(project, name=unique_name, presigned=3600)[0]

    stream_info = _get_stream_info(media_obj.media_files.archival[0].path)
    assert stream_info['pix_fmt'] == 'yuv420p'
    stream_info = _get_stream_info(media_obj.media_files.streaming[0].path)
    assert stream_info['pix_fmt'] == 'yuv420p'

def test_local_transcode_yuv444p(host, token, project, yuv444p_video_type, video_file):
    unique_name = f"{uuid.uuid4()}.mp4"
    cmd = [
        'python3', '-m', 'tator.transcode', video_file,
        '--host', host,
        '--token', token,
        '--project', str(project),
        '--type', str(yuv444p_video_type),
        '--section', 'Locally transcoded (yuv444p)',
        '--name', unique_name
    ]
    _assert_subprocess(cmd)
    api = tator.get_api(host, token)
    media_obj = api.get_media_list(project, name=unique_name, presigned=3600)[0]

    stream_info = _get_stream_info(media_obj.media_files.archival[0].path)
    assert stream_info['pix_fmt'] == 'yuv444p'
    stream_info = _get_stream_info(media_obj.media_files.streaming[0].path)
    assert stream_info['pix_fmt'] == 'yuv444p'

def test_bad_file(host, token, project, video_type, image_file):
    cmd = [
        'python3', '-m', 'tator.transcode', image_file,
        '--host', host,
        '--token', token,
        '--project', str(project),
        '--type', str(video_type),
        '--section', 'Bad transcodes',
    ]
    _assert_subprocess(cmd, False)
    time.sleep(2)
    # Make sure media file is gone.
    api = tator.get_api(host, token)
    sections = api.get_section_list(project)
    section_obj = [s for s in sections if s.name == 'Bad transcodes'][0]

    medias = api.get_media_list(project, attribute=[f'tator_user_sections::{section_obj.tator_user_sections}'])
    print(medias)
    assert(len(medias) == 0)

    medias = api.get_media_list(project, section=section_obj.id)
    print(medias)
    assert(len(medias) == 0)
