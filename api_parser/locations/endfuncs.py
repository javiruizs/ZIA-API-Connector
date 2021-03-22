"""
Module where end functions for the location parser are defined.
"""
import json

from zia_client import ZIAConnector
import zia_client.custom as cstm
import zia_client.locations as locs


# FINAL ACTION FUNCTIONS
def ids_location(c: ZIAConnector, args):
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


def search_location(c: ZIAConnector, args):
    """
    Searches locations with the `search_locations` method of the zia_client.

    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return locs.search_locations(c, search=args.search, sslScanEnabled=args.sslScan, xffEnabled=args.xff,
                                 authRequired=args.authReq, bwEnforced=args.bwEnf, page=args.page,
                                 pageSize=args.pageSize, full=args.all)


def update_location(c: ZIAConnector, args):
    """
    Updates locations.
    
    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    with open(args.file) as f:
        location = json.load(f)
    return locs.update_location(c, location)


def create_location(c: ZIAConnector, args):
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


def delete_location(c: ZIAConnector, args):
    """
    Deletes a location.
    
    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return locs.delete_location(c, args.loc_id)


def all_location(c: ZIAConnector, args):
    """
    Retrieves all location and sublocation infos.
    
    Args:
        c: API zia_client that must me logged in beforehand.
        args (unused): Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return cstm.obtain_all_locations_sublocations(c)


def info_location(c: ZIAConnector, args):
    """
    Retreives the info for the desired location.
    
    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return locs.get_location_info(c, args.loc_id)
