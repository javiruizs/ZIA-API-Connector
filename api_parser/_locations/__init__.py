"""
This subpackage contains the construction functions and the final action functions for the location parser.

The construction functions can be found in the location_parser module and the end action functions in the endfuncs
module.
"""
import api_parser._locations.subparsers as sp


def create_location_subparser(subparsers):
    """
    Creates the necessary location subparsers: search, info...

    Args:
        subparsers: Subparser object from argparse obtained from calling ArgumentParser.add_subparsers().
    """

    locs_prs = subparsers.add_parser('locs', description="Subparser for location management.")
    locs_subprs = locs_prs.add_subparsers(required=True,
                                          dest='Any of the subcommands'
                                          )

    sp.location_all_parents_subs_sp(locs_subprs)
    sp.location_search_sp(locs_subprs)
    sp.location_ids_sp(locs_subprs)
    sp.location_update_sp(locs_subprs)
    sp.location_create_sp(locs_subprs)
    sp.location_del_sp(locs_subprs)
    sp.location_info_sp(locs_subprs)
