import requests as re
import client.utils as u
from client.session import ZIAConnector


def get_departments(session: ZIAConnector, search='', page=None, pageSize=None, full=False):
    """
    Obtains departments.

    Args:
        full: If set to true, all departments will be retrieved.
        search: Search string.
        page: Page offset.
        pageSize: Elements contained per page.

    Returns:
        List of dictionaries with depts.

    """
    url = session.form_full_url('depts')

    params = u.clean_args(locals())

    return session.full_retrieval('GET', url, params, {}, pageSize, "Departments retrieval successful.", full)


def get_department(session: ZIAConnector, dept_id: int):
    """
    Gets department information from department id.

    Args:
        dept_id: Department id.

    Returns:
        JSON response.

    """
    url = session.form_full_url('dept', [dept_id])

    r = re.Request('GET', url)

    return session.send_recv(r, f'Information for department with id {dept_id} obtained successfully.')


def get_groups(session: ZIAConnector, search="", page=None, pageSize=None, full=False):
    """
    Retrieves groups.

    Args:
        search (str): Search string. Name of the group.
        page (int): Page offset. Server's default is 1.
        pageSize (int): Page size. Server's default 100.
        full (bool): Default is False. If set to True, all information is returned.

    Returns:
        JSON response.

    """
    params = u.clean_args(locals())

    url = session.form_full_url('groups')

    return session.full_retrieval('GET', url, params, {}, pageSize, "Group retrieval successful.", full)


def get_users(session: ZIAConnector, name="", dept="", group="", page=None, pageSize=None, full=False):
    """
    Gets a list of all users and allows user filtering by name, department, or group. The name search parameter
    performs a partial match. The dept and group parameters perform a 'starts with' match.

    Args:
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

    return session.full_retrieval('GET', url, params, {}, pageSize, "User retrieval successful.", full)


def update_user(session: ZIAConnector, userdata):
    """
    Updates the user information for the specified ID. However, the "email" attribute is read-only.

    Args:
        userdata (dict): Dictionary that contains the user information.

    Returns:
        JSON response.

    """
    if 'id' not in userdata:
        raise ValueError('Userdata has no id key.')

    url = session.form_full_url('usr', [userdata['id']])

    r = re.Request('PUT', url, json=userdata)

    return session.send_recv(r, f"User {userdata['id']} update successful.")


def get_user_info(session: ZIAConnector, usr_id):
    """
    Gets the user information for the specified ID.

    Args:
        usr_id (int): The unique identifer for the user.

    Returns:
        JSON dict with user's info.

    """
    url = session.form_full_url('usr', [usr_id])

    r = re.Request('GET', url)

    return session.send_recv(r, "User update successful.")
