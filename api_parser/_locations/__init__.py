"""
This subpackage contains the construction functions and the final action functions for the location parser.

The construction functions can be found in the location_parser module and the end action functions in the endfuncs
module.
"""
import api_parser._locations._structure as _str


def create_location_subparser(subparsers):
    """
    Creates the necessary location subparsers: search, info...

    Args:
        subparsers: Subparser object from argparse obtained from calling ArgumentParser.add_subparsers().
    """

    locs_prs = subparsers.add_parser('locs')
    locs_subprs = locs_prs.add_subparsers(required=True, dest='any of the subcommands')

    _str._get_all_locations_sublocations_parser(locs_subprs)
    _str._search_location_parser(locs_subprs)
    _str._ids_location_parser(locs_subprs)
    _str._update_location_parser(locs_subprs)
    _str._create_location_parser(locs_subprs)
    _str._delete_location_parser(locs_subprs)
    _str._info_location_parser(locs_subprs)
