from datetime import datetime
from functools import partial
from pprint import pprint
import pytest
import random
import string
import uuid

import tator


def random_state(project, state_type, video_obj, post=False):
    attributes = {
        "test_bool": random.choice([False, True]),
        "test_int": random.randint(-1000, 1000),
        "test_float": random.uniform(-1000.0, 1000.0),
        "test_enum": random.choice(["a", "b", "c"]),
        "test_string": str(uuid.uuid1()),
        "test_datetime": datetime.now().isoformat(),
        "test_geopos": [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
        "test_float_array": [random.uniform(-1.0, 1.0) for _ in range(3)],
    }
    out = {
        "project": project,
        "type": state_type,
        "media_ids": [video_obj.id],
        "frame": random.randint(0, video_obj.num_frames - 1),
        "attributes": attributes
    }

    return {**out}


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
        "test_string": str(uuid.uuid4()),
        "test_datetime": datetime.now().isoformat(),
        "test_geopos": [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
        "test_float_array": [random.uniform(-1.0, 1.0) for _ in range(3)],
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
        "attributes": attributes
    }

    return {**out}


def random_leaf(project, leaf_type, parent_obj=None, post=False):
    attributes = {
        "test_bool": random.choice([False, True]),
        "test_int": random.randint(-1000, 1000),
        "test_float": random.uniform(-1000.0, 1000.0),
        "test_enum": random.choice(["a", "b", "c"]),
        "test_string": str(uuid.uuid1()),
        "test_datetime": datetime.now().isoformat(),
        "test_geopos": [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
        "test_float_array": [random.uniform(-1.0, 1.0) for _ in range(3)],
    }
    name = "".join(random.choice(string.ascii_letters) for _ in range(10))
    out = {
        "project": project,
        "type": leaf_type,
        "name": name,
        "attributes": attributes
    }
    if parent_obj:
        out["parent"] = parent_obj.id

    return {**out}


def compare_change_logs(new, old):
    for old_in_new in new.description_of_change.old:
        for new_in_old in old.description_of_change.new:
            if new_in_old.name == old_in_new.name:
                if type(new_in_old.value) == float or type(old_in_new.value) == float:
                    is_equal = new_in_old.value == pytest.approx(old_in_new.value)
                else:
                    is_equal = new_in_old.value == old_in_new.value

                assert (
                    is_equal
                ), f"FAILED '{new_in_old.name}': {new_in_old.value} != {old_in_new.value}"


def change_log_helper(
    tator_api,
    random_entity,
    entity_type,
    project,
    create_list,
    update_one,
    update_list,
    delete_one,
    delete_list,
):
    num_entities = 2
    entities = [random_entity(post=True) for _ in range(num_entities)]
    response = create_list(project, entities)
    entity_ids = response.id

    assert len(entity_ids) == len(entities)

    # Creation tests
    create_changes = []
    for entity_id, box in zip(entity_ids, entities):
        changes = tator_api.get_change_log_list(
            project=project, entity_id=entity_id, entity_type=entity_type
        )

        # Assert one change returned
        assert len(changes) == 1
        changes = changes[0]

        # Assert all old values are None for creation
        for change in changes.description_of_change.old:
            assert change.value == None

        # Assert all new values match initial creation values
        for change in changes.description_of_change.new:
            if change.name == "_id":
                assert change.value == entity_id
            elif change.name in ["_x", "_y", "_width", "_height", "_frame"]:
                assert change.value == box[change.name.replace("_", "")]
            elif change.name.startswith("test_"):
                assert change.value == box['attributes'][change.name]
        create_changes.append(changes)

    patch_entities = [random_entity() for _ in range(num_entities)]
    for entity_id, patch_entity in zip(entity_ids, patch_entities):
        update_one(entity_id, patch_entity)

    # Update tests
    patch_changes = []
    for entity_id, box, old_change_log in zip(entity_ids, patch_entities, create_changes):
        changes = tator_api.get_change_log_list(
            project=project, entity_id=entity_id, entity_type=entity_type
        )

        # Assert two changes returned
        assert len(changes) == 2
        for new_change_log in changes:
            if new_change_log.id != old_change_log.id:
                break
        else:
            assert False, "No new change log detected"

        # Assert all old values are from creation
        compare_change_logs(new_change_log, old_change_log)

        # Assert all new values match initial creation values
        for change in new_change_log.description_of_change.new:
            if change.name == "_id":
                assert change.value == entity_id
            elif change.name in ["_x", "_y", "_width", "_height", "_frame"]:
                assert change.value == box[change.name.replace("_", "")]
            elif change.name.startswith("test_"):
                assert change.value == box["attributes"][change.name]
        patch_changes.append(new_change_log)

    bulk_patch_entity = random_entity()
    bulk_patch_entity = {"attributes": bulk_patch_entity["attributes"]}
    update_list(bulk_patch_entity)

    # Bulk update tests
    bulk_patch_changes = []
    for entity_id, create_change_log, patch_change_log in zip(
        entity_ids, create_changes, patch_changes
    ):
        changes = tator_api.get_change_log_list(
            project=project, entity_id=entity_id, entity_type=entity_type
        )

        # Assert two changes returned
        assert len(changes) == 3
        for new_change_log in changes:
            if new_change_log.id not in [patch_change_log.id, create_change_log.id]:
                break
        else:
            assert False, "No new change log detected"

        # Assert all new values match bulk update values
        for change in new_change_log.description_of_change.new:
            if change.name == "_id":
                assert change.value == entity_id
            elif change.name in ["_x", "_y", "_width", "_height", "_frame"]:
                assert change.value == bulk_patch_entity[change.name.replace("_", "")]
            elif change.name.startswith("test_"):
                assert change.value == bulk_patch_entity["attributes"][change.name]
        bulk_patch_changes.append(new_change_log)

    # Clean up
    delete_one(entity_ids[0])
    delete_list()

    # Deletion tests
    for entity_id, create_change_log, patch_change_log, bulk_change_log in zip(
        entity_ids, create_changes, patch_changes, bulk_patch_changes
    ):
        changes = tator_api.get_change_log_list(
            project=project, entity_id=entity_id, entity_type=entity_type
        )

        # Assert three changes returned
        assert len(changes) == 4
        for new_change_log in changes:
            if new_change_log.id not in [
                patch_change_log.id,
                create_change_log.id,
                bulk_change_log.id,
            ]:
                break
        else:
            assert False, "No deletion change log detected"

        # Assert all old values are from update
        compare_change_logs(new_change_log, bulk_change_log)

        # Assert all new values are None for deletion
        for change in new_change_log.description_of_change.new:
            assert change.value == True


def test_attribute_box_type_change_log(host, token, project, attribute_video, attribute_box_type):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(attribute_video)
    random_entity = partial(random_localization, project, attribute_box_type, video_obj)
    create_list = tator_api.create_localization_list
    update_one = tator_api.update_localization
    update_list = partial(tator_api.update_localization_list, project, media_id=[attribute_video])
    params = {"media_id": [attribute_video], "type": attribute_box_type}
    delete_one = tator_api.delete_localization
    delete_list = partial(tator_api.delete_localization_list, project, **params)
    change_log_helper(
        tator_api,
        random_entity,
        "localization",
        project,
        create_list,
        update_one,
        update_list,
        delete_one,
        delete_list,
    )


def test_state_type_change_log(host, token, project, attribute_video, state_type):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(attribute_video)
    random_entity = partial(random_state, project, state_type, video_obj)
    create_list = tator_api.create_state_list
    update_one = tator_api.update_state
    update_list = partial(tator_api.update_state_list, project, media_id=[attribute_video])
    params = {"media_id": [attribute_video], "type": state_type}
    delete_one = tator_api.delete_state
    delete_list = partial(tator_api.delete_state_list, project, **params)
    change_log_helper(
        tator_api,
        random_entity,
        "state",
        project,
        create_list,
        update_one,
        update_list,
        delete_one,
        delete_list,
    )


def test_media_change_log(host, token, project, attribute_video_type):
    tator_api = tator.get_api(host, token)

    # Define media spec.
    num_media = 3
    fname = "MediaChangeLogTest.mp4"
    media_specs = [
        {
            "type": attribute_video_type,
            "uid": str(uuid.uuid1()),
            "gid": str(uuid.uuid1()),
            "name": fname,
            "md5": str(uuid.uuid1())[:32],
            "section": "Test media change log",
            "attributes": {"test_int": random.randint(0, 100)},
        }
        for _ in range(num_media)
    ]

    # Create the media.
    media_ids = [
        tator_api.create_media_list(project=project, body=[media_spec]).id[0]
        for media_spec in media_specs
    ]

    # Creation tests
    create_changes = []
    for media_id, media_spec in zip(media_ids, media_specs):
        changes = tator_api.get_change_log_list(
            project=project, entity_id=media_id, entity_type="media"
        )

        # Assert one change returned
        assert len(changes) == 1
        changes = changes[0]

        # Assert all old values are None for creation
        for change in changes.description_of_change.old:
            assert change.value == None

        # Assert all new values match initial creation values
        for change in changes.description_of_change.new:
            if change.name == "_id":
                assert change.value == media_id
            elif change.name in ["_type", "_uid", "_gid", "_name", "_md5", "_section"]:
                assert change.value == media_spec[change.name.replace("_", "")]

        create_changes.append(changes)

    media_updates = [{"attributes": {"test_int": random.randint(0, 100)}} for _ in range(num_media)]
    for media_id, media_spec, media_update in zip(media_ids, media_specs, media_updates):
        media_spec["attributes"]["test_int"] = media_update["attributes"]["test_int"]
        tator_api.update_media(media_id, media_update)
    # tator_api.update_media_list(project, media_updates[1])

    # Update tests
    patch_changes = []
    for media_id, media_spec, create_change in zip(media_ids, media_specs, create_changes):
        changes = tator_api.get_change_log_list(
            project=project, entity_id=media_id, entity_type="media"
        )

        # Assert two changes returned
        assert len(changes) == 2
        for new_change_log in changes:
            if new_change_log.id != create_change.id:
                break
        else:
            assert False, "No new change log detected"

        # Assert all old values are from creation
        compare_change_logs(new_change_log, create_change)

        # Assert all new values match initial creation values
        for change in new_change_log.description_of_change.new:
            if change.name == "_id":
                assert change.value == media_id
            elif change.name in ["_type", "_uid", "_gid", "_name", "_md5", "_section"]:
                assert change.value == media_spec[change.name.replace("_", "")]
            elif change.name.startswith("test_"):
                assert change.value == media_spec["attributes"][change.name]

        patch_changes.append(new_change_log)

    media_update = {"attributes": {"test_int": random.randint(0, 100)}}
    for media_spec in media_specs:
        media_spec["attributes"]["test_int"] = media_update["attributes"]["test_int"]
    tator_api.update_media_list(project, media_update, type=attribute_video_type)

    # Bulk update tests
    bulk_patch_changes = []
    for media_id, media_spec, create_change, patch_change in zip(
        media_ids, media_specs, create_changes, patch_changes
    ):
        changes = tator_api.get_change_log_list(
            project=project, entity_id=media_id, entity_type="media"
        )

        # Assert three changes returned
        assert len(changes) == 3
        for new_change_log in changes:
            if new_change_log.id not in [patch_change.id, create_change.id]:
                break
        else:
            assert False, "No new change log detected"

        # Assert all new values match initial creation values
        for change in new_change_log.description_of_change.new:
            if change.name == "_id":
                assert change.value == media_id
            elif change.name in ["_type", "_uid", "_gid", "_name", "_md5", "_section"]:
                assert change.value == media_spec[change.name.replace("_", "")]
            elif change.name.startswith("test_"):
                assert change.value == media_spec["attributes"][change.name]

        bulk_patch_changes.append(new_change_log)

    tator_api.delete_media(media_ids[0])
    tator_api.delete_media_list(project, media_id=media_ids[1:])

    # Deletion tests
    for media_id, media_spec, create_change, patch_change, bulk_change in zip(
        media_ids, media_specs, create_changes, patch_changes, bulk_patch_changes
    ):
        changes = tator_api.get_change_log_list(
            project=project, entity_id=media_id, entity_type="media"
        )

        # Assert four changes returned
        assert len(changes) == 4
        for new_change_log in changes:
            if new_change_log.id not in [
                patch_change.id,
                create_change.id,
                bulk_change.id,
            ]:
                break
        else:
            assert False, "No deletion change log detected"

        # Assert all old values are from update
        compare_change_logs(new_change_log, bulk_change)

        # Assert all new values are None for deletion
        for change in new_change_log.description_of_change.new:
            assert change.value == True


def test_leaf_type_change_log(host, token, project, leaf_type):
    tator_api = tator.get_api(host, token)

    num_leaves = 3
    leaf_specs = [random_leaf(project, leaf_type, None, True) for _ in range(num_leaves)]
    response = tator_api.create_leaf_list(project=project, body=leaf_specs)
    leaf_ids = response.id

    assert len(leaf_ids) == len(leaf_specs)

    # Creation tests
    create_changes = []
    for leaf_id, leaf_spec in zip(leaf_ids, leaf_specs):
        changes = tator_api.get_change_log_list(
            project=project, entity_id=leaf_id, entity_type="leaf"
        )

        # Assert one change returned
        assert len(changes) == 1
        changes = changes[0]

        # Assert all old values are None for creation
        for change in changes.description_of_change.old:
            assert change.value == None

        # Assert all new values match initial creation values
        for change in changes.description_of_change.new:
            if change.name == "_id":
                assert change.value == leaf_id
            elif change.name in ["_project", "_name", "_type"]:
                assert change.value == leaf_spec[change.name.replace("_", "")]
            elif change.name.startswith("test_"):
                assert change.value == leaf_spec['attributes'][change.name]
        create_changes.append(changes)

    patch_leaves = [random_leaf(project, leaf_type) for _ in range(num_leaves)]
    for leaf_id, patch_leaf in zip(leaf_ids, patch_leaves):
        tator_api.update_leaf(leaf_id, leaf_update=patch_leaf)

    # Update tests
    patch_changes = []
    for leaf_id, leaf, old_change_log in zip(leaf_ids, patch_leaves, create_changes):
        changes = tator_api.get_change_log_list(
            project=project, entity_id=leaf_id, entity_type="leaf"
        )

        # Assert two changes returned
        assert len(changes) == 2
        for new_change_log in changes:
            if new_change_log.id != old_change_log.id:
                break
        else:
            assert False, "No new change log detected"

        # Assert all old values are from creation
        compare_change_logs(new_change_log, old_change_log)

        # Assert all new values match initial creation values
        for change in new_change_log.description_of_change.new:
            if change.name == "_id":
                assert change.value == leaf_id
            elif change.name in ["_project", "_name", "_type"]:
                assert change.value == leaf[change.name.replace("_", "")]
            elif change.name.startswith("test_"):
                assert change.value == leaf["attributes"][change.name]
        patch_changes.append(new_change_log)

    bulk_patch = random_leaf(project, leaf_type)
    bulk_patch_spec = {"attributes": bulk_patch["attributes"]}
    tator_api.update_leaf_list(project, bulk_patch_spec)

    # Update tests
    bulk_changes = []
    for leaf_id, leaf, create_change, patch_change in zip(
        leaf_ids, patch_leaves, create_changes, patch_changes
    ):
        changes = tator_api.get_change_log_list(
            project=project, entity_id=leaf_id, entity_type="leaf"
        )

        # Assert two changes returned
        assert len(changes) == 3
        for new_change_log in changes:
            if new_change_log.id not in [patch_change.id, create_change.id]:
                break
        else:
            assert False, "No new change log detected"

        # Assert all new values match initial creation values
        for change in new_change_log.description_of_change.new:
            if change.name == "_id":
                assert change.value == leaf_id
            elif change.name in ["_project", "_name", "_type"]:
                assert change.value == bulk_patch[change.name.replace("_", "")]
            elif change.name.startswith("test_"):
                assert change.value == bulk_patch["attributes"][change.name]
        bulk_changes.append(new_change_log)

    # Clean up
    tator_api.delete_leaf(leaf_ids[0])
    tator_api.delete_leaf_list(project, leaf_id=leaf_ids[1:])

    # Deletion tests
    for leaf_id, bulk_change, patch_change, create_change in zip(
        leaf_ids, bulk_changes, patch_changes, create_changes
    ):
        changes = tator_api.get_change_log_list(
            project=project, entity_id=leaf_id, entity_type="leaf"
        )

        # Assert three changes returned
        assert len(changes) == 4
        for new_change_log in changes:
            if new_change_log.id not in [
                patch_change.id,
                create_change.id,
                bulk_change.id,
            ]:
                break
        else:
            assert False, "No deletion change log detected"

        # Assert all old values are from update
        compare_change_logs(new_change_log, bulk_change)

        # Assert all new values are None for deletion
        for change in new_change_log.description_of_change.new:
            assert change.value == True


def test_change_log_util(host, token, project, video_type):
    # Tests `tator.util.find_single_change`
    tator_api = tator.get_api(host, token)

    # Define media spec.
    num_media = 3
    fname = "MediaChangeLogTest.mp4"
    test_int = random.randint(0, 100)
    media_spec = {
        "type": video_type,
        "uid": str(uuid.uuid1()),
        "gid": str(uuid.uuid1()),
        "name": fname,
        "md5": str(uuid.uuid1())[:32],
        "section": "Test media change log",
        "attributes": {"test_int": test_int},
    }


    # Create the media.
    media_id = tator_api.create_media_list(project=project, body=media_spec).id[0]

    # Look for change that shouldn't be there
    found_change = tator.util.find_single_change(
        tator_api, project, media_id, "test_int", new_value=test_int - 1
    )
    assert found_change is None

    # Get all changes for comparison
    changes = tator_api.get_change_log_list(
        project=project, entity_id=media_id, entity_type="media"
    )
    assert len(changes) == 1

    # Look for change that should be there
    found_change = tator.util.find_single_change(
        tator_api, project, media_id, "test_int", new_value=test_int
    )
    assert found_change == changes[0]

    # Change `test_int` value (tests attribute change)
    new_test_int = random.randint(0, 100)
    tator_api.update_media(media_id, {"attributes": {"test_int": new_test_int}})

    # Get all changes for comparison
    changes = tator_api.get_change_log_list(
        project=project, entity_id=media_id, entity_type="media"
    )
    assert len(changes) == 2

    # Look for change that should be there
    found_change = tator.util.find_single_change(
        tator_api, project, media_id, "test_int", old_value=test_int, new_value=new_test_int
    )
    assert found_change is not None
    assert found_change == changes[-1]

    # Look for change that shouldn't be there
    found_change = tator.util.find_single_change(
        tator_api, project, media_id, "test_int", old_value=new_test_int, new_value=test_int
    )
    assert found_change is None

    # Look for change that shouldn't be there
    found_change = tator.util.find_single_change(
        tator_api, project, media_id, "test_int", old_value=new_test_int
    )
    assert found_change is None

    # Delete media object (tests media property change)
    tator_api.delete_media(media_id)

    # Get all changes for comparison
    changes = tator_api.get_change_log_list(
        project=project, entity_id=media_id, entity_type="media"
    )
    assert len(changes) == 3

    # Look for change that should be there
    found_change = tator.util.find_single_change(
        tator_api,
        project,
        media_id,
        "_deleted",
        old_value=False,
        new_value=True,
        find_last_change=True,
    )
    assert found_change is not None
    assert found_change in changes
