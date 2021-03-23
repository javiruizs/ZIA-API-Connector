"""
This subpackage contains the construction functions and the final action functions for the user parser.

The construction functions can be found in the user_parser module and the end action functions in the endfuncs module.
"""
import api_parser._users._structure as _strc


def create_user_subparser(subparsers):
    """
    Creates the user subparser.

    Args:
        subparsers: Subparser object from argparse obtined from calling ArgumentParser.add_subparsers().
    """
    usr_prs = subparsers.add_parser('users')
    usr_subprs = usr_prs.add_subparsers(required=True, dest='any of the subcommands')

    _strc._search_user_parser(usr_subprs)
    _strc._update_user_parser(usr_subprs)
    _strc._create_user_parser(usr_subprs)
    _strc._delete_user_parser(usr_subprs)
    _strc._groups_user_parser(usr_subprs)
    _strc._depts_user_parser(usr_subprs)
    _strc._add_users_to_groups(usr_subprs)
    _strc._dept_info_user_parser(usr_subprs)
    _strc._group_info_user_parser(usr_subprs)
    _strc._bulk_del_user_parser(usr_subprs)
    _strc._info_user_parser(usr_subprs)
