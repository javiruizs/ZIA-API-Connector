"""
This package contains the necessary structures to use the implemented methods of the zia_client.session.ZIAConnector class
through the command line script ziaclient.py.

As of now, only the functionality for locations and users has been translated.

See the submodules for detailed functionality.
"""
import argparse as ap
import ast
import datetime as dt
import json

from api_parser._locations import create_location_subparser
from api_parser._traffic import create_traffic_subparser
from api_parser._users import create_user_subparser


def create_parser():
    """
    Creates the parser. It calls the necessary functions to build the subparsers.

    Returns:
        Returns the built parser.
    """
    parser = ap.ArgumentParser(
        description="""**ZIA API command line script.**
        
        Python script that communicates with the Zscaler Internet Access API.
        It's composed of various subparsers, each one representing the configured modules in the `zia_client` module.
        
        The keyword arguments listed below can be always specified before the desired subparser."""
    )

    # Main parser commands
    parser.add_argument('--pending', help="Lists pending changes.", action='store_true')
    parser.add_argument(
        '--apply_after',
        help='Forces application of changes before logging out after several requests.',
        type=int,
        default=0
    )
    parser.add_argument('--conf', help='Specifies config file.', default='config/config.json')
    parser.add_argument('--creds', help='Specifies config file.', type=_json_obj_file, default=None)
    parser.add_argument('--output', '-o', help='Custom path where the output JSON will be stored.',
                        default=_output_name())
    parser.add_argument('--no_verbosity', help='Disables detailed verbosity.', action='store_true')
    parser.add_argument('--print_results', '-p', help='Prints results.', action='store_true')

    # Create subparsers
    subparsers = parser.add_subparsers(required=True, dest='Any of the subcommands')

    # Create user parser
    create_user_subparser(subparsers)

    # Create location parser
    create_location_subparser(subparsers)

    # Create traffic parser
    create_traffic_subparser(subparsers)

    return parser


def _output_name():
    """
    Creates a name for the output file where the search or operation results will be stored if no custom name is \
    provided.

    Returns:
        str: A string with the format `search_%Y-%m-%d_%H-%M-%S.json`.
        ``Example: search_2021-01-01_14-13-12.json``


    """
    today = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f'query_{today}.json'


def _boolstring(arg):
    """
    Checks api_parser that are not required and have default values on the server. Argument is a string but mus be
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


def _json_obj_file(arg: str):
    if arg.endswith('.json'):
        with open(arg) as f:
            return json.load(f)
    else:
        data = ast.literal_eval(arg)
        try:
            return json.dumps(data)
        except json.JSONDecodeError:
            raise ap.ArgumentTypeError('Input should be a JSON object.')
