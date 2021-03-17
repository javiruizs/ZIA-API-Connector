import requests as re
from client.session import ZIAConnector


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
