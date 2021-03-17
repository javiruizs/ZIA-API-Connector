from typing import List, Dict

import requests as re

from client.session import ZIAConnector
from client.utils import clean_args


def get_vpn_creds(session: ZIAConnector):
    """Obtains the list of the existing VPN credentials in the platform.

    Raises:
        Exception: If the information retrieval was not possible.
    """

    url = session.form_full_url('vpnCreds')

    req = re.Request('GET', url)

    return session.send_recv(req, successful_msg='Obtaining VPN credentials successful.')


def del_vpn_creds(session: ZIAConnector, vpn_id):
    """
    Delete VPN credentials.

    Args:
        vpn_id: Credential identifier.

    Returns: JSON response.

    """
    url = session.form_full_url('vpn_credentials', [vpn_id])

    req = re.Request('DELETE', url)

    return session.send_recv(req, successful_msg=f'VPN credential with id {vpn_id} removed successfully.')


def add_vpn_creds(session: ZIAConnector, vpn_cred):
    # Todo
    pass


def bulk_del_vpn_creds(session: ZIAConnector, vpn_creds: list):
    # Todo
    pass


def get_vpn_cred_info(session: ZIAConnector, vpn_cred_id):
    # Todo
    pass


def upd_vpn_cred(session: ZIAConnector, vpn_cred_id):
    # Todo
    pass


def ip_gre_tunnel_info(session: ZIAConnector, ipAddresses: List[str] = False):
    """Gets a list of IP addresses with GRE tunnel details.



    Args:
        session: Active session.
        ipAddresses: IP addresses to search.

    Returns:
        JSON list of dictionaries: ::

        [
          {
            "ipAddress": "string",
            "greEnabled": false,
            "greTunnelIP": "string",
            "primaryGW": "string",
            "secondaryGW": "string",
            "tunID": 0,
            "greRangePrimary": "string",
            "greRangeSecondary": "string"
          }
        ]
    """

    if ipAddresses:
        params = {'ipAddresses': ipAddresses}
    else:
        params = False

    url = session.form_full_url('greInfo')

    return session.send_recv(re.Request('GET', url, params=params), successful_msg="GRE Info retrieved.")


def get_virtual_ips(session: ZIAConnector, dc: str = '', region: str = '', page: int = None, pageSize: int = None,
                    include: str = None, full: bool = False) -> List[Dict]:
    """Gets a paginated list of the virtual IP addresses (VIPs) available in the Zscaler cloud.

    Gets a paginated list of the virtual IP addresses (VIPs) available in the Zscaler cloud, including region and data
    center information. By default, the request gets all public VIPs in the cloud, but you can also include private or
    all VIPs in the request, if necessary.

    Args:
        session: API session logged in.
        dc: Filter based on data center.
        region: Filter based on region.
        page (int, optional): Specifies the page offset. Server's default is 1.
        pageSize (int, optional): Specifies the page size. Server's default is 100.
        include (str, optional): Include all, private, or public VIPs in the list. Server's default: public.
            * Available values: all, private, public
        full (bool, optional): Defaults to False. If set to True activates full retrieval.

    Returns:
        JSON list of dictionaries: ::

        [
          {
            "cloudName": "string",
            "region": "string",
            "city": "string",
            "dataCenter": "string",
            "location": "string",
            "vpnIps": [
              "string"
            ],
            "vpnDomainName": "string",
            "greIps": [
              "string"
            ],
            "greDomainName": "string",
            "pacIps": [
              "string"
            ],
            "pacDomainName": "string"
          }
        ]
    """
    params = clean_args(locals())

    url = session.form_full_url('virtualIp')

    return session.full_retrieval('GET', url, params, False, pageSize, "Virtual IP Addresses retrieved successfully.",
                                  full=full)
