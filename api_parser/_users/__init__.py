"""
This subpackage contains the construction functions and the final action functions for the user parser.

The construction functions can be found in the user_parser module and the end action functions in the endfuncs module.
"""
import api_parser._users.subparsers as sp


def create_user_subparser(subparsers):
    """
    Creates the user subparser.

    Args:
        subparsers: Subparser object from argparse obtined from calling ArgumentParser.add_subparsers().
    """
    usr_prs = subparsers.add_parser('users', description="Subparser for user management.")
    usr_subprs = usr_prs.add_subparsers(required=True, dest='Any of the subcommands')

    sp.user_search_sp(usr_subprs)
    sp.user_update_sp(usr_subprs)
    sp.user_create_sp(usr_subprs)
    sp.user_delete_sp(usr_subprs)
    sp.user_groups_sp(usr_subprs)
    sp.user_depts_p(usr_subprs)
    sp.user_u2g_sp(usr_subprs)
    sp.user_dept_sp(usr_subprs)
    sp.user_group_sp(usr_subprs)
    sp.user_bulkdel_sp(usr_subprs)
    sp.user_info_sp(usr_subprs)
