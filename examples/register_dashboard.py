""" This examples uploads a dashboard to the project
"""
import argparse

import tator

def main() -> None:
    """ Main routine of this script
    """

    # Set the arguments and grab them
    parser = argparse.ArgumentParser(description="Registers a dashboard to a Tator project")
    parser.add_argument("--host", type=str, required=True)
    parser.add_argument("--token", type=str, required=True)
    parser.add_argument(
        '--project',
        help='Unique project ID associated with the dashboard file',
        required=True,
        type=int)
    parser.add_argument(
        '--html-file',
        help='Path to the dashboard html file',
        type=str,
        required=True)
    parser.add_argument(
        '--name',
        help='Name of dashboard',
        type=str,
        required=True)
    parser.add_argument(
        '--description',
        help='Description of dashboard',
        type=str,
        required=True)
    parser.add_argument(
        '--categories',
        help='Categories the dashboard belongs to',
        type=str,
        nargs="+")
    args = parser.parse_args()

    tator.util.register_dashboard(
        host=args.host,
        token=args.token,
        project=args.project,
        html_file=args.html_file,
        dashboard_name=args.name,
        description=args.description)

if __name__ == "__main__":
    main()