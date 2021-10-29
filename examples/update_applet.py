""" This examples updates an existing project dashboard
"""
import argparse

import tator

def main() -> None:
    """ Main routine of this script
    """

    # Set the arguments and grab them
    parser = argparse.ArgumentParser(description="Registers a applet to a Tator project")
    parser.add_argument("--host", type=str, required=True)
    parser.add_argument("--token", type=str, required=True)
    parser.add_argument(
        '--applet-id',
        help='Unique applet ID',
        required=True,
        type=int)
    parser.add_argument(
        '--html-file',
        help='Path to the applet html file',
        type=str)
    parser.add_argument(
        '--name',
        help='Name of applet',
        type=str)
    parser.add_argument(
        '--description',
        help='Description of applet',
        type=str)
    parser.add_argument(
        '--categories',
        help='Categories the applet belongs to',
        type=str,
        nargs="+")
    args = parser.parse_args()

    tator.util.update_applet(
        host=args.host,
        token=args.token,
        applet_id=args.applet_id,
        html_file=args.html_file,
        applet_name=args.name,
        categories=args.categories,
        description=args.description)

if __name__ == "__main__":
    main()