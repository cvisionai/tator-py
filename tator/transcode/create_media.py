import json

from ..openapi.tator_openapi.models import CreateResponse
from ..util.get_api import get_api
from ..util.get_parser import get_parser

def parse_args():
    parser = get_parser()
    parser.add_argument('--project', type=int, help="Unique integer identifying a project.")
    parser.add_argument('--media_type', type=int, help="Unique integer identifying a media type.")
    parser.add_argument('--section', type=str, help="Name of section to upload to.")
    parser.add_argument('--section_id', type=int, help='Media section ID. If given `--section` is ignored.')
    parser.add_argument('--name', type=str, help="Name of file.")
    parser.add_argument('--md5', type=str, help="md5 sum of file.")
    parser.add_argument('--gid', type=str, help="Upload group ID.")
    parser.add_argument('--uid', type=str, help="Upload unique ID.")
    parser.add_argument('--output', type=str, help="Where to dump media ID.")
    parser.add_argument('--attributes', type=str, help="Attributes for media as a JSON string.")
    return parser.parse_args()

def create_media(host, token, project, media_type, section, name, md5, gid, uid,
                 attributes=None, url=None, section_id=None):
    """ Creates a media object and returns the ID.

    :param host: Host URL.
    :param token: API token.
    :param project: Unique integer identifying a project.
    :param media_type: Unique integer identifying a media type.
    :param section: Section name.
    :param section_id: Unique integer identifying a section. If given, `section` is ignored.
    :param name: File name.
    :param md5: md5 sum of file.
    :param gid: Upload group ID.
    :param uid: Upload unique ID.
    """
    api = get_api(host, token)
    section_blob = {'section_id': section_id} if section_id else {'section': section}
    spec ={
        'type': media_type,
        **section_blob,
        'name': name,
        'md5': md5,
        'gid': gid,
        'uid': uid
    }

    if attributes:
        spec.update({'attributes': json.loads(attributes)})
    if url:
        spec.update({'url': url})

    return api.create_media_list(project, body=[spec]).id[0] # pylint: disable=E1101


if __name__ == '__main__':
    args = parse_args()
    media_id = create_media(args.host, args.token, args.project, args.media_type,
                            args.section, args.name, args.md5, args.gid, args.uid, args.attributes, section_id=args.section_id)
    with open(args.output, 'w') as f:
        f.write(str(media_id))
