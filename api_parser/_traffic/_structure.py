"""
Functions to build the _traffic forwarding management subparser and its subparsers.
"""
import argparse as ap

import api_parser as apip
import api_parser._traffic._endfuncs as tfc


def _get_vpn_creds(sp):
    """Subparser for _traffic vpn credential search

    Args:
        sp: Subparsers object.

    """
    p = sp.add_parser('search', description='Subparser for searching for VPN credentials.')

    p.add_argument('--search',
                   help='The search string used to match against a VPN credential\'s commonName, fqdn, '
                        'ipAddress, comments, or locationName attributes.', type=str)
    p.add_argument('--type',
                   help='Only gets VPN credentials for the specified type. This parameter is not supported '
                        'for partner API keys.', choices=['CN', 'IP', 'UFQDN', 'XAUTH'], type=str)
    p.add_argument('--no_location',
                   help='Include VPN credential only if not associated to any location. Server\'s default: True',
                   type=apip._boolstring,
                   choices=[True, False, None])
    p.add_argument('--loc_id',
                   help='Gets the VPN credentials for the specified location ID.',
                   type=int)
    p.add_argument('--mngr',
                   help='Gets the VPN credentials that are managed by the given partner. This filter is automatically '
                        'applied when called with a partner API key, and it cannot be overridden.',
                   type=int)
    p.add_argument('--page',
                   help='Specifies the page offset. Server\'s default: 1.',
                   type=int)
    p.add_argument('--p_size',
                   help='Specifies the page size. The default size is 100, but the maximum size is 1000.',
                   type=int)
    p.add_argument('--all',
                   help='If specified, all available results will be retrieved.',
                   action='store_true')

    p.set_defaults(func=tfc.traffic_get_vpn_creds)


def _add_vpn_creds(sp):
    p = sp.add_parser('add', description='Subparser for adding VPN credentials.')

    p.add_argument('json_file', help='JSON file. It should be a list of dictionaries, each dictionary representing a'
                                     'credential.')

    p.set_defaults(func=tfc.traffic_add_vpn_creds)


def _bulk_del_vpn_creds(sp):
    """Bulk delete VPN credentials.

    Args:
        sp: Subparsers.
    """
    p: ap.ArgumentParser = sp.add_parser('bulkdel', description='VPN Credential Bulk Delete.')
    group = p.add_mutually_exclusive_group(required=True)

    group.add_argument('--ids', nargs='+', help='VPN credential identifiers.', type=int)
    group.add_argument('--json_file', type=str, help='JSON file with a list of identifiers.')

    p.set_defaults(func=tfc.traffic_bulk_del_vpn_creds)


def _get_vpn_cred_info(sp):
    p: ap.ArgumentParser = sp.add_parser('info', description='VPN Credential Bulk Delete.')

    p.add_argument('id', type=int, help='VPN Credential identifier.')

    p.set_defaults(func=tfc.traffic_get_vpn_cred_info)

def _upd_vpn_cred(sp):
    pass


def _del_vpn_cred(sp):
    pass


def _ip_gre_tunnel_info(sp):
    pass


def _get_vips(sp):
    pass
