import argparse
import os


def validate_string_argument(arg: str) -> str:
    """Validates string arguments that should not be empty"""
    if arg:
        return arg
    raise RuntimeError(f"Expected a non-empty string, received {arg=}")


def get_parser(parser=None, description=None):
    """Returns an argument parser that includes host and token.

    :returns: :class:`argparse.ArgumentParser` object that includes host and token arguments.
    """
    if parser is None:
        parser = argparse.ArgumentParser(
            description=description if description else "A tator-py utility.",
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    parser.add_argument(
        "--host",
        type=validate_string_argument,
        default=os.getenv("TATOR_HOST", "https://cloud.tator.io"),
        help=(
            "The Tator host to connect to; if no host is provided on the command line, this will "
            "fall back to the environment variable `TATOR_HOST`."
        ),
    )
    parser.add_argument(
        "--token",
        type=validate_string_argument,
        default=os.getenv("TATOR_TOKEN", ""),
        help=(
            "The authentication token to use; if no token is provided on the command line, this "
            "will fall back to the environment variable `TATOR_TOKEN`."
        ),
    )
    return parser
