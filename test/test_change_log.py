from time import sleep
from uuid import uuid4
import random
from datetime import datetime
import pytest

import tator


def random_localization(project, box_type, video_obj, post=False):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    w = random.uniform(0.0, 1.0 - x)
    h = random.uniform(0.0, 1.0 - y)
    attributes = {
        "test_bool": random.choice([False, True]),
        "test_int": random.randint(-1000, 1000),
        "test_float": random.uniform(-1000.0, 1000.0),
        "test_enum": random.choice(["a", "b", "c"]),
        "test_string": str(uuid4()),
        "test_datetime": datetime.now().isoformat(),
        "test_geopos": [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
    }
    out = {
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "project": project,
        "type": box_type,
        "media_id": video_obj.id,
        "frame": random.randint(0, video_obj.num_frames - 1),
    }
    if post:
        out = {**out, **attributes}
    else:
        out["attributes"] = attributes
    return out


def compare_change_logs(new, old):
    for change in new.description_of_change.old:
        for comp in old.description_of_change.new:
            if comp.name == change.name:
                if type(comp.value) == float or type(change.value) == float:
                    is_equal = comp.value == pytest.approx(change.value)
                else:
                    is_equal = comp.value == change.value

                if is_equal:
                    break
                else:
                    print(f"FAILED '{comp.name}': {change.value} != {comp.value}")
                    return False
    return True


def test_box_type_changelog(host, token, project, attribute_video, attribute_box_type):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(attribute_video)

    num_localizations = 2
    boxes = [
        random_localization(project, attribute_box_type, video_obj, post=True)
        for _ in range(num_localizations)
    ]
    box_ids = [
        box_id
        for response in tator.util.chunked_create(
            tator_api.create_localization_list, project, localization_spec=boxes
        )
        for box_id in response.id
    ]

    assert len(box_ids) == len(boxes)

    # Creation tests
    create_changes = []
    for box_id, box in zip(box_ids, boxes):
        changes = tator_api.get_change_log_list(project=project, entity_id=box_id)

        # Assert one change returned
        assert len(changes) == 1
        changes = changes[0]

        # Assert all old values are None for creation
        for change in changes.description_of_change.old:
            assert change.value == None

        # Assert all new values match initial creation values
        for change in changes.description_of_change.new:
            if change.name == "_id":
                assert change.value == box_id
            elif change.name in ["_x", "_y", "_width", "_height", "_frame"]:
                assert change.value == box[change.name.replace("_", "")]
            elif change.name.startswith("test_"):
                assert change.value == box[change.name]
        create_changes.append(changes)

    patch_boxes = [
        random_localization(project, attribute_box_type, video_obj)
        for _ in range(num_localizations)
    ]
    for box_id, patch_box in zip(box_ids, patch_boxes):
        tator_api.update_localization(box_id, localization_update=patch_box)

    # Update tests
    patch_changes = []
    for box_id, box, old_change_log in zip(box_ids, patch_boxes, create_changes):
        changes = tator_api.get_change_log_list(project=project, entity_id=box_id)

        # Assert one change returned
        assert len(changes) == 2
        for new_change_log in changes:
            if new_change_log.id != old_change_log.id:
                break
        else:
            assert False, "No new change log detected"

        # Assert all old values are from creation
        assert compare_change_logs(new_change_log, old_change_log)

        # Assert all new values match initial creation values
        for change in new_change_log.description_of_change.new:
            if change.name == "_id":
                assert change.value == box_id
            elif change.name in ["_x", "_y", "_width", "_height", "_frame"]:
                assert change.value == box[change.name.replace("_", "")]
            elif change.name.startswith("test_"):
                assert change.value == box["attributes"][change.name]
        patch_changes.append(new_change_log)

    # Clean up
    params = {"media_id": [attribute_video], "type": attribute_box_type}
    tator_api.delete_localization_list(project, **params)

    # Deletion tests
    for box_id, patch_change_log, create_change_log in zip(box_ids, patch_changes, create_changes):
        changes = tator_api.get_change_log_list(project=project, entity_id=box_id)

        # Assert one change returned
        assert len(changes) == 3
        for new_change_log in changes:
            if (
                new_change_log.id != patch_change_log.id
                and new_change_log.id != create_change_log.id
            ):
                break
        else:
            assert False, "No deletion change log detected"

        # Assert all old values are from update
        assert compare_change_logs(new_change_log, patch_change_log)

        # Assert all new values are None for deletion
        for change in new_change_log.description_of_change.new:
            assert change.value == None
