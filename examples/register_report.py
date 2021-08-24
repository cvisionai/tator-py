""" This examples uploads a report file to the project
"""

import tator

def main() -> None:
    """ Main routine of this script
    """

    # Set the arguments and grab them
    parser = tator.get_parser()
    parser.add_argument(
        '--project',
        help='Unique project ID associated with the report file',
        required=True,
        type=int)
    parser.add_argument(
        '--html-file',
        help='Path to the report html file',
        type=str,
        required=True)
    parser.add_argument(
        '--name',
        help='Name of report',
        type=str,
        required=True)
    parser.add_argument(
        '--description',
        help='Description of report',
        type=str,
        required=True)
    args = parser.parse_args()

    tator.util.register_report(
        host=args.host,
        token=args.token,
        project=args.project,
        html_file=args.html_file,
        name=args.name,
        description=args.description)

if __name__ == "__main__":
    main()