import argparse

def get_parser(parser=None, description=None):
    """ Returns an argument parser that includes host and token.

    :returns: :class:`argparse.ArgumentParser` object that includes host and token arguments.
    """
    if parser is None:
        parser = argparse.ArgumentParser(description=description if description else "A tator-py utility.")
    parser.add_argument('--host', default='https://cloud.tator.io')
    parser.add_argument('--token', help="Your API token.")
    return parser
