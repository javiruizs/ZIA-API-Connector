"""
End functions. Translates the arguments introduced per CL to the functions of the API connector.
"""
import json

import zia_client.traffic as tfc
from zia_client import ZIAConnector


def traffic_get_vpn_creds(c: ZIAConnector, args):
    """Calls the get_vpn_creds function.

    Args:
        c (:obj:ZIAConnector): Logged in API client.
        args (argparse.Namespace):  Namespace object returned by the ArgumentParser when arguments were parsed.

    Returns:
        The return of the get_vpn_creds function.
    """
    return tfc.get_vpn_creds(session=c, full=args.all, pageSize=args.page_size, page=args.page, managedBy=args.mngr,
                             locationId=args.loc_id, search=args.search, type=args.type)


def traffic_add_vpn_creds(c: ZIAConnector, args):
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


def traffic_bulk_del_vpn_creds(c: ZIAConnector, args):
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
            ids = json.loads(f)

        return tfc.bulk_del_vpn_creds(c, ids)


def traffic_get_vpn_cred_info(c: ZIAConnector, args):
    """Returns the credential info.

    Args:
        c (:obj:ZIAConnector): Logged in API client.
        args (argparse.Namespace):  Namespace object returned by the ArgumentParser when arguments were parsed.

    Returns:
        The return of the traffic function.
    """
    return tfc.ip_gre_tunnel_info(c, args.id)


def traffic_upd_vpn_cred(c: ZIAConnector, args):
    pass


def traffic_del_vpn_cred(c: ZIAConnector, args):
    pass


def traffic_ip_gretunnel_info(c: ZIAConnector, args):
    pass


def traffic_get_vips(c: ZIAConnector, args):
    pass
