""" This examples uploads an applet to the project
"""
import argparse

import tator

def main() -> None:
    """ Main routine of this script
    """

    # Set the arguments and grab them
    parser = argparse.ArgumentParser(description="Registers an applet (e.g. dashboard) to a Tator project")
    parser.add_argument("--host", type=str, required=True)
    parser.add_argument("--token", type=str, required=True)
    parser.add_argument(
        '--project',
        help='Unique project ID associated with the applet file',
        required=True,
        type=int)
    parser.add_argument(
        '--html-file',
        help='Path to the applet html file',
        type=str,
        required=True)
    parser.add_argument(
        '--name',
        help='Name of applet',
        type=str,
        required=True)
    parser.add_argument(
        '--description',
        help='Description of applet',
        type=str,
        required=True)
    parser.add_argument(
        '--categories',
        help='Categories the applet belongs to',
        type=str,
        nargs="+")
    args = parser.parse_args()

    tator.util.register_applet(
        host=args.host,
        token=args.token,
        project=args.project,
        html_file=args.html_file,
        dashboard_name=args.name,
        categories=args.categories,
        description=args.description)

if __name__ == "__main__":
    main()