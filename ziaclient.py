"""
Script that maps command line instructions with the available configured methods in the zia_client package.
"""
from sys import argv

import zia_client.activation as actv
from api_parser import create_parser
from zia_client import ZIAConnector
from zia_client._utils import print_json, save_json


def main():
    """
    Main function of the script
    """
    parser = create_parser()
    if len(argv) == 1:
        parser.parse_args(['-h'])

    # Parse args
    args = parser.parse_args()

    client = ZIAConnector(args.conf, verbosity=not args.no_verbosity, creds=args.creds)
    client.login()

    if 'func' in vars(args):
        result = args.func(client, args)

        save_json(result, args.output)

        if not args.no_print:
            print_json(result)

    if args.apply:
        print_json(actv.activate_changes(client))
    if args.pending:
        print_json(actv.get_status(client))

    client.logout()


if __name__ == "__main__":
    main()
