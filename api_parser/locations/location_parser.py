"""
Functions to build the location subparser.
"""
import api_parser
import api_parser.locations.endfuncs as ef


def create_location_subparser(subparsers):
    """
    Creates the necessary location subparsers: search, info...

    Args:
        subparsers: Subparser object from argparse obtained from calling ArgumentParser.add_subparsers().
    """

    locs_prs = subparsers.add_parser('locs')
    locs_subprs = locs_prs.add_subparsers(required=True, dest='any of the subcommands')

    get_all_locations_sublocations_parser(locs_subprs)
    search_location_parser(locs_subprs)
    ids_location_parser(locs_subprs)
    update_location_parser(locs_subprs)
    create_location_parser(locs_subprs)
    delete_location_parser(locs_subprs)
    info_location_parser(locs_subprs)


def info_location_parser(locs_subprs):
    """
    Creates the location information retrieval subparser.

    Args:
        locs_subprs: The location subparser.
    """

    sp = locs_subprs.add_parser('info')
    sp.add_argument('loc_id', type=int, help="Location identifier.")

    sp.set_defaults(func=ef.info_location)


def get_all_locations_sublocations_parser(locs_subprs):
    """
    Creates the subparser to obtain all locations and sublocations.

    Args:
        locs_subprs: The location subparser.
    """
    all_p = locs_subprs.add_parser('all')

    all_p.set_defaults(func=ef.all_location)


def ids_location_parser(locs_subprs):
    """
    Creates the subparser to retrieve all (sub)locations id-name maps.

    Args:
        locs_subprs: The location subparser.

    Returns:

    """
    ids_p = locs_subprs.add_parser('ids')
    ids_p.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')
    ids_p.add_argument(
        '--sub', type=api_parser._boolstring, choices=[True, False, None],
        help='If set to true, sub-locations will be included. Only works if --ids is specified.')
    ids_p.add_argument(
        '--parent', type=api_parser._boolstring, choices=[True, False, None],
        help='If set to true locations with sub locations will be included in the response, otherwise only locations'
             ' without sub-locations are included. Only works if --ids is specified.')
    ids_p.add_argument(
        '--page', default=1, help='Page offset in the results.')
    ids_p.add_argument(
        '--pageSize', default=100, help='Page offset in the results.')
    ids_p.add_argument(
        '--search', default=None, help='Searching string. Could be either name, IP and port attributes.')
    ids_p.add_argument('--ssl', type=api_parser._boolstring, choices=[True, False, None],
                       help="Filter based on whether the Enable SSL Scanning setting is enabled or disabled for a "
                            "location.")
    ids_p.add_argument('--auth', type=api_parser._boolstring, choices=[True, False, None],
                       help="Filter based on whether the Enforce Authentication setting is enabled or disabled for a"
                            " location")
    ids_p.add_argument('--bw', type=api_parser._boolstring, choices=[True, False, None],
                       help="Filter based on whether Bandwith Control is being enforced for a location.")
    ids_p.add_argument('--xff', type=api_parser._boolstring, choices=[True, False, None],
                       help="Filter based on whether the Enforce XFF Forwarding setting is enabled or disabled for a "
                            "location.")

    ids_p.set_defaults(func=ef.ids_location)


def search_location_parser(locs_subprs):
    """
    Creates the subparser for the searching subparser.

    Args:
        locs_subprs: The location subparser.
    """
    locs_search_p = locs_subprs.add_parser('search')
    locs_search_p.add_argument(
        '--search', default=None, help='Searching string. Could be either name, IP and port attributes.')
    locs_search_p.add_argument(
        '--sslScan', default=None, type=api_parser._boolstring, help='Filters results by the SSL Scanning option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--xff', default=None, type=api_parser._boolstring, help='Filters results by the XFF Forwarding option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--authReq', default=None, type=api_parser._boolstring, help='Filters results by the Enforce Authentication option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--bwEnf', default=None, type=api_parser._boolstring, help='Filters results by the Enforce Bandwidth Control option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--page', default=1, help='Page offset in the results.')
    locs_search_p.add_argument(
        '--pageSize', default=100, help='Page offset in the results.')
    locs_search_p.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')

    locs_search_p.set_defaults(func=ef.search_location)


def update_location_parser(locs_subprs):
    """
    Creates the subparser for updating locations.

    Args:
        locs_subprs: The location subparser.
    """
    locs_update_p = locs_subprs.add_parser('update')
    locs_update_p.add_argument(
        'file', help="File where the location JSON is located.")

    locs_update_p.set_defaults(func=ef.update_location)


def create_location_parser(locs_subprs):
    """
    Creates the subparser for the creation of locations.

    Args:
        locs_subprs: The location subparser.

    """
    locs_create_p = locs_subprs.add_parser('create')
    locs_create_p.add_argument(
        'file', help="File where the location JSON is located.")

    locs_create_p.set_defaults(func=ef.create_location)


def delete_location_parser(locs_subprs):
    """
    Creates the subparser for the delete location subparser.

    Args:
        locs_subprs: The location subparser.
    """

    locs_delete_p = locs_subprs.add_parser('delete')
    locs_delete_p.add_argument(
        'loc_id', help='Location id.')

    locs_delete_p.set_defaults(func=ef.delete_location)
