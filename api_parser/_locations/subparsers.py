"""
Functions to build the location subparser.
"""
import argparse as ap
import api_parser as prs
import api_parser._locations.mappers as mp


def location_info_sp(locs_subprs):
    """
    Creates the location information retrieval subparser.

    Args:
        locs_subprs: The location subparser.
    """

    sp = locs_subprs.add_parser('info', description="Gets location information based on specified ID.")
    sp.add_argument('loc_id', type=int, help="Location identifier.")

    sp.set_defaults(func=mp.location_info_mapper)


def location_all_parents_subs_sp(locs_subprs):
    """
    Creates the subparser to obtain all locations and sublocations.

    Args:
        locs_subprs: The location subparser.
    """
    all_p = locs_subprs.add_parser('all', description="Gets all existing locations.")

    all_p.set_defaults(func=mp.location_all_parents_subs_mapper)


def location_ids_sp(locs_subprs):
    """
    Creates the subparser to retrieve all (sub)locations id-name maps.

    Args:
        locs_subprs: The location subparser.

    Returns:

    """
    ids_p = locs_subprs.add_parser('ids', description="Gets the mapping of location ID and name.")
    ids_p.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')
    ids_p.add_argument(
        '--sub', type=prs._boolstring, choices=[True, False, None],
        help='If set to true, sub-locations will be included. Only works if --ids is specified.')
    ids_p.add_argument(
        '--parent', type=prs._boolstring, choices=[True, False, None],
        help='If set to true locations with sub locations will be included in the response, otherwise only locations'
             ' without sub-locations are included. Only works if --ids is specified.')
    ids_p.add_argument(
        '--page', default=1, help='Page offset in the results.')
    ids_p.add_argument(
        '--pageSize', default=100, help='Page offset in the results.')
    ids_p.add_argument(
        '--search', default=None, help='Searching string. Could be either name, IP and port attributes.')
    ids_p.add_argument('--ssl', type=prs._boolstring, choices=[True, False, None],
                       help="Filter based on whether the Enable SSL Scanning setting is enabled or disabled for a "
                            "location.")
    ids_p.add_argument('--auth', type=prs._boolstring, choices=[True, False, None],
                       help="Filter based on whether the Enforce Authentication setting is enabled or disabled for a"
                            " location")
    ids_p.add_argument('--bw', type=prs._boolstring, choices=[True, False, None],
                       help="Filter based on whether Bandwith Control is being enforced for a location.")
    ids_p.add_argument('--xff', type=prs._boolstring, choices=[True, False, None],
                       help="Filter based on whether the Enforce XFF Forwarding setting is enabled or disabled for a "
                            "location.")

    ids_p.set_defaults(func=mp.location_ids_mapper)


def location_search_sp(locs_subprs):
    """
    Creates the subparser for the searching subparser.

    Args:
        locs_subprs: The location subparser.
    """
    locs_search_p = locs_subprs.add_parser(
        'search',
        description="Gets locations only, not sub-locations. When a location matches the given search parameter "
                    "criteria only its parent location is included in the result set, not its sub-locations."
    )
    locs_search_p.add_argument(
        '--search', default=None, help="The search string used to partially match against a location's name and port "
                                       "attributes.")
    locs_search_p.add_argument(
        '--sslScan', default=None, type=prs._boolstring, help='Filters results by the SSL Scanning option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--xff', default=None, type=prs._boolstring, help='Filters results by the XFF Forwarding option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--authReq', default=None, type=prs._boolstring, help='Filters results by the Enforce Authentication option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--bwEnf', default=None, type=prs._boolstring, help='Filters results by the Enforce Bandwidth Control option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--page', default=1, help='Page offset in the results.')
    locs_search_p.add_argument(
        '--pageSize', default=100, help='Page offset in the results.')
    locs_search_p.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')

    locs_search_p.set_defaults(func=mp.location_search_mapper)


def location_update_sp(locs_subprs):
    """
    Creates the subparser for updating locations.

    Args:
        locs_subprs: The location subparser.
    """
    locs_update_p = locs_subprs.add_parser('update', description="Updates the specified locations.")
    locs_update_p.add_argument(
        'file', help="JSON file with a list of location objects (dicts).")

    locs_update_p.set_defaults(func=mp.location_update_mapper)


def location_create_sp(locs_subprs):
    """
    Creates the subparser for the creation of locations.

    Args:
        locs_subprs: The location subparser.

    """
    locs_create_p = locs_subprs.add_parser('create', description="Creates new location.")
    locs_create_p.add_argument(
        'file', help="JSON file with a list of location objects (dicts).")

    locs_create_p.set_defaults(func=mp.location_create_mapper)


def location_del_sp(locs_subprs):
    """
    Creates the subparser for the delete location subparser.

    Args:
        locs_subprs: The location subparser.
    """

    locs_delete_p = locs_subprs.add_parser('delete', description="Deletes a location.")
    locs_delete_p.add_argument(
        'loc_id', help='Location id.')

    locs_delete_p.set_defaults(func=mp.location_delete_mapper)


def location_bulkdel_sp(locs_subprs):
    p: ap.ArgumentParser = locs_subprs.add_parser(
        'bulkdel',
        description="Bulk delete locations up to a maximum of 100 users per request. The response returns the location "
                    "IDs that were successfully deleted."
    )

    g = p.add_mutually_exclusive_group(required=True)

    g.add_argument('--ids', nargs='+', type=int, help='Location IDs.')
    g.add_argument('--json_file', type=str, help='JSON file with a list of IDs.')

    p.set_defaults(func=mp.location_bulkdel_mapper)


def location_parent_subs_sp(locs_subprs):
    p: ap.ArgumentParser = locs_subprs.add_parser(
        'sublocs',
        desciprtion="Gets the sub-location information for the location with the specified ID."
                    "These are the sub-locations associated to the parent location."
    )

    g = p.add_mutually_exclusive_group(required=True)

    g.add_argument('--ids', nargs='+', type=int, help='List of parent IDs.')
    g.add_argument('--json_file', type=str, help='JSON file with a list of IDs.')

    p.set_defaults(func=mp.location_parent_subs_mapper)
