"""
Module where the parser is configured and built.
"""
import argparse as ap
import datetime as dt

from arguments.locations.location_parser import create_location_subparser
from arguments.users.user_parser import create_user_subparser


def create_parser():
    """
    Creates the parser. It calls the necessary functions to build the subparsers.
    Returns:
        Returns the built parser.
    """
    parser = ap.ArgumentParser(description="ZIA API command line script.")

    # Main parser commands
    parser.add_argument(
        '--pending', help="Lists pending changes.", action='store_true')
    parser.add_argument(
        '--apply', help='Forces application of changes before logging out.', action='store_true')
    parser.add_argument('--conf', help='Specifies config file.',
                        default='config/config.json')
    parser.add_argument('--output', '-o', help='Custom path where the output JSON will be stored.',
                        default=output_name())
    parser.add_argument('--no_verbosity', help='Disables detailed verbosity.', action='store_true')
    parser.add_argument('--no_print', help='Disables printing of results.', action='store_true')

    # Create subparsers
    subparsers = parser.add_subparsers()

    # Create user parser
    create_user_subparser(subparsers)

    # Create location parser
    create_location_subparser(subparsers)

    return parser


def output_name():
    """
    Creates a name for the output file where the search or operation results will be stored if no custom name is \
    provided.

    Returns:
        str: A string with the format `search_%Y-%m-%d_%H-%M-%S.json`.
        ``Example: search_2021-01-01_14-13-12.json``


    """
    today = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f'search_{today}.json'


# FUNCTIONS FOR TYPE
def boolstring(arg):
    """
    Checks arguments that are not required and have default values on the server. Argument is a string but mus be
    converted to True, False or ''.

    Args:
        arg (str): Parsed argument.

    Returns:
        bool or empty string:
            "True" -> `True`

            "False" -> `False`

            Anything else -> `''`

    """
    if arg == 'True':
        return True
    elif arg == 'False':
        return False
    else:
        return ''
