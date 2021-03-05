import ZIAapi
import json


def create_location_subparser(subparsers):
    locs_prs = subparsers.add_parser('locs')
    locs_subprs = locs_prs.add_subparsers()

    search_location_parser(locs_subprs)
    ids_location_parser(locs_subprs)
    update_location_parser(locs_subprs)
    create_location_parser(locs_subprs)
    delete_location_parser(locs_subprs)


def ids_location_parser(locs_subprs):
    ids_p = locs_subprs.add_parser('ids')
    ids_p.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')
    ids_p.add_argument(
        '--sub', type=boolstring, choices=[True, False, None],
        help='If set to true, sub-locations will be included. Only works if --ids is specified.')
    ids_p.add_argument(
        '--parent', type=boolstring, choices=[True, False, None],
        help='If set to true locations with sub locations will be included in the response, otherwise only locations'
             ' without sub-locations are included. Only works if --ids is specified.')
    ids_p.add_argument(
        '--page', default=1, help='Page offset in the results.')
    ids_p.add_argument(
        '--pageSize', default=100, help='Page offset in the results.')
    ids_p.add_argument(
        '--search', default=None, help='Searching string. Could be either name, IP and port attributes.')

    ids_p.set_defaults(func=ids_location)


def search_location_parser(locs_subprs):
    locs_search_p = locs_subprs.add_parser('search')
    locs_search_p.add_argument(
        '--search', default=None, help='Searching string. Could be either name, IP and port attributes.')
    locs_search_p.add_argument(
        '--sslScan', default=None, type=boolstring, help='Filters results by the SSL Scanning option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--xff', default=None, type=boolstring, help='Filters results by the XFF Forwarding option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--authReq', default=None, type=boolstring, help='Filters results by the Enforce Authentication option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--bwEnf', default=None, type=boolstring, help='Filters results by the Enforce Bandwidth Control option.',
        choices=[True, False, None])
    locs_search_p.add_argument(
        '--page', default=1, help='Page offset in the results.')
    locs_search_p.add_argument(
        '--pageSize', default=100, help='Page offset in the results.')
    locs_search_p.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')

    locs_search_p.set_defaults(func=search_location)


def update_location_parser(locs_subprs):
    locs_update_p = locs_subprs.add_parser('update')
    locs_update_p.add_argument(
        'file', help="File where the location JSON is located.")

    locs_update_p.set_defaults(func=update_location)


def create_location_parser(locs_subprs):
    locs_create_p = locs_subprs.add_parser('create')
    locs_create_p.add_argument(
        'file', help="File where the location JSON is located.")

    locs_create_p.set_defaults(func=create_location)


def delete_location_parser(locs_subprs):
    locs_delete_p = locs_subprs.add_parser('delete')
    locs_delete_p.add_argument(
        'loc_id', help='Location id.')

    locs_delete_p.set_defaults(func=delete_location)


# FUNCTIONS FOR TYPE
def boolstring(arg):
    if arg == 'True':
        return True
    elif arg == 'False':
        return False
    else:
        return ''


# FINAL ACTION FUNCTIONS
def ids_location(client: ZIAapi.ZIAConnector, args):
    return client.get_location_ids(includeSubLocations=args.sub, includeParentLocations=args.parent, full=args.all,
                                   search=args.search)


def search_location(client: ZIAapi.ZIAConnector, args):
    return client.search_locations(search=args.search, sslScanEnabled=args.sslScan, xffEnabled=args.xff,
                                   authRequired=args.authReq, bwEnforced=args.bwEnf, page=args.page,
                                   pageSize=args.pageSize, full=args.all)


def update_location(client: ZIAapi.ZIAConnector, args):
    with open(args.file) as f:
        location = json.load(f)
    return client.update_location(location)


def create_location(client: ZIAapi.ZIAConnector, args):
    with open(args.file) as f:
        location = json.load(f)
    return client.create_location(location)


def delete_location(client: ZIAapi.ZIAConnector, args):
    return client.delete_location(args.loc_id)