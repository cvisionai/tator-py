import logging
import os

from ..openapi.tator_openapi.models import MessageResponse
from ..util.get_api import get_api
from ..util.get_parser import get_parser

logger = logging.getLogger(__name__)

def parse_args():
    parser = get_parser()
    parser.add_argument('--input', type=str, help="Path to file containing media ID.")
    return parser.parse_args()

def delete_media(host, token, media_id):
    """ Deletes a media object.

    :param host: Host URL.
    :param token: API token.
    :param media_id: Unique integer identifying a media.
    """
    api = get_api(host, token)
    response = api.delete_media(media_id)
    assert isinstance(response, MessageResponse)

if __name__ == '__main__':
    args = parse_args()
    if os.path.exists(args.input):
        with open(args.input, 'r') as f:
            media_id = int(f.read())
            delete_media(args.host, args.token, media_id)
    else:
        logger.info(f"No media deleted, file {args.input} could not be found!")
