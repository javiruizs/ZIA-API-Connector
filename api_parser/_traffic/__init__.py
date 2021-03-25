"""
Traffic/VPN subparser package.
"""
import api_parser._traffic.subparsers as sps


def create_traffic_subparser(subparsers):
    """
    Creates the _traffic subparser.

    Args:
        subparsers: Subparser object from argparse obtined from calling ArgumentParser.add_subparsers().
    """
    p = subparsers.add_parser('vpn', description="Subparser for VPN/Traffic Forwarding management.")
    sp = p.add_subparsers(required=True,
                          description='Functionalities of the traffic fwd management module',
                          dest='Any of the subcommands'
                          )

    # Subparsers
    sps.get_vpn_creds_sp(sp)
    sps.add_vpn_creds_sp(sp)
    sps.bulk_del_vpn_creds_sp(sp)
    sps.get_vpn_cred_info_sp(sp)
    sps.upd_vpn_cred_sp(sp)
    sps.del_vpn_cred_sp(sp)
    sps.ip_gre_tunnel_info_sp(sp)
    sps.get_vips_sp(sp)
