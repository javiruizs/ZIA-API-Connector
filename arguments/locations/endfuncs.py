import json

import zia_api_client
import zia_api_client.custom as c


# FINAL ACTION FUNCTIONS
def ids_location(client: zia_api_client.ZIAConnector, args):
    return client.get_location_ids(includeSubLocations=args.sub, includeParentLocations=args.parent, full=args.all,
                                   search=args.search, sslScanEnabled=args.ssl, bwEnforced=args.bw,
                                   authRequired=args.auth, xffEnabled=args.xff)


def search_location(client: zia_api_client.ZIAConnector, args):
    return client.search_locations(search=args.search, sslScanEnabled=args.sslScan, xffEnabled=args.xff,
                                   authRequired=args.authReq, bwEnforced=args.bwEnf, page=args.page,
                                   pageSize=args.pageSize, full=args.all)


def update_location(client: zia_api_client.ZIAConnector, args):
    with open(args.file) as f:
        location = json.load(f)
    return client.update_location(location)


def create_location(client: zia_api_client.ZIAConnector, args):
    with open(args.file) as f:
        location = json.load(f)
    return client.create_location(location)


def delete_location(client: zia_api_client.ZIAConnector, args):
    return client.delete_location(args.loc_id)


def all_location(client: zia_api_client.ZIAConnector, args):
    return c.obtain_all_locations_sublocations(client)


def info_location(client: zia_api_client.ZIAConnector, args):
    return client.get_location_info(args.loc_id)
