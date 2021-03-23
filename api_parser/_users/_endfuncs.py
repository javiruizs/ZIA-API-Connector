"""
Endfunctions for the user parser.
"""
import pandas as pd

import zia_client.custom as cstm
import zia_client.users as usrs
from zia_client import ZIAConnector


def _search_groups(clt: ZIAConnector, args):
    """
    Searches for user groups.
    
    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return usrs.get_groups(clt, args.search, args.page, args.pageSize, args.all)


def _search_depts(clt: ZIAConnector, args):
    """
    Searches for user departments.
    
    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return usrs.get_departments(clt, args.search, args.page, args.pageSize, args.all)


def _search_usrs(clt: ZIAConnector, args):
    """
    Searches for _users.
    
    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return usrs.get_users(clt, args.search, args.dept, args.group, args.page, args.pageSize, args.all)


def _update_usrs(clt: ZIAConnector, args):
    """
    Updates the desired _users.
    
    Args:
        clt: API zia_client that must me logged in beforehand.
        args: Parsed api_parser. Namespace object.

    Returns:
        The requests' response. Generally a JSON object.

    """
    return cstm.update_users(clt, args.file)


def _add_u2g(clt: ZIAConnector, args):
    """
    Adds _users to desired groups and assigns them a default department if they don't have any.
    
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


def _create_usr(clt: ZIAConnector, args):
    result =[usrs.create_user(user) for user in args.file]

    return result


def _delete_user(clt: ZIAConnector, args):
    return usrs.del_user(clt, args.user_id)


def _dept_info(clt: ZIAConnector, args):
    if args.ids:
        ids = args.ids
    else:
        ids = args.json_file

    result = [usrs.get_department(clt, id_) for id_ in ids]

    return result


def _group_info(clt: ZIAConnector, args):
    if args.ids:
        ids = args.ids
    else:
        ids = args.json_file

    result = [usrs.get_group_info(clt, id_) for id_ in ids]

    return result


def _bulk_del_user(clt: ZIAConnector, args):
    if args.ids:
        ids = args.ids
    else:
        ids = args.json_file

    result = [usrs.bulk_del_user(clt, id_) for id_ in ids]

    return result


def _info_user(clt: ZIAConnector, args):
    if args.ids:
        ids = args.ids
    else:
        ids = args.json_file

    result = [usrs.get_user_info(clt, id_) for id_ in ids]

    return result
