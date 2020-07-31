""" This example launches the registered algorithm on the media in the given
    project/section
"""

import logging
import time

import tator

def launch_algorithm_workflow(
        host: str,
        token: str,
        project: int,
        section_name: str,
        algorithm_name: str) -> None:
    """ Launches the registered algorithm workflow on the media in the given project/section

    Args:
        host: str
            Project URL
        token: str
            User access token used for connecting to the host
        project: int
            Unique identifier of project
        section_name: str
            Unique section name containing media for the algorithm to process
        algorithm_name: str
            Unique algorithm name of registered workflow
    """

    # Create interface to tator
    tator_api = tator.get_api(host=host, token=token)

    # Grab the media in the provided section
    attribute_filter = f'tator_user_sections::{section_name}'
    medias = tator_api.get_media_list(project=project, attribute_contains=attribute_filter)
    
    # Now, launch the algorithm using all the media in the project
    spec = tator.models.AlgorithmLaunchSpec(algorithm_name=algorithm_name)
    response = tator_api.algorithm_launch(project=project, algorithm_launch_spec=spec)
    
    # Let the user know the UID of the launched workflow
    log_msg = f'Run UID: {response.run_uids}'
    print(log_msg)

if __name__ == '__main__':
    parser = tator.get_parser()
    parser.add_argument('--project', type=int, required=True,
        help='Unique project id')
    parser.add_argument('--section', type=str, required=True,
        help='Optional section name to process')
    parser.add_argument('--algorithm_name', type=str, required=True,
        help='Section with media to execute the algorithm on')
    args = parser.parse_args()

    launch_algorithm_workflow(
        host=args.host,
        token=args.token,
        project=args.project,
        section_name=args.section,
        algorithm_name=args.algorithm_name)