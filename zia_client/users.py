"""
Module for user management.
"""
from typing import Dict
from typing import List

import requests as re

import zia_client._utils as u
from zia_client import ZIAConnector


def get_departments(session: ZIAConnector, search='', page=None, pageSize=None, full=False):
    """
    Obtains departments.

    Args:
        session (ZIAConnector): Logged in API client.
        full: If set to true, all departments will be retrieved.
        search: Search string.
        page: Page offset.
        pageSize: Elements contained per page.

    Returns:
        List of dictionaries with depts.

    """
    url = session.form_full_url('depts')

    params = u.clean_args(locals())

    return session.full_retrieval('GET', url, params=params, page_size=pageSize,
                                  message="Departments retrieval successful.", full=full)


def get_department(session: ZIAConnector, dept_id: int):
    """
    Gets department information from department id.

    Args:
        session (ZIAConnector): Logged in API client.
        dept_id: Department id.

    Returns:
        JSON response.

    """
    url = session.form_full_url('dept', dept_id)

    r = re.Request('GET', url)

    return session.send_recv(r, f'Information for department with id {dept_id} obtained successfully.')


def get_groups(session: ZIAConnector, search="", page=None, pageSize=None, full=False):
    """
    Retrieves groups.

    Args:
        session (ZIAConnector): Logged in API client.
        search (str): Search string. Name of the group.
        page (int): Page offset. Server's default is 1.
        pageSize (int): Page size. Server's default 100.
        full (bool): Default is False. If set to True, all information is returned.

    Returns:
        JSON response.

    """
    params = u.clean_args(locals())

    url = session.form_full_url('groups')

    return session.full_retrieval('GET', url, params=params, page_size=pageSize, message="Group retrieval successful.",
                                  full=full)


def get_users(session: ZIAConnector, name="", dept="", group="", page=None, pageSize=None, full=False):
    """
    Gets a list of all _users and allows user filtering by name, department, or group. The name search parameter
    performs a partial match. The dept and group parameters perform a 'starts with' match.

    Args:
        session (ZIAConnector): Logged in API client.
        name (str): Filters by user name.
        dept (str): Filters by department name.
        group (str): Filters by group name.
        page (int): Defaults to 1. Specifies the page offset.
        pageSize (int): Defaults to 100. Specifies the page size.
        full (bool): Defaults to False. Set to True if complete search is wanted.

    Returns:
        JSON response.

    """
    url = session.form_full_url('usr')

    params = u.clean_args(locals())

    return session.full_retrieval('GET', url, params=params, page_size=pageSize, message="User retrieval successful.",
                                  full=full)


def update_user(session: ZIAConnector, userdata):
    """
    Updates the user information for the specified ID. However, the "email" attribute is read-only.

    Args:
        session (ZIAConnector): Logged in API client.
        userdata (dict): Dictionary that contains the user information.

    Returns:
        JSON response.

    """
    if 'id' not in userdata:
        raise ValueError('Userdata has no id key.')

    url = session.form_full_url('usr', userdata['id'])

    r = re.Request('PUT', url, json=userdata)

    return session.send_recv(r, f"User {userdata['id']} update successful.")


def get_user_info(session: ZIAConnector, usr_id):
    """
    Gets the user information for the specified ID.

    Args:
        session (ZIAConnector): Logged in API client.
        usr_id (int): The unique identifer for the user.

    Returns:
        JSON dict with user's info.

    """
    url = session.form_full_url('usr', usr_id)

    r = re.Request('GET', url)

    return session.send_recv(r, "User update successful.")


def get_group_info(session: ZIAConnector, group_id: int):
    """Gets the group for the specified ID.

    Args:
        session (ZIAConnector): Active API session.
        group_id: Group id.

    Returns:
        JSON dict: Representation of the group.
    """

    url = session.form_full_url('groups', group_id)

    return session.send_recv(re.Request('GET', url), f"Group info for group {group_id} obtained.")


def create_user(session: ZIAConnector, user_dict: Dict):
    """Adds new user.

    Adds a new user. A user can belong to multiple groups, but can only belong to one department.

    Args:
        session (ZIAConnector): Active API session.
        user_dict: User dictionary containing it's information.

    Example:
        Template for the `user_dict` parameter::

            {
                "name": "string", # User name. This appears when choosing _users for policies.
                "email": "string",  # User email consists of a user name and domain name. It does not have to be a valid
                                    # email address, but it must be unique and its domain must belong to the organization.
                "groups":	[], # List of Groups a user belongs to. Groups are used in policies.
                "department": {},
                "comments": "string", # Additional information about this user.
                "tempAuthEmail": "string",  # Temporary Authentication Email. If you enabled one-time tokens or links, enter
                                            # the email address to which the Zscaler service sends the tokens or links. If
                                            # this is empty, the service will send the email to the User email.
                "password":	"string",   # User's password. Applicable only when authentication type is Hosted DB.
                                        # Password strength must follow what is defined in the auth settings.
            }

    Returns:
        JSON dict: Same posted dict.
    """

    url = session.form_full_url("usr")

    return session.send_recv(re.Request('POST', url, json=user_dict), f"User with name {user_dict['name']} created.")


def bulk_del_user(session: ZIAConnector, user_ids: List[int]):
    """Bulk delete _users up to a maximum of 500 _users per request.

    Bulk delete _users up to a maximum of 500 _users per request.
    The response returns the user IDs that were successfully deleted.

    Args:
        session (ZIAConnector): Active API session.
        user_ids: User identifiers in a list.

    Returns:
        Ids that were deleted.
    """

    url = session.form_full_url('usr', 'bulkDelete')

    data = {
        "ids": user_ids
    }

    return session.send_recv(re.Request('POST', url, json=data), "Bulk user deletion made.")


def del_user(session: ZIAConnector, user_id: int):
    """Deletes the user for the specified ID.

    Args:
        session (ZIAConnector): Active API session.
        user_id: User identifier.

    Returns:
        JSON dict or HTTP response body.
    """

    url = session.form_full_url('usr', user_id)

    return session.send_recv(re.Request('DELETE', url), f"User {user_id} deleted.")
