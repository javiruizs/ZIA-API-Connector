import arguments.locations.endfuncs as ef
import arguments.parser as p


def create_location_subparser(subparsers):
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
    sp = locs_subprs.add_parser('info')
    sp.add_argument('loc_id', type=int, help="Location identifier.")

    sp.set_defaults(func=ef.info_location)


def get_all_locations_sublocations_parser(locs_subprs):
    all_p = locs_subprs.add_parser('all')

    all_p.set_defaults(func=ef.all_location)


def ids_location_parser(locs_subprs):
    ids_p = locs_subprs.add_parser('ids')
    ids_p.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')
    ids_p.add_argument(
        '--sub', type=p.boolstring, choices=[True, False, None],
        help='If set to true, sub-locations will be included. Only works if --ids is specified.')
    ids_p.add_argument(
        '--parent', type=p.boolstring, choices=[True, False, None],
        help='If set to true locations with sub locations will be included in the response, otherwise only locations'
             ' without sub-locations are included. Only works if --ids is specified.')
    ids_p.add_argument(
        '--page', default=1, help='Page offset in the results.')
    ids_p.add_argument(
        '--pageSize', default=100, help='Page offset in the results.')
    ids_p.add_argument(
        '--search', default=None, help='Searching string. Could be either name, IP and port attributes.')
    ids_p.add_argument('--ssl', type=p.boolstring, choices=[True, False, None],
                       help="Filter based on whether the Enable SSL Scanning setting is enabled or disabled for a "
                            "location.")
    ids_p.add_argument('--auth', type=p.boolstring, choices=[True, False, None],
                       help="Filter based on whether the Enforce Authentication setting is enabled or disabled for a"
                            " location")
    ids_p.add_argument('--bw', type=p.boolstring, choices=[True, False, None],
                       help="Filter based on whether Bandwith Control is being enforced for a location.")
    ids_p.add_argument('--xff', type=p.boolstring, choices=[True, False, None],
                       help="Filter based on whether the Enforce XFF Forwarding setting is enabled or disabled for a "
                            "location.")

    ids_p.set_defaults(func=ef.ids_location)


def search_location_parser(locs_subprs):
    locs_search_p = locs_subprs.add_parser('search')
    locs_search_p.add_argument(
        '--search', default=None, help='Searching string. Could be either name, IP and port attributes.')
    locs_search_p.add_argument(
        '--sslScan', default=None, type=p.boolstring, help='Filters results by the SSL Scanning option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--xff', default=None, type=p.boolstring, help='Filters results by the XFF Forwarding option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--authReq', default=None, type=p.boolstring, help='Filters results by the Enforce Authentication option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--bwEnf', default=None, type=p.boolstring, help='Filters results by the Enforce Bandwidth Control option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--page', default=1, help='Page offset in the results.')
    locs_search_p.add_argument(
        '--pageSize', default=100, help='Page offset in the results.')
    locs_search_p.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')

    locs_search_p.set_defaults(func=ef.search_location)


def update_location_parser(locs_subprs):
    locs_update_p = locs_subprs.add_parser('update')
    locs_update_p.add_argument(
        'file', help="File where the location JSON is located.")

    locs_update_p.set_defaults(func=ef.update_location)


def create_location_parser(locs_subprs):
    locs_create_p = locs_subprs.add_parser('create')
    locs_create_p.add_argument(
        'file', help="File where the location JSON is located.")

    locs_create_p.set_defaults(func=ef.create_location)


def delete_location_parser(locs_subprs):
    locs_delete_p = locs_subprs.add_parser('delete')
    locs_delete_p.add_argument(
        'loc_id', help='Location id.')

    locs_delete_p.set_defaults(func=ef.delete_location)
