"""
Endfunctions for the user parser.
"""
import pandas as pd

import client.session
import client.custom as cstm


def search_groups(clt: client.session.ZIAConnector, args):
    """
    Searches for user groups.
    
    Args:
        clt: API client that must me logged in beforehand.
        args: Parsed arguments. Namespace object. 

    Returns:
        The requests' response. Generally a JSON object.

    """
    return clt.get_groups(args.search, args.page, args.pageSize, args.all)


def search_depts(clt: client.session.ZIAConnector, args):
    """
    Searches for user departments.
    
    Args:
        clt: API client that must me logged in beforehand.
        args: Parsed arguments. Namespace object. 

    Returns:
        The requests' response. Generally a JSON object.

    """
    return clt.get_departments(args.search, args.page, args.pageSize, args.all)


def search_usrs(clt: client.session.ZIAConnector, args):
    """
    Searches for users.
    
    Args:
        clt: API client that must me logged in beforehand.
        args: Parsed arguments. Namespace object. 

    Returns:
        The requests' response. Generally a JSON object.

    """
    return clt.get_users(args.search, args.dept, args.group, args.page, args.pageSize, args.all)


def update_usrs(clt: client.session.ZIAConnector, args):
    """
    Updates the desired users.
    
    Args:
        clt: API client that must me logged in beforehand.
        args: Parsed arguments. Namespace object. 

    Returns:
        The requests' response. Generally a JSON object.

    """
    return cstm.update_users(clt, args.file)


def add_u2g(clt: client.session.ZIAConnector, args):
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
