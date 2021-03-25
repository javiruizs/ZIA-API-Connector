"""
Endfunctions for the user parser.
"""
import pandas as pd

import zia_client.custom as cstm
import zia_client.users as usrs
from zia_client import ZIAConnector


def search_groups_mapper(clt: ZIAConnector, args):
    """
    Searches for user groups.
    
    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return usrs.get_groups(clt, args.search, args.page, args.pageSize, args.all)


def search_depts_mapper(clt: ZIAConnector, args):
    """
    Searches for user departments.
    
    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return usrs.get_departments(clt, args.search, args.page, args.pageSize, args.all)


def search_usrs_mapper(clt: ZIAConnector, args):
    """
    Searches for users.
    
    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return usrs.get_users(clt, args.name, args.dept, args.group, args.page, args.pageSize, args.all)


def update_usrs_mapper(clt: ZIAConnector, args):
    """
    Updates the desired users.
    
    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return cstm.update_users(clt, args.file)


def add_u2g_mapper(clt: ZIAConnector, args):
    """
    Adds users to desired groups and assigns them a default department if they don't have any.
    
    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    # Take first column for both files and convert them to list
    users = pd.read_csv(args.users).iloc[:, 0].to_list()
    groups = pd.read_csv(args.groups).iloc[:, 0].to_list()

    return cstm.add_users_to_group(clt, users, groups, args.dft_dept)


def create_usr_mapper(clt: ZIAConnector, args):
    """Maps the arguments to the function for creating users.

    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.
    """
    result = [usrs.create_user(clt, user) for user in args.file]

    return result


def delete_user_mapper(clt: ZIAConnector, args):
    """Maps the arguments to the function for user deletion.

    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.
    """
    return usrs.del_user(clt, args.user_id)


def dept_info_mapper(clt: ZIAConnector, args):
    """Maps the arguments to the function for retrieving department information.

    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    if args.ids:
        ids = args.ids
    else:
        ids = args.json_file

    result = [usrs.get_department(clt, id_) for id_ in ids]

    return result


def group_info_mapper(clt: ZIAConnector, args):
    """Maps the arguments to the function for group info retrieval.

    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    if args.ids:
        ids = args.ids
    else:
        ids = args.json_file

    result = [usrs.get_group_info(clt, id_) for id_ in ids]

    return result


def bulk_del_user_mapper(clt: ZIAConnector, args):
    """Maps the arguments to the function for user bulk deletion.

    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    if args.ids:
        ids = args.ids
    else:
        ids = args.json_file

    result = [usrs.bulk_del_user(clt, id_) for id_ in ids]

    return result


def info_user_mapper(clt: ZIAConnector, args):
    """Maps the arguments to the function for user info retrieval.

    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    if args.ids:
        ids = args.ids
    else:
        ids = args.json_file

    result = [usrs.get_user_info(clt, id_) for id_ in ids]

    return result
