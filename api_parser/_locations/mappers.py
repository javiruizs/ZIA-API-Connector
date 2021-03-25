"""
Module where end functions for the location parser are defined.
"""
import json

import zia_client.custom as cstm
import zia_client.locations as locs
from zia_client import ZIAConnector


# FINAL ACTION FUNCTIONS
def location_ids_mapper(c: ZIAConnector, args):
    """
    Retrieves the dictionary with the mapping of the locations and sublocations names and their ids.

    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return locs.get_location_ids(c, includeSubLocations=args.sub, includeParentLocations=args.parent, full=args.all,
                                 search=args.search, sslScanEnabled=args.ssl, bwEnforced=args.bw,
                                 authRequired=args.auth, xffEnabled=args.xff)


def location_search_mapper(c: ZIAConnector, args):
    """
    Searches locations with the `searchlocations` method of the zia_client.

    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return locs.search_locations(c, search=args.search, sslScanEnabled=args.sslScan, xffEnabled=args.xff,
                                 authRequired=args.authReq, bwEnforced=args.bwEnf, page=args.page,
                                 pageSize=args.pageSize, full=args.all)


def location_update_mapper(c: ZIAConnector, args):
    """
    Updates locations.
    
    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    with open(args.file) as f:
        locations = json.load(f)

    result = [locs.update_location(c, location) for location in locations]
    return result


def location_create_mapper(c: ZIAConnector, args):
    """
    Creates a new location.
    
    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    with open(args.file) as f:
        location = json.load(f)
    return locs.create_location(c, location)


def location_delete_mapper(c: ZIAConnector, args):
    """
    Deletes a location.
    
    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return locs.delete_location(c, args.loc_id)


def location_all_parents_subs_mapper(c: ZIAConnector, args):
    """
    Retrieves all location and sublocation infos.
    
    Args:
        c: API zia_client that must me logged in beforehand.
        args (unused): Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return cstm.obtain_all_locations_sublocations(c)


def location_info_mapper(c: ZIAConnector, args):
    """
    Retreives the info for the desired location.
    
    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return locs.get_location_info(c, args.loc_id)


def location_bulkdel_mapper(c: ZIAConnector, args):
    if args.json_file:
        with open(args.json_file) as f:
            ids = json.load(f)
    else:
        ids = args.ids

    return locs.bulk_del_location(c, ids)


def location_parent_subs_mapper(c: ZIAConnector, args):
    if args.json_file:
        with open(args.json_file) as f:
            ids = json.load(f)
    else:
        ids = args.ids

    result = [locs.get_location_info(c, id_) for id_ in ids]

    return result
