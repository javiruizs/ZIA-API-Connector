import argparse as ap
import datetime as dt

from .location_parser import create_location_subparser
from .user_parser import create_user_subparser


def create_parser():
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

    # Create subparsers
    subparsers = parser.add_subparsers()

    # Create user parser
    create_user_subparser(subparsers)

    # Create location parser
    create_location_subparser(subparsers)

    return parser


def output_name():
    today = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f'search_{today}.json'
