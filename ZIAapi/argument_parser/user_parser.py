import argparse as ap

def create_user_subparser(subparsers):
    usr_prs = subparsers.add_parser('users')
    usr_subprs = usr_prs.add_subparsers()

    usr_search_p = usr_subprs.add_parser('search')
    usr_search_p.add_argument('--all')

    usr_update_p = usr_subprs.add_parser('update')
    usr_update_p.add_argument(
        'file', help="File from which the updated user configuration will be loaded and updated.")

    usr_create_p = usr_subprs.add_parser('create')
    usr_create_p.add_argument(
        'file', help="File from which the updated user configuration will be loaded and created.")

    usr_delete_p = usr_subprs.add_parser('delete')
    usr_delete_p.add_argument(
        'user_id', help='User identification. If you don\'t know the UID, search it first.')
