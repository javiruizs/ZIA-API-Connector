from api_parser._traffic._structure import _get_vpn_creds, _add_vpn_creds, _bulk_del_vpn_creds, _get_vpn_cred_info, \
    _upd_vpn_cred, _del_vpn_cred, _ip_gre_tunnel_info, _get_vips


def create_traffic_subparser(subparsers):
    """
    Creates the _traffic subparser.

    Args:
        subparsers: Subparser object from argparse obtined from calling ArgumentParser.add_subparsers().
    """
    p = subparsers.add_parser('vpn')
    sp = p.add_subparsers(required=True, dest='any of the subcommands')

    # Subparsers
    _get_vpn_creds(sp)
    _add_vpn_creds(sp)
    _bulk_del_vpn_creds(sp)
    _get_vpn_cred_info(sp)
    _upd_vpn_cred(sp)
    _del_vpn_cred(sp)
    _ip_gre_tunnel_info(sp)
    _get_vips(sp)