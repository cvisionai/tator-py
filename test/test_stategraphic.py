import tator
import datetime

from ._common import assert_vector_equal

def _make_box(project, box_type, video, frame):
    return {
        'x': 0,
        'y': 0,
        'width': 1,
        'height': 1,
        'project': project,
        'type': box_type,
        'media_id': video,
        'frame': frame,
    }

def test_stategraphic(host, token, project, video, box_type, track_type):
    TRACK_LENGTH=200

    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    # Make boxes for track.
    boxes = [_make_box(project, box_type, video, frame) for frame in range(TRACK_LENGTH)]
    response = tator_api.create_localization_list(project, boxes)
    assert isinstance(response, tator.models.CreateListResponse)
    print(response.message)
    box_ids = response.id

    # Make track.
    response = tator_api.create_state_list(
        project,
        body={
            'project': project,
            'type': track_type,
            'media_ids': [video],
            'localization_ids': box_ids,
        },
    )
    print(response.message)
    assert isinstance(response, tator.models.CreateListResponse)
    track_id = response.id[0]

    # Get state graphic.
    t0 = datetime.datetime.now()
    stategraphic = tator.util.full_state_graphic(tator_api, track_id)
    t1 = datetime.datetime.now()
    print(f"State graphic took {t1 - t0} seconds.")
    assert(len(stategraphic) == TRACK_LENGTH)
    for frame_data in stategraphic:
        size = (frame_data.height, frame_data.width, len(frame_data.mode))
        assert_vector_equal(size, (224,224,3))

