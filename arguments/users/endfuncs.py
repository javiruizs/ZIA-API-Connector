"""
Endfunctions for the user parser.
"""
import pandas as pd

import client.custom as cstm
from client.session import ZIAConnector
import client.users as usrs


def search_groups(clt: ZIAConnector, args):
    """
    Searches for user groups.
    
    Args:
        clt: API client that must me logged in beforehand.
        args: Parsed arguments. Namespace object. 

    Returns:
        The requests' response. Generally a JSON object.

    """
    return usrs.get_groups(clt, args.search, args.page, args.pageSize, args.all)


def search_depts(clt: ZIAConnector, args):
    """
    Searches for user departments.
    
    Args:
        clt: API client that must me logged in beforehand.
        args: Parsed arguments. Namespace object. 

    Returns:
        The requests' response. Generally a JSON object.

    """
    return usrs.get_departments(clt, args.search, args.page, args.pageSize, args.all)


def search_usrs(clt: ZIAConnector, args):
    """
    Searches for users.
    
    Args:
        clt: API client that must me logged in beforehand.
        args: Parsed arguments. Namespace object. 

    Returns:
        The requests' response. Generally a JSON object.

    """
    return usrs.get_users(clt, args.search, args.dept, args.group, args.page, args.pageSize, args.all)


def update_usrs(clt: ZIAConnector, args):
    """
    Updates the desired users.
    
    Args:
        clt: API client that must me logged in beforehand.
        args: Parsed arguments. Namespace object. 

    Returns:
        The requests' response. Generally a JSON object.

    """
    return cstm.update_users(clt, args.file)


def add_u2g(clt: ZIAConnector, args):
    """
    Adds users to desired groups and assigns them a default department if they don't have any.
    
    Args:
        clt: API client that must me logged in beforehand.
        args: Parsed arguments. Namespace object. 

    Returns:
        The requests' response. Generally a JSON object.

    """
    # Take first column for both files and convert them to list
    users = pd.read_csv(args.users).iloc[:, 0].to_list()
    groups = pd.read_csv(args.groups).iloc[:, 0].to_list()

    return cstm.add_users_to_group(clt, users, groups, args.dft_dept)
