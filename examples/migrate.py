#!/usr/bin/env python3

import argparse
import logging
import os
import shutil
import sys
import traceback
from textwrap import dedent

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
    - Sections (idempotent, based on section name)
    - Versions (idempotent, based on version name)
    - Media (idempotent, based on section name and media name)
    - Localizations (only migrated if parent media is migrated)
    - States (only migrated if parent media is migrated)
    The following objects must be explicitly included in the migration:
    - Projects (idempotent, based on project name)
    - Memberships (idempotent, based on matching username)
    - Leaves (NOT idempotent)

    Examples:
    Migrate project settings on same host
    python3 migrate.py --host https://tatorapp.com --token asdf --project 1 --skip_sections
    --skip_media

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
                                               'Alternatively, use --include_project to create a '
                                               'new project.', type=int)
    parser.add_argument('--sections', help='Specific sections to migrate. If not given, all media '
                                           'in the source project will be migrated.', nargs='+')
    parser.add_argument('--skip_sections', help='If given, section objects will not be migrated.',
                        action='store_true')
    parser.add_argument('--skip_versions', help='If given, version objects will not be migrated.',
                        action='store_true')
    parser.add_argument('--skip_media', help='If given, media will not be migrated. Use this to '
                                             'only migrate a project configuration.',
                        action='store_true')
    parser.add_argument('--skip_localizations', help='If given, localizations will not be migrated.',
                        action='store_true')
    parser.add_argument('--skip_states', help='If given, states will not be migrated.',
                        action='store_true')
    parser.add_argument('--include_project', help='If given, a new project will be created if an '
                                                  'existing project with matching name does not '
                                                  'already exist.',
                        action='store_true')
    parser.add_argument('--include_memberships', help='If given, memberships will be migrated.',
                        action='store_true')
    parser.add_argument('--include_leaves', help='If given, leaves will be migrated.',
                        action='store_true')
    return parser.parse_args()

def setup_apis(args):
    """ Sets up API objects.
    """
    # Set up API objects.
    src_api = tator.get_api(host=args.host, token=args.token)
    if (args.dest_host is not None) and (args.dest_token is not None):
        dest_api = tator.get_api(host=args.dest_host, token=args.dest_token)
        logger.info(f"Migrating to different host ({args.dest_host}).")
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
            logger.info(f"New project with name {src_project.name} will be created.")
    return dest_project

def find_sections(args, src_api, dest_api, dest_project):
    """ Finds existing sections in destination project. Returns sections in source project
        that need to be created.
    """
    sections = []
    if args.skip_sections:
        logger.info(f"Skipping sections due to --skip_sections.")
    else:
        sections = src_api.get_section_list(args.project)
        if args.sections:
            sections = [section for section in sections if section.name in args.sections]
        if dest_project is not None:
            existing = dest_api.get_section_list(dest_project.id)
            existing_names = [section.name for section in existing]
            sections = [section for section in sections if section.name not in existing_names]
        logger.info(f"{len(sections)} sections will be created.")
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

if __name__ == '__main__':
    args = parse_args()
    src_api, dest_api = setup_apis(args)
    dest_project = find_dest_project(args, src_api, dest_api)
    sections = find_sections(args, src_api, dest_api, dest_project)
    versions, version_mapping = find_versions(args, src_api, dest_api, dest_project)
    
