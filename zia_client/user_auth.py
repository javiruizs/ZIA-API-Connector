"""
Module for URL user authentication settings.
"""

from typing import List

import requests as re

from zia_client import ZIAConnector


def get_exempted_auth_urls(session: ZIAConnector):
    """
    Gets a list of URLs that were exempted from `cookie authentication`_. To learn more, see `URL Format Guidelines`_.

    .. _cookie authentication: https://help.zscaler.com/zia/about-zscaler-cookies
    .. _URL Format Guidelines: https://help.zscaler.com/zia/url-format-guidelines

    Args:
        session (ZIAConnector): Active API session.

    Returns:
        JSON dict.
    """

    url = session.form_full_url('authSettings')

    return session.send_recv(re.Request('GET', url), "Exempted User Authentication URLs obtained.")


def mod_auth_urls_exemptions(session: ZIAConnector, action: str, urls: List[str]):
    """
    Adds a URL to or removes a URL from the cookie authentication exempt list.
    To add a URL to the list, set the action parameter to ADD_TO_LIST. To remove a URL, set action to REMOVE_FROM_LIST.

    Args:
        session (ZIAConnector): Active API session.
        action: Action to do with the URLs. Either "ADD_TO_LIST" or "REMOVE_FROM_LIST".
        urls: List of urls or domains to modify.

    Returns:
        JSON dict: Resulting exemption list.
    """

    url = session.form_full_url('authSettings')

    data = {
        "ids": urls
    }

    params = {
        'action': action
    }

    return session.send_recv(re.Request('POST', url, params=params, json=data),
                             "Modification of the User Authentication Exempted URL list done.")
