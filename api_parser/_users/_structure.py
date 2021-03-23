"""
Functions to build the user subparser and its subparsers.
"""
import argparse as ap

import api_parser as apip
import api_parser._users._endfuncs as ef


def _depts_user_parser(usr_subprs):
    """
    Creates the user department subparser.

    Args:
        usr_subprs: The user subparser to create this subparser.

    Returns:

    """
    sp = usr_subprs.add_parser('depts')
    sp.add_argument(
        '--search', default=None, help='Searching string.')
    sp.add_argument(
        '--page', default=None, help='Page offset in the results.')
    sp.add_argument(
        '--pageSize', default=None, help='Page offset in the results.')
    sp.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')

    sp.set_defaults(func=ef._search_depts)


def _add_users_to_groups(usr_subprs):
    """
    Creates the subparser to add _users to groups.

    Args:
        usr_subprs: The user subparser to create this subparser.
    """
    sp = usr_subprs.add_parser('add-u2g')
    sp.add_argument('--_users', type=str, required=True,
                    help='Text file (CSV) with only one column and first line is label.')
    sp.add_argument('--groups', type=str, required=True,
                    help='Text file (CSV) with only one column and first line is label.')
    sp.add_argument('--dft_dept', type=int, required=True, help='Default department id in case user has none.')

    sp.set_defaults(func=ef._add_u2g)


def _groups_user_parser(usr_subprs):
    """
    Creates the subparser to manage user groups.

    Args:
        usr_subprs: The user subparser to create this subparser.
    """
    usr_groups_p = usr_subprs.add_parser('groups')
    usr_groups_p.add_argument(
        '--search', default=None, help='Searching string.')
    usr_groups_p.add_argument(
        '--page', default=None, help='Page offset in the results.')
    usr_groups_p.add_argument(
        '--pageSize', default=None, help='Page offset in the results.')
    usr_groups_p.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')

    usr_groups_p.set_defaults(func=ef._search_groups)


def _search_user_parser(usr_subprs):
    """
    Creates the subparser to do user searching queries.

    Args:
        usr_subprs: The user subparser to create this subparser.
    """
    usr_search_p = usr_subprs.add_parser('search')
    usr_search_p.add_argument(
        '--search', default=None, help='Searching string.')
    usr_search_p.add_argument(
        '--group', default=None, help='Filters results by group.')
    usr_search_p.add_argument(
        '--dept', default=None, help='Filters results by the XFF Forwarding option.')
    usr_search_p.add_argument(
        '--page', default=1, help='Page offset in the results.')
    usr_search_p.add_argument(
        '--pageSize', default=100, help='Page offset in the results.')
    usr_search_p.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')

    usr_search_p.set_defaults(func=ef._search_usrs)


def _update_user_parser(usr_subprs):
    """
    Creates the subparser for updating _users.

    Args:
        usr_subprs: The user subparser to create this subparser.
    """
    usr_update_p = usr_subprs.add_parser('update')
    usr_update_p.add_argument(
        'file', help="File from which the updated user configuration will be loaded and updated.")

    usr_update_p.set_defaults(func=ef._update_usrs)


def _create_user_parser(usr_subprs):
    """
    Creates the subparser for creating _users.

    Args:
        usr_subprs: The user subparser to create this subparser.
    """
    usr_create_p = usr_subprs.add_parser('create')
    usr_create_p.add_argument('file', type=apip._json_obj_file, help="JSON file with list of user dicts.")

    usr_create_p.set_defaults(func=ef._create_usr)


def _delete_user_parser(usr_subprs):
    """
    Creates the subparser to for deleting _users.

    Args:
        usr_subprs: The user subparser to create this subparser.
    """
    usr_delete_p: ap.ArgumentParser = usr_subprs.add_parser('delete')

    usr_delete_p.add_argument('user_id', help='User identification. If you don\'t know the UID, search it first.')

    usr_delete_p.set_defaults(func=ef._delete_user)


def _dept_info_user_parser(usr_subprs):
    p: ap.ArgumentParser = usr_subprs.add_parser('deptinfo')

    g = p.add_mutually_exclusive_group(required=True)

    g.add_argument('--ids', type=int, help='List of ids.', nargs='+')
    g.add_argument('--json_file', type=apip._json_obj_file, help='JSON file with ids.')

    p.set_defaults(func=ef._dept_info)


def _group_info_user_parser(usr_subprs):
    p: ap.ArgumentParser = usr_subprs.add_parser('groupinfo')

    g = p.add_mutually_exclusive_group(required=True)

    g.add_argument('--ids', type=int, help='List of ids.', nargs='+')
    g.add_argument('--json_file', type=apip._json_obj_file, help='JSON file with ids.')

    p.set_defaults(func=ef._group_info)


def _bulk_del_user_parser(usr_subprs):
    p: ap.ArgumentParser = usr_subprs.add_parser('bulkdel')

    g = p.add_mutually_exclusive_group(required=True)

    g.add_argument('--ids', type=int, help='List of ids.', nargs='+')
    g.add_argument('--json_file', type=apip._json_obj_file, help='JSON file with ids.')

    p.set_defaults(func=ef._bulk_del_user)


def _info_user_parser(usr_subprs):
    p: ap.ArgumentParser = usr_subprs.add_parser('info')

    g = p.add_mutually_exclusive_group(required=True)

    g.add_argument('--ids', type=int, help='List of ids.', nargs='+')
    g.add_argument('--json_file', type=apip._json_obj_file, help='JSON file with ids.')

    p.set_defaults(func=ef._info_user)
