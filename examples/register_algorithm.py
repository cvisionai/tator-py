""" This examples uploads an algorithm manifest file and registers an algorithm workflow
"""

import tator

def main() -> None:
    """ Main routine of this script
    """

    # Set the arguments and grab them
    parser = tator.get_parser()
    parser.add_argument(
        '--project',
        help='Unique project ID associated with the argo workflow',
        required=True,
        type=int)
    parser.add_argument(
        '--manifest',
        help='Path to the argo manifest .yaml file to be uploaded',
        required=True)
    parser.add_argument(
        '--algorithm_name',
        help='Unique name of algorithm argo workflow',
        required=True)
    parser.add_argument(
        '--files_per_job',
        help='Number of files to process per job batch',
        type=int)
    parser.add_argument(
        '--description',
        help='Description of algorithm workflow')
    parser.add_argument(
        '--cluster_id',
        help='Cluster ID to run the workflow on',
        type=int)
    args = parser.parse_args()

    tator.util.register_algorithm(
        host=args.host,
        token=args.token,
        project=args.project,
        manifest=args.manifest,
        algorithm_name=args.algorithm_name,
        files_per_job=args.files_per_job,
        description=args.description,
        cluster_id=args.cluster_id)

if __name__ == "__main__":
    main()