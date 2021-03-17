import requests as re

import client.utils as u
from client.session import ZIAConnector


def get_admin_roles(session: ZIAConnector, includeAuditorRole=None, includePartnerRole=None):
    """Obtains the administrator roles and their ids.

    Args:
        includeAuditorRole (boolean): If True, includes auditor roles in the results.
        includePartnerRole (boolean): If True, includes partner roles in the results.

    Returns:
        dict: A dict containing the information regarding the roles: id, rank, name and role type.
    """

    url = session.form_full_url('adminRoles')

    r = re.Request('GET', url, params=u.clean_args(locals()))

    return session.send_recv(r, successful_msg="Admin roles retrieval successful.")


def get_admin_users(session: ZIAConnector, includeAuditorUsers=False, includeAdminUsers=True, search: str = "",
                    page=None, pageSize=None, full=False):
    """Obtains the list containing all the admin users.

    Args:
        full: If set to True, all admin users will be retrieved.
        includeAuditorUsers (bool, optional): Includes auditor users. Defaults to False.
        includeAdminUsers (bool, optional): Includes admin users. Defaults to True.
        search (str, optional): The search string used to partially match against an admin/auditor user's Login ID
            or Name. Defaults to "".
        page (int, optional): Specifies the page offset. Defaults to 1.
        pageSize (int, optional): Specifies the page size. The default size is 100, but the maximum size is 1000.
            Defaults to 100.

    Returns:
        [type]: [description]
    """
    url = session.form_full_url("adminUsers")

    args = locals()
    params = u.clean_args(args)

    return session.full_retrieval('GET', url, params, {}, pageSize, "Admin usr retrieval successful.", full)


def create_admin_user(session: ZIAConnector, userinfo):
    """Creates the user with the information contained in userinfo.

    Args:
        userinfo (JSON dict): A dictionary containing the user information.

    Returns:
        JSON dict: The created JSON dict representing the new user with all other information.
    """

    url = session.form_full_url("adminUsers")

    r = re.Request('POST', url, json=userinfo)

    return session.send_recv(r, f"Admin user '{userinfo['loginName']}' created successfully.")


def update_admin_user(session: ZIAConnector, userinfo):
    """Updates the information of an existing admin user.

    Args:
        userinfo (JSON dict): The updated JSON representation of the user.

    Returns:
        JSON dict: The representation of the updated user as confirmation.
    """

    url = session.form_full_url("adminUsers", [userinfo['userId']])

    r = re.Request('PUT', url, json=userinfo)

    return session.send_recv(r, f"Admin user {userinfo['userId']} updated success"
                                f"fully.")


def delete_admin_user(session: ZIAConnector, userId):
    """Deletes the desired user.

    Args:
        userId (int): The user ID.

    Returns:
        None: None-type should be returned.
    """
    url = session.form_full_url("adminUsers", [userId])

    r = re.Request('DELETE', url)

    return session.send_recv(r, f"Successfully deleted admin user: {userId}.")
