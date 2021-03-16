import ZIAapi.arguments.parser as p
import ZIAapi.arguments.users.endfuncs as ef
import argparse as ap


def create_user_subparser(subparsers):
    usr_prs = subparsers.add_parser('users')
    usr_subprs = usr_prs.add_subparsers(required=True, dest='any of the subcommands')

    search_user_parser(usr_subprs)
    update_user_parser(usr_subprs)
    create_user_parser(usr_subprs)
    delete_user_parser(usr_subprs)
    groups_user_parser(usr_subprs)
    depts_user_parser(usr_subprs)
    add_users_to_groups(usr_subprs)


def depts_user_parser(usr_subprs):
    sp = usr_subprs.add_parser('depts')
    sp.add_argument(
        '--search', default=None, help='Searching string.')
    sp.add_argument(
        '--page', default=None, help='Page offset in the results.')
    sp.add_argument(
        '--pageSize', default=None, help='Page offset in the results.')
    sp.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')

    sp.set_defaults(func=ef.search_depts)


def add_users_to_groups(usr_subprs):
    sp = usr_subprs.add_parser('add-u2g')
    sp.add_argument('--users', type=str, required=True, help='Text file (CSV) with only one column and first line is label.')
    sp.add_argument('--groups', type=str, required=True, help='Text file (CSV) with only one column and first line is label.')
    sp.add_argument('--dft_dept', type=int, required=True, help='Default department id in case user has none.')

    sp.set_defaults(func=ef.add_u2g)


def groups_user_parser(usr_subprs):
    usr_groups_p = usr_subprs.add_parser('groups')
    usr_groups_p.add_argument(
        '--search', default=None, help='Searching string.')
    usr_groups_p.add_argument(
        '--page', default=None, help='Page offset in the results.')
    usr_groups_p.add_argument(
        '--pageSize', default=None, help='Page offset in the results.')
    usr_groups_p.add_argument(
        '--all', action='store_true', help='Retrieves all results. This option overrides page and pageSize.')

    usr_groups_p.set_defaults(func=ef.search_groups)


def search_user_parser(usr_subprs):
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

    usr_search_p.set_defaults(func=ef.search_usrs)


def update_user_parser(usr_subprs):
    usr_update_p = usr_subprs.add_parser('update')
    usr_update_p.add_argument(
        'file', help="File from which the updated user configuration will be loaded and updated.")

    usr_update_p.set_defaults(func=ef.update_usrs)


def create_user_parser(usr_subprs):
    usr_create_p = usr_subprs.add_parser('create')
    usr_create_p.add_argument(
        'file', help="File from which the updated user configuration will be loaded and created.")


def delete_user_parser(usr_subprs):

    usr_delete_p = usr_subprs.add_parser('delete')
    usr_delete_p.add_argument(
        'user_id', help='User identification. If you don\'t know the UID, search it first.')
