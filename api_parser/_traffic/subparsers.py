"""
Functions to build the _traffic forwarding management subparser and its subparsers.
"""
import argparse as ap

import api_parser as prs
import api_parser._traffic.mappers as mp


def get_vpn_creds_sp(sp):
    """Subparser for traffic vpn credential search

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
                   type=prs._boolstring,
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

    p.set_defaults(func=mp.get_vpn_creds_mapper)


def add_vpn_creds_sp(sp):
    """Subparser for vpn credential addition/creation.

    Args:
        sp: VPN subparsers.
    """
    p = sp.add_parser('add', description='Subparser for adding VPN credentials.')

    p.add_argument('json_file', help='JSON file. It should be a list of dictionaries, each dictionary representing a'
                                     'credential.')

    p.set_defaults(func=mp.add_vpn_creds_mapper)


def bulk_del_vpn_creds_sp(sp):
    """Bulk delete VPN credentials.

    Args:
        sp: Subparsers.
    """
    p: ap.ArgumentParser = sp.add_parser('bulkdel', description='VPN Credential Bulk Delete.')
    group = p.add_mutually_exclusive_group(required=True)

    group.add_argument('--ids', nargs='+', help='VPN credential identifiers.', type=int)
    group.add_argument('--json_file', type=str, help='JSON file with a list of identifiers.')

    p.set_defaults(func=mp.bulk_del_vpn_creds_mapper)


def get_vpn_cred_info_sp(sp):
    """Subparser for vpn credential info retrieval.

    Args:
        sp: VPN subparsers.
    """
    p: ap.ArgumentParser = sp.add_parser('info', description='Obtains specified credentials information')

    group = p.add_mutually_exclusive_group(required=True)

    group.add_argument('--ids', nargs='+', help='VPN credential identifiers.', type=int)
    group.add_argument('--json_file', type=str, help='JSON file with a list of credential ids.')

    p.set_defaults(func=mp.get_vpn_cred_info_mapper)


def upd_vpn_cred_sp(sp):
    """Subparser for vpn credential update.

    Args:
        sp: VPN subparsers.
    """
    p: ap.ArgumentParser = sp.add_parser('update', description='Updates specified credentials.')

    p.add_argument('json_file', type=str, help='JSON file with a list of credential dicts.')

    p.set_defaults(func=mp.upd_vpn_cred_mapper)


def del_vpn_cred_sp(sp):
    """Subparser for vpn credential deletion.

    Args:
        sp: VPN subparsers.
    """
    p: ap.ArgumentParser = sp.add_parser('delete', description='Deletes specified credentials information')

    p.add_argument('id', help='VPN credential identifier.', type=int)

    p.set_defaults(func=mp.del_vpn_cred_mapper)


def ip_gre_tunnel_info_sp(sp):
    """Subparser for GRE tunnel information serach.

    Args:
        sp: VPN subparsers.
    """
    p: ap.ArgumentParser = sp.add_parser('gre_search', description='Searches for the existing GRE tunnels.')

    group = p.add_mutually_exclusive_group()

    group.add_argument('--ips', nargs='+', help='IP addresses.', type=str)
    group.add_argument('--json_file', type=str, help='JSON file with a list IP addresses as strings.')

    p.set_defaults(func=mp.ip_gretunnel_info_mapper)


def get_vips_sp(sp):
    """Subparser for virtual IP search.

    Args:
        sp: VPN subparsers.
    """
    p: ap.ArgumentParser = sp.add_parser('vips', description='Gets a paginated list of the virtual IP addresses (VIPs) '
                                                             'available in the Zscaler cloud. Search result can be '
                                                             'filtered with the listed arguments.')

    p.add_argument('--dc', type=str, help='Filter based on data center.')
    p.add_argument('--region', type=str, help='Filter based on region.')
    p.add_argument('--incl', help='Include all, private, or public VIPs in the list.', type=str, default='public',
                   choices=['all', 'private', 'public'])
    p.add_argument('--page', help='Specifies the page offset.', type=int, default=1)
    p.add_argument('--pageSize', help='Specifies the page size.', type=int, default=100)
    p.add_argument('--all', help='Enables full retrieval and gets all available pages for the specified page size.',
                   action='store_true')

    p.set_defaults(func=mp.upd_vpn_cred_mapper)
