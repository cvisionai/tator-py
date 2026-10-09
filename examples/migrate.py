#!/usr/bin/env python3

import argparse
import copy
from functools import wraps
import logging
import os
import shutil
import sys
import traceback
from textwrap import dedent
from collections import defaultdict

import tator
from migrate_acl import ACLMigration, add_acl_arguments

logging.basicConfig(
    filename='migrate.log',
    filemode='w',
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO)
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
logger.addHandler(console_handler)
logging.getLogger('migrate_acl').addHandler(console_handler)
logging.getLogger('migrate_acl').setLevel(logging.DEBUG)

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
    - File types (idempoent, based on file type name)
    - Media (idempotent, based on section name and media name)
    - Localizations (only migrated if destination media has no localizations)
    - States (only migrated if destination media has no states)
    - Leaves (idempotent, based on path)

    If the --dest_project is not specified, a new project will be created with the name
    specified by --new_project_name or with the same name if neither are given.

    By default, organizations/groups and their memberships are selected from the
    migrated resources' row protections. Existing objects are mapped even when creation is
    skipped. Users are never created. Use --skip_user_row_protections to omit direct user
    grants, and --map_organization/--map_group SOURCE_ID:DEST_ID for renamed dependencies.
    --dest_organization maps the source project owner regardless of its name.

    Examples:
    Duplicate a project on same host
    python3 migrate.py --host https://cloud.tator.io --token asdf --project 1 --new_project_name
    'My Cloned Project'

    Migrate project settings on same host
    python3 migrate.py --host https://cloud.tator.io --token asdf --project 1 --dest_project 2
    --skip_sections --skip_media

    Migrate media only to existing project
    python3 migrate.py --host https://cloud.tator.io --token asdf --project 1 --dest_project 2
    --skip_localizations --skip_states

    Migrate to another host
    python3 migrate.py --host https://cloud.tator.io --token asdf --project 1
    --dest_host https://other.tator.io --dest_token asdf --dest_project 2
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
    parser.add_argument('--dest_organization', help='Destination organization for a new project. '
                                                    'Unless --skip_acl is set, maps the source owner regardless of name; '
                                                    'if omitted, the owner is matched or created.', type=int)
    parser.add_argument('--section_ids', help='IDs of Specific sections to migrate. If not given, all media '
                                           'in the source project will be migrated. If the sections identified in this list are nested, parent and child sections will also be migrated and the folder structure will be preserved in the destination project.', nargs='+', type=int)
    parser.add_argument('--version_ids', type=int, nargs='+',
                        help='Source version IDs whose annotations and version definitions will be migrated. '
                             'Required base version definitions are included as dependencies. '
                             'If omitted, all versions are included. Section and version selections '
                             'also scope row protection migration.')
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
    parser.add_argument('--skip_file_types', help='If given, file types will not be migrated.',
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
    parser.add_argument('--ignore-media-transfer', help='If given, media will not be transferred but '
                                                        'the media objects will still be created.',
                        action='store_true')
    add_acl_arguments(parser)
    return parser.parse_args()

def discover_when_skipped(kind):
    """ACL-only passes still need mappings for previously migrated resources."""
    def decorate(find):
        @wraps(find)
        def wrapped(args, src_api, dest_api, dest_project, *rest, **kwargs):
            skipped = getattr(args, 'skip_' + kind)
            if skipped and dest_project is None:
                logger.info("Skipping %s; new destination project has no existing objects to map", kind)
                return ({} if kind == 'leaves' else []), {}
            if getattr(args, 'skip_acl', False) or not skipped:
                return find(args, src_api, dest_api, dest_project, *rest, **kwargs)
            discovery_args = copy.copy(args)
            setattr(discovery_args, 'skip_' + kind, False)
            discovery_args._mapping_only = True
            pending, mapping = find(discovery_args, src_api, dest_api, dest_project, *rest, **kwargs)
            logger.info("Skipping creation of %s; retained %d existing mappings", kind, len(mapping))
            return ({} if isinstance(pending, dict) else []), mapping
        return wrapped
    return decorate


def log_discovery(args, message, *values):
    # The wrapper reports retained mappings separately when creation is disabled.
    if not getattr(args, '_mapping_only', False):
        logger.info(message, *values)


def get_tator_user_sections(media):
    tator_user_sections = None
    if media.attributes:
        tator_user_sections = media.attributes.get('tator_user_sections', None)
    return tator_user_sections

def get_section_list_from_ids(api, args):
    sections = api.get_section_list(args.project)
    id_set = {int(s) for s in args.section_ids}
    missing = id_set - {section.id for section in sections}
    if missing:
        raise ValueError(f'Section IDs not found in source project: {sorted(missing)}')
    selected_sections = [section for section in sections if section.id in id_set]

    def path(section):
        return section.path if section.path not in (None, 'None') else section.name.replace(' ', '_')

    def ancestor(parent, child):
        # Paths use dot-separated components: A.B must not select A.Beta.
        return path(child).startswith(path(parent) + '.')

    return [section for section in sections if section.id in id_set or any(
        ancestor(section, selected) or ancestor(selected, section) for selected in selected_sections)]


def select_versions(versions, version_ids):
    """Select definitions in base-first order without silently breaking inheritance."""
    by_id = {version.id: version for version in versions}
    requested = list(dict.fromkeys(version_ids)) if version_ids else list(by_id)
    missing = set(requested) - set(by_id)
    if missing:
        raise ValueError(f'Version IDs not found in source project: {sorted(missing)}')
    result, visited, visiting = [], set(), set()

    def visit(version_id):
        if version_id in visited:
            return
        if version_id in visiting:
            raise ValueError(f'Cycle in version bases at version {version_id}')
        if version_id not in by_id:
            raise ValueError(f'Required base version {version_id} is not visible in source project')
        visiting.add(version_id)
        version = by_id[version_id]
        for base in getattr(version, 'bases', None) or []:
            visit(base)
        visiting.remove(version_id)
        visited.add(version_id)
        result.append(version)

    for version_id in requested:
        visit(version_id)
    dependencies = visited - set(requested)
    if version_ids and dependencies:
        logger.info('Including required base version definitions: %s (their annotations are not selected)',
                    sorted(dependencies))
    return result


def annotation_version_filter(args):
    selected = getattr(args, 'version_ids', None)
    return {'version': list(dict.fromkeys(selected))} if selected else {}


def selected_annotations(args, objects):
    # Enforce exact versions locally as well as in the server query.
    selected = set(getattr(args, 'version_ids', None) or [])
    return list({obj.id: obj for obj in objects if not selected or obj.version in selected}.values())

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
        name = args.new_project_name if args.new_project_name else src_project.name
        organization = args.dest_organization
        if not args.skip_acl:
            organization = organization or dict(args.map_organization).get(src_project.organization)
        candidates = [p for p in dest_projects if p.name == name and
                      (args.skip_acl or organization is None or p.organization == organization)]
        if not args.skip_acl and len(candidates) > 1:
            raise ValueError('Ambiguous destination project; specify --dest_project')
        for project_obj in candidates:
            if project_obj.name == name:
                dest_project = project_obj
                logger.info(f"Migrating to existing project with ID {project_obj.id}.")
                break
        if dest_project is None:
            logger.info(f"New project with name {name} will be created.")
    return dest_project

def find_memberships(args, src_api, dest_api, dest_project):
    """Plan memberships only for users that already exist on the destination host."""
    membership_mapping, user_mapping = {}, {}
    if args.skip_memberships and (args.skip_acl or dest_project is None):
        logger.info("Skipping memberships")
        return [], [], membership_mapping, user_mapping
    memberships = src_api.get_membership_list(args.project)
    users = [src_api.get_user(m.user) for m in memberships]
    existing = dest_api.get_membership_list(dest_project.id) if dest_project else []
    by_username = {dest_api.get_user(m.user).username: m for m in existing}
    creator_id = dest_api.whoami().id if dest_project is None and memberships else None
    pending, pending_users = [], []
    missing_users, creator_memberships = 0, 0
    for membership, user in zip(memberships, users):
        match = by_username.get(user.username)
        if match:
            membership_mapping[membership.id] = match.id
            user_mapping[user.id] = match.user
        elif not args.skip_memberships:
            matches = [u for u in dest_api.get_user_list(username=user.username)
                       if u.username == user.username]
            if len(matches) > 1:
                raise ValueError(f'Ambiguous destination username {user.username!r}')
            if not matches:
                missing_users += 1
                continue
            user_mapping[user.id] = matches[0].id
            # Retain the creator for mapping after create_project automatically adds it.
            creator_memberships += matches[0].id == creator_id
            pending.append(membership)
            pending_users.append(user)
    if args.skip_memberships:
        logger.info("Skipping membership creation; retained %d existing mappings", len(membership_mapping))
    else:
        logger.info("%d memberships will be created (%d already exist, %d supplied by project creation, "
                    "%d skipped: no matching destination user)",
                    len(pending) - creator_memberships, len(membership_mapping), creator_memberships, missing_users)
    return pending, pending_users, membership_mapping, user_mapping

def find_sections(args, src_api, dest_api, dest_project):
    """Find sections to create and retain the existing section ID mapping."""
    if args.skip_sections and (args.skip_acl or dest_project is None):
        logger.info("Skipping sections")
        return [], {}
    sections = (get_section_list_from_ids(src_api, args) if args.section_ids
                else src_api.get_section_list(args.project))
    existing = dest_api.get_section_list(dest_project.id) if dest_project else []
    mapping, pending = {}, []
    for section in sections:
        matches = [s for s in existing if s.name == section.name]
        if len(matches) > 1:
            matches = [s for s in matches if s.path == section.path]
        if len(matches) > 1:
            raise ValueError(f'Ambiguous destination section {section.name!r}')
        if matches:
            mapping[section.id] = matches[0].id
        elif not args.skip_sections:
            pending.append(section)
    logger.info("%d sections will be created (%d already exist)", len(pending), len(mapping))
    return pending, mapping

@discover_when_skipped('versions')
def find_versions(args, src_api, dest_api, dest_project):
    """ Finds existing versions in destination project. Returns ID mapping between source
        and destination versions and versions that need to be created.
    """
    version_mapping = {}
    versions = select_versions(src_api.get_version_list(args.project), getattr(args, 'version_ids', None))
    if dest_project is not None:
        existing = dest_api.get_version_list(dest_project.id)
        existing_names = [version.name for version in existing]
        for version in versions:
            if version.name in existing_names:
                version_mapping[version.id] = existing[existing_names.index(version.name)].id
        versions = [version for version in versions if version.name not in existing_names]
    if args.skip_versions:
        versions = []
        log_discovery(args, f"Skipping versions due to --skip_versions.")
    else:
        log_discovery(args, f"{len(versions)} versions will be created ({len(version_mapping.values())} "
                     "already exist).")
    return versions, version_mapping

@discover_when_skipped('media_types')
def find_media_types(args, src_api, dest_api, dest_project):
    """ Finds existing media types in destination project. Returns ID mapping between source
        and destination media types and media types that need to be created.
    """
    media_types = []
    media_type_mapping = {}
    if args.skip_media_types:
        log_discovery(args, f"Skipping media types due to --skip_media_types.")
    else:
        media_types = src_api.get_media_type_list(args.project)
        if dest_project is not None:
            existing = dest_api.get_media_type_list(dest_project.id)
            existing_names = [media_type.name for media_type in existing]
            for media_type in media_types:
                if media_type.name in existing_names:
                    media_type_mapping[media_type.id] = existing[existing_names.index(media_type.name)].id
            media_types = [media_type for media_type in media_types if media_type.name not in existing_names]
        log_discovery(args, f"{len(media_types)} media types will be created ({len(media_type_mapping.values())} "
                     "already exist).")
    return media_types, media_type_mapping

@discover_when_skipped('localization_types')
def find_localization_types(args, src_api, dest_api, dest_project):
    """ Finds existing localization types in destination project. Returns ID mapping between source
        and destination localization types and localization types that need to be created.
    """
    localization_types = []
    localization_type_mapping = {}
    if args.skip_localization_types:
        log_discovery(args, f"Skipping localization types due to --skip_localization_types.")
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
        log_discovery(args, f"{len(localization_types)} localization types will be created "
                    f"({len(localization_type_mapping.values())} already exist).")
    return localization_types, localization_type_mapping

@discover_when_skipped('state_types')
def find_state_types(args, src_api, dest_api, dest_project):
    """ Finds existing state types in destination project. Returns ID mapping between source
        and destination state types and state types that need to be created.
    """
    state_types = []
    state_type_mapping = {}
    if args.skip_state_types:
        log_discovery(args, f"Skipping state types due to --skip_state_types.")
    else:
        state_types = src_api.get_state_type_list(args.project)
        if dest_project is not None:
            existing = dest_api.get_state_type_list(dest_project.id)
            existing_names = [state_type.name for state_type in existing]
            for state_type in state_types:
                if state_type.name in existing_names:
                    state_type_mapping[state_type.id] = existing[existing_names.index(state_type.name)].id
            state_types = [state_type for state_type in state_types if state_type.name not in existing_names]
        log_discovery(args, f"{len(state_types)} state types will be created ({len(state_type_mapping.values())} "
                     "already exist).")
    return state_types, state_type_mapping

@discover_when_skipped('leaf_types')
def find_leaf_types(args, src_api, dest_api, dest_project):
    """ Finds existing leaf types in destination project. Returns ID mapping between source
        and destination leaf types and leaf types that need to be created.
    """
    leaf_types = []
    leaf_type_mapping = {}
    if args.skip_leaf_types:
        log_discovery(args, f"Skipping leaf types due to --skip_leaf_types.")
    else:
        leaf_types = src_api.get_leaf_type_list(args.project)
        if dest_project is not None:
            existing = dest_api.get_leaf_type_list(dest_project.id)
            existing_names = [leaf_type.name for leaf_type in existing]
            for leaf_type in leaf_types:
                if leaf_type.name in existing_names:
                    leaf_type_mapping[leaf_type.id] = existing[existing_names.index(leaf_type.name)].id
            leaf_types = [leaf_type for leaf_type in leaf_types if leaf_type.name not in existing_names]
        log_discovery(args, f"{len(leaf_types)} leaf types will be created ({len(leaf_type_mapping.values())} "
                     "already exist).")
    return leaf_types, leaf_type_mapping

@discover_when_skipped('file_types')
def find_file_types(args, src_api, dest_api, dest_project):
    """ Finds existing file types in destination project. Returns ID mapping between source
        and destination file types and file types that need to be created.
    """
    file_types = []
    file_type_mapping = {}
    if args.skip_file_types:
        log_discovery(args, f"Skipping file types due to --skip_file_types.")
    else:
        file_types = src_api.get_file_type_list(args.project)
        if dest_project is not None:
            existing = dest_api.get_file_type_list(dest_project.id)
            existing_names = [file_type.name for file_type in existing]
            for file_type in file_types:
                if file_type.name in existing_names:
                    file_type_mapping[file_type.id] = existing[existing_names.index(file_type.name)].id
            file_types = [file_type for file_type in file_types if file_type.name not in existing_names]
        log_discovery(args, f"{len(file_types)} file types will be created ({len(file_type_mapping.values())} "
                     "already exist).")
    return file_types, file_type_mapping

@discover_when_skipped('media')
def find_media(args, src_api, dest_api, dest_project):
    """ Finds existing media in destination project. Returns media that need to be created and ID
        mapping between source and destination medias.
    """
    media = []
    media_mapping = {}
    if args.skip_media:
        log_discovery(args, f"Skipping media due to --skip_media.")
    else:
        if args.section_ids:
            sections = get_section_list_from_ids(src_api, args)
            for section in sections:
                section_media = src_api.get_media_list(project=args.project, section=section.id)
                num_src_media = len(section_media)
                if dest_project is not None:
                    existing_section = dest_api.get_section_list(dest_project.id, name=section.name)
                    if existing_section:
                        existing = dest_api.get_media_list(project=dest_project.id, section=existing_section[0].id)
                        existing_names = [m.name for m in existing]
                        for m in section_media:
                            if m.name in existing_names:
                                media_mapping[m.id] = existing[existing_names.index(m.name)].id
                        section_media = [m for m in section_media if m.name not in existing_names]
                log_discovery(args, f"{len(section_media)} media from section {section.name} will be "
                            f"created ({num_src_media - len(section_media)} already exist).")
                media += section_media
        else:
            media = src_api.get_media_list(project=args.project)
            num_src_media = len(media)
            if dest_project is not None:
                src_sections = src_api.get_section_list(args.project)
                dest_sections = dest_api.get_section_list(dest_project.id)
                src_section_names = {s.tator_user_sections: s.name for s in src_sections}
                dest_section_names = {s.tator_user_sections: s.name for s in dest_sections}
                src_section_names[None] = None
                dest_section_names[None] = None
                existing = dest_api.get_media_list(project=dest_project.id)
                existing_name_section = [
                    (m.name, dest_section_names[get_tator_user_sections(m)])
                    for m in existing
                ]
                for m in media:
                    key = (m.name, src_section_names[get_tator_user_sections(m)])
                    if key in existing_name_section:
                        media_mapping[m.id] = existing[existing_name_section.index(key)].id
                media = [m for m in media
                         if (m.name, src_section_names[get_tator_user_sections(m)])
                         not in existing_name_section]
            log_discovery(args, f"{len(media)} media will be created ({num_src_media - len(media)} "
                         "already exist).")
    return media, media_mapping

def _is_num(x):
    return isinstance(x, float) or isinstance(x, int)

def _same_localization(a, b, localization_type_mapping, version_mapping):
    """ Returns true if two localizations have nearly identical geometry.
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

@discover_when_skipped('localizations')
def find_localizations(args, src_api, dest_api, dest_project, media, media_mapping,
                       localization_type_mapping, version_mapping):
    """ Finds existing localizations in destination project. Returns localizations that need to 
        be created and ID mapping between source and destination medias.
    """
    count = 0
    localization_media_ids = []
    if args.skip_localizations:
        log_discovery(args, "Skipping localizations due to --skip_localizations")
        localizations = []
        localization_mapping = {}
    else:
        # Get existing localizations.
        dest_media_ids = list(media_mapping.values())
        existing_loc = []
        print("Retrieving existing localizations...")
        for idx in range(0, len(dest_media_ids), 100):
            existing_loc += dest_api.get_localization_list(dest_project.id,
                                                           media_id=dest_media_ids[idx:idx+100])
        # Get all source localizations.
        src_media_ids = list(media_mapping.keys())
        source_loc = []
        print("Retrieving source localizations...")
        for idx in range(0, len(media), 100):
            source_loc += src_api.get_localization_list(args.project,
                                                        media_id=[m.id for m in media[idx:idx+100]],
                                                        **annotation_version_filter(args))
        for idx in range(0, len(src_media_ids), 100):
            source_loc += src_api.get_localization_list(args.project,
                                                        media_id=src_media_ids[idx:idx+100],
                                                        **annotation_version_filter(args))
        source_loc = selected_annotations(args, source_loc)
        # Group source and dest localizations by source media ID and frame number.
        print("Building lookups by media/frame...")
        reverse_media = {v:k for k, v in media_mapping.items()}
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
                    same = _same_localization(src_loc, dest_loc, localization_type_mapping, version_mapping)
                    if same:
                        found = True
                        localization_mapping[src_loc.id] = dest_loc.id
                if not found:
                    localizations.append(src_loc)
        log_discovery(args, f"{len(localizations)} localizations will be created ({len(localization_mapping.keys())} "
                     "already exist).")
    return localizations, localization_mapping

def _same_state(a, b, state_type_mapping, version_mapping):
    """ Returns true if two states have same version and type.
    """
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

@discover_when_skipped('states')
def find_states(args, src_api, dest_api, dest_project, media, media_mapping,
                state_type_mapping, version_mapping):
    """ Finds existing states in destination project. Returns 
    """
    count = 0
    state_media_ids = []
    if args.skip_states:
        log_discovery(args, "Skipping states due to --skip_states")
        states = []
        state_mapping = {}
    else:
        # Get existing states.
        dest_media_ids = list(media_mapping.values())
        existing_states = []
        print("Retrieving existing states...")
        for idx in range(0, len(dest_media_ids), 100):
            existing_states += dest_api.get_state_list(dest_project.id,
                                                       media_id=dest_media_ids[idx:idx+100])
        # Get all source states.
        src_media_ids = list(media_mapping.keys())
        source_states = []
        print("Retrieving source states...")
        for idx in range(0, len(media), 100):
            source_states += src_api.get_state_list(args.project,
                                                    media_id=[m.id for m in media[idx:idx+100]],
                                                        **annotation_version_filter(args))
        for idx in range(0, len(src_media_ids), 100):
            source_states += src_api.get_state_list(args.project,
                                                    media_id=src_media_ids[idx:idx+100],
                                                        **annotation_version_filter(args))
        source_states = selected_annotations(args, source_states)
        selected_media = set(media_mapping) | {m.id for m in media}
        spanning_states = [state for state in source_states if not set(state.media) <= selected_media]
        if spanning_states:
            logger.warning('Skipping %d states that reference media outside the selected sections', len(spanning_states))
            source_states = [state for state in source_states if set(state.media) <= selected_media]
        # Group source and dest states by source media ID and frame number.
        print("Building lookups by media/frame...")
        reverse_media = {v:k for k, v in media_mapping.items()}
        existing_grouped = defaultdict(list)
        source_grouped = defaultdict(list)
        for state in existing_states:
            if state.media and all(media_id in reverse_media for media_id in state.media):
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
                    same = _same_state(src_state, dest_state, state_type_mapping, version_mapping)
                    if same:
                        found = True
                        state_mapping[src_state.id] = dest_state.id
                if not found:
                    states.append(src_state)
        log_discovery(args, f"{len(states)} states will be created ({len(state_mapping.keys())} "
                     "already exist).")
    return states, state_mapping

@discover_when_skipped('leaves')
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
        log_discovery(args, "Skipping leaves due to --skip_leaves")
    else:
        depth = 2
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
                leaves[depth] = [leaf for leaf in src_leaves
                                 if leaf.path[1] not in dest_paths]
            else:
                leaves[depth] = list(src_leaves)
            num_leaves += len(leaves[depth])
            num_skipped += len(src_leaves) - len(leaves[depth])
            depth += 1
        log_discovery(args, f"{num_leaves} leaves will be created ({num_skipped} "
                     "already exist).")
    return leaves, leaf_mapping

def create_project(args, src_api, dest_api, dest_project):
    """ Creates a project if necessary. Returns the destination project ID.
    """
    if dest_project is None:
        src_project = src_api.get_project(args.project)
        name = args.new_project_name if args.new_project_name else src_project.name
        spec = {'name': name,
                'organization': args.dest_organization}
        if src_project.summary:
            spec['summary'] = src_project.summary
        response = dest_api.create_project(project_spec=spec)
        logger.info(f"Created new project with ID {response.id}")
        dest_project = response.id
    else:
        dest_project = dest_project.id
    return dest_project

def create_memberships(src_api, dest_api, dest_project, memberships, users,
                       membership_mapping, user_mapping):
    """Create memberships for existing users, including mapping automatic creator membership."""
    if not memberships:
        return
    existing = {m.user: m for m in dest_api.get_membership_list(dest_project)}
    for membership, user in zip(memberships, users):
        matches = [u for u in dest_api.get_user_list(username=user.username)
                   if u.username == user.username]
        if not matches:
            logger.warning("Skipping membership for missing destination user %s", user.username)
            continue
        if len(matches) > 1:
            raise ValueError(f'Ambiguous destination username {user.username!r}')
        dest_user = matches[0]
        user_mapping[user.id] = dest_user.id
        if dest_user.id in existing:
            membership_mapping[membership.id] = existing[dest_user.id].id
        else:
            response = dest_api.create_membership(dest_project, membership_spec={
                'user': dest_user.id, 'permission': membership.permission})
            membership_mapping[membership.id] = response.id
            existing[dest_user.id] = response

def create_sections(src_api, dest_api, dest_project, sections, section_mapping):
    """ Creates sections.
    """
    for section in sections:
        response = tator.util.clone_section(src_api, section.id, dest_project, dest_api)
        assert(isinstance(response, tator.models.CreateResponse))
        section_mapping[section.id] = response.id
    logger.info(f"Created {len(sections)} sections.")
    return section_mapping

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

def create_file_types(src_api, dest_api, dest_project, file_types, file_type_mapping):
    """ Creates file types. Returns updated file type mapping.
    """
    for file_type in file_types:
        response = tator.util.clone_file_type(src_api, file_type.id, dest_project, dest_api)
        assert(isinstance(response, tator.models.CreateResponse))
        file_type_mapping[file_type.id] = response.id
    logger.info(f"Created {len(file_types)} file types.")
    return file_type_mapping

def create_media(args, src_api, dest_api, dest_project, media, media_type_mapping, media_mapping, ignore_media_transfer):
    """ Creates media. Returns media mapping.
    """
    num_total = len(media)
    if not media:
        return media_mapping
    # Look up sections in destination project, create a dict between tator_user_sections and
    # section name.
    if args.section_ids:
        sections = get_section_list_from_ids(src_api, args)
    else:
        sections = src_api.get_section_list(args.project)
    section_mapping = {s.tator_user_sections: s.name for s in sections}
    section_mapping[None] = None
    # Construct dictionary between destination type/destination section and media IDs.
    media_ids = defaultdict(list)
    for single in media:
        key = (media_type_mapping[single.type],
               section_mapping[get_tator_user_sections(single)])
        media_ids[key].append(single.id)
    # Sort keys so that multi are created after images/videos.
    sorter = lambda mtype: 1 if dest_api.get_media_type(mtype[0]).dtype == 'multi' else 0
    keys = list(media_ids.keys())
    keys.sort(key=sorter)
    # Iterate through type/sections and create media.
    use_dest_api = None if src_api is dest_api else dest_api
    total_created = 0
    for key in keys:
        dest_type, dest_section = key
        for idx in range(0, len(media_ids[key]), 100): # Do batching here to manage ID query size.
            query_params = {'project': args.project,
                            'media_id': media_ids[key][idx:idx+100]}
            generator = tator.util.clone_media_list(src_api, query_params, dest_project, media_mapping,
                                                    dest_type, dest_section, use_dest_api, ignore_media_transfer)
            for _, _, response, id_map in generator:
                if isinstance(response, tator.models.CreateResponse):
                    total_created += 1
                elif isinstance(response, tator.models.CreateListResponse):
                    total_created += len(response.id)
                else:
                    raise ValueError("Error cloning media!")
                logger.info(f"Created {total_created} of {num_total} files...")
                media_mapping = {**media_mapping, **id_map}
    # Fix multi media IDs in destination project.
    logger.info(f"Updating components media IDs of cloned multis...")
    multi_medias = dest_api.get_media_list(dest_project, dtype="multi")
    for multi in multi_medias:
        updated_ids = [media_mapping[id_] if id_ in media_mapping else id_ for id_ in multi.media_files.ids]
        if updated_ids != multi.media_files.ids:
            media_update_spec = {"multi": {"ids": updated_ids}}
            response = dest_api.update_media(id=multi.id, media_update=media_update_spec)
            logger.info(response.message)
    logger.info(f"Created {num_total} media.")
    return media_mapping

def create_localizations(args, src_api, dest_api, dest_project, localizations,
                         localization_type_mapping, localization_mapping, media_mapping,
                         version_mapping):
    """ Creates localizations. Returns localization mapping.
    """
    # Iterate through media and create localization.
    total_created = 0
    for idx in range(0, len(localizations), 100): # Do batching here to manage ID query size.
        query_params = {'project': args.project,
                        'localization_id_query': {'ids': [loc.id for loc in localizations[idx:idx+100]]}}
        generator = tator.util.clone_localization_list(src_api, query_params, dest_project,
                                                       version_mapping, media_mapping,
                                                       localization_type_mapping, dest_api)
        for _, _, response, id_map in generator:
            total_created += len(response.id)
            logger.info(f"Created {total_created} of {len(localizations)} localizations...")
            localization_mapping = {**localization_mapping, **id_map}
    logger.info(f"Created {total_created} localizations.")
    return localization_mapping

def create_states(args, src_api, dest_api, dest_project, states,
                  state_type_mapping, state_mapping, media_mapping, version_mapping,
                  localization_mapping):
    """ Creates states.
    """
    # Iterate through media and create state.
    total_created = 0
    for idx in range(0, len(states), 100): # Do batching here to manage ID query size.
        query_params = {'project': args.project,
                        'state_id_query': {'ids': [state.id for state in states[idx:idx+100]]}}
        generator = tator.util.clone_state_list(src_api, query_params, dest_project,
                                                version_mapping, media_mapping,
                                                localization_mapping, state_type_mapping, dest_api)
        for _, _, response, id_map in generator:
            total_created += len(response.id)
            logger.info(f"Created {total_created} of {len(states)} states...")
            state_mapping = {**state_mapping, **id_map}
    logger.info(f"Created {total_created} states.")
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
    return leaf_mapping

def migrate(args):
    src_api, dest_api = setup_apis(args)
    # Find which resources need to be migrated.
    dest_project = find_dest_project(args, src_api, dest_api)
    acl = ACLMigration(args, src_api, dest_api) if not args.skip_acl else None
    if acl:
        acl.bind_project_organization(dest_project)
    memberships, users, membership_mapping, user_mapping = find_memberships(args, src_api, dest_api, dest_project)
    sections, section_mapping = find_sections(args, src_api, dest_api, dest_project)
    versions, version_mapping = find_versions(args, src_api, dest_api, dest_project)
    media_types, media_type_mapping = find_media_types(args, src_api, dest_api, dest_project)
    localization_types, localization_type_mapping = find_localization_types(args, src_api, dest_api,
                                                                            dest_project)
    state_types, state_type_mapping = find_state_types(args, src_api, dest_api, dest_project)
    leaf_types, leaf_type_mapping = find_leaf_types(args, src_api, dest_api, dest_project)
    file_types, file_type_mapping = find_file_types(args, src_api, dest_api, dest_project)
    media, media_mapping = find_media(args, src_api, dest_api, dest_project)
    localizations, localization_mapping = find_localizations(args, src_api, dest_api, dest_project, media,
                                                             media_mapping, localization_type_mapping,
                                                             version_mapping)
    states, state_mapping = find_states(args, src_api, dest_api, dest_project, media, media_mapping, state_type_mapping,
                                        version_mapping)
    leaves, leaf_mapping = find_leaves(args, src_api, dest_api, dest_project)
    ignore_media_transfer = True if args.ignore_media_transfer else False
    if ignore_media_transfer:
        logger.info("Will not transfer media_files")

    if acl:
        acl.preview(dest_project, {
            'user': user_mapping, 'section': section_mapping, 'version': version_mapping,
            'media': media_mapping, 'localization': localization_mapping, 'state': state_mapping,
        }, {
            'section': sections, 'version': versions, 'media': media,
            'localization': localizations, 'state': states,
        })

    # Confirm migration with user.
    proceed = input("Continue with migration [y/N]? ")
    if proceed == 'y':
        # Perform migration.
        if acl:
            acl.prepare_project_organization()
        dest_project = create_project(args, src_api, dest_api, dest_project)
        create_memberships(src_api, dest_api, dest_project, memberships, users,
                           membership_mapping, user_mapping)
        section_mapping = create_sections(src_api, dest_api, dest_project, sections, section_mapping)
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
        file_type_mapping = create_file_types(src_api, dest_api, dest_project, file_types, file_type_mapping)
        media_mapping = create_media(args, src_api, dest_api, dest_project, media,
                                     media_type_mapping, media_mapping, ignore_media_transfer)
        if acl:
            acl.maps.update({'project': {args.project: dest_project}, 'section': section_mapping,
                             'media': media_mapping})
            acl.preserve_master_sections(dest_project)
        localization_mapping = create_localizations(args, src_api, dest_api, dest_project,
                                                    localizations, localization_type_mapping,
                                                    localization_mapping, media_mapping, version_mapping)
        state_mapping = create_states(args, src_api, dest_api, dest_project, states, state_type_mapping, state_mapping,
                      media_mapping, version_mapping, localization_mapping)
        leaf_mapping = create_leaves(args, src_api, dest_api, dest_project, leaves, leaf_type_mapping,
                      leaf_mapping)
        mappings = {
            'membership': membership_mapping, 'user': user_mapping,
            'project': {args.project: dest_project}, 'section': section_mapping,
            'version': version_mapping, 'media_type': media_type_mapping,
            'localization_type': localization_type_mapping, 'state_type': state_type_mapping,
            'leaf_type': leaf_type_mapping, 'file_type': file_type_mapping,
            'media': media_mapping, 'localization': localization_mapping,
            'state': state_mapping, 'leaf': leaf_mapping,
        }
        if acl:
            acl.maps.update(mappings)
            return acl.run()
        return mappings
    else:
        logger.info("Migration cancelled by user.")


if __name__ == '__main__':
    try:
        migrate(parse_args())
    except ValueError as exc:
        logger.error('%s', exc)
        sys.exit(1)

