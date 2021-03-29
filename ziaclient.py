"""
Script that maps command line instructions with the available configured methods in the zia_client package.
"""

from api_parser import create_parser
from zia_client import ZIAConnector
from zia_client._utils import print_json, save_json


def main():
    """
    Main function of the script
    """
    parser = create_parser()

    # Parse args
    args = parser.parse_args()

    client = ZIAConnector(args.conf, verbosity=not args.no_verbosity, creds=args.creds, apply_after=args.apply_after)
    client.login()

    if 'func' in vars(args):
        result = args.func(client, args)

        save_json(result, args.output)

        if args.print_results:
            print_json(result)

    if args.pending:
        print_json(client.activation_status())

    client.logout()


if __name__ == "__main__":
    main()
