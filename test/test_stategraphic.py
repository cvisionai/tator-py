import tator
from tator.util import get_images

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

def test_stategraphic(url, token, project, video, box_type, track_type):
    tator_api = tator.get_api(url, token)
    video_obj = tator_api.get_media(video)

    # Make boxes for track.
    boxes = [_make_box(project, box_type, video, frame) for frame in range(10)]
    response = tator_api.create_localization_list(project, localization_spec=boxes)
    assert isinstance(response, tator.CreateListResponse)
    print(response.message)
    box_ids = response.id

    # Make track.
    response = tator_api.create_state_list(project, state_spec=[{
        'project': project,
        'type': track_type,
        'media_ids': [video],
        'localization_ids': box_ids,
    }])
    print(response.message)
    assert isinstance(response, tator.CreateListResponse)
    track_id = response.id[0]

    # Get state graphic.
    file_path = tator_api.get_state_graphic(track_id, mode='tile')
    state = tator_api.get_state(track_id)
    stategraphic = get_images(file_path, state)
    assert(len(stategraphic) == 10)
    for frame_data in stategraphic:
        size = (frame_data.height, frame_data.width, len(frame_data.mode))
        assert_vector_equal(size, (720,1280,3))

