#!/usr/bin/env python3

import argparse
import logging
import os
import shutil
import sys
import traceback
from textwrap import dedent
from collections import defaultdict

import tator

logging.basicConfig(
    filename='migrate.log',
    filemode='w',
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))

def parse_args():
    parser = argparse.ArgumentParser(description=dedent('''\
    Migrates data from one project to another.

    Destination project may be on a different host. Migrations are additive; this script cannot
    delete data. The following objects will be migrated unless explicitly skipped or if the objects
    already exist:
    - Memberships (idempotent, based on matching username)
    - Sections (idempotent, based on section name)
    - Versions (idempotent, based on version name)
    - Media types (idempotent, based on media type name)
    - Localization types (idempotent, based on localization type name)
    - State types (idempotent, based on state type name)
    - Leaf types (idempotent, based on leaf type name)
    - Media (idempotent, based on section name and media name)
    - Localizations (only migrated if parent media is migrated)
    - States (only migrated if parent media is migrated)
    - Leaves (idempotent, based on path)

    If the --dest_project is not specified, a new project will be created with the name
    specified by --new_project_name or with the same name if neither are given.

    Examples:
    Duplicate a project on same host
    python3 migrate.py --host https://tatorapp.com --token asdf --project 1 --new_project_name
    'My Cloned Project'

    Migrate project settings on same host
    python3 migrate.py --host https://tatorapp.com --token asdf --project 1 --dest_project 2
    --skip_sections --skip_media

    Migrate media only to existing project
    python3 migrate.py --host https://tatorapp.com --token asdf --project 1 --dest_project 2
    --skip_localizations --skip_states

    Migrate to another host
    python3 migrate.py --host https://tatorapp.com --token asdf --project 1
    --dest_host https://other.tatorapp.com --dest_token asdf --dest_project 2
    '''), formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--host', help='Host containing source project.', required=True)
    parser.add_argument('--token', help='Token for host containing source project.', required=True)
    parser.add_argument('--project', help='Unique integer identifying project containing data to '
                                          'be migrated.', required=True, type=int)
    parser.add_argument('--dest_host', help='Host containing destination project. If not given '
                                            'the destination project is assumed to be on the same '
                                            'host as the source.')
    parser.add_argument('--dest_token', help='Token for host containing destination project. If '
                                             'not given the destination project is assumed to be '
                                             'on the same host as the source.')
    parser.add_argument('--dest_project', help='Destination project, if it already exists. '
                                               'If omitted, a new project will be created using '
                                               'either the same name or the name specified by '
                                               '--new_project_name.', type=int)
    parser.add_argument('--new_project_name', help='Name to user for new project if --dest_project '
                                                   'is omitted.', type=str)
    parser.add_argument('--sections', help='Specific sections to migrate. If not given, all media '
                                           'in the source project will be migrated.', nargs='+')
    parser.add_argument('--skip_memberships', help='If given, membership objects will not be migrated.',
                        action='store_true')
    parser.add_argument('--skip_sections', help='If given, section objects will not be migrated.',
                        action='store_true')
    parser.add_argument('--skip_versions', help='If given, version objects will not be migrated.',
                        action='store_true')
    parser.add_argument('--skip_media_types', help='If given, media types will not be migrated.',
                        action='store_true')
    parser.add_argument('--skip_localization_types', help='If given, localization types will not '
                                                          'be migrated.',
                        action='store_true')
    parser.add_argument('--skip_state_types', help='If given, state types will not be migrated.',
                        action='store_true')
    parser.add_argument('--skip_leaf_types', help='If given, leaf types will not be migrated.',
                        action='store_true')
    parser.add_argument('--skip_media', help='If given, media will not be migrated. Use this to '
                                             'only migrate a project configuration.',
                        action='store_true')
    parser.add_argument('--skip_localizations', help='If given, localizations will not be migrated.',
                        action='store_true')
    parser.add_argument('--skip_states', help='If given, states will not be migrated.',
                        action='store_true')
    parser.add_argument('--skip_leaves', help='If given, leaves will not be migrated.',
                        action='store_true')
    parser.add_argument('--include_memberships', help='If given, memberships will be migrated.',
                        action='store_true')
    return parser.parse_args()

def setup_apis(args):
    """ Sets up API objects.
    """
    # Set up API objects.
    src_api = tator.get_api(host=args.host, token=args.token)
    if (args.dest_host is not None) and (args.dest_token is not None):
        dest_api = tator.get_api(host=args.dest_host, token=args.dest_token)
        logger.info(f"Migrating to different host (to {args.dest_host} from {args.host}).")
    else:
        dest_api = src_api
        logger.info(f"Migrating to same host ({args.host}).")
    return src_api, dest_api

def find_dest_project(args, src_api, dest_api):
    """ Finds destination project if it exists.
    """
    if args.dest_project:
        dest_project = dest_api.get_project(args.dest_project)
        logger.info(f"Migrating to existing project {dest_project.name} specified by "
                     "--dest_project.")
    else:
        src_project = src_api.get_project(args.project)
        dest_projects = dest_api.get_project_list()
        dest_project = None
        for project_obj in dest_projects:
            if project_obj.name == src_project.name:
                dest_project = project_obj
                logger.info(f"Migrating to existing project with ID {project_obj.id}.")
                break
        if dest_project is None:
            name = args.new_project_name if args.new_project_name else src_project.name
            logger.info(f"New project with name {name} will be created.")
    return dest_project

def find_memberships(args, src_api, dest_api, dest_project):
    """ Finds existing memberships in destination project. Returns users and memberships
        corresponding to memberships in source project that need to be created.
    """
    memberships = []
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
            memberships = [membership for user, membership in zip(users, memberships)
                           if user.username not in existing_usernames]
            users = [user for user in users if user.username not in existing_usernames]
        logger.info(f"{len(users)} memberships will be created ({num_src - len(users)} "
                     "already exist).")
    return memberships, users

def find_sections(args, src_api, dest_api, dest_project):
    """ Finds existing sections in destination project. Returns sections in source project
        that need to be created and sections for which media should be migrated.
    """
    sections = []
    if args.skip_sections:
        logger.info(f"Skipping sections due to --skip_sections.")
    else:
        sections = src_api.get_section_list(args.project)
        num_src = len(sections)
        if args.sections:
            sections = [section for section in sections if section.name in args.sections]
        if dest_project is not None:
            existing = dest_api.get_section_list(dest_project.id)
            existing_names = [section.name for section in existing]
            sections = [section for section in sections if section.name not in existing_names]
        logger.info(f"{len(sections)} sections will be created ({num_src - len(sections)} "
                     "already exist).")
    return sections

def find_versions(args, src_api, dest_api, dest_project):
    """ Finds existing versions in destination project. Returns ID mapping between source 
        and destination versions and versions that need to be created.
    """
    versions = []
    version_mapping = {}
    if args.skip_versions:
        logger.info(f"Skipping versions due to --skip_versions.")
    else:
        versions = src_api.get_version_list(args.project)
        if dest_project is not None:
            existing = dest_api.get_version_list(dest_project.id)
            existing_names = [version.name for version in existing]
            for version in versions:
                if version.name in existing_names:
                    version_mapping[version.id] = existing[existing_names.index(version.name)].id
            versions = [version for version in versions if version.name not in existing_names]
        logger.info(f"{len(versions)} versions will be created ({len(version_mapping.values())} "
                     "already exist).")
    return versions, version_mapping

def find_media_types(args, src_api, dest_api, dest_project):
    """ Finds existing media types in destination project. Returns ID mapping between source
        and destination media types and media types that need to be created.
    """
    media_types = []
    media_type_mapping = {}
    if args.skip_media_types:
        logger.info(f"Skipping media types due to --skip_media_types.")
    else:
        media_types = src_api.get_media_type_list(args.project)
        if dest_project is not None:
            existing = dest_api.get_media_type_list(dest_project.id)
            existing_names = [media_type.name for media_type in existing]
            for media_type in media_types:
                if media_type.name in existing_names:
                    media_type_mapping[media_type.id] = existing[existing_names.index(media_type.name)].id
            media_types = [media_type for media_type in media_types if media_type.name not in existing_names]
        logger.info(f"{len(media_types)} media types will be created ({len(media_type_mapping.values())} "
                     "already exist).")
    return media_types, media_type_mapping

def find_localization_types(args, src_api, dest_api, dest_project):
    """ Finds existing localization types in destination project. Returns ID mapping between source
        and destination localization types and localization types that need to be created.
    """
    localization_types = []
    localization_type_mapping = {}
    if args.skip_localization_types:
        logger.info(f"Skipping localization types due to --skip_localization_types.")
    else:
        localization_types = src_api.get_localization_type_list(args.project)
        if dest_project is not None:
            existing = dest_api.get_localization_type_list(dest_project.id)
            existing_names = [localization_type.name for localization_type in existing]
            for localization_type in localization_types:
                if localization_type.name in existing_names:
                    existing_id = existing[existing_names.index(localization_type.name)].id
                    localization_type_mapping[localization_type.id] = existing_id
            localization_types = [localization_type for localization_type in localization_types
                                  if localization_type.name not in existing_names]
        logger.info(f"{len(localization_types)} localization types will be created "
                    f"({len(localization_type_mapping.values())} already exist).")
    return localization_types, localization_type_mapping

def find_state_types(args, src_api, dest_api, dest_project):
    """ Finds existing state types in destination project. Returns ID mapping between source
        and destination state types and state types that need to be created.
    """
    state_types = []
    state_type_mapping = {}
    if args.skip_state_types:
        logger.info(f"Skipping state types due to --skip_state_types.")
    else:
        state_types = src_api.get_state_type_list(args.project)
        if dest_project is not None:
            existing = dest_api.get_state_type_list(dest_project.id)
            existing_names = [state_type.name for state_type in existing]
            for state_type in state_types:
                if state_type.name in existing_names:
                    state_type_mapping[state_type.id] = existing[existing_names.index(state_type.name)].id
            state_types = [state_type for state_type in state_types if state_type.name not in existing_names]
        logger.info(f"{len(state_types)} state types will be created ({len(state_type_mapping.values())} "
                     "already exist).")
    return state_types, state_type_mapping

def find_leaf_types(args, src_api, dest_api, dest_project):
    """ Finds existing leaf types in destination project. Returns ID mapping between source
        and destination leaf types and leaf types that need to be created.
    """
    leaf_types = []
    leaf_type_mapping = {}
    if args.skip_leaf_types:
        logger.info(f"Skipping leaf types due to --skip_leaf_types.")
    else:
        leaf_types = src_api.get_leaf_type_list(args.project)
        if dest_project is not None:
            existing = dest_api.get_leaf_type_list(dest_project.id)
            existing_names = [leaf_type.name for leaf_type in existing]
            for leaf_type in leaf_types:
                if leaf_type.name in existing_names:
                    leaf_type_mapping[leaf_type.id] = existing[existing_names.index(leaf_type.name)].id
            leaf_types = [leaf_type for leaf_type in leaf_types if leaf_type.name not in existing_names]
        logger.info(f"{len(leaf_types)} leaf types will be created ({len(leaf_type_mapping.values())} "
                     "already exist).")
    return leaf_types, leaf_type_mapping

def find_media(args, src_api, dest_api, dest_project):
    """ Finds existing media in destination project. Returns media that need to be created.
    """
    media = []
    if args.skip_media:
        logger.info(f"Skipping media due to --skip_media.")
    else:
        if args.sections:
            sections = src_api.get_section_list(args.project)
            sections = [section for section in sections if section.name in args.sections]
            for section in sections:
                section_media = src_api.get_media_list(args.project, section=section.id)
                num_src_media = len(section_media)
                if dest_project is not None:
                    existing_section = dest_api.get_section_list(dest_project.id, name=section.name)
                    if existing_section:
                        existing = dest_api.get_media_list(dest_project.id,
                                                           section=existing_section[0].id)
                        existing_names = [m.name for m in existing]
                        section_media = [m for m in section_media if m.name not in existing_names]
                logger.info(f"{len(section_media)} media from section {section.name} will be "
                            f"created ({num_src_media - len(section_media)} already exist).")
                media += section_media
        else:
            media = src_api.get_media_list(args.project)
            num_src_media = len(media)
            if dest_project is not None:
                src_sections = src_api.get_section_list(args.project)
                dest_sections = dest_api.get_section_list(dest_project.id)
                src_section_names = {s.tator_user_sections: s.name for s in src_sections}
                dest_section_names = {s.tator_user_sections: s.name for s in dest_sections}
                src_section_names[None] = None
                dest_section_names[None] = None
                existing = dest_api.get_media_list(dest_project.id)
                existing_name_section = [
                    (m.name, dest_section_names[m.attributes.get('tator_user_sections', None)])
                    for m in existing
                ]
                media = [m for m in media
                         if (m.name, src_section_names[m.attributes.get('tator_user_sections', None)])
                         not in existing_name_section]
            logger.info(f"{len(media)} media will be created ({num_src_media - len(media)} "
                         "already exist).")
    return media

def find_localizations(args, src_api, media):
    """ Counts localizations in media that will be created.
    """
    count = 0
    if args.skip_localizations:
        logger.info("Skipping localizations due to --skip_localizations")
    else:
        for idx in range(0, len(media), 100):
            media_ids = [m.id for m in media[idx:idx+100]]
            count += src_api.get_localization_count(args.project, media_id=media_ids)
        logger.info(f"{count} localizations will be created.")
    return count

def find_states(args, src_api, media):
    """ Counts states in media that will be created.
    """
    count = 0
    if args.skip_states:
        logger.info("Skipping states due to --skip_states")
    else:
        for idx in range(0, len(media), 100):
            media_ids = [m.id for m in media[idx:idx+100]]
            count += src_api.get_state_count(args.project, media_id=media_ids)
        logger.info(f"{count} states will be created.")
    return count

def find_leaves(args, src_api, dest_api, dest_project):
    """ Finds existing leaves in destination project. Returns leaves that need to be created, 
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
        while True:
            src_leaves = src_api.get_leaf_list(args.project, depth=depth)
            if len(src_leaves) == 0:
                break
            dest_leaves = dest_api.get_leaf_list(dest_project.id, depth=depth)
            dest_paths = [leaf.path.split('.', 1)[1] for leaf in dest_leaves]
            for leaf in src_leaves:
                path = leaf.path.split('.', 1)[1]
                if path in dest_paths:
                    leaf_mapping[leaf.id] = dest_leaves[dest_paths.index(path)].id
            leaves[depth] = [leaf for leaf in src_leaves
                             if leaf.path.split('.', 1)[1] not in dest_paths]
            num_leaves += len(leaves[depth])
            num_skipped += len(src_leaves) - len(leaves[depth])
            depth += 1
        logger.info(f"{num_leaves} leaves will be created ({num_skipped} "
                     "already exist).")
    return leaves, leaf_mapping

def create_project(args, src_api, dest_api, dest_project):
    """ Creates a project if necessary. Returns the destination project ID.
    """
    if dest_project is None:
        src_project = src_api.get_project(args.project)
        name = args.new_project_name if args.new_project_name else src_project.name
        spec = {'name': name}
        if src_project.summary:
            spec['summary'] = src_project.summary
        response = dest_api.create_project(project_spec=spec)
        logger.info(f"Created new project with ID {response.id}")
        dest_project = response.id
    else:
        dest_project = dest_project.id
    return dest_project

def create_memberships(src_api, dest_api, dest_project, memberships, users):
    """ Creates memberships.
    """
    num_skipped = 0
    num_created = 0
    for membership, user in zip(memberships, users):
        # Look up user by username.
        dest_users = dest_api.get_user_list(username=user.username)
        if len(dest_users) == 0:
            num_skipped += 1
        else:
            dest_user = dest_users[0]
            spec = {'user': dest_user.id, 'permission': membership.permission}
            response = dest_api.create_membership(dest_project, membership_spec=spec)
            assert(isinstance(response, tator.models.CreateResponse))
            num_created += 1
    msg = f"Created {num_created} memberships."
    if num_skipped > 0:
        msg += f" Skipped {num_skipped} (no matching user)."
    logger.info(msg)

def create_sections(src_api, dest_api, dest_project, sections):
    """ Creates sections.
    """
    for section in sections:
        response = tator.util.clone_section(src_api, section.id, dest_project, dest_api)
        assert(isinstance(response, tator.models.CreateResponse))
    logger.info(f"Created {len(sections)} sections.")

def create_versions(src_api, dest_api, dest_project, versions, version_mapping):
    """ Creates versions. Returns updated version mapping.
    """
    for version in versions:
        response = tator.util.clone_version(src_api, version.id, dest_project, version_mapping,
                                            dest_api)
        assert(isinstance(response, tator.models.CreateResponse))
        version_mapping[version.id] = response.id
    logger.info(f"Created {len(versions)} versions.")
    return version_mapping

def create_media_types(src_api, dest_api, dest_project, media_types, media_type_mapping):
    """ Creates media types. Returns updated media type mapping.
    """
    for media_type in media_types:
        response = tator.util.clone_media_type(src_api, media_type.id, dest_project, dest_api)
        assert(isinstance(response, tator.models.CreateResponse))
        media_type_mapping[media_type.id] = response.id
    logger.info(f"Created {len(media_types)} media types.")
    return media_type_mapping

def create_localization_types(src_api, dest_api, dest_project, localization_types,
                              localization_type_mapping, media_type_mapping):
    """ Creates localization types. Returns updated localization type mapping.
    """
    for localization_type in localization_types:
        response = tator.util.clone_localization_type(src_api, localization_type.id, dest_project,
                                                      media_type_mapping, dest_api)
        assert(isinstance(response, tator.models.CreateResponse))
        localization_type_mapping[localization_type.id] = response.id
    logger.info(f"Created {len(localization_types)} localization types.")
    return localization_type_mapping

def create_state_types(src_api, dest_api, dest_project, state_types,
                       state_type_mapping, media_type_mapping):
    """ Creates state types. Returns updated state type mapping.
    """
    for state_type in state_types:
        response = tator.util.clone_state_type(src_api, state_type.id, dest_project,
                                               media_type_mapping, dest_api)
        assert(isinstance(response, tator.models.CreateResponse))
        state_type_mapping[state_type.id] = response.id
    logger.info(f"Created {len(state_types)} state types.")
    return state_type_mapping

def create_leaf_types(src_api, dest_api, dest_project, leaf_types, leaf_type_mapping):
    """ Creates leaf types. Returns updated leaf type mapping.
    """
    for leaf_type in leaf_types:
        response = tator.util.clone_leaf_type(src_api, leaf_type.id, dest_project, dest_api)
        assert(isinstance(response, tator.models.CreateResponse))
        leaf_type_mapping[leaf_type.id] = response.id
    logger.info(f"Created {len(leaf_types)} leaf types.")
    return leaf_type_mapping

def create_media(args, src_api, dest_api, dest_project, media, media_type_mapping):
    """ Creates media. Returns media mapping.
    """
    num_total = len(media)
    # Look up sections in destination project, create a dict between tator_user_sections and 
    # section name.
    sections = src_api.get_section_list(args.project)
    if args.sections:
        sections = [section for section in sections if section.name in args.sections]
    section_mapping = {s.tator_user_sections: s.name for s in sections}
    # Construct dictionary between destination type/destination section and media IDs.
    media_ids = defaultdict(list)
    for single in media:
        key = (media_type_mapping[single.meta],
               section_mapping[single.attributes.get('tator_user_sections', None)])
        media_ids[key].append(single.id)
    # Iterate through type/sections and create media.
    media_mapping = {}
    use_dest_api = None if src_api is dest_api else dest_api
    total_created = 0
    for key in media_ids:
        dest_type, dest_section = key
        for idx in range(0, len(media_ids[key]), 100): # Do batching here to manage ID query size.
            query_params = {'project': args.project,
                            'media_id': media_ids[key][idx:idx+100]}
            generator = tator.util.clone_media_list(src_api, query_params, dest_project, dest_type,
                                                    dest_section, use_dest_api)
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

def create_localizations(args, src_api, dest_api, dest_project, media, localization_count,
                         localization_type_mapping, media_mapping, version_mapping):
    """ Creates localizations. Returns localization mapping.
    """
    media_ids = [m.id for m in media]
    # Iterate through media and create localization.
    localization_mapping = {}
    total_created = 0
    for idx in range(0, len(media_ids), 100): # Do batching here to manage ID query size.
        query_params = {'project': args.project,
                        'media_id': media_ids[idx:idx+100]}
        generator = tator.util.clone_localization_list(src_api, query_params, dest_project,
                                                       version_mapping, media_mapping,
                                                       localization_type_mapping, dest_api)
        for _, _, response, id_map in generator:
            total_created += len(response.id)
            logger.info(f"Created {total_created} of {localization_count} localizations...")
            localization_mapping = {**localization_mapping, **id_map}
    logger.info(f"Created {localization_count} localizations.")
    return localization_mapping

def create_states(args, src_api, dest_api, dest_project, media, state_count,
                  state_type_mapping, media_mapping, version_mapping, localization_mapping):
    """ Creates states.
    """
    media_ids = [m.id for m in media]
    # Iterate through media and create state.
    state_mapping = {}
    total_created = 0
    for idx in range(0, len(media_ids), 100): # Do batching here to manage ID query size.
        query_params = {'project': args.project,
                        'media_id': media_ids[idx:idx+100]}
        generator = tator.util.clone_state_list(src_api, query_params, dest_project,
                                                version_mapping, media_mapping,
                                                localization_mapping, state_type_mapping, dest_api)
        for _, _, response, id_map in generator:
            total_created += len(response.id)
            logger.info(f"Created {total_created} of {state_count} states...")
            state_mapping = {**state_mapping, **id_map}
    logger.info(f"Created {state_count} states.")
    return state_mapping

def create_leaves(args, src_api, dest_api, dest_project, leaves, leaf_type_mapping, leaf_mapping):
    """ Creates leaves. Returns leaf mapping.
    """
    total_created = 0
    leaf_count = sum([len(leaf_list) for leaf_list in leaves.values()])
    for depth in leaves:
        for idx in range(0, len(leaves[depth]), 100):
            leaf_ids = [leaf.id for leaf in leaves[depth][idx:idx+100]]
            query_params = {'project': args.project,
                            'leaf_id': leaf_ids}
            generator = tator.util.clone_leaf_list(src_api, query_params, dest_project,
                                                   leaf_mapping, leaf_type_mapping, dest_api)
            for _, _, response, id_map in generator:
                total_created += len(response.id)
                logger.info(f"Created {total_created} of {leaf_count}")
                leaf_mapping = {**leaf_mapping, **id_map}
    logger.info(f"Created {leaf_count} leaves.")

if __name__ == '__main__':
    args = parse_args()
    src_api, dest_api = setup_apis(args)
    # Find which resources need to be migrated.
    dest_project = find_dest_project(args, src_api, dest_api)
    memberships, users = find_memberships(args, src_api, dest_api, dest_project)
    sections = find_sections(args, src_api, dest_api, dest_project)
    versions, version_mapping = find_versions(args, src_api, dest_api, dest_project)
    media_types, media_type_mapping = find_media_types(args, src_api, dest_api, dest_project)
    localization_types, localization_type_mapping = find_localization_types(args, src_api, dest_api,
                                                                            dest_project)
    state_types, state_type_mapping = find_state_types(args, src_api, dest_api, dest_project)
    leaf_types, leaf_type_mapping = find_leaf_types(args, src_api, dest_api, dest_project)
    media = find_media(args, src_api, dest_api, dest_project)
    localization_count = find_localizations(args, src_api, media)
    state_count = find_states(args, src_api, media)
    leaves, leaf_mapping = find_leaves(args, src_api, dest_api, dest_project)

    # Confirm migration with user.
    proceed = input("Continue with migration [y/N]? ")
    if proceed == 'y':
        # Perform migration.
        dest_project = create_project(args, src_api, dest_api, dest_project)
        create_memberships(src_api, dest_api, dest_project, memberships, users)
        create_sections(src_api, dest_api, dest_project, sections)
        version_mapping = create_versions(src_api, dest_api, dest_project, versions,
                                          version_mapping)
        media_type_mapping = create_media_types(src_api, dest_api, dest_project, media_types,
                                                media_type_mapping)
        localization_type_mapping = create_localization_types(src_api, dest_api, dest_project,
                                                              localization_types,
                                                              localization_type_mapping,
                                                              media_type_mapping)
        state_type_mapping = create_state_types(src_api, dest_api, dest_project, state_types,
                                                state_type_mapping, media_type_mapping)
        leaf_type_mapping = create_leaf_types(src_api, dest_api, dest_project, leaf_types,
                                              leaf_type_mapping)
        media_mapping = create_media(args, src_api, dest_api, dest_project, media,
                                     media_type_mapping)
        localization_mapping = create_localizations(args, src_api, dest_api, dest_project, media,
                                                    localization_count, localization_type_mapping,
                                                    media_mapping, version_mapping)
        create_states(args, src_api, dest_api, dest_project, media,
                      state_count, state_type_mapping,
                      media_mapping, version_mapping, localization_mapping)
        create_leaves(args, src_api, dest_api, dest_project, leaves, leaf_type_mapping,
                      leaf_mapping)
    else:
        logger.info("Migration cancelled by user.")
    
