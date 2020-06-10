import argparse

def get_parser():
    """ Returns an argument parser that includes host and token.

    :returns: :class:`argparse.ArgumentParser` object that includes host and token arguments.
    """
    parser = argparse.ArgumentParser(description="Creates a test project.")
    parser.add_argument('--host', default='https://www.tatorapp.com')
    parser.add_argument('--token', help="Your API token.")
    return parser
