import argparse
import logging
import sys
from textwrap import dedent

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


def parse_args():
    parser = argparse.ArgumentParser(
        description=dedent(
            """\
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
    - Localizations (only migrated if destination media has no localizations)
    - States (only migrated if destination media has no states)
    - Leaves (idempotent, based on path)

    If the --dest_project is not specified, a new project will be created with the name
    specified by --new_project_name or with the same name if neither are given.

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
    """
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--host", help="Host containing source project.", required=True)
    parser.add_argument("--token", help="Token for host containing source project.", required=True)
    parser.add_argument(
        "--project",
        help="Unique integer identifying project containing data to " "be migrated.",
        required=True,
        type=int,
    )
    parser.add_argument(
        "--dest_host",
        help="Host containing destination project. If not given "
        "the destination project is assumed to be on the same "
        "host as the source.",
    )
    parser.add_argument(
        "--dest_token",
        help="Token for host containing destination project. If "
        "not given the destination project is assumed to be "
        "on the same host as the source.",
    )
    parser.add_argument(
        "--dest_project",
        help="Destination project, if it already exists. "
        "If omitted, a new project will be created using "
        "either the same name or the name specified by "
        "--new_project_name.",
        type=int,
    )
    parser.add_argument(
        "--new_project_name",
        help="Name to user for new project if --dest_project " "is omitted.",
        type=str,
    )
    parser.add_argument(
        "--dest_organization",
        help="Destination organization. Required if using " "--new_project_name.",
        type=int,
    )
    parser.add_argument(
        "--sections",
        help="Specific sections to migrate. If not given, all media "
        "in the source project will be migrated.",
        nargs="+",
    )
    parser.add_argument(
        "--skip_memberships",
        help="If given, membership objects will not be migrated.",
        action="store_true",
    )
    parser.add_argument(
        "--skip_sections",
        help="If given, section objects will not be migrated.",
        action="store_true",
    )
    parser.add_argument(
        "--skip_versions",
        help="If given, version objects will not be migrated.",
        action="store_true",
    )
    parser.add_argument(
        "--skip_media_types",
        help="If given, media types will not be migrated.",
        action="store_true",
    )
    parser.add_argument(
        "--skip_localization_types",
        help="If given, localization types will not " "be migrated.",
        action="store_true",
    )
    parser.add_argument(
        "--skip_state_types",
        help="If given, state types will not be migrated.",
        action="store_true",
    )
    parser.add_argument(
        "--skip_leaf_types", help="If given, leaf types will not be migrated.", action="store_true"
    )
    parser.add_argument(
        "--skip_media",
        help="If given, media will not be migrated. Use this to "
        "only migrate a project configuration.",
        action="store_true",
    )
    parser.add_argument(
        "--skip_localizations",
        help="If given, localizations will not be migrated.",
        action="store_true",
    )
    parser.add_argument(
        "--skip_states", help="If given, states will not be migrated.", action="store_true"
    )
    parser.add_argument(
        "--skip_leaves", help="If given, leaves will not be migrated.", action="store_true"
    )
    parser.add_argument(
        "--ignore-media-transfer",
        help="If given, media will not be transferred but "
        "the media objects will still be created.",
        action="store_true",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    migration_config = get_migration_config(args)
