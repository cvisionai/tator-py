#!/usr/bin/env python3

import logging
import sys
from collections import defaultdict

import tator

logging.basicConfig(
    filename="migrate.log",
    filemode="w",
    format="%(asctime)s %(levelname)s:%(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))


def get_tator_user_sections(media):
    tator_user_sections = None
    if media.attributes:
        tator_user_sections = media.attributes.get("tator_user_sections", None)
    return tator_user_sections


def setup_apis(args, migration_config):
    """Sets up API objects."""
    # Set up API objects.
    migration_config["src_api"] = tator.get_api(host=args.host, token=args.token)
    if (args.dest_host is not None) and (args.dest_token is not None):
        migration_config["dest_api"] = tator.get_api(host=args.dest_host, token=args.dest_token)
        logger.info(f"Migrating to different host (to {args.dest_host} from {args.host}).")
    else:
        migration_config["dest_api"] = migration_config["src_api"]
        logger.info(f"Migrating to same host ({args.host}).")


def find_dest_project(args, migration_config):
    """Finds destination project if it exists."""
    dest_project = None
    dest_api = migration_config["dest_api"]
    if args.dest_project:
        dest_project = dest_api.get_project(args.dest_project)
        logger.info(
            f"Migrating to existing project {dest_project.name} specified by --dest_project."
        )
    else:
        src_project = migration_config["src_api"].get_project(args.project)
        dest_projects = dest_api.get_project_list()
        name = args.new_project_name if args.new_project_name else src_project.name
        for project_obj in dest_projects:
            if project_obj.name == name:
                dest_project = project_obj
                logger.info(f"Migrating to existing project with ID {project_obj.id}.")
                break
        if dest_project is None:
            logger.info(f"New project with name {name} will be created.")
    migration_config["dest_project"] = dest_project


def find_memberships(args, migration_config):
    """Finds existing memberships in destination project. Returns users and memberships
    corresponding to memberships in source project that need to be created.
    """
    memberships = []
    users = []
    if args.skip_memberships:
        logger.info(f"Skipping memberships due to --skip_memberships.")
    else:
        memberships = src_api.get_membership_list(args.project)
        users = [src_api.get_user(membership.user) for membership in memberships]
        num_src = len(memberships)
        if dest_project is not None:
            existing = dest_api.get_membership_list(dest_project.id)
            existing_users = [dest_api.get_user(membership.user) for membership in existing]
            existing_usernames = [user.username for user in existing_users]
            memberships = [
                membership
                for user, membership in zip(users, memberships)
                if user.username not in existing_usernames
            ]
            users = [user for user in users if user.username not in existing_usernames]
        logger.info(
            f"{len(users)} memberships will be created ({num_src - len(users)} " "already exist)."
        )

    migration_config["memberships"] = memberships
    migration_config["users"] = users


def find_sections(args, migration_config):
    """Finds existing sections in destination project. Returns sections in source project
    that need to be created and sections for which media should be migrated.
    """
    sections = []
    if args.skip_sections:
        logger.info(f"Skipping sections due to --skip_sections.")
    else:
        dest_project = migration_config["dest_project"]
        sections = src_api.get_section_list(args.project)
        num_src = len(sections)
        if args.sections:
            sections = [section for section in sections if section.name in args.sections]
        if dest_project is not None:
            existing = dest_api.get_section_list(dest_project.id)
            existing_names = [section.name for section in existing]
            sections = [section for section in sections if section.name not in existing_names]
        logger.info(
            f"{len(sections)} sections will be created ({num_src - len(sections)} "
            "already exist)."
        )
    migration_config["sections"] = sections


def find_versions(args, migration_config):
    """Finds existing versions in destination project. Returns ID mapping between source
    and destination versions and versions that need to be created.
    """
    versions = []
    version_mapping = {}
    if args.skip_versions:
        logger.info(f"Skipping versions due to --skip_versions.")
    else:
        versions = migration_config["src_api"].get_version_list(args.project)
        dest_project = migration_config["dest_project"]
        if dest_project is not None:
            existing = migration_config["dest_api"].get_version_list(dest_project.id)
            existing_names = [version.name for version in existing]
            version_mapping = {
                version.id: existing[existing_names.index(version.name)].id
                for version in versions
                if version.name in existing_names
            }
            # for version in versions:
            #     if version.name in existing_names:
            #         version_mapping[version.id] = existing[existing_names.index(version.name)].id
            versions = [version for version in versions if version.name not in existing_names]
        logger.info(
            f"{len(versions)} versions will be created ({len(version_mapping.values())} "
            "already exist)."
        )
    migration_config["versions"] = versions
    migration_config["version_mapping"] = version_mapping


def find_media_types(args, migration_config):
    """Finds existing media types in destination project. Returns ID mapping between source
    and destination media types and media types that need to be created.
    """
    media_types = []
    media_type_mapping = {}
    if args.skip_media_types:
        logger.info(f"Skipping media types due to --skip_media_types.")
    else:
        media_types = migration_config["src_api"].get_media_type_list(args.project)
        dest_project = migration_config["dest_project"]
        if dest_project is not None:
            existing = migration_config["dest_api"].get_media_type_list(dest_project.id)
            existing_names = [media_type.name for media_type in existing]
            media_type_mapping = {
                media_type.id: existing[existing_names.index(media_type.name)].id
                for media_type in media_types
                if media_type.name in existing_names
            }
            # for media_type in media_types:
            #     if media_type.name in existing_names:
            #         media_type_mapping[media_type.id] = existing[
            #             existing_names.index(media_type.name)
            #         ].id
            media_types = [
                media_type for media_type in media_types if media_type.name not in existing_names
            ]
        logger.info(
            f"{len(media_types)} media types will be created ({len(media_type_mapping.values())} "
            "already exist)."
        )
    migration_config["media_types"] = media_types
    migration_config["media_type_mapping"] = media_type_mapping


def find_localization_types(args, migration_config):
    """Finds existing localization types in destination project. Returns ID mapping between source
    and destination localization types and localization types that need to be created.
    """
    localization_types = []
    localization_type_mapping = {}
    if args.skip_localization_types:
        logger.info(f"Skipping localization types due to --skip_localization_types.")
    else:
        localization_types = migration_config["src_api"].get_localization_type_list(args.project)
        dest_project = migration_config["dest_project"]
        if dest_project is not None:
            existing = migration_config["dest_api"].get_localization_type_list(dest_project.id)
            existing_names = [localization_type.name for localization_type in existing]
            localization_type_mapping = {
                localization_type.id: existing[existing_names.index(localization_type.name)].id
                for localization_type in localization_types
                if localization_type.name in existing_names
            }
            # for localization_type in localization_types:
            #     if localization_type.name in existing_names:
            #         existing_id = existing[existing_names.index(localization_type.name)].id
            #         localization_type_mapping[localization_type.id] = existing_id
            localization_types = [
                localization_type
                for localization_type in localization_types
                if localization_type.name not in existing_names
            ]
        logger.info(
            f"{len(localization_types)} localization types will be created "
            f"({len(localization_type_mapping.values())} already exist)."
        )
    migration_config["localization_types"] = localization_types
    migration_config["localization_type_mapping"] = localization_type_mapping


def find_state_types(args, migration_config):
    """Finds existing state types in destination project. Returns ID mapping between source
    and destination state types and state types that need to be created.
    """
    state_types = []
    state_type_mapping = {}
    if args.skip_state_types:
        logger.info(f"Skipping state types due to --skip_state_types.")
    else:
        state_types = migration_config["src_api"].get_state_type_list(args.project)
        dest_project = migration_config["dest_project"]
        if dest_project is not None:
            existing = migration_config["dest_api"].get_state_type_list(dest_project.id)
            existing_names = [state_type.name for state_type in existing]
            state_type_mapping = {
                state_type.id: existing[existing_names.index(state_type.name)].id
                for state_type in state_types
                if state_type.name in existing_names
            }
            # for state_type in state_types:
            #     if state_type.name in existing_names:
            #         state_type_mapping[state_type.id] = existing[
            #             existing_names.index(state_type.name)
            #         ].id
            state_types = [
                state_type for state_type in state_types if state_type.name not in existing_names
            ]
        logger.info(
            f"{len(state_types)} state types will be created ({len(state_type_mapping.values())} "
            "already exist)."
        )
    migration_config["state_types"] = state_types
    migration_config["state_type_mapping"] = state_type_mapping


def find_leaf_types(args, migration_config):
    """Finds existing leaf types in destination project. Returns ID mapping between source
    and destination leaf types and leaf types that need to be created.
    """
    leaf_types = []
    leaf_type_mapping = {}
    if args.skip_leaf_types:
        logger.info(f"Skipping leaf types due to --skip_leaf_types.")
    else:
        leaf_types = migration_config["src_api"].get_leaf_type_list(args.project)
        dest_project = migration_config["dest_project"]
        if dest_project is not None:
            existing = migration_config["dest_api"].get_leaf_type_list(dest_project.id)
            existing_names = [leaf_type.name for leaf_type in existing]
            leaf_type_mapping = {
                leaf_type.id: existing[existing_names.index(leaf_type.name)].id
                for leaf_type in leaf_types
                if leaf_type.name in existing_names
            }
            # for leaf_type in leaf_types:
            #     if leaf_type.name in existing_names:
            #         leaf_type_mapping[leaf_type.id] = existing[
            #             existing_names.index(leaf_type.name)
            #         ].id
            leaf_types = [
                leaf_type for leaf_type in leaf_types if leaf_type.name not in existing_names
            ]
        logger.info(
            f"{len(leaf_types)} leaf types will be created ({len(leaf_type_mapping.values())} "
            "already exist)."
        )
    migration_config["leaf_types"] = leaf_types
    migration_config["leaf_type_mapping"] = leaf_type_mapping


def find_media(args, migration_config):
    """Finds existing media in destination project. Returns media that need to be created and ID
    mapping between source and destination medias.
    """
    media = []
    media_mapping = {}
    if args.skip_media:
        logger.info(f"Skipping media due to --skip_media.")
    else:
        # Set up media paginators
        src_api = migration_config["src_api"]
        src_media_paginator = tator.util.get_paginator(src_api, "get_media_list")
        dest_project = migration_config["dest_project"]
        if dest_project is not None:
            dest_api = migration_config["dest_api"]
            dest_media_paginator = tator.utilPaginator.get_paginator(dest_api, "get_media_list")

        if args.sections:
            sections = src_api.get_section_list(args.project)
            sections = [section for section in sections if section.name in args.sections]
            for section in sections:
                page_iter = src_media_paginator.paginate(project=args.project, section=section.id)
                section_media = [m for page in page_iter for m in page]
                num_src_media = len(section_media)
                if dest_project is not None:
                    existing_section = dest_api.get_section_list(dest_project.id, name=section.name)
                    if existing_section:
                        page_iter = dest_media_paginator.paginate(
                            project=dest_project.id, section=existing_section[0].id
                        )
                        existing = [m for page in page_iter for m in page]
                        existing_names = [m.name for m in existing]
                        for m in section_media:
                            if m.name in existing_names:
                                media_mapping[m.id] = existing[existing_names.index(m.name)].id
                        section_media = [m for m in section_media if m.name not in existing_names]
                logger.info(
                    f"{len(section_media)} media from section {section.name} will be "
                    f"created ({num_src_media - len(section_media)} already exist)."
                )
                media += section_media
        else:
            page_iter = src_media_paginator.paginate(project=args.project)
            media = [m for page in page_iter for m in page]
            num_src_media = len(media)
            if dest_project is not None:
                src_sections = src_api.get_section_list(args.project)
                dest_sections = dest_api.get_section_list(dest_project.id)
                src_section_names = {s.tator_user_sections: s.name for s in src_sections}
                dest_section_names = {s.tator_user_sections: s.name for s in dest_sections}
                page_iter = dest_media_paginator.paginate(project=dest_project.id)
                existing = [m for page in page_iter for m in page]
                existing_name_section = [
                    (m.name, dest_section_names.get(get_tator_user_sections(m))) for m in existing
                ]
                for m in media:
                    key = (m.name, src_section_names.get(get_tator_user_sections(m)))
                    if key in existing_name_section:
                        media_mapping[m.id] = existing[existing_name_section.index(key)].id
                media = [
                    m
                    for m in media
                    if (m.name, src_section_names[get_tator_user_sections(m)])
                    not in existing_name_section
                ]
            logger.info(
                f"{len(media)} media will be created ({num_src_media - len(media)} "
                "already exist)."
            )
    migration_config["media"] = media
    migration_config["media_mapping"] = media_mapping


def _is_num(x):
    return isinstance(x, float) or isinstance(x, int)


def _same_localization(a, b, localization_type_mapping, version_mapping):
    """Returns true if two localizations have nearly identical geometry.
    a is a source localization, b is a dest localization
    """
    ok = localization_type_mapping.get(a.type) == b.type
    ok = ok and version_mapping.get(a.version) == b.version
    ok = ok and a.frame == b.frame
    for key in a.attributes:
        attr_a = a.attributes.get(key)
        attr_b = b.attributes.get(key)
        if attr_a is None or attr_b is None:
            # It is possible for an attribute to be present that is not carried
            # over to a clone if that attribute been deleted from the type since
            # it was defined.
            continue
        if _is_num(attr_a) and _is_num(attr_b):
            ok = ok and abs(attr_a - attr_b) < 0.01
        else:
            ok = ok and a.attributes.get(key) == b.attributes.get(key)
    if a.x and b.x:
        ok = ok and abs(a.x - b.x) < 0.01
    if a.y and b.y:
        ok = ok and abs(a.y - b.y) < 0.01
    if a.width and b.width:
        ok = ok and abs(a.width - b.width) < 0.01
    if a.height and b.height:
        ok = ok and abs(a.height - b.height) < 0.01
    if a.u and b.u:
        ok = ok and abs(a.u - b.u) < 0.01
    if a.v and b.v:
        ok = ok and abs(a.v - b.v) < 0.01
    return ok


def find_localizations(args, migration_config):
    """Finds existing localizations in destination project. Returns localizations that need to
    be created and ID mapping between source and destination medias.
    """
    count = 0
    localization_media_ids = []
    if args.skip_localizations:
        logger.info("Skipping localizations due to --skip_localizations")
        localizations = []
        localization_mapping = {}
    else:
        # Get existing localizations.
        media_mapping = migration_config["media_mapping"]
        dest_media_ids = list(media_mapping.values())
        existing_loc = []
        print("Retrieving existing localizations...")
        for idx in range(0, len(dest_media_ids), 100):
            # TODO paginate?
            existing_loc += migration_config["dest_api"].get_localization_list(
                dest_project.id, media_id=dest_media_ids[idx : idx + 100]
            )
        # Get all source localizations.
        src_api = migration_config["src_api"]
        media = migration_config["media"]
        src_media_ids = list(media_mapping.keys())
        source_loc = []
        print("Retrieving source localizations...")
        for idx in range(0, len(media), 100):
            # TODO paginate?
            source_loc += src_api.get_localization_list(
                args.project, media_id=[m.id for m in media[idx : idx + 100]]
            )
        for idx in range(0, len(src_media_ids), 100):
            # TODO paginate?
            source_loc += src_api.get_localization_list(
                args.project, media_id=src_media_ids[idx : idx + 100]
            )
        # Group source and dest localizations by source media ID and frame number.
        print("Building lookups by media/frame...")
        reverse_media = {v: k for k, v in media_mapping.items()}
        existing_grouped = defaultdict(list)
        source_grouped = defaultdict(list)
        for loc in existing_loc:
            existing_grouped[(reverse_media[loc.media], loc.frame)].append(loc)
        for loc in source_loc:
            source_grouped[(loc.media, loc.frame)].append(loc)
        # Add localizations to mapping or create list depending on geometry match.
        localizations = []
        localization_mapping = {}
        for key, locs in source_grouped.items():
            for src_loc in locs:
                found = False
                for dest_loc in existing_grouped[key]:
                    same = _same_localization(
                        src_loc,
                        dest_loc,
                        migration_config["localization_type_mapping"],
                        migration_config["version_mapping"],
                    )
                    if same:
                        found = True
                        localization_mapping[src_loc.id] = dest_loc.id
                if not found:
                    print(
                        f"NOT FOUND: SRC ID {src_loc.id}, DEST IDS {[loc.id for loc in existing_grouped[key]]}"
                    )
                    raise RuntimeError("Shouldn't be missing any...")
                    localizations.append(src_loc)
        logger.info(
            f"{len(localizations)} localizations will be created ({len(localization_mapping.keys())} "
            "already exist)."
        )
    migration_config["localizations"] = localizations
    migration_config["localization_mapping"] = localization_mapping


def _same_state(a, b, state_type_mapping, version_mapping):
    """Returns true if two states have same version and type."""
    ok = state_type_mapping.get(a.type) == b.type
    ok = ok and version_mapping.get(a.version) == b.version
    ok = ok and a.frame == b.frame
    for key in a.attributes:
        attr_a = a.attributes.get(key)
        attr_b = b.attributes.get(key)
        if _is_num(attr_a) and _is_num(attr_b):
            ok = ok and abs(attr_a - attr_b) < 0.01
        else:
            ok = ok and a.attributes.get(key) == b.attributes.get(key)
    return ok


def find_states(args, migration_config):
    """Finds existing states in destination project. Returns"""
    count = 0
    state_media_ids = []
    if args.skip_states:
        logger.info("Skipping states due to --skip_states")
        states = []
        state_mapping = {}
    else:
        # Get existing states.
        media_mapping = migration_config["media_mapping"]
        dest_media_ids = list(media_mapping.values())
        existing_states = []
        print("Retrieving existing states...")
        for idx in range(0, len(dest_media_ids), 100):
            existing_states += migration_config["dest_api"].get_state_list(
                dest_project.id, media_id=dest_media_ids[idx : idx + 100]
            )
        # Get all source states.
        src_api = migration_config["src_api"]
        src_media_ids = list(media_mapping.keys())
        source_states = []
        print("Retrieving source states...")
        for idx in range(0, len(media), 100):
            # TODO paginate?
            source_states += src_api.get_state_list(
                args.project, media_id=[m.id for m in media[idx : idx + 100]]
            )
        for idx in range(0, len(src_media_ids), 100):
            # TODO paginate?
            source_states += src_api.get_state_list(
                args.project, media_id=src_media_ids[idx : idx + 100]
            )
        # Group source and dest states by source media ID and frame number.
        print("Building lookups by media/frame...")
        reverse_media = {v: k for k, v in media_mapping.items()}
        existing_grouped = defaultdict(list)
        source_grouped = defaultdict(list)
        for state in existing_states:
            existing_grouped[(reverse_media[state.media[0]], state.frame)].append(state)
        for state in source_states:
            source_grouped[(state.media[0], state.frame)].append(state)
        # Add states to mapping or create list depending on geometry match.
        states = []
        state_mapping = {}
        for key, state_list in source_grouped.items():
            for src_state in state_list:
                found = False
                for dest_state in existing_grouped[key]:
                    same = _same_state(
                        src_state,
                        dest_state,
                        migration_config["state_type_mapping"],
                        migration_config["version_mapping"],
                    )
                    if same:
                        found = True
                        state_mapping[src_state.id] = dest_state.id
                if not found:
                    states.append(src_state)
        logger.info(
            f"{len(states)} states will be created ({len(state_mapping.keys())} " "already exist)."
        )
    migration_config["states"] = states
    migration_config["state_mapping"] = state_mapping


def find_leaves(args, migration_config):
    """Finds existing leaves in destination project. Returns leaves that need to be created,
    grouped in a dictionary by depth and mapping of src and dest leaves for existing
    leaves.
    """
    leaves = {}
    leaf_mapping = {}
    num_leaves = 0
    num_skipped = 0
    if args.skip_leaves:
        logger.info("Skipping leaves due to --skip_leaves")
    else:
        depth = 0
        src_api = migration_config["src_api"]
        dest_project = migration_config["dest_project"]
        if dest_project:
            dest_api = migration_config["dest_api"]
        while True:
            src_leaves = src_api.get_leaf_list(args.project, depth=depth)
            if len(src_leaves) == 0:
                break
            if dest_project:
                dest_leaves = dest_api.get_leaf_list(dest_project.id, depth=depth)
                dest_paths = [leaf.path[1] for leaf in dest_leaves]
                for leaf in src_leaves:
                    path = leaf.path[1]
                    if path in dest_paths:
                        leaf_mapping[leaf.id] = dest_leaves[dest_paths.index(path)].id
                leaves[depth] = [leaf for leaf in src_leaves if leaf.path[1] not in dest_paths]
            else:
                leaves[depth] = list(src_leaves)
            num_leaves += len(leaves[depth])
            num_skipped += len(src_leaves) - len(leaves[depth])
            depth += 1
        logger.info(f"{num_leaves} leaves will be created ({num_skipped} " "already exist).")
    leaves = migration_config["leaves"]
    leaf_mapping = migration_config["leaf_mapping"]


def create_project(args, src_api, dest_api, dest_project):
    """Creates a project if necessary. Returns the destination project ID."""
    if dest_project is None:
        src_project = src_api.get_project(args.project)
        name = args.new_project_name if args.new_project_name else src_project.name
        spec = {"name": name, "organization": args.dest_organization}
        if src_project.summary:
            spec["summary"] = src_project.summary
        response = dest_api.create_project(project_spec=spec)
        logger.info(f"Created new project with ID {response.id}")
        dest_project = response.id
    else:
        dest_project = dest_project.id
    return dest_project


def create_memberships(src_api, dest_api, dest_project, memberships, users):
    """Creates memberships."""
    num_skipped = 0
    num_created = 0
    for membership, user in zip(memberships, users):
        # Look up user by username.
        dest_users = dest_api.get_user_list(username=user.username)
        if len(dest_users) == 0:
            num_skipped += 1
        else:
            dest_user = dest_users[0]
            spec = {"user": dest_user.id, "permission": membership.permission}
            response = dest_api.create_membership(dest_project, membership_spec=spec)
            assert isinstance(response, tator.models.CreateResponse)
            num_created += 1
    msg = f"Created {num_created} memberships."
    if num_skipped > 0:
        msg += f" Skipped {num_skipped} (no matching user)."
    logger.info(msg)


def create_sections(src_api, dest_api, dest_project, sections):
    """Creates sections."""
    for section in sections:
        response = tator.util.clone_section(src_api, section.id, dest_project, dest_api)
        assert isinstance(response, tator.models.CreateResponse)
    logger.info(f"Created {len(sections)} sections.")


def create_versions(src_api, dest_api, dest_project, versions, version_mapping):
    """Creates versions. Returns updated version mapping."""
    for version in versions:
        response = tator.util.clone_version(
            src_api, version.id, dest_project, version_mapping, dest_api
        )
        assert isinstance(response, tator.models.CreateResponse)
        version_mapping[version.id] = response.id
    logger.info(f"Created {len(versions)} versions.")
    return version_mapping


def create_media_types(src_api, dest_api, dest_project, media_types, media_type_mapping):
    """Creates media types. Returns updated media type mapping."""
    for media_type in media_types:
        response = tator.util.clone_media_type(src_api, media_type.id, dest_project, dest_api)
        assert isinstance(response, tator.models.CreateResponse)
        media_type_mapping[media_type.id] = response.id
    logger.info(f"Created {len(media_types)} media types.")
    return media_type_mapping


def create_localization_types(
    src_api,
    dest_api,
    dest_project,
    localization_types,
    localization_type_mapping,
    media_type_mapping,
):
    """Creates localization types. Returns updated localization type mapping."""
    for localization_type in localization_types:
        response = tator.util.clone_localization_type(
            src_api, localization_type.id, dest_project, media_type_mapping, dest_api
        )
        assert isinstance(response, tator.models.CreateResponse)
        localization_type_mapping[localization_type.id] = response.id
    logger.info(f"Created {len(localization_types)} localization types.")
    return localization_type_mapping


def create_state_types(
    src_api, dest_api, dest_project, state_types, state_type_mapping, media_type_mapping
):
    """Creates state types. Returns updated state type mapping."""
    for state_type in state_types:
        response = tator.util.clone_state_type(
            src_api, state_type.id, dest_project, media_type_mapping, dest_api
        )
        assert isinstance(response, tator.models.CreateResponse)
        state_type_mapping[state_type.id] = response.id
    logger.info(f"Created {len(state_types)} state types.")
    return state_type_mapping


def create_leaf_types(src_api, dest_api, dest_project, leaf_types, leaf_type_mapping):
    """Creates leaf types. Returns updated leaf type mapping."""
    for leaf_type in leaf_types:
        response = tator.util.clone_leaf_type(src_api, leaf_type.id, dest_project, dest_api)
        assert isinstance(response, tator.models.CreateResponse)
        leaf_type_mapping[leaf_type.id] = response.id
    logger.info(f"Created {len(leaf_types)} leaf types.")
    return leaf_type_mapping


def create_media(
    args,
    src_api,
    dest_api,
    dest_project,
    media,
    media_type_mapping,
    media_mapping,
    ignore_media_transfer,
):
    """Creates media. Returns media mapping."""
    num_total = len(media)
    # Look up sections in destination project, create a dict between tator_user_sections and
    # section name.
    sections = src_api.get_section_list(args.project)
    if args.sections:
        sections = [section for section in sections if section.name in args.sections]
    section_mapping = {s.tator_user_sections: s.name for s in sections}
    section_mapping[None] = None
    # Construct dictionary between destination type/destination section and media IDs.
    media_ids = defaultdict(list)
    for single in media:
        key = (media_type_mapping[single.type], section_mapping[get_tator_user_sections(single)])
        media_ids[key].append(single.id)
    # Sort keys so that multi are created after images/videos.
    sorter = lambda mtype: 1 if dest_api.get_media_type(mtype[0]).dtype == "multi" else 0
    keys = list(media_ids.keys())
    keys.sort(key=sorter)
    # Iterate through type/sections and create media.
    use_dest_api = None if src_api is dest_api else dest_api
    total_created = 0
    for key in keys:
        dest_type, dest_section = key
        for idx in range(0, len(media_ids[key]), 100):  # Do batching here to manage ID query size.
            query_params = {"project": args.project, "media_id": media_ids[key][idx : idx + 100]}
            generator = tator.util.clone_media_list(
                src_api,
                query_params,
                dest_project,
                media_mapping,
                dest_type,
                dest_section,
                use_dest_api,
                ignore_media_transfer,
            )
            for _, _, response, id_map in generator:
                if isinstance(response, tator.models.CreateResponse):
                    total_created += 1
                elif isinstance(response, tator.models.CreateListResponse):
                    total_created += len(response.id)
                else:
                    raise ValueError("Error cloning media!")
                logger.info(f"Created {total_created} of {num_total} files...")
                media_mapping = {**media_mapping, **id_map}
    logger.info(f"Created {num_total} media.")
    return media_mapping


def create_localizations(
    args,
    src_api,
    dest_api,
    dest_project,
    localizations,
    localization_type_mapping,
    localization_mapping,
    media_mapping,
    version_mapping,
):
    """Creates localizations. Returns localization mapping."""
    # Iterate through media and create localization.
    total_created = 0
    for idx in range(0, len(localizations), 100):  # Do batching here to manage ID query size.
        query_params = {
            "project": args.project,
            "localization_id_query": {"ids": [loc.id for loc in localizations[idx : idx + 100]]},
        }
        generator = tator.util.clone_localization_list(
            src_api,
            query_params,
            dest_project,
            version_mapping,
            media_mapping,
            localization_type_mapping,
            dest_api,
        )
        for _, _, response, id_map in generator:
            total_created += len(response.id)
            logger.info(f"Created {total_created} of {len(localizations)} localizations...")
            localization_mapping = {**localization_mapping, **id_map}
    logger.info(f"Created {total_created} localizations.")
    return localization_mapping


def create_states(
    args,
    src_api,
    dest_api,
    dest_project,
    states,
    state_type_mapping,
    state_mapping,
    media_mapping,
    version_mapping,
    localization_mapping,
):
    """Creates states."""
    # Iterate through media and create state.
    total_created = 0
    for idx in range(0, len(states), 100):  # Do batching here to manage ID query size.
        query_params = {
            "project": args.project,
            "state_id_query": {"ids": [state.id for state in states[idx : idx + 100]]},
        }
        generator = tator.util.clone_state_list(
            src_api,
            query_params,
            dest_project,
            version_mapping,
            media_mapping,
            localization_mapping,
            state_type_mapping,
            dest_api,
        )
        for _, _, response, id_map in generator:
            total_created += len(response.id)
            logger.info(f"Created {total_created} of {len(states)} states...")
            state_mapping = {**state_mapping, **id_map}
    logger.info(f"Created {total_created} states.")
    return state_mapping


def create_leaves(args, src_api, dest_api, dest_project, leaves, leaf_type_mapping, leaf_mapping):
    """Creates leaves. Returns leaf mapping."""
    total_created = 0
    leaf_count = sum([len(leaf_list) for leaf_list in leaves.values()])
    for depth in leaves:
        for idx in range(0, len(leaves[depth]), 100):
            leaf_ids = [leaf.id for leaf in leaves[depth][idx : idx + 100]]
            query_params = {"project": args.project, "leaf_id": leaf_ids}
            generator = tator.util.clone_leaf_list(
                src_api, query_params, dest_project, leaf_mapping, leaf_type_mapping, dest_api
            )
            for _, _, response, id_map in generator:
                total_created += len(response.id)
                logger.info(f"Created {total_created} of {leaf_count}")
                leaf_mapping = {**leaf_mapping, **id_map}
    logger.info(f"Created {leaf_count} leaves.")


def get_migration_config(args):

    migration_config = {}
    setup_apis(args, migration_config)
    # Find which resources need to be migrated.
    find_dest_project(args, migration_config)
    find_memberships(args, migration_config)
    find_sections(args, migration_config)
    find_versions(args, migration_config)
    find_media_types(args, migration_config)
    find_localization_types(args, migration_config)
    find_state_types(args, migration_config)
    find_leaf_types(args, migration_config)
    find_media(args, migration_config)
    find_localizations(args, migration_config)
    find_states(args, migration_config)
    find_leaves(args, migration_config)
    migration_config["ignore_media_transfer"] = True if args.ignore_media_transfer else False
    if migration_config["ignore_media_transfer"]:
        logger.info("Will not transfer media_files")
    return migration_config


def perform_migration(
    args,
    src_api,
    dest_api,
    dest_project,
    memberships,
    users,
    sections,
    versions,
    version_mapping,
    media_types,
    media_type_mapping,
    localization_types,
    localization_type_mapping,
    state_types,
    state_type_mapping,
    leaf_types,
    leaf_type_mapping,
    media,
    media_mapping,
    ignore_media_transfer,
    localizations,
    localization_mapping,
    states,
    state_mapping,
    leaves,
    leaf_mapping,
):
    dest_project = create_project(args, src_api, dest_api, dest_project)
    create_memberships(src_api, dest_api, dest_project, memberships, users)
    create_sections(src_api, dest_api, dest_project, sections)
    version_mapping = create_versions(src_api, dest_api, dest_project, versions, version_mapping)
    media_type_mapping = create_media_types(
        src_api, dest_api, dest_project, media_types, media_type_mapping
    )
    localization_type_mapping = create_localization_types(
        src_api,
        dest_api,
        dest_project,
        localization_types,
        localization_type_mapping,
        media_type_mapping,
    )
    state_type_mapping = create_state_types(
        src_api, dest_api, dest_project, state_types, state_type_mapping, media_type_mapping
    )
    leaf_type_mapping = create_leaf_types(
        src_api, dest_api, dest_project, leaf_types, leaf_type_mapping
    )
    media_mapping = create_media(
        args,
        src_api,
        dest_api,
        dest_project,
        media,
        media_type_mapping,
        media_mapping,
        ignore_media_transfer,
    )
    localization_mapping = create_localizations(
        args,
        src_api,
        dest_api,
        dest_project,
        localizations,
        localization_type_mapping,
        localization_mapping,
        media_mapping,
        version_mapping,
    )
    create_states(
        args,
        src_api,
        dest_api,
        dest_project,
        states,
        state_type_mapping,
        state_mapping,
        media_mapping,
        version_mapping,
        localization_mapping,
    )
    create_leaves(args, src_api, dest_api, dest_project, leaves, leaf_type_mapping, leaf_mapping)
