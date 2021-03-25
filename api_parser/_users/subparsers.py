"""
Functions to build the user subparser and its subparsers.
"""
import argparse as ap

import api_parser as prs
import api_parser._users.mappers as mp


def user_depts_p(usr_subprs):
    """
    Creates the user department subparser.

    Args:
        usr_subprs: The user subparser to create this subparser.

    Returns:

    """
    sp = usr_subprs.add_parser('depts', description='Searches through all user departments. Use the available arguments'
                                                    ' to apply filters in your search.')
    sp.add_argument(
        '--search', default=None, help='Searching string.')
    sp.add_argument(
        '--page', default=None, help='Page offset in the results.')
    sp.add_argument(
        '--pageSize', default=None, help='Page offset in the results.')
    sp.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')

    sp.set_defaults(func=mp.search_depts_mapper)


def user_u2g_sp(usr_subprs):
    """
    Creates the subparser to add users to groups.

    Args:
        usr_subprs: The user subparser to create this subparser.
    """
    sp = usr_subprs.add_parser('u2g', description='Adds users to groups. Works with email addresses and group IDs.')
    sp.add_argument('--mails', type=str, required=True,
                    help='CSV file that contains the emails. The script will only take the first column and assume that'
                         ' that the first line represents the column label.')
    sp.add_argument('--groups', type=str, required=True,
                    help='CSV file that contains the group IDs. The script will only take the first column and assume '
                         'that the first line represents the column label.')
    sp.add_argument('--dft_dept', type=int, required=True, help='Default department ID in case user has none. '
                                                                'This is required as users must belong to a department.')

    sp.set_defaults(func=mp.add_u2g_mapper)


def user_groups_sp(usr_subprs):
    """
    Creates the subparser to manage user groups.

    Args:
        usr_subprs: The user subparser to create this subparser.
    """
    usr_groups_p = usr_subprs.add_parser('groups', description='Searches all user groups with the applied filters, '
                                                               'if any were chosen, with the available parameters.')
    usr_groups_p.add_argument(
        '--search', default=None, help="The search string used to match against a group's name or comments attributes.")
    usr_groups_p.add_argument(
        '--page', default=1, help='Specifies the page offset.', type=int)
    usr_groups_p.add_argument(
        '--pageSize', default=100, help='Specifies the page size.', type=int)
    usr_groups_p.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')

    usr_groups_p.set_defaults(func=mp.search_groups_mapper)


def user_search_sp(usr_subprs):
    """
    Creates the subparser to do user searching queries.

    Args:
        usr_subprs: The user subparser to create this subparser.
    """
    usr_search_p = usr_subprs.add_parser('search', description='Gets a list of all users and allows user filtering by '
                                                               'name, department or group.')
    usr_search_p.add_argument(
        '--name', default=None, help='User name.')
    usr_search_p.add_argument(
        '--group', default=None, help='User group.')
    usr_search_p.add_argument(
        '--dept', default=None, help='User department.')
    usr_search_p.add_argument(
        '--page', default=1, help='Specifies page offset.', type=int)
    usr_search_p.add_argument(
        '--pageSize', default=100, help='Specifies page size.', type=int)
    usr_search_p.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')

    usr_search_p.set_defaults(func=mp.search_usrs_mapper)


def user_update_sp(usr_subprs):
    """
    Creates the subparser for updating users.

    Args:
        usr_subprs: The user subparser to create this subparser.
    """
    usr_update_p = usr_subprs.add_parser('update', description='Updates the user info.')
    usr_update_p.add_argument('file', help="JSON file with a list of user dicts.", type=str)

    usr_update_p.set_defaults(func=mp.update_usrs_mapper)


def user_create_sp(usr_subprs):
    """
    Creates the subparser for creating users.

    Args:
        usr_subprs: The user subparser to create this subparser.
    """
    usr_create_p = usr_subprs.add_parser('create', description="Adds a new user.")
    usr_create_p.add_argument('file', type=prs._json_obj_file, help="JSON file with list of user dicts.")

    usr_create_p.set_defaults(func=mp.create_usr_mapper)


def user_delete_sp(usr_subprs):
    """
    Creates the subparser to for deleting users.

    Args:
        usr_subprs: The user subparser to create this subparser.
    """
    usr_delete_p: ap.ArgumentParser = usr_subprs.add_parser(
        'delete',
        description='Deletes the user for the specified ID.')

    usr_delete_p.add_argument('user_id', help="The unique identifier for the user.")

    usr_delete_p.set_defaults(func=mp.delete_user_mapper)


def user_dept_sp(usr_subprs):
    p: ap.ArgumentParser = usr_subprs.add_parser('deptinfo',
                                                 description="Gets the department information for the specified ID.")

    g = p.add_mutually_exclusive_group(required=True)

    g.add_argument('--ids', type=int, help='List of ids.', nargs='+')
    g.add_argument('--json_file', type=prs._json_obj_file, help='JSON file with ids.')

    p.set_defaults(func=mp.dept_info_mapper)


def user_group_sp(usr_subprs):
    p: ap.ArgumentParser = usr_subprs.add_parser('groupinfo',
                                                 description="Gets the group information for the specified ID.")

    g = p.add_mutually_exclusive_group(required=True)

    g.add_argument('--ids', type=int, help='List of ids.', nargs='+')
    g.add_argument('--json_file', type=prs._json_obj_file, help='JSON file with ids.')

    p.set_defaults(func=mp.group_info_mapper)


def user_bulkdel_sp(usr_subprs):
    p: ap.ArgumentParser = usr_subprs.add_parser(
        'bulkdel',
        description="Bulk delete users up to a maximum of 500 users per request.")

    g = p.add_mutually_exclusive_group(required=True)

    g.add_argument('--ids', type=int, help='List of ids.', nargs='+')
    g.add_argument('--json_file', type=prs._json_obj_file, help='JSON file with ids.')

    p.set_defaults(func=mp.bulk_del_user_mapper)


def user_info_sp(usr_subprs):
    p: ap.ArgumentParser = usr_subprs.add_parser('info', description="Gets the user information for the specified ID.")

    g = p.add_mutually_exclusive_group(required=True)

    g.add_argument('--ids', type=int, help='List of ids.', nargs='+')
    g.add_argument('--json_file', type=prs._json_obj_file, help='JSON file with ids.')

    p.set_defaults(func=mp.info_user_mapper)
