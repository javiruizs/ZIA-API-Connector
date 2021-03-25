"""
End functions. Translates the arguments introduced per CL to the functions of the API connector.
"""
import json

import zia_client.traffic as tfc
from zia_client import ZIAConnector


def get_vpn_creds_mapper(c: ZIAConnector, args):
    """Calls the get_vpn_creds function.

    Args:
        c (:obj:ZIAConnector): Logged in API client.
        args (argparse.Namespace):  Namespace object returned by the ArgumentParser when arguments were parsed.

    Returns:
        The return of the get_vpn_creds function.
    """
    return tfc.get_vpn_creds(session=c, full=args.all, pageSize=args.page_size, page=args.page, managedBy=args.mngr,
                             locationId=args.loc_id, search=args.search, type=args.type)


def add_vpn_creds_mapper(c: ZIAConnector, args):
    """Calls the add_vpn_creds function.

    Args:
        c (:obj:ZIAConnector): Logged in API client.
        args (argparse.Namespace):  Namespace object returned by the ArgumentParser when arguments were parsed.

    Returns:
        The return of the add_vpn_creds function.
    """
    with open(args.json_file) as f:
        creds = json.load(f)

    result = []
    for cred in creds:
        result.append(tfc.add_vpn_creds(c, cred))

    return result


def bulk_del_vpn_creds_mapper(c: ZIAConnector, args):
    """Calls the bulk delete vpn creds.

    Args:
        c (:obj:ZIAConnector): Logged in API client.
        args (argparse.Namespace):  Namespace object returned by the ArgumentParser when arguments were parsed.

    Returns:
        The return of the called function.
    """
    if args.ids:
        return tfc.bulk_del_vpn_creds(c, args.ids)
    else:
        with open(args.json_file) as f:
            ids = json.load(f)

        return tfc.bulk_del_vpn_creds(c, ids)


def get_vpn_cred_info_mapper(c: ZIAConnector, args):
    """Returns the credential info.

    Args:
        c (:obj:ZIAConnector): Logged in API client.
        args (argparse.Namespace):  Namespace object returned by the ArgumentParser when arguments were parsed.

    Returns:
        The return of the _traffic function.
    """
    return tfc.ip_gre_tunnel_info(c, args.id)


def upd_vpn_cred_mapper(c: ZIAConnector, args):
    """Maps the arguments to the function for vpn credential retrieval.

    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    with open(args.json_file) as f:
        creds = json.load(f)

    result = [tfc.upd_vpn_cred(c, cred) for cred in creds]

    return result


def del_vpn_cred_mapper(c: ZIAConnector, args):
    """Maps the arguments to the function for vpn credential deletion.

    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return tfc.del_vpn_cred(c, args.id)


def ip_gretunnel_info_mapper(c: ZIAConnector, args):
    """Maps the arguments to the function for retrieving GRE tunnel information.

    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    if args.ips:
        ips = args.ips
    else:
        with open(args.json_file) as f:
            ips = json.load(f)

    results = [tfc.ip_gre_tunnel_info(c, ip) for ip in ips]

    return results


def get_vips_mapper(c: ZIAConnector, args):
    """Maps the arguments to the function for getting Virtual IPs information.

    Args:
        c: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return tfc.get_virtual_ips(c, args.dc, args.region, args.page, args.pageSize, args.include, args.all)
