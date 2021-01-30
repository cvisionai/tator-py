import os
import tator
import tempfile

from tator.extractor.extractor import process_file

def test_extract(host, token, project, video_temp, box_type,
                 image_type,
                 state_type):
    video = video_temp
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)
    localization={'x':0.50,
                  'y':0.50,
                  'width': 0.25,
                  'height': 0.25,
                  'type': box_type,
                  'media_id': video,
                  'frame': 0}
    state={'frame': 1, 'media_ids':[video], 'type': state_type}
    api = tator.get_api(host,token)
    response = api.create_localization_list(project, [localization])
    localization_id = response.id[0]
    response = api.create_state_list(project, [state])
    state_id = response.id[0]

    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, "temp.mp4")
        for _ in tator.download_media(api, api.get_media(video), out):
            pass
        
        process_file(api,
                     project,
                     out,
                     api.get_media(video),
                     'localization_thumbnail',
                     api.get_localization_list(project,media_id=[video]),
                     td)

        process_file(api,
                     project,
                     out,
                     api.get_media(video),
                     'localization_keyframe',
                     api.get_localization_list(project,media_id=[video]),
                     td)

        process_file(api,
                     project,
                     out,
                     api.get_media(video),
                     'state',
                     api.get_state_list(project,media_id=[video]),
                     td)

        image_cnt = 0
        for _, __, files in os.walk(td):
            for fp in files:
                if os.path.splitext(fp)[1] == '.png':
                    image_cnt += 1


        assert image_cnt == 3

    # Clean up.
    api.delete_localization(localization_id)
    api.delete_state(state_id)

