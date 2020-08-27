#!/usr/bin/env python3
"""
Launches a registered algorithm on the given set of media
"""

import argparse
import logging

import tator

logging.basicConfig(
    filename='launch_algorithm.log',
    filemode='w',
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args() -> argparse.Namespace:
    """ Parse the provided script arguments

    Returns:
        Parsed arguments in a namespace object
    """

    parser = argparse.ArgumentParser(
        description="Launches the registered algorithm workflow (via name) on the given set of media")
    parser = tator.get_parser(parser=parser)
    parser.add_argument(
        '--project', type=int, required=True, help='Unique project id')
    parser.add_argument(
        '--algorithm', type=str, required=True, help='Name of registered algorithm to launch')
    parser.add_argument(
        '--media', type=int, required=True, nargs='+', help='Media IDs to process')

    args = parser.parse_args()
    logger.info(args)

    return args

def launch_algorithm(
        host: str,
        token: str,
        project: int,
        algorithm_name: str,
        media_ids: list) -> None:
    """ Launches the registered algorithm on the given set of media

    Args:
        host (str): Tator server url
        token (str): User access token to tator server
        project_id (int): Unique identifier of project that contains the algorithm/media
        algorithm_name (str): Name of algorithm to launch
        media_ids (list of ints): List of media IDs for the algorithm to process

    Postconditions:
        Algorithm launched. UID and GID are printed.
    """

    # Get the interface to tator
    tator_api = tator.get_api(host=host, token=token)

    # Launch the algorithm
    spec = tator.models.AlgorithmLaunchSpec(
        algorithm_name=algorithm_name,
        media_ids=media_ids)

    response = tator_api.algorithm_launch(
        project=project,
        algorithm_launch_spec=spec)

    print('Algorithm launch response logged.')

    logger.info('Algorithm launch response')
    logger.info(response)

def main() -> None:
    """ Main routine of this script
    """

    args = parse_args()

    launch_algorithm(
        host=args.host,
        token=args.token,
        project=args.project,
        algorithm_name=args.algorithm,
        media_ids=args.media)

    print('[FINISHED] launch_algorithm.py')

if __name__ == "__main__":
    main()