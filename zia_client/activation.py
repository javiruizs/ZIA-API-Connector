"""
Module for activation functions.
"""
import requests as re

from zia_client import ZIAConnector


def get_status(session: ZIAConnector):
    """Gets the current status in the current session.
    Active means no changes must be activated. Otherwise, consider
    calling method activate_changes() if you are not going to log off immediately
    afterwards.

    Raises:
        Exception: [description]
    """
    url = session.get_url('activation', 'main')

    return session.send_recv(re.Request('GET', url), "Status obtained successfully.")


def activate_changes(session: ZIAConnector):
    """Applies the changes that have been made.
    It is not necessary to call this method if you are going
    to log off.

    Raises:
        Exception: If the changes were not applied due to error.
    """
    url = session.get_url('activation', 'act')

    r = re.Request('POST', url)

    return session.send_recv(r, "Changes activated successfully.")
