import time
import subprocess

import tator

def test_local_transcode(host, token, project, video_type, video_file):
    cmd = [
        'python3', '-m', 'tator.transcode', video_file,
        '--host', host,
        '--token', token,
        '--project', str(project),
        '--type', str(video_type),
        '--section', 'Locally transcoded',
    ]
    subprocess.run(cmd, check=True)

def test_bad_file(host, token, project, video_type, image_file):
    failed = False
    try:
        cmd = [
            'python3', '-m', 'tator.transcode', image_file,
            '--host', host,
            '--token', token,
            '--project', str(project),
            '--type', str(video_type),
            '--section', 'Bad transcodes',
        ]
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as cpe:
        failed = True
    assert(failed)
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
