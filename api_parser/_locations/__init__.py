"""
This subpackage contains the construction functions and the final action functions for the location parser.

The construction functions can be found in the location_parser module and the end action functions in the endfuncs
module.
"""
from api_parser._locations._structure import _get_all_locations_sublocations_parser, _search_location_parser, \
    _ids_location_parser, _update_location_parser, _create_location_parser, _delete_location_parser, \
    _info_location_parser


def create_location_subparser(subparsers):
    """
    Creates the necessary location subparsers: search, info...

    Args:
        subparsers: Subparser object from argparse obtained from calling ArgumentParser.add_subparsers().
    """

    locs_prs = subparsers.add_parser('locs')
    locs_subprs = locs_prs.add_subparsers(required=True, dest='any of the subcommands')

    _get_all_locations_sublocations_parser(locs_subprs)
    _search_location_parser(locs_subprs)
    _ids_location_parser(locs_subprs)
    _update_location_parser(locs_subprs)
    _create_location_parser(locs_subprs)
    _delete_location_parser(locs_subprs)
    _info_location_parser(locs_subprs)
