"""
Module for traffic forwarding management.
"""
from typing import List, Dict

import requests as re

from zia_client import ZIAConnector
from zia_client.utils import clean_args


def get_vpn_creds(session: ZIAConnector, search: str = '', type: str = '', includeOnlyWithoutLocation: bool = None,
                  locationId: int = '', managedBy: int = '', page: int = '', pageSize: int = '',
                  full: bool = False) -> list:
    """Obtains the list of the existing VPN credentials in the platform.

    Args:
        session (:obj:ZIAConnector): Active API session.
        search (str, optional): The search string used to match against a VPN credential\'s commonName, fqdn, ipAddress,
            comments, or locationName attributes.
        type (str, optional): Only gets VPN credentials for the specified type. This parameter is not supported for
            partner API keys. Reconized values: 'CN', 'IP', 'UFQDN' or 'XAUTH'.
        includeOnlyWithoutLocation (bool, optional): Include VPN credential only if not associated to any location.
            Server\'s default: `True`.
        locationId (int, optional): Gets the VPN credentials for the specified location ID.
        managedBy (int, optional): Gets the VPN credentials that are managed by the given partner. This filter is
            automatically applied when called with a partner API key, and it cannot be overridden.
        page (int, optional): Specifies the page offset. Server\'s default: 1.
        pageSize (int, optional): Specifies the page size. The default size is 100, but the maximum size is 1000.
        full (bool, optional): If `True`, indicates that full retrieval of results should be called.

    Raises:
        Exception: If the information retrieval was not possible.

    Returns:
        :obj:`list` of :obj:`dicts`: VPN credentials.
    """

    params = clean_args(locals(), 'session')

    url = session.form_full_url('vpnCreds')

    return session.full_retrieval('GET', url, params, page_size=pageSize, full=full)


def del_vpn_creds(session: ZIAConnector, vpn_id):
    """
    Delete VPN credentials.

    Args:
        session (ZIAConnector): Logged in API client.
        vpn_id: Credential identifier.

    Returns:
        204 No Content
    """
    url = session.form_full_url('vpn_credentials', vpn_id)

    req = re.Request('DELETE', url)

    return session.send_recv(req, successful_msg=f'VPN credential with id {vpn_id} removed successfully.')


def add_vpn_creds(session: ZIAConnector, vpn_cred: Dict):
    """Adds VPN credentials that can be associated to locations.

    Adds VPN credentials that can be associated to locations. When invoked with a partner API key, it automatically
    sets the managedBy attribute to the partner associated with the key.

    Args:
        session (ZIAConnector): Logged in session.
        vpn_cred: VPN credential structure of the following format.

    Examples:
        `vpn_cred` should take the following form::

            {
                "type": "CN", # recognized values [ CN, IP, UFQDN, XAUTH ]
                "fqdn": "string", # Applicable only to UFQDN or XAUTH (or HOSTED_MOBILE_USERS) auth type.
                "preSharedKey": "string", # This is a required field for UFQDN and IP auth type.
                "comments": "string"
            }

    Returns:
        JSON dictionary: configured credential.

    """

    url = session.form_full_url("vpnCreds")

    req = re.Request('POST', url, json=vpn_cred)

    return session.send_recv(req, "VPN credential was added successfully.")


def bulk_del_vpn_creds(session: ZIAConnector, vpn_creds: List):
    """Bulk delete VPN credentials up to a maximum of 100 credentials per request.

    Bulk delete VPN credentials up to a maximum of 100 credentials per request.
    The response returns the VPN IDs that were successfully deleted.

    Args:
        session (ZIAConnector): Logged in session.
        vpn_creds (list[int]): List of the identifiers of the VPN credentials.

    Returns:
        JSON dictionary: On 204 code, Successful Operation. On 404, error returned.
    """

    url = session.form_full_url('vpnCreds', 'bulkDelete')

    data = {
        "ids": vpn_creds
    }

    req = re.Request('POST', url, json=data)

    return session.send_recv(req, "VPN credential was added successfully.")


def get_vpn_cred_info(session: ZIAConnector, vpn_cred_id: int):
    """Gets the VPN credentials for the specified ID.

    Args:
        session (ZIAConnector): Logged in session.
        vpn_cred_id (int): Credential identifier.

    Returns:
        JSON dictionary: Dictionary representing the credential.
    """

    url = session.form_full_url("vpnCreds", vpn_cred_id)

    req = re.Request('GET', url)

    return session.send_recv(req, successful_msg="VPN credential information successfully retrieved.")


def upd_vpn_cred(session: ZIAConnector, vpn_cred: Dict):
    """Updates the VPN credentials for the specified ID.

    Args:
        session (ZIAConnector): Logged in session.
        vpn_cred: Credential JSON dictionary obtained from the get_vpn_cred function.

    Returns:
        JSON dictionary: Dictionary representing the credential.
    """

    url = session.form_full_url("vpnCreds", vpn_cred['id'])

    req = re.Request('PUT', url, json=vpn_cred)

    return session.send_recv(req, "VPN credential updated successfully.")


def ip_gre_tunnel_info(session: ZIAConnector, ipAddresses: List[str] = False):
    """Gets a list of IP addresses with GRE tunnel details.



    Args:
        session (ZIAConnector): Active session.
        ipAddresses: IP addresses to search.

    Returns:
        :obj:`list[dict]`: List of dictionaries.

        Here a template of the return object::

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
        session (ZIAConnector): API session logged in.
        dc: Filter based on data center.
        region: Filter based on region.
        page (int, optional): Specifies the page offset. Server's default is 1.
        pageSize (int, optional): Specifies the page size. Server's default is 100.
        include (str, optional): Include all, private, or public VIPs in the list. Server's default: `public`.

            * Available values: `all`, `private`, `public`

        full (bool, optional): Defaults to False. If set to True activates full retrieval.

    Returns:
        List of dictionaries: The dictionaries representing the virtual IP addresses.

        Example of the returned object::

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

    return session.full_retrieval('GET', url, params=params, page_size=pageSize,
                                  message="Virtual IP Addresses retrieved successfully.", full=full)
